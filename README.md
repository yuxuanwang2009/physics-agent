# $G–\Sigma$ → Coadjoint-Orbit Bosonization: a Claim-Adjudication Agent

A small multi-round LLM agent (built on the Anthropic API) that **adjudicates** a
physics claim: whether the bilocal $G-\Sigma$ action of a free, gapless Fermi gas
reduces directly to the coadjoint-orbit bosonization action.

The full problem — conventions, the two endpoint actions, and why their equality is
nontrivial — lives in [`task_background.tex`](task_background.tex) (compiled:
`task_background.pdf`). In brief: **Section 1** derives the exact bilocal action
$S[G,\Sigma] = -\mathrm{Tr}\ln(G_0^{-1}+\Sigma) + \mathrm{Tr}(\Sigma G)$
and its free saddle; **Section 2** writes down the proposed coadjoint-orbit action
$S = S_{\mathrm{WZW}} + S_H$ — a Kirillov–Kostant–Souriau Berry term plus a Hamiltonian
term, on the coadjoint orbit of canonical transformations through the Fermi-sea
projector. Both are exact rewritings of the same free-fermion theory; whether one
*reduces to* the other is the open question. The agent's goal is a **correct verdict**,
not reaching the proposed action — a confidently-wrong derivation is the worst possible
outcome.

## Design of the agentic workflow

The harness ([`run.py`](run.py)) is deliberately minimal: the model does the physics;
the code only frames, chains, adjudicates, and renders. It runs an **author vs.
isolated-referee** loop under a binding standard of rigor.

1. **Brainstorm & rank.** Propose and rank up to two candidate strategies for a
   direct bridge.
2. **Develop (author).** Execute the top-ranked strategy as a rigorous, step-by-step
   derivation, labelling each step `exact` / `controlled` / `plausible` /
   `unjustified`. No self-judging.
3. **Referee (isolated adversary).** A *separate* conversation — it sees only the
   author's finalised argument and its own earlier critiques, never the author's
   reasoning — tries to break the derivation and returns one verdict, ordered
   worst→best: `incorrect < unjustified < plausible < controlled < exact`. It must
   pinpoint the single weakest step and give concrete, actionable feedback.
4. **Loop.** If the referee rates the argument at least `plausible`, the agent
   renders. Otherwise it revises the same strategy once (the referee's critique is
   fed back to the author), then falls through to the next-ranked strategy. If every
   strategy is exhausted, nothing is rendered and the best attempt plus the referee's
   post-mortem is the deliverable.
5. **Render.** The winning bridge is re-emitted as a self-contained LaTeX document
   (`derivation.tex`, compiled to `derivation.pdf`); a merely-`plausible` result is
   typeset but must flag its uncontrolled assumptions up front.

The **standard of rigor defaults to REJECT**: an approximation is *controlled* only if
it names a dimensionless small parameter, bounds what it drops, and shows the parameter
is small in the regime of interest; a fluctuating field may be replaced by its
saddle point only if it can be integrated out *exactly*. Author and referee live in
separate contexts so the effort to justify a step cannot quietly launder the verdict.
Every round is checkpointed to `output/raw_outputs.json` (re-running resumes), and a
human-readable `output/transcript.md` is emitted.

## Outcome

The agent reconstructs the intended bridge — parametrise $G$ on the orbit of the
Fermi-sea projector, use the conjugation-invariance of $-\mathrm{Tr}\ln$, and
Wigner–Moyal-map the result to recover the KKS/WZW Berry term and the Hamiltonian term
— and then, correctly, **declines to call it exact**. It pins the binding obstruction
to the **restriction of $G$ to the coadjoint orbit**: the clean Fermi surface is
gapless, so the transverse (off-orbit) particle–hole modes carry no protecting small
parameter, and the only parameter that controls the restriction (long wavelength,
$q/k_F \ll 1$) simultaneously truncates the Moyal product to its Poisson limit. The
honest verdict is that the reduction holds as a *controlled long-wavelength (Poisson)
effective theory*, **not** as an exact full-Moyal identity. When a strategy clears the
`plausible` bar it renders that conditional result — flagging the uncontrolled orbit
restriction up front — rather than overclaiming.

## A known imperfection

The accepted derivation leans on a step the referee passes only as `plausible`:
replacing $\Sigma$ by its (Dyson) saddle point to eliminate it. **That step is
unnecessary.** A cleaner, exact argument exists: along the coadjoint orbit the functional integral
$\int \mathcal{D}\tilde \Sigma e^{\mathrm{Tr}\ln(\tilde\Sigma) - \mathrm{Tr}(\tilde \Sigma G)}$
is invariant under $G \to \hat U G_0 \hat U^{-1}$, so the
conclusion follows regardless of $\Sigma$ — no saddle-point approximation required. The
agent settled for the weaker route instead of finding this one; its verdict is
defensible but its reasoning is not optimal. This is a real limitation, not a rendering
artifact.

## Running it

```bash
export ANTHROPIC_API_KEY=...   # or set API_KEY at the top of run.py
python run.py                  # artifacts land in output/
```
