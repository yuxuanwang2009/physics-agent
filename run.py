#!/usr/bin/env python3
"""G-Sigma -> coadjoint-orbit bosonization: a claim-adjudication agent.

A multi-round Claude pipeline that ADJUDICATES, rather than assumes, a physics
claim: that the bilocal G-Sigma action of a free gapless Fermi gas (Section 1 of
the task-background document) reduces directly to the coadjoint-orbit bosonization
action (Section 2). The Section-2 action is shown as a PROPOSAL to test -- not as an
established theorem to reproduce, and not as a necessary endpoint. The agent's job is
to reach a correct VERDICT about the claim, not to reach the proposed action.

Design (author vs. referee, with an iterate-until-plausible loop):
  * Round 1 -- brainstorm/rank. Propose and rank candidate strategies for a direct
    bridge. The harness then walks the ranking from the top.
  * Round 2 -- develop (the AUTHOR). Execute the current strategy as a genuine,
    rigorous, step-by-step derivation; no self-judging. On a retry it is handed the
    referee's pinpointed weak point and food for thought, and revises in substance.
  * Round 3 -- referee (an ISOLATED ADVERSARY). A separate context that sees only the
    author's finalized argument (plus the task-background and its own earlier
    critiques), and tries to BREAK it. It returns one outcome, ordered worst->best:
        incorrect | unjustified | plausible | controlled | exact,
    and is REQUIRED to pinpoint the single weakest step and give the author concrete
    food for thought.
  * The loop. If the referee rates the argument at least `plausible`, the agent
    advances. Otherwise it loops back to Round 2 ONCE (revise the SAME strategy); if
    still below the bar, it abandons that strategy for the next-ranked one (a fresh
    single-retry budget). If every strategy is exhausted, the agent stops: no document
    is rendered, and the best attempt plus the referee's post-mortem is the deliverable.
  * Render runs once a strategy clears the bar (outcome at least `plausible`): it
    re-renders the winning bridge as a SELF-CONTAINED LaTeX document (-> derivation.tex,
    compiled to derivation.pdf). A `plausible` document is typeset but must flag its
    uncontrolled assumptions up front.
  * Checkpoint after every round; emit raw JSON + a readable transcript.

Notes:
  * A binding STANDARD OF RIGOR (see SYSTEM_INSTRUCTIONS) classifies each step as
    exact / controlled / plausible / unjustified, and defaults to REJECT:
    an approximation is controlled only if it names a small parameter and bounds what
    it drops; a fluctuating field may be replaced by its saddle point ONLY IF it can
    be integrated out exactly.
  * The task-background document is fed as cached context. Section 2 may be drawn on
    as inspiration but not as a wholesale shortcut (see SYSTEM_INSTRUCTIONS).
  * Server-side tools are AVAILABLE but governed via the ENABLE_* flags. The model may
    NOT claim a numerical/symbolic verification it did not actually run with a tool.
  * Re-running resumes from raw_outputs.json. Because the prompts define the design, a
    state written under a different DESIGN_VERSION is refused, not mixed.
"""

import json
import os
import shutil
import subprocess
from pathlib import Path

import anthropic


# -- Configuration -----------------------------------------------------------

API_KEY = ""              # or set ANTHROPIC_API_KEY in the environment
MODEL = "claude-opus-4-8"
EFFORT = "high"           # low | medium | high | xhigh | max  (xhigh/max: Opus-tier)
MAX_TOKENS = 64000        # streaming ceiling per segment
DISPLAY_THINKING = "summarized"   # "summarized" folds reasoning into the transcript

HERE = Path(__file__).resolve().parent
RUN_DIR = HERE / "output"
TASK_BACKGROUND = HERE / "task_background.tex"

# Governed tool access. Web tools are present-but-rare; code execution is opt-in.
# Including code execution ALONGSIDE the _20260209 web tools is discouraged (two
# execution environments confuse the model), so the two are kept mutually exclusive:
# enable code execution only for a run where you expect symbolic checks and no web
# reading. With code execution OFF, the model may not claim numerical verification.
ENABLE_WEB = True
ENABLE_CODE = False
MAX_TOOL_CONTINUATIONS = 8   # safety bound on the server-tool pause_turn loop

# Bumped when the prompts/design change. A saved state with a different version is
# refused on resume rather than silently mixed with new prompts.
DESIGN_VERSION = "6-no-strengthen"

# -- The referee's outcome vocabulary ----------------------------------------
# Ordered worst -> best. The author advances past the referee only if the outcome
# is at least THRESHOLD; otherwise the strategy is revised (up to
# MAX_ATTEMPTS_PER_STRATEGY) and then abandoned for the next-ranked one.
OUTCOME_ORDER = ["incorrect", "unjustified", "plausible", "controlled", "exact"]
OUTCOME_RANK = {name: i for i, name in enumerate(OUTCOME_ORDER)}
THRESHOLD = "plausible"
MAX_ATTEMPTS_PER_STRATEGY = 2   # one initial attempt + at most one feedback-driven retry
MAX_STRATEGIES = 2

# Which rounds belong to which conversation. The author chain and the referee chain
# are kept SEPARATE: the referee is isolated (it never sees the author's chain), but
# it does see its own earlier critiques. Cross-pollination happens only by injecting
# finalized text (the author's argument into the referee prompt; the referee's
# feedback into the author's retry prompt).
EXECUTOR_KINDS = {"brainstorm", "develop", "render"}
REFEREE_KINDS = {"referee"}


SYSTEM_INSTRUCTIONS = """\
You are an expert in condensed-matter QFT: bilocal / collective-field (G-Sigma)
methods, Fermi-surface bosonization, coadjoint-orbit and noncommutative (Moyal) field
theory, and the G-Sigma bilocal-field construction.

The task-background document has two sections. Section 1 fixes the bilocal G-Sigma
action of a free, gapless Fermi gas (the STARTING POINT), with conventions and saddle.
Section 2 writes down a PROPOSED coadjoint-orbit bosonization action.

CLAIM UNDER TEST: that Section 1 reduces DIRECTLY to Section 2's action. ADJUDICATE it;
do not assume it. Section 2 is a proposal -- not established, not necessarily true, not
a required endpoint. Reaching it is NOT success; a correct verdict is. Decide, by honest
analysis, whether the reduction holds and under exactly what conditions. A
confidently-wrong derivation that reaches Section 2 by glossing a step is the WORST
outcome -- worse than an honest "it does not go through, and here is where."

STANDARD OF RIGOR (binding; defaults to REJECT). Label every step exact, controlled,
plausible, or unjustified. CONTROLLED needs all of: (a) a named dimensionless small
parameter, (b) a stated/computed bound that the dropped piece is higher order in it,
(c) that the parameter is small in the regime of interest. PLAUSIBLE needs a concrete
physical argument or partial evidence genuinely supporting the step (state it); it is
strictly weaker than controlled, and a bare assertion does not earn it. Replacing a
fluctuating field by its saddle value is allowed ONLY IF that field integrates out
EXACTLY (Gaussian, or an exactly doable Lagrange-multiplier integral); otherwise it is
uncontrolled and FORBIDDEN. "Standard", "well known", "mean-field is exact" (unproven),
"in the appropriate limit", or "to leading order" (no explicit parameter+bound) do NOT
justify a step. This applies independently to BOTH eliminating Sigma AND any
restriction of G to the orbit.

OUTCOMES. A candidate derivation is adjudicated into exactly one of the following,
ordered worst -> best:
  - incorrect   : a load-bearing step is false, the argument is circular, or it
                  substitutes the Section-2 route -- the claim is not established by
                  this argument.
  - unjustified : the bridge closes only by leaning on one or more bare assumptions,
                  neither controlled nor made plausible by a concrete argument.
  - plausible   : the bridge closes; its uncontrolled step(s) are not proven, but each
                  is made genuinely plausible by a concrete physical argument or partial
                  evidence, not left as a bare assumption.
  - controlled  : every step is exact or a controlled approximation.
  - exact       : every load-bearing step is exact -- a complete rigorous bridge from
                  Section 1 to the Section-2 action.
Compute the outcome from the steps, not from the prose you would like to write. An
outcome can NEVER be improved by rewording -- only by changing the mathematics.

GROUND RULES. The spine must DIRECTLY transform the Section-1 action; borrow Section-2
identities/results as inspiration only -- do not substitute its route, restate its
result as derived, or detour through the microscopic free-fermion action. Justify every
step and name the identity it rests on; flag every approximate/heuristic/
convention-dependent step. Never claim a check you did not run: "verified
numerically/symbolically" requires an ACTUAL code-execution tool THIS session, else
label it by-hand.

TOOLS (sparingly; most rounds need none). A code tool, if present, is only for checking
algebra you already reasoned out (Tr ln expansions, Moyal->Poisson bookkeeping,
scalings, index algebra) -- never to search for the derivation -- and is the ONLY
license for "verified numerically". Web tools, if present, are a rare last resort to
read a PUBLISHED paper for a technique/identity (search by topic, then fetch/read);
never search for a conclusion or worked derivation, never retrieve the proposed
derivation; cite any paper used.

FORMAT: in every round except the final render round, write standard self-contained
LaTeX for a stock Markdown/MathJax engine with NO custom macros -- expand the
task-background shorthands (\\Tr -> \\operatorname{Tr}; \\bx -> \\boldsymbol{x};
\\psib -> \\bar\\psi; \\dd -> \\mathrm{d}; \\Moyal{A}{B} -> \\{A,B\\}_{\\mathrm{M}};
\\coloneqq -> :=). The render round gives its own LaTeX rules.
"""


# -- Round 1: brainstorm (unchanged) -----------------------------------------

BRAINSTORM_PROMPT = f"""Determine whether the Section-1 G-Sigma action reduces directly
to Section 2's coadjoint-orbit action, and under what conditions -- testing the claim,
not assuming it.

Propose the {MAX_STRATEGIES} most promising strategies for a DIRECT bridge. For each,
give the key technical move (how the saddle's Fermi-sea projector, the orbit
parametrization of the bilocal G, a Wigner/Moyal map, and the -Tr ln expansion would
produce the Berry/Wess-Zumino and Hamiltonian terms) and the main obstruction (say
whether it looks fundamental or merely technical). Rank them S1 (most promising) down to
S{MAX_STRATEGIES}; a later round develops them one at a time, in that order."""


# -- Round 2: develop (the author) -------------------------------------------

def _ordinal_word(rank: int) -> str:
    return {1: "top-ranked", 2: "second-ranked", 3: "third-ranked",
            4: "fourth-ranked", 5: "fifth-ranked"}.get(rank, f"rank-{rank}")


_STEP_CLASSIFY = (
    "Label each step: exact (an identity); controlled (named small parameter + bound on "
    "what is dropped + smallness in the regime); plausible (a concrete argument or partial "
    "evidence supports it, stated); or unjustified.\n"
)

# Shared single-token verdict contract for the referee round.
_STATUS_LINE = (
    "End with exactly one line, nothing after it: `STATUS: <token>`, where <token> is "
    "EXACTLY ONE of exact, controlled, plausible, unjustified, incorrect (one token only)."
)


def develop_prompt(rank: int, attempt: int, referee_feedback: str) -> str:
    """The author's prompt: first attempt at a strategy, or a feedback-driven retry."""
    ordinal = _ordinal_word(rank)
    if attempt == 1:
        return (
            f"Develop your {ordinal} strategy as a genuine, rigorous, step-by-step "
            "derivation. EXECUTION only -- carry it as far as it honestly goes; do not "
            "self-judge (an independent referee adjudicates next).\n\n"
            + _STEP_CLASSIFY +
            "Do not manufacture justifications, and do not take an uncontrolled step (e.g. a "
            "saddle substitution for a field you cannot integrate out exactly) and proceed "
            "as if exact. If a step breaks, stop there, name it, and say why (technical or "
            "fundamental). Build the strongest honest version; follow the tool policy and "
            "macro-free LaTeX rules."
        )
    return (
        f"A referee did NOT find your previous attempt at your {ordinal} strategy at least "
        f"`plausible` (attempt {attempt} of {MAX_ATTEMPTS_PER_STRATEGY}). Its weak point and "
        "food for thought:\n\n"
        "----- REFEREE FEEDBACK -----\n" + referee_feedback + "\n----- END FEEDBACK -----\n\n"
        "Fix the SUBSTANCE of the pinpointed step (repair, re-route, or concede it plainly "
        "-- do not relabel to dodge the critique); re-derive every affected part, keep the "
        "rest. Re-label each step:\n\n" + _STEP_CLASSIFY
    )


# -- Round 3: referee (the isolated adversary) -------------------------------

def referee_prompt(argument: str, attempt: int) -> str:
    """The isolated referee's prompt: judge ONLY the author's finalized argument."""
    return (
        "You are an INDEPENDENT ADVERSARIAL REFEREE. A separate author produced the "
        "candidate below (claim: the Section-1 G-Sigma action reduces directly to Section "
        "2's coadjoint-orbit action). You see only their finalized argument and your own "
        "earlier critiques. Try to BREAK it.\n\n"
        f"----- AUTHOR'S DERIVATION (attempt {attempt}) -----\n"
        + argument +
        "\n----- END DERIVATION -----\n\n"
        "Check, with evidence: (a) is each load-bearing step truly what it is labeled -- "
        "exact / controlled (real parameter + bound + smallness) / plausible (a concrete "
        "argument) / merely asserted? re-derive any you doubt; reject unbounded or "
        "\"standard\" justifications. (b) is it a DIRECT transform of the Section-1 action, "
        "or does it smuggle in / restate Section 2's route? (c) does any \"verified\" check "
        "correspond to a real tool run this session? (d) for each uncontrolled step, is the "
        "plausibility genuine or decorative?\n\n"
        "Classify the WHOLE candidate: incorrect (a step false/circular, or substitutes "
        "Section 2's route); unjustified (closes only on bare assumptions); plausible "
        "(closes; uncontrolled steps made genuinely plausible); controlled (every step "
        "exact or controlled); exact (every step exact).\n\n"
        "REQUIRED: (1) PINPOINT the single weakest load-bearing step and why it is binding; "
        "(2) give concrete FOOD FOR THOUGHT -- what specifically must change to improve the "
        "outcome, or why it cannot be done.\n\n"
        + _STATUS_LINE
    )


# -- Render round (runs once a strategy clears the bar) ----------------------

_RENDER_BODY = r"""Emit a COMPLETE compilable document: \documentclass, a standard preamble, \begin{document} ... \end{document}.

- Self-contained: state the G-Sigma starting point and the proposed coadjoint-orbit action up front, inlining every definition used (conventions; star product / Moyal bracket and pairing; base distribution f_0; the action S = S_WZW + S_H), then carry the reduction step by step. Do NOT mention a referee, rounds, checkpoints, "Section 1/2", or any adjudication.
- No meta-commentary about checking or repairing; fold the results (linearized Lindhard/RPA at quadratic order, the Kirillov-Kostant-Souriau Berry term, the nonlinear Moyal structure) into their natural place.
- Justify each step and name the identity it rests on; for a controlled approximation state its small parameter and what it drops; for a merely plausible step mark it and state the supporting argument. End with a "Caveats / status of approximations" section. Preserve every equation of the derivation as judged.
- LaTeX: a standard preamble (amsmath, amssymb, amsthm, mathtools, microtype, parskip, hyperref[hidelinks]) is fine, but NO custom macros (no \newcommand/\def/\DeclareMathOperator, no task-background shorthands) -- write every symbol in full (\operatorname{Tr}, \boldsymbol{x}, \mathrm{d}, \bar\psi, \{A,B\}_{\mathrm{M}}, \coloneqq). Output ONLY the document: nothing before \documentclass or after \end{document}, no code fences."""


def render_prompt(outcome: str, caveats: str) -> str:
    """Render the judged derivation as a self-contained LaTeX deliverable.

    `caveats` (the surviving uncontrolled steps) is passed non-empty ONLY for a
    `plausible` outcome; for `exact`/`controlled` it is empty, so a clean result is not
    handed a referee's mandatory weakest-step note to typeset as a spurious caveat.
    """
    preamble = (
        "A referee judged this derivation `" + outcome + "`. Render it as a SELF-CONTAINED "
        "LaTeX document (the deliverable, compiled with pdflatex). Status handling: `exact` "
        "-> present as a complete rigorous derivation; `controlled` -> complete to a "
        "controlled order, stating each approximation's small parameter and what it drops; "
        "`plausible` -> say so prominently at the top (a boxed \"Status: plausible\" note) "
        "and list every uncontrolled step up front, NOT claiming a complete rigorous "
        "derivation.\n\n"
    )
    if caveats.strip():
        preamble += (
            "Fold these still-flagged steps into the top status note and the closing "
            "caveats, in your own words (do not mention the referee):\n\n"
            "----- FLAGGED STEPS -----\n" + caveats + "\n----- END -----\n\n"
        )
    return preamble + _RENDER_BODY


# -- Helpers -----------------------------------------------------------------

def save_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_status(text: str) -> str:
    """Return the text after the last 'STATUS:' line (stripped), or '' if none."""
    found = ""
    for line in text.splitlines():
        s = line.strip().lstrip("*->#").strip()
        if s.upper().startswith("STATUS:"):
            found = s.split(":", 1)[1].strip()
    return found


def normalize_outcome(raw: str) -> str:
    """Map a STATUS payload to ONE OUTCOME_ORDER token, or '' if it is not a single
    clean verdict.

    Strict by design: a menu echo ("exact | controlled | ..."), a hedged answer
    ("exact? not quite"), or any compound/multi-word payload returns '' so the caller
    can reprompt -- rather than the old prefix match silently reading it as a verdict
    (and, because the menu is listed best-first, as the BEST one).
    """
    s = raw.strip().lower().strip("`*.,;:\"'()[]{} ")
    s = s.replace("_", "-").replace(" ", "-")
    if not s:
        return ""
    # A real verdict is a single token: reject menus / lists / compound answers.
    if any(sep in s for sep in ("|", "/", ",")):
        return ""
    if s in ("plausible", "plausible-by-analogy", "by-analogy"):
        return "plausible"
    return s if s in OUTCOME_RANK else ""


def referee_outcome(entry) -> str:
    """The normalized outcome a referee round reported ('' if none)."""
    return normalize_outcome(parse_status(entry.get("output_text", "")))


def meets_threshold(outcome: str) -> bool:
    return outcome in OUTCOME_RANK and OUTCOME_RANK[outcome] >= OUTCOME_RANK[THRESHOLD]


def rounds_of(state, kind: str) -> list:
    """All recorded rounds of a given kind, in order."""
    return [e for e in state["rounds"] if e.get("kind") == kind]


def history_for(rounds, kinds) -> list:
    """Reconstruct one conversation (executor or referee) from completed rounds."""
    messages = []
    for entry in rounds:
        if entry.get("kind") in kinds:
            messages.append({"role": "user", "content": entry["user_prompt"]})
            messages.append({"role": "assistant", "content": entry["output_text"]})
    return messages


# Banners whose enclosed derivation is elided from the REFEREE chain's replayed
# history: the referee re-reads its own prior critiques, not the full author text it
# already judged once (which it does not need again and which costs many tokens).
_ELIDE_BANNERS = [
    ("----- AUTHOR'S CANDIDATE DERIVATION", "----- END AUTHOR'S CANDIDATE DERIVATION -----"),
]


def _elide_embedded(prompt: str) -> str:
    """Replace an embedded derivation block with a short stub, keeping the surround."""
    for start, end in _ELIDE_BANNERS:
        i = prompt.find(start)
        j = prompt.find(end)
        if i != -1 and j > i:
            prompt = (prompt[:i]
                      + "[derivation under review omitted from history to save context; "
                        "your critique of it follows]"
                      + prompt[j + len(end):])
    return prompt


def referee_history(rounds) -> list:
    """The isolated referee conversation: prior referee turns, with the bulky author
    derivation each embedded elided (the critiques carry forward, the re-read of
    already-judged text does not). The CURRENT argument is in the live prompt, in full
    -- only prior turns are trimmed.
    """
    messages = []
    for entry in rounds:
        if entry.get("kind") in REFEREE_KINDS:
            messages.append({"role": "user", "content": _elide_embedded(entry["user_prompt"])})
            messages.append({"role": "assistant", "content": entry["output_text"]})
    return messages


def tail_history(rounds, strategy, attempt) -> list:
    """Executor history for the render round: brainstorm + ONLY the winning develop (the
    exact one the referee judged). Excludes the failed strategies' derivations -- to save
    tokens and to remove the ambiguity of which derivation 'the derivation as judged'
    refers to.
    """
    messages = []
    for entry in rounds:
        kind = entry.get("kind")
        keep = (kind == "brainstorm"
                or (kind == "develop"
                    and entry.get("strategy") == strategy
                    and entry.get("attempt") == attempt))
        if keep:
            messages.append({"role": "user", "content": entry["user_prompt"]})
            messages.append({"role": "assistant", "content": entry["output_text"]})
    return messages


# Sent when a judge round's STATUS line cannot be parsed to a single verdict token:
# a cheap one-shot nudge for just the token, so a malformed verdict is not silently
# read as below-threshold (which would burn an attempt or discard a passing result).
STATUS_REPROMPT = (
    "Your reply had no parseable verdict. Reply with EXACTLY one line and nothing else: "
    "`STATUS: <token>`, token one of exact, controlled, plausible, unjustified, incorrect."
)


def strip_code_fences(text: str) -> str:
    """Drop a leading ```/```latex fence and a trailing ``` if the model added them."""
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()[1:]                       # drop opening fence
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]                           # drop closing fence
        t = "\n".join(lines)
    return t.strip()


def compile_pdf(tex_path: Path) -> bool:
    """Compile <tex> to PDF with pdflatex (twice, to resolve cross-references).

    Best-effort: if pdflatex is absent or the source fails to compile, the .tex is
    still kept and a warning is printed. Returns True iff a PDF was produced.
    """
    pdflatex = shutil.which("pdflatex")
    if not pdflatex:
        print("[warning] pdflatex not found; wrote .tex only, skipped PDF.")
        return False
    proc = None
    for _ in range(2):
        proc = subprocess.run(
            [pdflatex, "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
            cwd=tex_path.parent, capture_output=True, text=True,
        )
    if proc.returncode != 0:
        log = tex_path.with_suffix(".log")
        errs = []
        if log.exists():
            errs = [ln for ln in log.read_text(encoding="utf-8", errors="ignore").splitlines()
                    if ln.startswith("!")]
        print("[warning] pdflatex failed; .tex kept. First error: "
              + (errs[0] if errs else "see derivation.log"))
        return False
    return True


def build_tools() -> list:
    """Server-side tools, governed by the ENABLE_* flags (see Configuration)."""
    if ENABLE_CODE and not ENABLE_WEB:
        return [{"type": "code_execution_20260120", "name": "code_execution"}]
    tools = []
    if ENABLE_WEB:
        tools += [
            {"type": "web_search_20260209", "name": "web_search"},
            {"type": "web_fetch_20260209", "name": "web_fetch"},
        ]
    if ENABLE_CODE:
        tools += [{"type": "code_execution_20260120", "name": "code_execution"}]
    return tools


def build_system() -> list:
    """Instructions + the task-background document, as cached system blocks."""
    if not TASK_BACKGROUND.exists():
        raise SystemExit(f"Task-background document not found: {TASK_BACKGROUND}")
    doc = TASK_BACKGROUND.read_text(encoding="utf-8")
    return [
        {"type": "text", "text": SYSTEM_INSTRUCTIONS},
        {
            "type": "text",
            "text": (
                "TASK-BACKGROUND DOCUMENT (LaTeX source; context, the claim under "
                "test, and permitted inspiration -- not a wholesale shortcut):\n\n" + doc
            ),
            "cache_control": {"type": "ephemeral"},
        },
    ]


# -- Core --------------------------------------------------------------------

def run_round(client, history, user_prompt, system, tools):
    """Run one round to completion and return (text, thinking, usage, stop_reason).

    A round may span several segments if the model invokes a server-side tool:
    such a call ends a segment with stop_reason == "pause_turn", after which we
    re-send (the server resumes automatically) until the turn ends. We keep the
    full content blocks locally for that continuation, but return only the
    accumulated VISIBLE text for cross-round chaining.
    """
    work = list(history) + [{"role": "user", "content": user_prompt}]
    text_parts, thinking_parts = [], []
    usage = None
    stop_reason = None

    for _ in range(MAX_TOOL_CONTINUATIONS + 1):
        with client.messages.stream(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system,
            messages=work,
            tools=tools,
            thinking={"type": "adaptive", "display": DISPLAY_THINKING},
            # `output_config` (effort) and top-level `cache_control` are real API
            # fields but are not yet typed kwargs in anthropic SDK 0.106, so the
            # typed method rejects them; forward them as raw body fields instead.
            extra_body={
                "output_config": {"effort": EFFORT},
                "cache_control": {"type": "ephemeral"},  # cache the growing prefix
            },
        ) as stream:
            for event in stream:
                if event.type == "content_block_delta" and event.delta.type == "text_delta":
                    print(event.delta.text, end="", flush=True)
            message = stream.get_final_message()

        usage = message.usage
        stop_reason = message.stop_reason
        for b in message.content:
            if b.type == "text" and b.text:
                text_parts.append(b.text)
            elif b.type == "thinking" and getattr(b, "thinking", ""):
                thinking_parts.append(b.thinking)
            elif b.type == "server_tool_use":
                print(f"\n[tool: {b.name} {json.dumps(b.input)[:120]}]")

        if stop_reason != "pause_turn":
            break
        # Server paused after a tool call; append the turn and let it resume.
        work.append({"role": "assistant", "content": message.content})

    print()
    return "\n".join(text_parts).strip(), "\n".join(thinking_parts).strip(), usage, stop_reason


def append_round(state, state_path, round_number, kind, prompt, result, **meta):
    """Record a completed round to the on-disk state (with optional round metadata)."""
    text, thinking, usage, stop_reason = result
    if stop_reason == "max_tokens":
        print(f"[warning] round {round_number} ({kind}) hit max_tokens; output may be truncated.")
    entry = {
        "round": round_number,
        "kind": kind,
        "user_prompt": prompt,
        "thinking_text": thinking,
        "output_text": text,
        "usage": usage.model_dump(mode="json"),
        "stop_reason": stop_reason,
    }
    entry.update(meta)
    print(
        f"[round {round_number}:{kind}] in={usage.input_tokens} "
        f"cache_read={usage.cache_read_input_tokens} out={usage.output_tokens} "
        f"stop={stop_reason}"
    )
    state["rounds"].append(entry)
    save_json(state_path, state)


def main() -> None:
    api_key = API_KEY or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("Set API_KEY in this file, or ANTHROPIC_API_KEY in the env.")

    client = anthropic.Anthropic(api_key=api_key)
    system = build_system()
    tools = build_tools()

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    state_path = RUN_DIR / "raw_outputs.json"

    if state_path.exists():
        state = load_json(state_path)
        if state.get("design_version") != DESIGN_VERSION:
            raise SystemExit(
                f"{state_path} was written under design "
                f"{state.get('design_version')!r}, but this script is "
                f"{DESIGN_VERSION!r}. The cached rounds use different prompts and must "
                f"not be mixed with the new design. Remove or archive it, then re-run:"
                f"\n    rm {state_path}"
            )
    else:
        state = {"model": MODEL, "design_version": DESIGN_VERSION, "rounds": []}

    def run_and_record(kind, prompt, kinds_for_history, label=None, history=None, **meta):
        """Run the next round in the appropriate conversation and checkpoint it.

        `history` overrides the default kind-filtered reconstruction; the render round
        passes a trimmed winning-derivation history (see tail_history).
        """
        n = len(state["rounds"]) + 1
        print(f"\n=== Round {n}: {label or kind} ===")
        if history is None:
            history = history_for(state["rounds"], kinds_for_history)
        result = run_round(client, history, prompt, system, tools)
        append_round(state, state_path, n, kind, prompt, result, **meta)
        return state["rounds"][-1]

    def run_judge(kind, prompt, label, **meta):
        """Run an isolated referee round. If the verdict does not parse
        to a single STATUS token, reprompt ONCE for just the token (so a malformed
        verdict is not silently read as below-threshold), then checkpoint as one round.
        """
        n = len(state["rounds"]) + 1
        print(f"\n=== Round {n}: {label} ===")
        history = referee_history(state["rounds"])
        text, thinking, usage, stop = run_round(client, history, prompt, system, tools)
        if not normalize_outcome(parse_status(text)):
            print("\n[verdict unparseable; reprompting once for a single STATUS token]")
            followup = history + [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": text},
            ]
            t2, th2, _u2, _s2 = run_round(client, followup, STATUS_REPROMPT, system, tools)
            if t2.strip():
                text = (text + "\n\n" + t2).strip()
                thinking = "\n\n".join(p for p in (thinking, th2) if p)
        append_round(state, state_path, n, kind, prompt, (text, thinking, usage, stop), **meta)
        return state["rounds"][-1]

    # -- Round 1: brainstorm (author) ----------------------------------------
    if not rounds_of(state, "brainstorm"):
        run_and_record("brainstorm", BRAINSTORM_PROMPT, EXECUTOR_KINDS, label="brainstorm")

    # -- Rounds 2-3: develop <-> referee loop over the ranked strategies -------
    # The next action is derived from the recorded rounds, so the loop is naturally
    # resumable: on restart it reconstructs its position and continues.
    winner = None
    while True:
        cleared = [e for e in rounds_of(state, "referee") if meets_threshold(referee_outcome(e))]
        if cleared:
            winner = cleared[0]   # the loop breaks on the first clear; [0] is that one
            break

        devs = rounds_of(state, "develop")
        if not devs:
            action = ("develop", 1, 1, "")            # strategy 1, attempt 1
        else:
            last = devs[-1]
            rank, attempt = last.get("strategy", 1), last.get("attempt", 1)
            refs = [e for e in rounds_of(state, "referee")
                    if e.get("strategy") == rank and e.get("attempt") == attempt]
            if not refs:
                action = ("referee", rank, attempt, last["output_text"])
            elif attempt < MAX_ATTEMPTS_PER_STRATEGY:
                action = ("develop", rank, attempt + 1, refs[-1]["output_text"])
            elif rank < MAX_STRATEGIES:
                action = ("develop", rank + 1, 1, "")  # abandon strategy; next-ranked
            else:
                action = None                          # every strategy exhausted

        if action is None:
            break

        kind, rank, attempt, payload = action
        if kind == "develop":
            run_and_record(
                "develop", develop_prompt(rank, attempt, payload), EXECUTOR_KINDS,
                label=f"develop S{rank} attempt {attempt}", strategy=rank, attempt=attempt,
            )
        else:
            entry = run_judge(
                "referee", referee_prompt(payload, attempt),
                f"referee S{rank} attempt {attempt}", strategy=rank, attempt=attempt,
            )
            print(f"[referee outcome: {referee_outcome(entry) or 'unparseable'}]")

    # -- Resolve the outcome and set the verdict ------------------------------
    if winner is None:
        all_ref = rounds_of(state, "referee")
        final_outcome = max((referee_outcome(e) for e in all_ref),
                            key=lambda o: OUTCOME_RANK.get(o, -1), default="")
        print(f"\nAll strategies exhausted; best referee outcome: {final_outcome or 'none'}.")
    else:
        final_outcome = referee_outcome(winner)
        print(f"\nThreshold met: referee outcome `{final_outcome}` on strategy "
              f"S{winner.get('strategy')}.")

    state["verdict"] = final_outcome or None
    save_json(state_path, state)
    if final_outcome not in OUTCOME_RANK:
        print("[warning] final STATUS missing or unparseable; treating as not-rendered.")

    # -- Render round: only when the final outcome clears the threshold --------
    do_render = (winner is not None and meets_threshold(final_outcome)
                 and not rounds_of(state, "render"))
    if do_render:
        # A `plausible` result carries the referee's flagged steps into the caveats;
        # exact/controlled renders clean (empty caveats).
        caveats = (winner["output_text"]
                   if OUTCOME_RANK[final_outcome] == OUTCOME_RANK[THRESHOLD] else "")
        run_and_record(
            "render", render_prompt(final_outcome, caveats), EXECUTOR_KINDS,
            label=f"render (outcome={final_outcome})",
            history=tail_history(state["rounds"], winner.get("strategy"), winner.get("attempt")),
        )

    # -- Deliverable -----------------------------------------------------------
    tex_path = RUN_DIR / "derivation.tex"
    pdf_path = RUN_DIR / "derivation.pdf"
    pdf_ok = False
    render_entry = next((e for e in reversed(state["rounds"]) if e.get("kind") == "render"), None)
    # Materialize the .tex only if a render round exists AND the final outcome still
    # clears the threshold -- so a stale render from an earlier run does not leave a
    # derivation contradicting a now-below-threshold verdict.
    if render_entry and meets_threshold(final_outcome):
        derivation = strip_code_fences(render_entry["output_text"])
        tex_path.write_text(derivation + "\n", encoding="utf-8")
        pdf_ok = compile_pdf(tex_path)
        rendered = True
    else:
        rendered = False
        # Keep the output set faithful to a non-rendering outcome: no stale derivation
        # should linger when the claim was not (even plausibly) established.
        for p in (tex_path, pdf_path):
            if p.exists():
                p.unlink()

    # -- Human-readable transcript --------------------------------------------
    verdict = state.get("verdict")
    parts = ["# Transcript: G-Sigma -> coadjoint-orbit bosonization (adjudication)",
             "", f"**Final verdict:** {verdict or 'unparseable'}", ""]
    for entry in state["rounds"]:
        label = f"Round {entry['round']} — {entry.get('kind', 'round')}"
        if entry.get("strategy"):
            label += f" (S{entry['strategy']}, attempt {entry.get('attempt')})"
        parts += [f"---\n\n# {label}", "", "## Prompt", "", entry["user_prompt"], ""]
        if entry.get("thinking_text"):
            parts += ["## Reasoning (summary)", "", entry["thinking_text"], ""]
        parts += ["## Response", "", entry["output_text"], ""]
    (RUN_DIR / "transcript.md").write_text("\n".join(parts) + "\n", encoding="utf-8")

    print(f"\nPipeline complete. Outputs in {RUN_DIR}/")
    print("  raw_outputs.json — full state + per-round usage + verdict")
    print("  transcript.md    — full conversation")
    if rendered:
        print(f"  derivation.tex   — self-contained derivation (verdict: {verdict})")
        print("  derivation.pdf   — compiled PDF" + ("" if pdf_ok else " (skipped; see warning)"))
    else:
        print(f"  (verdict: {verdict or 'unparseable'} — no derivation rendered; the "
              "adjudication rounds in transcript.md are the deliverable)")


if __name__ == "__main__":
    main()
