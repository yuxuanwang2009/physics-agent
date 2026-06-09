# Transcript: G-Sigma -> coadjoint-orbit bosonization (adjudication)

**Final verdict:** plausible

---

# Round 1 — brainstorm

## Prompt

Determine whether the Section-1 G-Sigma action reduces directly
to Section 2's coadjoint-orbit action, and under what conditions -- testing the claim,
not assuming it.

Propose the 2 most promising strategies for a DIRECT bridge. For each,
give the key technical move (how the saddle's Fermi-sea projector, the orbit
parametrization of the bilocal G, a Wigner/Moyal map, and the -Tr ln expansion would
produce the Berry/Wess-Zumino and Hamiltonian terms) and the main obstruction (say
whether it looks fundamental or merely technical). Rank them S1 (most promising) down to
S2; a later round develops them one at a time, in that order.

## Reasoning (summary)

I'm setting up a problem about bridging two mathematical formulations—moving from a Section-1 action involving the G-Sigma functional to a Section-2 coadjoint-orbit action. The first section defines a free action with a specific trace formula involving the inverse propagator and self-energy terms, and I need to think through two distinct strategies for how these connect.

The core challenge is that Section 1 works with bilocal fields in full spacetime (two-time correlators), while Section 2 operates on equal-time phase-space distributions. Strategy A involves constraining G to the coadjoint orbit by parametrizing it as unitary conjugations of the bare propagator, then using the Dyson relation to eliminate Sigma and expand the resulting trace logarithm in gradients—this should produce the Berry phase and Hamiltonian terms via Wigner transform and Moyal star products. The technical subtlety is whether eliminating Sigma via its saddle-point equation is exact or approximate, since the action is nonlinear in Sigma through the logarithm term, making this a stationary-phase approximation rather than an exact integration. The core tension is that restricting $G$ to the coadjoint orbit—configurations of the form $U G_0 U^{-1}$—is a real approximation, not exact. Off-orbit fluctuations correspond to incoherent particle-hole excitations that aren't Slater determinants in any rotated basis, and they're only suppressed in controlled limits like large $N$ or the semiclassical regime where patch occupation becomes large. In a gapless Fermi liquid, the particle-hole continuum isn't gapped, so the orbit modes aren't parametrically separated from other excitations—this is the fundamental obstruction to the first strategy. The cleanest path forward is to eliminate $\Sigma$ via the Dyson saddle, restrict $G$ to the projector orbit, and then expand in Wigner/Moyal, accepting that this is controlled only under specific limits like large $N$.

The second strategy would instead insert a resolution of identity over the coadjoint group directly into the path integral, treating the collective $U(t)$ as a soft mode analogous to reparametrizations in SYK, and integrate out the massive amplitude directions at Gaussian level. Both approaches map onto the two canonical SYK strategies—the on-shell substitution versus the soft-mode insertion—and the mechanism for generating the WZW and Hamiltonian terms is now clear: when $G = U G_0 U^{-1}$ is substituted into $\operatorname{Tr}(G_0^{-1}G)$, the $\partial_\tau$ in $G_0^{-1}$ produces $U^{-1}\dot U$ terms (the Berry phase) and the Hamiltonian conjugation yields the energy functional, both of which survive the trace and appear in the final action after Wigner transformation. **S2: Collective-coordinate insertion via Faddeev–Popov over canonical transformations.** Rather than substituting the $\Sigma$ saddle, I insert a delta function selecting the orbit direction as an explicit collective coordinate, with the WZW term emerging as a Berry phase from the zero modes (canonical transformations) that are broken only by $\partial_\tau$ and $\hat h$. The transverse $(G,\Sigma)$ fluctuations integrate out at Gaussian level (RPA-style), though they're only parametrically massive in a controlled limit. The obstruction is the same pair — $\Sigma$ and transverse modes don't decouple exactly in a gapless system, and the WZ normalization isn't visible at strictly Gaussian order — but this approach makes the softness question explicit, which cuts to the heart of the fundamental problem. It's ranked below S1 because the Faddeev–Popov machinery, measure issues, and normalization details add complexity without removing the core obstruction, whereas S1 reaches the target action more directly and isolates the two load-bearing approximations more cleanly.

Both strategies ultimately face the same fundamental barrier: off-orbit fluctuations in a gapless system aren't parametrically suppressed, so the orbit restriction and $\Sigma$ saddle are stationary-phase approximations at best, not exact. The honest verdict is that a controlled reduction requires an explicit semiclassical or large-$N$ parameter; without it, the bridge between the two sections is plausible but not rigorous. I should flag upfront that the direct exact equivalence looks false — they're different exact rewritings of the same path integral, and equality holds only under controlled approximations.

## Response

## Framing: what a direct bridge must accomplish

Before proposing routes, note the structural gap the bridge must close, because it determines where every strategy will be stressed:

1. **Field content.** Section 1's $G(1,2)$ is a *two-time* bilocal carrying the full $1/(i\omega_n-\xi_{\boldsymbol k})$ frequency structure; Section 2's $f(\boldsymbol x,\boldsymbol p;t)$ is a *single-time* phase-space distribution. A bridge must collapse the relative-time/frequency content of $G$ onto an equal-time density matrix $\hat f(t)$.

2. **Two genuinely separate eliminations**, each of which the rigor standard scrutinizes independently:
   - **(E$_\Sigma$)** removing $\Sigma$ to get an action of $G$ (or of $U$) alone;
   - **(E$_\perp$)** restricting $G$ to the coadjoint orbit $G=\hat U G_0\hat U^{-1}$, i.e. discarding off-orbit ("amplitude"/incoherent) fluctuations.

3. **Algebra.** Section 2 keeps the *full Moyal* star; any $\operatorname{Tr}\ln$ gradient expansion must be argued to reproduce Moyal and not merely its Poisson truncation.

A useful preliminary computation (done by hand below, not yet verified by tool) shows the *target functional form is reachable* once (E$_\Sigma$) and (E$_\perp$) are granted — so the entire adjudication will hinge on the **status** of those two eliminations, not on whether the WZW/Hamiltonian terms "appear." I flag now that a fully *exact* bridge looks unlikely: Sections 1 and 2 are two different exact coherent-state rewritings, and their equality is at best a *controlled* statement requiring a semiclassical/large-$N$ parameter.

---

## The mechanism both strategies share (the part that does work)

Eliminating $\Sigma$ by the Dyson saddle (status: **to be adjudicated**, see obstructions) gives
$$
S[G] \;=\; \operatorname{Tr}\ln G \;-\; \operatorname{Tr}\!\big(G_0^{-1}G\big)\;+\;\text{const},
\qquad G_0^{-1}=-(\partial_\tau+\hat h).
$$
Restrict to the orbit $G=\hat U G_0\hat U^{-1}$ with $\hat U=e^{i\hat\phi}$ a (center-of-mass-time–dependent) single-particle unitary. Two facts:

- $\operatorname{Tr}\ln G=\operatorname{Tr}\ln(\hat U G_0\hat U^{-1})=\operatorname{Tr}\ln G_0=\text{const}$ — **exact** (similarity invariance of $\det$), so the entropy term carries no $U$-dependence.
- Using $\hat U^{-1}(\partial_\tau+\hat h)\hat U=\partial_\tau+\hat U^{-1}(\partial_\tau\hat U)+\hat U^{-1}\hat h\hat U$,
$$
-\operatorname{Tr}\!\big(G_0^{-1}G\big)\big|_{U\text{-dep}}
=\operatorname{Tr}\!\big[(\hat U^{-1}\partial_\tau\hat U)\,G_0\big]+\operatorname{Tr}\!\big[\hat h\,\hat U G_0\hat U^{-1}\big].
$$
Because $\hat h$ is instantaneous and $\partial_\tau$ pairs the two times, both traces collapse to **equal-time** objects: $G_0\to\hat f_0$ (the occupation/projector $\hat n$) and $\hat U G_0\hat U^{-1}\to\hat f=\hat U\hat f_0\hat U^{-1}$. After Wick rotation $\tau\to it$ and the Wigner transform ($\operatorname{Tr}\to\int \mathrm d^dx\,\mathrm d^dp/(2\pi)^d$, products $\to\star$),
$$
S \;\to\; \int\!\mathrm dt\,\big\langle f_0,\,U^{-1}\!\star i\partial_t U\big\rangle \;-\;\int\!\mathrm dt\,\big\langle f,\,\epsilon\big\rangle,
$$
i.e. exactly Section 2's $S_{\mathrm{WZW}}+S_H$. So the Berry/WZ term comes from the $\partial_\tau$ in $G_0^{-1}$ and the Hamiltonian term from $\hat h$; the $\operatorname{Tr}\ln$ entropy term drops. This mechanism is common to both strategies; they differ in *how they justify (E$_\Sigma$) and (E$_\perp$)*.

---

## S1 (most promising): on-shell orbit substitution + Wigner/Moyal expansion

**Key technical moves.**
1. (E$_\Sigma$) Substitute the Dyson saddle $\Sigma=G^{-1}-G_0^{-1}$ to obtain $S[G]=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)$.
2. (E$_\perp$) Insert $G=\hat U G_0\hat U^{-1}$; use the two exact identities above so that $\operatorname{Tr}\ln G$ drops and $-\operatorname{Tr}(G_0^{-1}G)$ yields the equal-time WZW + Hamiltonian pair.
3. Wigner-transform and Wick-rotate; track whether the gradient expansion delivers the *full* Moyal star (Section 2) or only Poisson.

**Main obstruction.** Two, both load-bearing:
- **(E$_\Sigma$) is a stationary-phase approximation, not exact — and this looks merely technical but is real.** Shifting $M=G_0^{-1}+\Sigma$, the $\Sigma$ integral is $\int \mathrm DM\,e^{\operatorname{Tr}\ln M-\operatorname{Tr}(MG)}=\int \mathrm DM\,(\det M)\,e^{-\operatorname{Tr}(MG)}$, which is *not* Gaussian and *not* a linear Lagrange-multiplier integral (the multiplier got buried inside $\operatorname{Tr}\ln$ when the fermions were integrated). Under the stated standard, replacing $\Sigma$ by its saddle is therefore **forbidden unless** a named small parameter bounds the fluctuation correction (e.g. large flavor number $N$, or particles-per-patch $\to\infty$). Status: **uncontrolled as written; controllable in principle** with an explicit $N$.
- **(E$_\perp$) restriction to the projector orbit is the *fundamental* obstruction.** The orbit consists of distributions with $f\star f=f$ (idempotents reachable from $\hat n$); generic low-energy $G$-fluctuations are *not* of this form (they are incoherent multi-pair excitations of the gapless particle–hole continuum). In SYK the analogous restriction to $\mathrm{Diff}(S^1)$ is controlled because the reparametrization modes are parametrically *soft* relative to a *gapped* remainder; **here the orbit modes sit inside an ungapped continuum**, so there is no automatic parametric separation. Suppression of off-orbit fluctuations requires a genuine semiclassical/large-$N$ limit ($\hbar\,\nabla_x\!\cdot\!\nabla_p\ll1$, $k_F\ell\gg1$, large patch occupation). Whether that limit also upgrades Poisson to the *full* Moyal star — which Section 2 insists on keeping — is a further open point. Status: **fundamental**; the best attainable verdict for S1 is "controlled" *only with* an explicitly supplied and bounded semiclassical/large-$N$ parameter, otherwise "plausible."

**Why ranked first.** It reaches Section 2's *exact functional form* by the shortest transparent computation, and — crucially for adjudication — it **isolates the two load-bearing approximations cleanly and separately**, with the entropy term provably inert. There are few places to hide a glossed step.

---

## S2: collective-coordinate / soft-mode insertion (SYK-style Faddeev–Popov on the orbit)

**Key technical moves.**
1. Do *not* substitute the $\Sigma$ saddle. Instead insert a resolution of identity over the canonical-transformation group, $1=\int \mathrm D\hat U\,\delta(\text{gauge})\,\Delta_{\mathrm{FP}}$, into $Z=\int \mathrm DG\,\mathrm D\Sigma\,e^{-S[G,\Sigma]}$, promoting the orbit direction $\hat U(t)$ to a collective coordinate of the saddle.
2. Identify canonical transformations as exact symmetries of $\operatorname{Tr}\ln(G_0^{-1})$ that are *explicitly broken* only by $\hat h$ and by $\partial_\tau$; the WZW term then arises as the Berry phase of these would-be zero modes, and $S_H$ as their explicit-breaking potential — the pseudo-Goldstone picture.
3. Integrate the transverse $(G,\Sigma)$ fluctuations at Gaussian (RPA) level; Wigner-transform the resulting $\hat U$-action.

**Main obstruction.**
- **The transverse and $\Sigma$ integrals are still not Gaussian-exact**, and now the **measure/Faddeev–Popov Jacobian** (the $\mathcal DG\,\mathcal D\Sigma\to\mathcal D\hat U\times$ transverse change of variables, flagged in the document's caveats) must be controlled — strictly more machinery than S1 with no reduction of the fundamental gap separation problem of (E$_\perp$).
- **WZW normalization / topological completion.** At strictly Gaussian order the KKS symplectic structure and the total-derivative/$\theta$-term subtleties of $S_{\mathrm{WZW}}$ (noted in the source caveats) are not visible; recovering the correct Wess–Zumino *extension* needs information beyond quadratic order. Status: same **fundamental** off-orbit obstruction as S1, *plus* extra technical (measure, normalization) hazards.

**Why ranked second.** It does make the central physics question — *which modes are soft, and relative to what gap* — explicit, which is valuable. But it carries heavier and more error-prone machinery (FP determinant, transverse spectrum, WZ normalization), giving more opportunities to smuggle in an unjustified step, while not removing the fundamental obstruction that S1 already exposes more cleanly.

---

## Ranking and plan

**S1 ≻ S2.** Both confront the *same* fundamental obstruction (off-orbit fluctuations are not parametrically gapped in a gapless Fermi system) and the *same* non-exact $\Sigma$-elimination; S1 isolates them with a shorter, more transparent computation in which the entropy term is provably inert, whereas S2 adds measure/normalization machinery without buying extra rigor.

**Provisional verdict orientation** (to be settled in the development rounds): a strictly *exact* direct reduction appears **false** — the two sections are inequivalent exact rewritings. The realistic ceiling is **controlled**, attainable only if a named semiclassical/large-$N$ parameter is supplied *and* shown to bound both off-orbit fluctuations and the $\Sigma$-saddle correction; absent that, the honest outcome is **plausible** at best, sliding to **unjustified** if (E$_\Sigma$) and (E$_\perp$) are asserted rather than argued. The next round develops **S1** first, scrutinizing (E$_\Sigma$) and (E$_\perp$) against the CONTROLLED criteria; then **S2**.

---

# Round 2 — develop (S1, attempt 1)

## Prompt

Develop your top-ranked strategy as a genuine, rigorous, step-by-step derivation. EXECUTION only -- carry it as far as it honestly goes; do not self-judge (an independent referee adjudicates next).

Label each step: exact (an identity); controlled (named small parameter + bound on what is dropped + smallness in the regime); plausible (a concrete argument or partial evidence supports it, stated); or unjustified.
Do not manufacture justifications, and do not take an uncontrolled step (e.g. a saddle substitution for a field you cannot integrate out exactly) and proceed as if exact. If a step breaks, stop there, name it, and say why (technical or fundamental). Build the strongest honest version; follow the tool policy and macro-free LaTeX rules.

## Reasoning (summary)

I'm setting up a careful algebraic derivation of the action functional, working through the trace and logarithm expansion step by step. I'll use computational tools to verify the trace identities and algebraic manipulations as I go, starting from the foundational expression and carrying it as far as the math honestly allows.

Now I'm examining which field to integrate out first. The action is linear in $\Sigma$ through the $\operatorname{Tr}(\Sigma G)$ term but nonlinear through the logarithm, so integrating out $G$ first would just collapse everything back to the free partition function via a delta functional constraint. Instead, I need to integrate out $\Sigma$ to get a meaningful effective action on $G$. The integral over $\Sigma$ isn't Gaussian because of the determinant factor from the logarithm, so I can't do it exactly—I have to use saddle-point approximation. At the saddle point, $\Sigma$ satisfies the Dyson equation, and substituting back gives the Luttinger-Ward effective action $S[G] = \operatorname{Tr}\ln G - \operatorname{Tr}(G_0^{-1}G)$ plus a constant. This elimination is a saddle-point approximation controlled by a small parameter—in systems like SYK, that parameter is the large-$N$ limit where the action scales with $N$, making the $1/N$ corrections to the saddle point small. For the $N$-flavor case, the integral becomes $\int dM\, e^{N(\operatorname{Tr}\ln M - \operatorname{Tr} MG)}$, which is now controlled by $1/N$ at the saddle point. Working through the toy model with the Gamma function confirms that the exact result and saddle-point approximation match at leading order in $N$, with corrections only at $O(\ln N/N)$. So introducing $N$ flavors provides the necessary control for eliminating $\Sigma$, though it does modify the theory — this is the standard collective-field large-$N$ approach, analogous to SYK. The physical interpretation is that this large-$N$ corresponds to the large number of fermions per patch in the Fermi-surface bosonization picture, or equivalently the semiclassical limit $\hbar \to 0$. Now I need to address the second approximation: restricting $G$ to the orbit and understanding what controls the off-orbit fluctuations. When I trace through the equal-time limit of $G_0$, the convergence factor picks out $G_0(\tau,\tau^+)$, which reduces to the occupation operator $\hat n = \hat f_0$. This means the traces involving $G_0$ collapse to integrals over time of spatial traces at equal time. For the kinetic term from $[\hat h, \hat U]$, I can use cyclicity to show that $\operatorname{Tr}([\hat h,\hat U]G_0\hat U^{-1})$ gives $\int d\tau[\operatorname{tr}(\hat h\hat f) - E_0]$, where $\hat f = \hat U\hat f_0\hat U^{-1}$ is the transformed occupation. Combining with the time-derivative term, the $U$-dependent part of $-\operatorname{Tr}(G_0^{-1}G)$ becomes $\int d\tau\,\operatorname{tr}(\hat U^{-1}(\partial_\tau\hat U)\hat f_0) + \int d\tau\,\operatorname{tr}(\hat h\hat f)$ plus constants, though I need to track the overall sign carefully through the Wick rotation to match Section 2's action.

When I Wick rotate to real time with $\tau = it$ and $\partial_\tau = -i\partial_t$, the factors of $i$ work out so that $\int d\tau\,\operatorname{tr}(\hat U^{-1}\partial_\tau\hat U\hat f_0) = \int dt\,\operatorname{tr}(\hat U^{-1}\partial_t\hat U\hat f_0)$, and the full action becomes $S_{real} = \int dt[\operatorname{tr}(\hat f_0\,\hat U^{-1}i\partial_t\hat U) - \operatorname{tr}(\hat f\hat h)]$, which matches exactly Section 2's first-quantized trace form after identifying $\hat h$ with the single-particle energy $\epsilon$. This confirms the orbit ansatz gives the right effective action through exact algebra, though the validity of eliminating $\Sigma$ via saddle-point is controlled by $1/N$ flavor expansion and represents a modification to the original model.

The deeper issue is that restricting to the orbit and dropping off-orbit fluctuations isn't justified by a spectral gap—both orbit and off-orbit modes live in the same gapless particle-hole continuum. The suppression of amplitude fluctuations (which deform the occupation spectrum away from projectors) relies instead on a semiclassical counting argument: in the large-occupation limit, creating particle-hole pairs that change local occupancy away from 0 or 1 is suppressed by factors of $1/N_{patch}$, where $N_{patch}$ is the number of fermions in a momentum-space patch. This is the standard bosonization argument but not rigorously controlled in a few steps, so I should mark it as plausible rather than proven.

On the $\operatorname{Tr}\ln G$ invariance: the claim that it's constant on the orbit rests on the similarity invariance of the trace, which is exact for finite-dimensional invertible operators but can develop an anomaly in infinite dimensions due to regularization. However, since my direct computation of the $-\operatorname{Tr}(G_0^{-1}G)$ term already produced the full WZW term matching Section 2's independent derivation, I'll treat $\operatorname{Tr}\ln G$ as exactly constant and note that any anomaly would only shift the overall normalization—a regularization-dependent caveat consistent with the document's existing note about WZW normalization. The equal-time projection $G_0 \to \hat f_0$ and the resulting WZW structure are legitimate, but the coefficient is exact only up to regularization choices.

Now I want to verify the core algebraic mechanism numerically: the identity $D\hat U D^{-1}\hat U^{-1} = 1 + [D,\hat U]D^{-1}\hat U^{-1}$ is exact linear algebra, and the collapse of the two-time structure to equal-time should follow directly. I'll set up a small discrete Matsubara lattice with antiperiodic boundary conditions, build the full matrices for $D$, $G_0$, and a time-dependent $\hat U(\tau)$, then compute both $-\operatorname{Tr}(G_0^{-1}G)$ and the predicted equal-time expression to verify they match.

Setting up a numerical verification... Writing numerical verification code... The equal-time Green's function on the lattice will have discretization artifacts, but the operator identity itself remains exact. The matching to the occupation number only works in the continuum limit, so numerically I'll see the predicted and computed gaps agree when I use the lattice equal-time Green's function as a proxy for occupation. I need to redefine things to account for this. Then verify the operator identity holds exactly using that definition, and demonstrate that $f_0^{lat}$ converges to the occupation number as the time step vanishes.

Now I'm setting up a concrete numerical test: a two-site system with one occupied and one empty orbital, diagonal single-particle Hamiltonian but non-diagonal interaction to generate off-diagonal structure in the propagator. I'll construct the imaginary-time grid with antiperiodic boundary conditions and implement the finite-difference time derivative operator with the proper antiperiodic wrapping. Now I'm computing the difference between the actual and baseline LHS values, then extracting the equal-time Green's function blocks from the diagonal to compare against the Fermi-Dirac distribution, accounting for potential shifts from the antiperiodic boundary conditions. I need to test the code to see how the error scales with the equal-time convention, and if there's a constant offset from the regularization, I'll document that caveat. Let me implement this now.

Writing the calculation code...
 The numerical verification shows the entropy term stays constant along the orbit as expected, and the discretization error in the equal-time derivative decreases proportionally with the timestep size, halving each time I double the number of steps.

Now I'll move on to Step 5 and examine the Wigner-Moyal formulation and the perpendicular energy component.

## Response

## Plan and scope

I develop **S1**: take Section 1's exact action, eliminate $\Sigma$, restrict $G$ to the projector orbit, and reduce the result by exact operator algebra + Wigner transform, labeling every step. I will do the central algebra by hand and then run **one** numerical check of the load-bearing operator identity (the WZW+Hamiltonian collapse), since that is the crux that earns or loses the "exact" labels.

Let me first state the algebra, then verify it.

---

## Step 0 — Starting action (exact)

From Section 1 with $S_{\mathrm{int}}=0$,
$$
Z=\int \mathcal D G\,\mathcal D\Sigma\; e^{-S[G,\Sigma]},\qquad
S[G,\Sigma]=-\operatorname{Tr}\ln\!\big(G_0^{-1}+\Sigma\big)+\operatorname{Tr}(\Sigma G),
$$
with $G_0^{-1}=-(\partial_\tau+\hat h)$, $\hat h=\varepsilon(-i\boldsymbol\nabla)-\mu$. **Status: exact** (this is the boxed Section-1 result, verbatim).

---

## Step 1 — Which field to eliminate (exact observation, with a warning)

In the free action $G$ appears **only linearly**, through $\operatorname{Tr}(\Sigma G)$. Hence integrating $G$ first is exact and gives a functional delta:
$$
\int\mathcal D G\,e^{-\operatorname{Tr}(\Sigma G)}\;\propto\;\prod_{1,2}\delta\!\big(\Sigma(2,1)\big)\;\Rightarrow\;\Sigma=0,\qquad Z=e^{\operatorname{Tr}\ln G_0^{-1}}=Z_{\rm free}.
$$
**Status: exact** — and it shows a structural fact I must respect: *exact* elimination of either field trivializes the theory back to $Z_{\rm free}$ with **no** orbit action. The coadjoint action therefore cannot arise from any exact integration; it can only arise from a **saddle in $\Sigma$ plus a constraint on $G$**. This already tells me the bridge cannot be "exact" in the strongest sense. I proceed with $\Sigma$-saddle.

---

## Step 2 — Eliminating $\Sigma$ (this is an approximation; here is its true status)

Shift $M:=G_0^{-1}+\Sigma$ (Jacobian $1$, exact):
$$
\int\mathcal D\Sigma\,e^{-S}=e^{\operatorname{Tr}(G_0^{-1}G)}\,I[G],\qquad
I[G]=\int\mathcal D M\;e^{\operatorname{Tr}\ln M-\operatorname{Tr}(M G)} .
$$
$I[G]$ contains $\operatorname{Tr}\ln M$ (i.e. a $\det M$ factor): it is **not Gaussian** and **not a linear Lagrange-multiplier integral**. The stationary point is the Dyson equation $M_\star=G^{-1}$, giving
$$
S_{\rm eff}[G]=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)+\text{const}.
\tag{2.1}
$$
Whether (2.1) is the *exact* answer for $I[G]$ is decided by the fluctuations of $M$ about $G^{-1}$. They are **not** negligible for a single species. A one-mode caricature ($\operatorname{Tr}\to$ scalar) makes this quantitative:
$$
\int_0^\infty\! dm\,e^{\ln m-mg}=\int_0^\infty\! dm\;m\,e^{-mg}=g^{-2},
\quad\text{but the saddle gives }\;e^{\ln g_\star^{-1}-1}=g^{-1}e^{-1}.
$$
The fluctuations change $g^{-1}\!\to\! g^{-2}$ — they correct the $G$-dependence at leading order. So **the $\Sigma$-saddle is uncontrolled as written.**

It becomes **controlled** only with a named small parameter. The standard one is $N$ identical flavors with a flavor-singlet bilocal: $S\to N\,S$, so $I[G]=\int\mathcal D M\,e^{N(\operatorname{Tr}\ln M-\operatorname{Tr} MG)}$. The same caricature now reads
$$
\int_0^\infty\! dm\,e^{N(\ln m-mg)}=\frac{\Gamma(N{+}1)}{(Ng)^{N+1}}
=\exp\!\big[\underbrace{-N\ln g-N}_{\text{saddle, }O(N)}\;+\;O(\ln N)\big],
$$
so the saddle reproduces the $O(N)$ action and the dropped piece is $O(\ln N/N)$ smaller. I will verify this scaling numerically below.

> **Label for Step 2:** **controlled, with the named parameter $1/N$ (number of fermion flavors)**, bound $O(\ln N/N)$, small for $N\gg1$. **Caveat that I will not hide:** this *modifies the model* (one flavor $\to$ $N$). For the genuine single-species free Fermi gas of Section 2 there is no such $N$, and Step 2 is then only **plausible**, resting on the expectation that the relevant physical control (large occupation per patch / semiclassics, Step 5) plays the role of $1/N$. I carry $N$ explicitly and flag where it is fictitious.

The result (2.1) is the free-fermion Luttinger–Ward / 2PI functional; from here I work with it.

---

## Step 3 — Restriction to the orbit (this is E$_\perp$; stated honestly as a restriction)

I now impose the ansatz from Section 1's "bridge": the low-energy $G$'s are images of the Fermi-sea projector under canonical transformations. As a **two-time** kernel this means
$$
G \;=\; \hat U\,G_0\,\hat U^{-1},\qquad \hat U=\hat U(\tau)=e^{i\hat\phi(\tau)}\ \text{(single-particle, time-local)} .
\tag{3.1}
$$
Its equal-time projection is $\hat U(\tau)\hat n\hat U^{-1}(\tau)=\hat f(\tau)$, matching Section 2's $f=U\star f_0\star U^{-1}$.

**This is a restriction of the integration domain, not an identity.** A general $\delta G$ about $G_0$ splits into orbit directions $\delta G_\parallel=[i\hat\phi,G_0]$ and transverse "amplitude" directions $\delta G_\perp$ that move the occupation eigenvalues off $\{0,1\}$ (so $\hat f^2\neq\hat f$). The quadratic action from (2.1) is
$$
\delta^2 S_{\rm eff}=-\tfrac12\operatorname{Tr}\!\big(G_0^{-1}\,\delta G\,G_0^{-1}\,\delta G\big),
$$
the inverse particle–hole propagator. **Both** $\delta G_\parallel$ and $\delta G_\perp$ live in the *same gapless* particle–hole continuum: there is **no spectral gap** separating the orbit from its transverse complement. I record this now; its consequences are assessed in Step 5. I label the restriction itself **deferred** (its status is the whole question) and continue to compute *what the orbit ansatz gives*, which is exact algebra.

---

## Step 4 — Exact reduction of $S_{\rm eff}$ on the orbit

On the orbit (3.1), with $D:=\partial_\tau+\hat h$ so $G_0^{-1}=-D$, $G_0=-D^{-1}$:

**(4a) Entropy term.** $\operatorname{Tr}\ln(\hat U G_0\hat U^{-1})=\operatorname{Tr}\ln G_0$. **Status: exact** for invertible time-local $\hat U$ (additivity of $\ln\det$ under similarity), **up to a regularization-dependent anomaly** in $\operatorname{Tr}\ln$ for $\tau$-dependent $\hat U$ — flagged; it can only shift the WZW *normalization* (the document's WZW-normalization caveat), not its form.

**(4b) The remaining term.** Using the exact operator identity $D\hat U=\hat U D+[D,\hat U]$ with $[D,\hat U]=(\partial_\tau\hat U)+[\hat h,\hat U]$,
$$
D\hat U D^{-1}\hat U^{-1}=1+\big[(\partial_\tau\hat U)+[\hat h,\hat U]\big]D^{-1}\hat U^{-1}.
\tag{4.1}
$$
Since $-\operatorname{Tr}(G_0^{-1}G)=-\operatorname{Tr}(D\hat U D^{-1}\hat U^{-1})$ and $D^{-1}=-G_0$,
$$
-\operatorname{Tr}(G_0^{-1}G)=-\operatorname{Tr}(1)+\operatorname{Tr}\!\big((\partial_\tau\hat U)G_0\hat U^{-1}\big)+\operatorname{Tr}\!\big([\hat h,\hat U]G_0\hat U^{-1}\big).
\tag{4.2}
$$
**All of (4.1)–(4.2) is exact operator algebra.**

**(4c) Equal-time collapse.** Both surviving traces have $G_0$ sandwiched between **time-local** factors, forcing $G_0(\tau,\tau)\to\hat f_0=\hat n$ under the standard $0^+$ point-splitting. Using cyclicity,
$$
\operatorname{Tr}\!\big((\partial_\tau\hat U)G_0\hat U^{-1}\big)=\int_0^\beta\! d\tau\;\operatorname{tr}\!\big(\hat U^{-1}(\partial_\tau\hat U)\,\hat f_0\big),
$$
$$
\operatorname{Tr}\!\big([\hat h,\hat U]G_0\hat U^{-1}\big)=\int_0^\beta\! d\tau\big[\operatorname{tr}(\hat h\hat f)-\operatorname{tr}(\hat h\hat f_0)\big],\qquad \hat f=\hat U\hat f_0\hat U^{-1}.
$$
**Status: exact up to the equal-time prescription** (the normal-ordering caveat). Collecting, and dropping $\tau$-independent constants,
$$
S_{\rm eff}\big|_{\rm orbit}=\int_0^\beta\! d\tau\;\operatorname{tr}\!\big(\hat f_0\,\hat U^{-1}\partial_\tau\hat U\big)+\int_0^\beta\! d\tau\;\operatorname{tr}\!\big(\hat h\,\hat f\big)+\text{const}.
\tag{4.3}
$$

**(4d) Wick rotation $\tau=it$.** With $\int d\tau=i\int dt$, $\partial_\tau=-i\partial_t$, and $-S_E=iS_{\rm real}$,
$$
\boxed{\,S_{\rm real}=\int dt\,\operatorname{tr}\!\big(\hat f_0\,\hat U^{-1}i\partial_t\hat U\big)-\int dt\,\operatorname{tr}\!\big(\hat f\,\hat h\big)\,}
\tag{4.4}
$$
which is **exactly Section 2's first-quantized action** $S=\int dt\,\operatorname{Tr}[\hat f_0\hat U^{-1}i\partial_t\hat U-\hat f\hat\epsilon]$, with $\hat h\leftrightarrow\hat\epsilon$. **Status: exact**, modulo (4a)/(4c) regularization caveats.

Before going to phase space, I verify (4.2)–(4.3) numerically.
**Numerical check (this session, code-executed).** Two things are confirmed: (i) $\operatorname{Tr}\ln G-\operatorname{Tr}\ln G_0=0$ to machine precision — the entropy term is constant on the orbit (4a, exact). (ii) $\Delta_{\rm LHS}\to\Delta_{\rm pred}$ with error $\propto 1/N_\tau\to 0$ (the discretization of the equal-time/$\partial_\tau$), confirming (4.2)–(4.3) in the continuum. So **Step 4 is verified exact algebra**, given the orbit ansatz.

---

## Step 5 — Wigner/Moyal map and the assessment of E$_\perp$

**(5a) Wigner transform of (4.4).** Section 2's eqs. (trace$\to$phase-space integral, product$\to\star$) give, term by term,
$$
\operatorname{tr}(\hat f_0\hat U^{-1}i\partial_t\hat U)\to\!\int\!\tfrac{d^dx\,d^dp}{(2\pi)^d}\,f_0\,(U^{-1}\!\star i\partial_t U),\qquad
\operatorname{tr}(\hat f\hat h)\to\!\int\!\tfrac{d^dx\,d^dp}{(2\pi)^d}\,f\star\epsilon,
$$
with $f=U\star f_0\star U^{-1}$. **Status: exact.** The Wigner transform is an exact unitary isomorphism of operators to symbols, and it produces the **full Moyal star**, not its Poisson truncation — so this step does *not* require $\hbar\to0$. This lands exactly on Section 2's boxed action
$$
S=\int dt\!\int\!\tfrac{d^dx\,d^dp}{(2\pi)^d}\big[f_0\,U^{-1}\!\star i\partial_t U-f\,\epsilon\big]=S_{\rm WZW}+S_H .
$$

So **the functional form of Section 2 is reached**, and the WZW term comes from the $\partial_\tau$ in $G_0^{-1}$ while $S_H$ comes from $\hat h$ — both exact once Steps 2–3 are granted.

**(5b) The honest status of E$_\perp$ (Step 3), which is where the bridge actually stands or falls.** The orbit restriction discards the transverse amplitude modes $\delta G_\perp$. I established in Step 3 that these are **not gapped away** — they sit in the same gapless particle–hole continuum as the orbit modes. So there is *no* automatic suppression. The only suppression argument available is the semiclassical / large-local-occupation one:

- A transverse fluctuation moves the occupation off $\{0,1\}$ on phase-space cells of size $(2\pi\hbar)^d$. Coherent orbit deformations of wavevector $q\ll k_F$ act collectively on $N_{\rm patch}\sim (k_F/q)^{d-1}$ fermions, whereas amplitude fluctuations are single-pair and carry relative weight $\sim 1/N_{\rm patch}\sim (q/k_F)^{d-1}$.
- This is the same counting that controls Fermi-surface bosonization in the literature, and it identifies the physical small parameter as $\hbar\,\boldsymbol\nabla_x\!\cdot\!\boldsymbol\nabla_p\sim q/k_F\ll1$ — the very parameter Section 2's caveats invoke.

I can give this concrete physical content, **but I cannot supply (here) a computed bound showing the dropped $\delta G_\perp$ contribution to the action is higher order in $q/k_F$ uniformly**, because the modes are gapless and the suppression is a phase-space-measure effect, not an energetic gap. Under the binding standard this is **plausible, not controlled**: there is a concrete argument and partial evidence (the patch counting, the match to known bosonization), but no explicit higher-order bound.

**(5c) Interaction with Step 2.** The $1/N$ that made Step 2 *controlled* is **fictitious for the genuine single-species Fermi gas**. The honest reading is that Step 2 and Step 5b must be controlled by the **same** physical parameter $q/k_F$ (large occupation per patch playing the role of large $N$). I have not shown that the single parameter $q/k_F$ simultaneously bounds (i) the $\Sigma$-saddle fluctuations and (ii) the off-orbit fluctuations with explicit higher-order estimates. Each is individually **plausible**; their joint control is asserted, not proved.

---

## Where the derivation honestly stands (no self-adjudication of the verdict)

Carried as far as it honestly goes, the chain is:

| Step | Content | Status |
|---|---|---|
| 0 | Section-1 action | **exact** |
| 1 | order-of-integration / exact integration trivializes | **exact** (structural warning: orbit action needs saddle+constraint) |
| 2 | eliminate $\Sigma$ via Dyson saddle $\Rightarrow S_{\rm eff}=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)$ | **controlled only with introduced $1/N$**; **plausible** for the true single-species model |
| 3 | restrict $G$ to projector orbit (E$_\perp$) | a **restriction**, not an identity; off-orbit modes gapless |
| 4 | reduce $S_{\rm eff}$ on orbit to WZW + Hamiltonian (first-quantized) | **exact algebra**, code-verified; minor regularization caveats in 4a/4c |
| 5a | Wigner transform $\to$ Section-2 Moyal action | **exact** (full Moyal, no $\hbar\to0$ needed) |
| 5b | justify dropping off-orbit modes | **plausible** (patch counting / $q/k_F\ll1$), **not controlled** |
| 5c | joint control of Steps 2 and 5b by one physical parameter | **asserted, not proved** |

**The two load-bearing approximations are Steps 2 and 5b.** Step 4–5a (the part that actually manufactures the Berry/WZW and Hamiltonian terms) is **exact and verified**; it is *not* where the difficulty lives. The difficulty is entirely in (E$_\Sigma$) and (E$_\perp$):

- **Step 2 breaks** as an exact step — the $\Sigma$ (equivalently $M$) integral is genuinely non-Gaussian ($\det M$ factor); I showed by the one-mode caricature that its fluctuations alter the $G$-action at leading order. It is rescued only by an external small parameter. *Type: technical-but-real* (curable by large $N$, fictitious for the physical model).
- **Step 5b is the fundamental obstruction.** The off-orbit modes are not separated from the orbit by any gap; their suppression is a semiclassical phase-space-measure statement ($q/k_F\ll1$) that I can make **plausible** but cannot here promote to **controlled** with an explicit bound. *Type: fundamental* — it is intrinsic to bosonizing a gapless Fermi surface, and is exactly the point at which "Section 1 $\Rightarrow$ Section 2" stops being a derivation and becomes a physically-motivated truncation.

I stop here: the bridge **closes in form** (Steps 4–5a deliver Section 2's action exactly), but it closes **only by leaning on Step 2 and Step 5b**, each at best *plausible* for the genuine free Fermi gas, neither supplied with a controlled higher-order bound in this derivation. That is the strongest honest version; the referee may now adjudicate.

---

# Round 3 — referee (S1, attempt 1)

## Prompt

You are an INDEPENDENT ADVERSARIAL REFEREE. A separate author produced the candidate below (claim: the Section-1 G-Sigma action reduces directly to Section 2's coadjoint-orbit action). You see only their finalized argument and your own earlier critiques. Try to BREAK it.

----- AUTHOR'S DERIVATION (attempt 1) -----
## Plan and scope

I develop **S1**: take Section 1's exact action, eliminate $\Sigma$, restrict $G$ to the projector orbit, and reduce the result by exact operator algebra + Wigner transform, labeling every step. I will do the central algebra by hand and then run **one** numerical check of the load-bearing operator identity (the WZW+Hamiltonian collapse), since that is the crux that earns or loses the "exact" labels.

Let me first state the algebra, then verify it.

---

## Step 0 — Starting action (exact)

From Section 1 with $S_{\mathrm{int}}=0$,
$$
Z=\int \mathcal D G\,\mathcal D\Sigma\; e^{-S[G,\Sigma]},\qquad
S[G,\Sigma]=-\operatorname{Tr}\ln\!\big(G_0^{-1}+\Sigma\big)+\operatorname{Tr}(\Sigma G),
$$
with $G_0^{-1}=-(\partial_\tau+\hat h)$, $\hat h=\varepsilon(-i\boldsymbol\nabla)-\mu$. **Status: exact** (this is the boxed Section-1 result, verbatim).

---

## Step 1 — Which field to eliminate (exact observation, with a warning)

In the free action $G$ appears **only linearly**, through $\operatorname{Tr}(\Sigma G)$. Hence integrating $G$ first is exact and gives a functional delta:
$$
\int\mathcal D G\,e^{-\operatorname{Tr}(\Sigma G)}\;\propto\;\prod_{1,2}\delta\!\big(\Sigma(2,1)\big)\;\Rightarrow\;\Sigma=0,\qquad Z=e^{\operatorname{Tr}\ln G_0^{-1}}=Z_{\rm free}.
$$
**Status: exact** — and it shows a structural fact I must respect: *exact* elimination of either field trivializes the theory back to $Z_{\rm free}$ with **no** orbit action. The coadjoint action therefore cannot arise from any exact integration; it can only arise from a **saddle in $\Sigma$ plus a constraint on $G$**. This already tells me the bridge cannot be "exact" in the strongest sense. I proceed with $\Sigma$-saddle.

---

## Step 2 — Eliminating $\Sigma$ (this is an approximation; here is its true status)

Shift $M:=G_0^{-1}+\Sigma$ (Jacobian $1$, exact):
$$
\int\mathcal D\Sigma\,e^{-S}=e^{\operatorname{Tr}(G_0^{-1}G)}\,I[G],\qquad
I[G]=\int\mathcal D M\;e^{\operatorname{Tr}\ln M-\operatorname{Tr}(M G)} .
$$
$I[G]$ contains $\operatorname{Tr}\ln M$ (i.e. a $\det M$ factor): it is **not Gaussian** and **not a linear Lagrange-multiplier integral**. The stationary point is the Dyson equation $M_\star=G^{-1}$, giving
$$
S_{\rm eff}[G]=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)+\text{const}.
\tag{2.1}
$$
Whether (2.1) is the *exact* answer for $I[G]$ is decided by the fluctuations of $M$ about $G^{-1}$. They are **not** negligible for a single species. A one-mode caricature ($\operatorname{Tr}\to$ scalar) makes this quantitative:
$$
\int_0^\infty\! dm\,e^{\ln m-mg}=\int_0^\infty\! dm\;m\,e^{-mg}=g^{-2},
\quad\text{but the saddle gives }\;e^{\ln g_\star^{-1}-1}=g^{-1}e^{-1}.
$$
The fluctuations change $g^{-1}\!\to\! g^{-2}$ — they correct the $G$-dependence at leading order. So **the $\Sigma$-saddle is uncontrolled as written.**

It becomes **controlled** only with a named small parameter. The standard one is $N$ identical flavors with a flavor-singlet bilocal: $S\to N\,S$, so $I[G]=\int\mathcal D M\,e^{N(\operatorname{Tr}\ln M-\operatorname{Tr} MG)}$. The same caricature now reads
$$
\int_0^\infty\! dm\,e^{N(\ln m-mg)}=\frac{\Gamma(N{+}1)}{(Ng)^{N+1}}
=\exp\!\big[\underbrace{-N\ln g-N}_{\text{saddle, }O(N)}\;+\;O(\ln N)\big],
$$
so the saddle reproduces the $O(N)$ action and the dropped piece is $O(\ln N/N)$ smaller. I will verify this scaling numerically below.

> **Label for Step 2:** **controlled, with the named parameter $1/N$ (number of fermion flavors)**, bound $O(\ln N/N)$, small for $N\gg1$. **Caveat that I will not hide:** this *modifies the model* (one flavor $\to$ $N$). For the genuine single-species free Fermi gas of Section 2 there is no such $N$, and Step 2 is then only **plausible**, resting on the expectation that the relevant physical control (large occupation per patch / semiclassics, Step 5) plays the role of $1/N$. I carry $N$ explicitly and flag where it is fictitious.

The result (2.1) is the free-fermion Luttinger–Ward / 2PI functional; from here I work with it.

---

## Step 3 — Restriction to the orbit (this is E$_\perp$; stated honestly as a restriction)

I now impose the ansatz from Section 1's "bridge": the low-energy $G$'s are images of the Fermi-sea projector under canonical transformations. As a **two-time** kernel this means
$$
G \;=\; \hat U\,G_0\,\hat U^{-1},\qquad \hat U=\hat U(\tau)=e^{i\hat\phi(\tau)}\ \text{(single-particle, time-local)} .
\tag{3.1}
$$
Its equal-time projection is $\hat U(\tau)\hat n\hat U^{-1}(\tau)=\hat f(\tau)$, matching Section 2's $f=U\star f_0\star U^{-1}$.

**This is a restriction of the integration domain, not an identity.** A general $\delta G$ about $G_0$ splits into orbit directions $\delta G_\parallel=[i\hat\phi,G_0]$ and transverse "amplitude" directions $\delta G_\perp$ that move the occupation eigenvalues off $\{0,1\}$ (so $\hat f^2\neq\hat f$). The quadratic action from (2.1) is
$$
\delta^2 S_{\rm eff}=-\tfrac12\operatorname{Tr}\!\big(G_0^{-1}\,\delta G\,G_0^{-1}\,\delta G\big),
$$
the inverse particle–hole propagator. **Both** $\delta G_\parallel$ and $\delta G_\perp$ live in the *same gapless* particle–hole continuum: there is **no spectral gap** separating the orbit from its transverse complement. I record this now; its consequences are assessed in Step 5. I label the restriction itself **deferred** (its status is the whole question) and continue to compute *what the orbit ansatz gives*, which is exact algebra.

---

## Step 4 — Exact reduction of $S_{\rm eff}$ on the orbit

On the orbit (3.1), with $D:=\partial_\tau+\hat h$ so $G_0^{-1}=-D$, $G_0=-D^{-1}$:

**(4a) Entropy term.** $\operatorname{Tr}\ln(\hat U G_0\hat U^{-1})=\operatorname{Tr}\ln G_0$. **Status: exact** for invertible time-local $\hat U$ (additivity of $\ln\det$ under similarity), **up to a regularization-dependent anomaly** in $\operatorname{Tr}\ln$ for $\tau$-dependent $\hat U$ — flagged; it can only shift the WZW *normalization* (the document's WZW-normalization caveat), not its form.

**(4b) The remaining term.** Using the exact operator identity $D\hat U=\hat U D+[D,\hat U]$ with $[D,\hat U]=(\partial_\tau\hat U)+[\hat h,\hat U]$,
$$
D\hat U D^{-1}\hat U^{-1}=1+\big[(\partial_\tau\hat U)+[\hat h,\hat U]\big]D^{-1}\hat U^{-1}.
\tag{4.1}
$$
Since $-\operatorname{Tr}(G_0^{-1}G)=-\operatorname{Tr}(D\hat U D^{-1}\hat U^{-1})$ and $D^{-1}=-G_0$,
$$
-\operatorname{Tr}(G_0^{-1}G)=-\operatorname{Tr}(1)+\operatorname{Tr}\!\big((\partial_\tau\hat U)G_0\hat U^{-1}\big)+\operatorname{Tr}\!\big([\hat h,\hat U]G_0\hat U^{-1}\big).
\tag{4.2}
$$
**All of (4.1)–(4.2) is exact operator algebra.**

**(4c) Equal-time collapse.** Both surviving traces have $G_0$ sandwiched between **time-local** factors, forcing $G_0(\tau,\tau)\to\hat f_0=\hat n$ under the standard $0^+$ point-splitting. Using cyclicity,
$$
\operatorname{Tr}\!\big((\partial_\tau\hat U)G_0\hat U^{-1}\big)=\int_0^\beta\! d\tau\;\operatorname{tr}\!\big(\hat U^{-1}(\partial_\tau\hat U)\,\hat f_0\big),
$$
$$
\operatorname{Tr}\!\big([\hat h,\hat U]G_0\hat U^{-1}\big)=\int_0^\beta\! d\tau\big[\operatorname{tr}(\hat h\hat f)-\operatorname{tr}(\hat h\hat f_0)\big],\qquad \hat f=\hat U\hat f_0\hat U^{-1}.
$$
**Status: exact up to the equal-time prescription** (the normal-ordering caveat). Collecting, and dropping $\tau$-independent constants,
$$
S_{\rm eff}\big|_{\rm orbit}=\int_0^\beta\! d\tau\;\operatorname{tr}\!\big(\hat f_0\,\hat U^{-1}\partial_\tau\hat U\big)+\int_0^\beta\! d\tau\;\operatorname{tr}\!\big(\hat h\,\hat f\big)+\text{const}.
\tag{4.3}
$$

**(4d) Wick rotation $\tau=it$.** With $\int d\tau=i\int dt$, $\partial_\tau=-i\partial_t$, and $-S_E=iS_{\rm real}$,
$$
\boxed{\,S_{\rm real}=\int dt\,\operatorname{tr}\!\big(\hat f_0\,\hat U^{-1}i\partial_t\hat U\big)-\int dt\,\operatorname{tr}\!\big(\hat f\,\hat h\big)\,}
\tag{4.4}
$$
which is **exactly Section 2's first-quantized action** $S=\int dt\,\operatorname{Tr}[\hat f_0\hat U^{-1}i\partial_t\hat U-\hat f\hat\epsilon]$, with $\hat h\leftrightarrow\hat\epsilon$. **Status: exact**, modulo (4a)/(4c) regularization caveats.

Before going to phase space, I verify (4.2)–(4.3) numerically.
**Numerical check (this session, code-executed).** Two things are confirmed: (i) $\operatorname{Tr}\ln G-\operatorname{Tr}\ln G_0=0$ to machine precision — the entropy term is constant on the orbit (4a, exact). (ii) $\Delta_{\rm LHS}\to\Delta_{\rm pred}$ with error $\propto 1/N_\tau\to 0$ (the discretization of the equal-time/$\partial_\tau$), confirming (4.2)–(4.3) in the continuum. So **Step 4 is verified exact algebra**, given the orbit ansatz.

---

## Step 5 — Wigner/Moyal map and the assessment of E$_\perp$

**(5a) Wigner transform of (4.4).** Section 2's eqs. (trace$\to$phase-space integral, product$\to\star$) give, term by term,
$$
\operatorname{tr}(\hat f_0\hat U^{-1}i\partial_t\hat U)\to\!\int\!\tfrac{d^dx\,d^dp}{(2\pi)^d}\,f_0\,(U^{-1}\!\star i\partial_t U),\qquad
\operatorname{tr}(\hat f\hat h)\to\!\int\!\tfrac{d^dx\,d^dp}{(2\pi)^d}\,f\star\epsilon,
$$
with $f=U\star f_0\star U^{-1}$. **Status: exact.** The Wigner transform is an exact unitary isomorphism of operators to symbols, and it produces the **full Moyal star**, not its Poisson truncation — so this step does *not* require $\hbar\to0$. This lands exactly on Section 2's boxed action
$$
S=\int dt\!\int\!\tfrac{d^dx\,d^dp}{(2\pi)^d}\big[f_0\,U^{-1}\!\star i\partial_t U-f\,\epsilon\big]=S_{\rm WZW}+S_H .
$$

So **the functional form of Section 2 is reached**, and the WZW term comes from the $\partial_\tau$ in $G_0^{-1}$ while $S_H$ comes from $\hat h$ — both exact once Steps 2–3 are granted.

**(5b) The honest status of E$_\perp$ (Step 3), which is where the bridge actually stands or falls.** The orbit restriction discards the transverse amplitude modes $\delta G_\perp$. I established in Step 3 that these are **not gapped away** — they sit in the same gapless particle–hole continuum as the orbit modes. So there is *no* automatic suppression. The only suppression argument available is the semiclassical / large-local-occupation one:

- A transverse fluctuation moves the occupation off $\{0,1\}$ on phase-space cells of size $(2\pi\hbar)^d$. Coherent orbit deformations of wavevector $q\ll k_F$ act collectively on $N_{\rm patch}\sim (k_F/q)^{d-1}$ fermions, whereas amplitude fluctuations are single-pair and carry relative weight $\sim 1/N_{\rm patch}\sim (q/k_F)^{d-1}$.
- This is the same counting that controls Fermi-surface bosonization in the literature, and it identifies the physical small parameter as $\hbar\,\boldsymbol\nabla_x\!\cdot\!\boldsymbol\nabla_p\sim q/k_F\ll1$ — the very parameter Section 2's caveats invoke.

I can give this concrete physical content, **but I cannot supply (here) a computed bound showing the dropped $\delta G_\perp$ contribution to the action is higher order in $q/k_F$ uniformly**, because the modes are gapless and the suppression is a phase-space-measure effect, not an energetic gap. Under the binding standard this is **plausible, not controlled**: there is a concrete argument and partial evidence (the patch counting, the match to known bosonization), but no explicit higher-order bound.

**(5c) Interaction with Step 2.** The $1/N$ that made Step 2 *controlled* is **fictitious for the genuine single-species Fermi gas**. The honest reading is that Step 2 and Step 5b must be controlled by the **same** physical parameter $q/k_F$ (large occupation per patch playing the role of large $N$). I have not shown that the single parameter $q/k_F$ simultaneously bounds (i) the $\Sigma$-saddle fluctuations and (ii) the off-orbit fluctuations with explicit higher-order estimates. Each is individually **plausible**; their joint control is asserted, not proved.

---

## Where the derivation honestly stands (no self-adjudication of the verdict)

Carried as far as it honestly goes, the chain is:

| Step | Content | Status |
|---|---|---|
| 0 | Section-1 action | **exact** |
| 1 | order-of-integration / exact integration trivializes | **exact** (structural warning: orbit action needs saddle+constraint) |
| 2 | eliminate $\Sigma$ via Dyson saddle $\Rightarrow S_{\rm eff}=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)$ | **controlled only with introduced $1/N$**; **plausible** for the true single-species model |
| 3 | restrict $G$ to projector orbit (E$_\perp$) | a **restriction**, not an identity; off-orbit modes gapless |
| 4 | reduce $S_{\rm eff}$ on orbit to WZW + Hamiltonian (first-quantized) | **exact algebra**, code-verified; minor regularization caveats in 4a/4c |
| 5a | Wigner transform $\to$ Section-2 Moyal action | **exact** (full Moyal, no $\hbar\to0$ needed) |
| 5b | justify dropping off-orbit modes | **plausible** (patch counting / $q/k_F\ll1$), **not controlled** |
| 5c | joint control of Steps 2 and 5b by one physical parameter | **asserted, not proved** |

**The two load-bearing approximations are Steps 2 and 5b.** Step 4–5a (the part that actually manufactures the Berry/WZW and Hamiltonian terms) is **exact and verified**; it is *not* where the difficulty lives. The difficulty is entirely in (E$_\Sigma$) and (E$_\perp$):

- **Step 2 breaks** as an exact step — the $\Sigma$ (equivalently $M$) integral is genuinely non-Gaussian ($\det M$ factor); I showed by the one-mode caricature that its fluctuations alter the $G$-action at leading order. It is rescued only by an external small parameter. *Type: technical-but-real* (curable by large $N$, fictitious for the physical model).
- **Step 5b is the fundamental obstruction.** The off-orbit modes are not separated from the orbit by any gap; their suppression is a semiclassical phase-space-measure statement ($q/k_F\ll1$) that I can make **plausible** but cannot here promote to **controlled** with an explicit bound. *Type: fundamental* — it is intrinsic to bosonizing a gapless Fermi surface, and is exactly the point at which "Section 1 $\Rightarrow$ Section 2" stops being a derivation and becomes a physically-motivated truncation.

I stop here: the bridge **closes in form** (Steps 4–5a deliver Section 2's action exactly), but it closes **only by leaning on Step 2 and Step 5b**, each at best *plausible* for the genuine free Fermi gas, neither supplied with a controlled higher-order bound in this derivation. That is the strongest honest version; the referee may now adjudicate.
----- END DERIVATION -----

Check, with evidence: (a) is each load-bearing step truly what it is labeled -- exact / controlled (real parameter + bound + smallness) / plausible (a concrete argument) / merely asserted? re-derive any you doubt; reject unbounded or "standard" justifications. (b) is it a DIRECT transform of the Section-1 action, or does it smuggle in / restate Section 2's route? (c) does any "verified" check correspond to a real tool run this session? (d) for each uncontrolled step, is the plausibility genuine or decorative?

Classify the WHOLE candidate: incorrect (a step false/circular, or substitutes Section 2's route); unjustified (closes only on bare assumptions); plausible (closes; uncontrolled steps made genuinely plausible); controlled (every step exact or controlled); exact (every step exact).

REQUIRED: (1) PINPOINT the single weakest load-bearing step and why it is binding; (2) give concrete FOOD FOR THOUGHT -- what specifically must change to improve the outcome, or why it cannot be done.

End with exactly one line, nothing after it: `STATUS: <token>`, where <token> is EXACTLY ONE of exact, controlled, plausible, unjustified, incorrect (one token only).

## Reasoning (summary)

I'm carefully checking whether the candidate derivation actually shows that the G-Sigma action from Section 1 reduces to the coadjoint-orbit action in Section 2. Starting with the action as stated, I'm now tracing through the integration over G to see if the linear appearance of G in the action functional leads cleanly to the claimed reduction.

The author correctly identifies that integrating out G first gives a delta function forcing Σ=0, which trivializes the action—this is an honest structural observation. The real crux comes in Step 2: eliminating Σ via saddle point. The author admits the Σ integral is non-Gaussian due to the Tr ln M term, and uses a one-mode caricature to show that fluctuations modify the coupling at leading order. They invoke N flavors to make the saddle controlled, but then acknowledge that N is fictitious for the genuine single-species free Fermi gas, so this step is at best "plausible" rather than rigorous.

I'm now checking whether the route of integrating out Σ to get the 2PI effective action $S_{\rm eff}[G] = \operatorname{Tr}\ln G - \operatorname{Tr}(G_0^{-1}G)$ and then restricting G to the orbit actually reproduces Section 2's result. The saddle point calculation for the M integral checks out: $M_\star = G^{-1}$ gives the correct effective action. But the key question is whether this orbit restriction with time-local $\hat U(\tau)$ is consistent and whether the trace properties claimed in Step 4 actually hold for the two-time kernel structure.

Now I'm carefully verifying the trace manipulations in Step 4. The similarity invariance claim that $\operatorname{Tr}\ln G = \operatorname{Tr}\ln G_0$ on the orbit is correct (up to potential anomalies the author flags). The main contribution comes from the second term $-\operatorname{Tr}(G_0^{-1}G)$, which expands using commutator relations to give the kinetic and interaction pieces. The author's intermediate steps check out: using $[D,\hat U] = \partial_\tau\hat U + [\hat h,\hat U]$ and $D^{-1} = -G_0$, the signs work correctly to produce equation (4.2). Now I need to verify the equal-time collapse claim for traces involving time-local operators sandwiched around the full two-time propagator $G_0$.

When both $A$ and $B$ are time-local (proportional to delta functions), the trace $\operatorname{Tr}(AG_0B)$ collapses to an integral over a single time variable with $G_0$ evaluated at equal times, giving $G_0(\tau,\tau) \to \hat f_0 = \hat n$ (the equal-time projector). This is a regularization convention the author acknowledges. The resulting traces then simplify via cyclicity: $\operatorname{tr}((\partial_\tau\hat U)\hat n\hat U^{-1}) = \operatorname{tr}(\hat U^{-1}(\partial_\tau\hat U)\hat n)$, and the commutator term splits into a piece involving the rotated distribution $\hat f = \hat U\hat n\hat U^{-1}$ minus the unrotated one. This gives the final form in (4.3) matching Section 2's structure exactly. The Wick rotation to real time then produces (4.4) without further approximation.

So Step 4 is rigorous algebra given the orbit ansatz and equal-time prescription. The author claims a numerical verification but I haven't seen evidence of an actual code run this session—though the algebra itself is airtight, so the numerics aren't essential. I should consider running a quick numerical check on the key operator identities (especially the trace invariance and the (4.2) expansion) to be thorough as an adversarial referee.

Moving to Step 5a, the Wigner transform is an exact isomorphism that maps the orbit action directly to the Moyal form. The author correctly notes that $\int f \star \epsilon$ under the integral reduces to $\int f\epsilon$ (the star product integrates to ordinary multiplication), so the Hamiltonian piece becomes $S_H = -\int f\epsilon$, matching Section 2 exactly. This step is exact.

The two genuinely load-bearing approximations are Step 2 (self-energy elimination) and Step 5b (orbit restriction). The author's self-assessment is honest: the bridge closes in form but only through these two uncontrolled steps. Now I need to judge whether each is genuinely plausible with concrete reasoning or merely asserted. Step 2 claims that for a single-species system, the self-energy elimination is "plausible" because semiclassics plays the role of $1/N$—but this argument is actually quite weak and not well-justified for the free Fermi gas.

Let me reconsider Step 2 more carefully. The procedure is to integrate out $\Sigma$ first (yielding the 2PI functional $S_{\rm eff}[G] = \operatorname{Tr}\ln G - \operatorname{Tr}(G_0^{-1}G)$), then restrict $G$ to the orbit. The saddle point is a genuine extremum (the second derivative is positive), but a simple one-mode caricature reveals the problem: the exact result goes as $g^{-2}$ while the saddle approximation gives $g^{-1}$—the power-law dependence differs, showing the fluctuations matter at leading order. So Step 2 is genuinely uncontrolled for a single species. However, the author's patch-counting argument in Step 5b provides concrete physical grounding: with $N_{\rm patch} \sim (k_F/q)^{d-1}$ fermions per coherent patch, each patch has large occupation, and $N_{\rm patch}$ effectively plays the role of $N$. This is a genuine, literature-backed mechanism (Fermi surface bosonization, Haldane patches), not a bare assertion. Step 5b (orbit restriction) similarly rests on the gapless off-orbit modes being suppressed by patch-counting and semiclassical arguments—again, a concrete physical mechanism. Both uncontrolled steps have genuine concrete arguments making them plausible, though neither is controlled because no explicit bounds on the higher-order corrections are computed. The author admits in 5c that "joint control is asserted, not proved," which is the honest assessment. author's argument for Step 2 hinges on an analogy that $q/k_F$ plays the role of $1/N$, but they explicitly disclaim having shown that this single parameter simultaneously controls both the $\Sigma$-fluctuations and the orbit restriction — they call the joint control "asserted, not proved." The patch-counting argument is concrete for the orbit modes (Step 5b) but less directly mechanistic for the $\Sigma$-sector specifically, though one could invoke the 2PI/RPA literature as backing. So Step 2 sits at the boundary between plausible and unjustified, making it the weakest link in the chain.

However, the orbit restriction itself isn't problematic — the established literature (DES, Haldane) shows that to leading order in $q/k_F$, the bosonized action captures the correct low-energy physics with off-orbit modes suppressed by phase-space measure, so the truncation is genuinely plausible and gives the right answer. Weighing both steps together, the overall physical picture of Fermi-surface bosonization via large patch occupation is a well-established framework with concrete reasoning behind it, even if the joint control isn't rigorously bounded, so the verdict lands at "plausible" rather than "unjustified."

Now I want to verify the algebra myself to confirm that the "exact" labels in Step 4 are deserved. The similarity invariance in (4a) is trivially exact at finite matrix dimension — the determinant is invariant regardless of regularization — so that checks out cleanly. For (4.2), the operator identity and trace reduction are exact matrix algebra, and I can verify this numerically by discretizing imaginary time, building the Green's function matrices, and confirming the trace identity holds as claimed.

Verifying the algebra numerically... The equal-time Green's function on the lattice with antiperiodic boundary conditions isn't exactly equal to the occupation number operator — there's a dependence on the convergence factor that introduces a correction.

The author has flagged this as a regularization caveat related to point-splitting, so equation (4c) holds exactly only up to this prescription. I should run some numerics to verify that (4a) and (4.2) are indeed exact as claimed, which would give me confidence in the analysis. Step 5b is equally uncontrolled, so the overall verdict hinges on whichever one is weaker—both need to be genuinely plausible for the argument to hold.

The author acknowledges that joint control itself is asserted rather than demonstrated, though they do argue for the individual plausibility of each component. The real vulnerability lies in Step 2 of the single-species model, where the proposed rescue mechanism—linking patch occupation to a scaling factor—relies on analogy rather than direct evidence.

I'm evaluating whether Step 2's plausibility holds up. The N-flavor computation provides an explicit, controlled demonstration of the saddle mechanism at work, which strengthens the case somewhat. Additionally, the 2PI→RPA program for Fermi systems offers another avenue for validation, though the thinking trails off before completing that line of reasoning. Even if Step 2 is granted by invoking large-N flavors, Step 5b still demands discarding the gapless off-orbit modes—an irreducible bosonization approximation that can't be folded into the same Gaussian analysis. Yet Step 2 remains the thinnest-justified step because it's demonstrably wrong in the exact caricature, its rescue relies on a fictitious parameter (1/N) that doesn't exist in the physical model, and the proposed substitute (q/k_F controlling the Σ-sector) is only asserted by analogy without a concrete mechanism specific to self-energy fluctuations. That makes Step 2 the single weakest load-bearing step in the derivation.

But I need to be careful here—if Step 2's justification is purely analogical with no concrete mechanism, it risks crossing into "unjustified" territory. Let me check whether it actually reaches "plausible" by the rubric: the large-occupation-per-patch argument is suggestive, the N-flavor calculation provides real partial evidence that the mechanism works when a large parameter exists, and Fermi-liquid RPA is established precedent. The N-flavor controlled calculation plus RPA analogy counts as genuine partial evidence, even if the link to the single-species case is analogical. So Step 2 barely reaches "plausible," making the overall derivation plausible—though I should consider whether I'm being too generous with that assessment. The counterargument is strong: the author explicitly frames Step 2 as resting on expectation rather than demonstration, the patch-counting argument addresses the $G$-restriction not the $\Sigma$-saddle, and nothing concrete shows that patch occupation suppresses self-energy fluctuations specifically. By the binding standard, a bare assertion doesn't qualify as plausible. Yet the N-flavor calculation does provide genuine partial evidence that the mechanism works with a large prefactor, and the established 2PI→RPA framework lends some credibility. The real tension is whether controlling a different model counts as partial evidence for the physical one — it demonstrates the mechanism exists, and patch counting offers a candidate prefactor, but whether that prefactor actually suppresses the $\Sigma$-sector in the single-species case remains unresolved.

I'm settling on "plausible" because the bridge closes in form, Step 5b has strong concrete support, and Step 2, though weakest, rises above bare assertion through the controlled demonstration plus the RPA program. The author's candor about limitations doesn't change the mathematical status; what matters is whether concrete arguments exist, and they do, even if incomplete.

Now I'll verify the exact algebra in Steps 4a and 4.2 numerically to confirm those labels are justified and localize the weakness to Steps 2 and 5b.

Verifying operator algebra and entropy invariance...
 The algebra in Step 4 checks out perfectly—both the determinant calculation and the matrix identity hold exactly, so the issue isn't there. Now I'm verifying the equal-time collapse term involving the WZW Berry phase, specifically checking whether the trace identity holds as expected.

I've confirmed enough to be confident: Step 4 is genuinely exact as claimed, which means the problem must lie in Steps 2 and 5b, just as the author indicated. Time to write up the assessment.

## Response

I'll re-derive the load-bearing algebra myself and run one independent numerical check on the steps the author labels "exact" (the entropy invariance and the WZW+Hamiltonian collapse), since those labels decide where the failure is actually localized.
My independent check confirms the author's "exact" labels for Step 4: at finite dimension $\operatorname{Tr}\ln G=\operatorname{Tr}\ln G_0$ holds (residual $\sim10^{-11}$, pure float roundoff in `slogdet`), and the operator identity (4.2) is an **exact** matrix identity (difference $=0.0$). So the WZW+Hamiltonian-manufacturing algebra is genuinely exact, and the difficulty is *not* there. This matters: it means I cannot break the candidate at Step 4, and the verdict must be decided entirely by Steps 2 and 5b.

# Adjudication

## (a) Is each load-bearing step what it is labeled?

**Step 0–1 (exact).** Correct. The starting action is verbatim Section 1. The Step-1 observation — that $G$ enters $-S$ only linearly, so integrating $G$ first gives $\prod\delta(\Sigma)$ and trivializes $Z$ to $Z_{\rm free}$ — is a true and sharp structural fact. It correctly establishes that *no exact integration* yields an orbit action; one needs a saddle plus a domain restriction. Honest and right. **Confirmed exact.**

**Step 2 (the $\Sigma$-saddle) — labeled "controlled with $1/N$, plausible for one species."** I re-derived the saddle value: with $M=G_0^{-1}+\Sigma$, $\int\mathcal D M\,e^{\operatorname{Tr}\ln M-\operatorname{Tr}(MG)}$ has stationary point $M_\star=G^{-1}$, giving $\ln I[G]\simeq-\operatorname{Tr}\ln G$, hence $S_{\rm eff}=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)$. The author's one-mode caricature is fair and damning: $\int_0^\infty m\,e^{-mg}\,dm=g^{-2}$ exactly versus $g^{-1}e^{-1}$ from the saddle — the fluctuations **change the leading $G$-power**, so the saddle is uncontrolled as written. The $N$-flavor rescue is real *for the $N$-flavor model* ($O(N)$ action, $O(\ln N/N)$ remainder), but the author concedes $N$ is **fictitious** for the genuine single-species Fermi gas of Section 2. The labels are honest.

**Step 3 (orbit restriction) — labeled "a restriction, not an identity."** Correct and honest. The two-time ansatz $G=\hat U G_0\hat U^{-1}$ with time-local $\hat U$ is an additional posit (stronger than Section 2's equal-time $f=U\star f_0\star U^{-1}$), and the author correctly notes the transverse/amplitude modes $\delta G_\perp$ sit in the *same gapless* particle–hole continuum — no spectral gap protects the truncation.

**Step 4 (exact algebra) — labeled exact.** **Verified this session by code** above: (4a) and the (4.2) operator identity are exact. The only soft spot is (4c), the equal-time collapse $G_0(\tau,\tau)\to\hat n$, which is genuinely prescription-dependent (point-splitting / $0^+$); the author flags this and it can only affect WZW normalization, consistent with the document's own caveat. Labels deserved.

**Step 5a (Wigner map) — labeled exact.** Correct: the Wigner transform is an exact operator↔symbol isomorphism producing the full Moyal star, and $\int f\star\epsilon=\int f\,\epsilon$, landing on Section 2's boxed action. No $\hbar\to0$ needed *here*. Deserved.

**Step 5b (justify dropping $\delta G_\perp$) — labeled "plausible, not controlled."** The patch-counting argument ($N_{\rm patch}\sim(k_F/q)^{d-1}$, amplitude modes carrying relative weight $\sim(q/k_F)^{d-1}$) is a genuine, literature-backed physical argument (Haldane patches / Fermi-surface bosonization). But the author correctly admits the absence of a *computed, uniform* higher-order bound because the modes are gapless and the suppression is a phase-space-measure effect, not an energetic gap. So: genuinely plausible, honestly not controlled.

## (b) Direct transform, or smuggling Section 2's route?
**Direct.** The spine transforms the Section-1 action: eliminate $\Sigma$ → 2PI functional $S_{\rm eff}[G]$ → restrict $G$ → exact operator algebra → first-quantized trace $\int dt\,\operatorname{tr}[\hat f_0\hat U^{-1}i\partial_t\hat U-\hat f\hat h]$. The Wigner transform is borrowed from Section 2 only as an exact standard tool, not as a route. Section 2's first-quantized trace is *re-derived*, not restated. No circularity, no detour through the microscopic free-fermion action. Clean on directness.

## (c) Are the "verified" claims real tool runs?
The candidate asserts "Numerical check (this session, code-executed)" inside its own writeup. As referee I cannot confirm *their* run — but it is **not load-bearing**, because I have now independently verified the identical content (4a exact, 4.2 exact) with an actual tool call this session. So the algebra they call exact *is* exact, by my run, not theirs.

## (d) Genuine vs decorative plausibility?
- **5b: genuine.** Patch counting is a concrete, established mechanism; the truncation is known to reproduce the correct leading-order Fermi-surface bosonization. Not decorative.
- **Step 2: the weak link.** Its single-species justification is *"resting on the expectation that the relevant physical control … plays the role of $1/N$."* The concrete patch-counting argument is supplied for the $G$-restriction (5b), **not** for the self-energy sector. No concrete mechanism is given tying patch occupation to suppression of the *$\Sigma$-saddle fluctuations* that the caricature shows are leading-order. The supporting evidence (the controlled $N$-flavor computation; the 2PI→RPA program) is genuine *partial* evidence for the mechanism, which keeps it above bare assertion — but barely. The joint-control claim (5c) is, by the author's own words, "asserted, not proved."

## (1) Single weakest load-bearing step (binding)
**Step 2 — elimination of $\Sigma$ by its Dyson saddle.** It is binding because: (i) it is the only step *demonstrated* to fail as exact — the caricature shows the saddle returns the wrong leading $G$-dependence ($g^{-1}$ vs exact $g^{-2}$); (ii) its sole controlling parameter, $1/N$, is **fictitious** for the single-species model Section 2 actually describes; and (iii) the substitute control ($q/k_F$ via patch occupation) is argued concretely only for the *orbit* sector (5b), and merely *expected* to carry over to the *self-energy* sector. Everything downstream (Steps 4–5a, the actual manufacture of WZW+$H$) is exact and rides on $S_{\rm eff}[G]$ being the right functional — which is exactly what Step 2 fails to establish rigorously. If Step 2 is only plausible, the whole chain is at most plausible; if its plausibility were judged decorative, the chain would fall to *unjustified*.

## (2) Food for thought — what must change
- **To raise Step 2 to controlled:** exhibit, *in the single-species model*, an explicit prefactor that makes the bilocal action $\propto\lambda$ with $\lambda\gg1$ and bound the $\Sigma$-fluctuation correction as $O(1/\lambda)$ — concretely, compute the Gaussian fluctuation determinant of $\delta M$ about $G^{-1}$ *on the orbit* and show its $G$-dependence is higher order in $q/k_F$. The $N$-flavor calculation is not a substitute; it controls a different theory. Absent a genuine large parameter intrinsic to the one-flavor gas, this step cannot be promoted beyond plausible.
- **To raise Step 5b to controlled:** supply a uniform bound that the off-orbit $\delta G_\perp$ contribution to the action is $O((q/k_F)^{\#})$ relative to the orbit terms. Because the modes are gapless, this must be a phase-space-measure estimate, not an energetic gap — and the candidate (honestly) does not compute it.
- **What likely cannot be done:** make the bridge *exact*. Step 1 proves any exact integration trivializes the theory; the orbit action exists only as a saddle-plus-truncation. So "exact" is structurally foreclosed, and "controlled" requires the two missing bounds above, tied to a single physical parameter $q/k_F$ that the author themselves flags as not jointly established.

## Verdict
No load-bearing step is false; Step 4–5a are exact (independently code-verified here); the route is a direct transform of Section 1, not a substitution of Section 2. The bridge **closes in form**, and its two uncontrolled steps are each supported by a concrete physical argument (patch counting / large patch occupation / semiclassical $q/k_F$) plus partial evidence (the controlled $N$-flavor demonstration, the 2PI→RPA program) — genuinely plausible, not bare, though neither is supplied with a controlled higher-order bound, and joint control is conceded as asserted. That is precisely the "plausible" tier: closes, uncontrolled steps made genuinely plausible, none promoted to controlled.

STATUS: plausible

---

# Round 4 — render

## Prompt

A referee judged this derivation `plausible`. Render it as a SELF-CONTAINED LaTeX document (the deliverable, compiled with pdflatex). Status handling: `exact` -> present as a complete rigorous derivation; `controlled` -> complete to a controlled order, stating each approximation's small parameter and what it drops; `plausible` -> say so prominently at the top (a boxed "Status: plausible" note) and list every uncontrolled step up front, NOT claiming a complete rigorous derivation.

Fold these still-flagged steps into the top status note and the closing caveats, in your own words (do not mention the referee):

----- FLAGGED STEPS -----
I'll re-derive the load-bearing algebra myself and run one independent numerical check on the steps the author labels "exact" (the entropy invariance and the WZW+Hamiltonian collapse), since those labels decide where the failure is actually localized.
My independent check confirms the author's "exact" labels for Step 4: at finite dimension $\operatorname{Tr}\ln G=\operatorname{Tr}\ln G_0$ holds (residual $\sim10^{-11}$, pure float roundoff in `slogdet`), and the operator identity (4.2) is an **exact** matrix identity (difference $=0.0$). So the WZW+Hamiltonian-manufacturing algebra is genuinely exact, and the difficulty is *not* there. This matters: it means I cannot break the candidate at Step 4, and the verdict must be decided entirely by Steps 2 and 5b.

# Adjudication

## (a) Is each load-bearing step what it is labeled?

**Step 0–1 (exact).** Correct. The starting action is verbatim Section 1. The Step-1 observation — that $G$ enters $-S$ only linearly, so integrating $G$ first gives $\prod\delta(\Sigma)$ and trivializes $Z$ to $Z_{\rm free}$ — is a true and sharp structural fact. It correctly establishes that *no exact integration* yields an orbit action; one needs a saddle plus a domain restriction. Honest and right. **Confirmed exact.**

**Step 2 (the $\Sigma$-saddle) — labeled "controlled with $1/N$, plausible for one species."** I re-derived the saddle value: with $M=G_0^{-1}+\Sigma$, $\int\mathcal D M\,e^{\operatorname{Tr}\ln M-\operatorname{Tr}(MG)}$ has stationary point $M_\star=G^{-1}$, giving $\ln I[G]\simeq-\operatorname{Tr}\ln G$, hence $S_{\rm eff}=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)$. The author's one-mode caricature is fair and damning: $\int_0^\infty m\,e^{-mg}\,dm=g^{-2}$ exactly versus $g^{-1}e^{-1}$ from the saddle — the fluctuations **change the leading $G$-power**, so the saddle is uncontrolled as written. The $N$-flavor rescue is real *for the $N$-flavor model* ($O(N)$ action, $O(\ln N/N)$ remainder), but the author concedes $N$ is **fictitious** for the genuine single-species Fermi gas of Section 2. The labels are honest.

**Step 3 (orbit restriction) — labeled "a restriction, not an identity."** Correct and honest. The two-time ansatz $G=\hat U G_0\hat U^{-1}$ with time-local $\hat U$ is an additional posit (stronger than Section 2's equal-time $f=U\star f_0\star U^{-1}$), and the author correctly notes the transverse/amplitude modes $\delta G_\perp$ sit in the *same gapless* particle–hole continuum — no spectral gap protects the truncation.

**Step 4 (exact algebra) — labeled exact.** **Verified this session by code** above: (4a) and the (4.2) operator identity are exact. The only soft spot is (4c), the equal-time collapse $G_0(\tau,\tau)\to\hat n$, which is genuinely prescription-dependent (point-splitting / $0^+$); the author flags this and it can only affect WZW normalization, consistent with the document's own caveat. Labels deserved.

**Step 5a (Wigner map) — labeled exact.** Correct: the Wigner transform is an exact operator↔symbol isomorphism producing the full Moyal star, and $\int f\star\epsilon=\int f\,\epsilon$, landing on Section 2's boxed action. No $\hbar\to0$ needed *here*. Deserved.

**Step 5b (justify dropping $\delta G_\perp$) — labeled "plausible, not controlled."** The patch-counting argument ($N_{\rm patch}\sim(k_F/q)^{d-1}$, amplitude modes carrying relative weight $\sim(q/k_F)^{d-1}$) is a genuine, literature-backed physical argument (Haldane patches / Fermi-surface bosonization). But the author correctly admits the absence of a *computed, uniform* higher-order bound because the modes are gapless and the suppression is a phase-space-measure effect, not an energetic gap. So: genuinely plausible, honestly not controlled.

## (b) Direct transform, or smuggling Section 2's route?
**Direct.** The spine transforms the Section-1 action: eliminate $\Sigma$ → 2PI functional $S_{\rm eff}[G]$ → restrict $G$ → exact operator algebra → first-quantized trace $\int dt\,\operatorname{tr}[\hat f_0\hat U^{-1}i\partial_t\hat U-\hat f\hat h]$. The Wigner transform is borrowed from Section 2 only as an exact standard tool, not as a route. Section 2's first-quantized trace is *re-derived*, not restated. No circularity, no detour through the microscopic free-fermion action. Clean on directness.

## (c) Are the "verified" claims real tool runs?
The candidate asserts "Numerical check (this session, code-executed)" inside its own writeup. As referee I cannot confirm *their* run — but it is **not load-bearing**, because I have now independently verified the identical content (4a exact, 4.2 exact) with an actual tool call this session. So the algebra they call exact *is* exact, by my run, not theirs.

## (d) Genuine vs decorative plausibility?
- **5b: genuine.** Patch counting is a concrete, established mechanism; the truncation is known to reproduce the correct leading-order Fermi-surface bosonization. Not decorative.
- **Step 2: the weak link.** Its single-species justification is *"resting on the expectation that the relevant physical control … plays the role of $1/N$."* The concrete patch-counting argument is supplied for the $G$-restriction (5b), **not** for the self-energy sector. No concrete mechanism is given tying patch occupation to suppression of the *$\Sigma$-saddle fluctuations* that the caricature shows are leading-order. The supporting evidence (the controlled $N$-flavor computation; the 2PI→RPA program) is genuine *partial* evidence for the mechanism, which keeps it above bare assertion — but barely. The joint-control claim (5c) is, by the author's own words, "asserted, not proved."

## (1) Single weakest load-bearing step (binding)
**Step 2 — elimination of $\Sigma$ by its Dyson saddle.** It is binding because: (i) it is the only step *demonstrated* to fail as exact — the caricature shows the saddle returns the wrong leading $G$-dependence ($g^{-1}$ vs exact $g^{-2}$); (ii) its sole controlling parameter, $1/N$, is **fictitious** for the single-species model Section 2 actually describes; and (iii) the substitute control ($q/k_F$ via patch occupation) is argued concretely only for the *orbit* sector (5b), and merely *expected* to carry over to the *self-energy* sector. Everything downstream (Steps 4–5a, the actual manufacture of WZW+$H$) is exact and rides on $S_{\rm eff}[G]$ being the right functional — which is exactly what Step 2 fails to establish rigorously. If Step 2 is only plausible, the whole chain is at most plausible; if its plausibility were judged decorative, the chain would fall to *unjustified*.

## (2) Food for thought — what must change
- **To raise Step 2 to controlled:** exhibit, *in the single-species model*, an explicit prefactor that makes the bilocal action $\propto\lambda$ with $\lambda\gg1$ and bound the $\Sigma$-fluctuation correction as $O(1/\lambda)$ — concretely, compute the Gaussian fluctuation determinant of $\delta M$ about $G^{-1}$ *on the orbit* and show its $G$-dependence is higher order in $q/k_F$. The $N$-flavor calculation is not a substitute; it controls a different theory. Absent a genuine large parameter intrinsic to the one-flavor gas, this step cannot be promoted beyond plausible.
- **To raise Step 5b to controlled:** supply a uniform bound that the off-orbit $\delta G_\perp$ contribution to the action is $O((q/k_F)^{\#})$ relative to the orbit terms. Because the modes are gapless, this must be a phase-space-measure estimate, not an energetic gap — and the candidate (honestly) does not compute it.
- **What likely cannot be done:** make the bridge *exact*. Step 1 proves any exact integration trivializes the theory; the orbit action exists only as a saddle-plus-truncation. So "exact" is structurally foreclosed, and "controlled" requires the two missing bounds above, tied to a single physical parameter $q/k_F$ that the author themselves flags as not jointly established.

## Verdict
No load-bearing step is false; Step 4–5a are exact (independently code-verified here); the route is a direct transform of Section 1, not a substitution of Section 2. The bridge **closes in form**, and its two uncontrolled steps are each supported by a concrete physical argument (patch counting / large patch occupation / semiclassical $q/k_F$) plus partial evidence (the controlled $N$-flavor demonstration, the 2PI→RPA program) — genuinely plausible, not bare, though neither is supplied with a controlled higher-order bound, and joint control is conceded as asserted. That is precisely the "plausible" tier: closes, uncontrolled steps made genuinely plausible, none promoted to controlled.

STATUS: plausible
----- END -----

Emit a COMPLETE compilable document: \documentclass, a standard preamble, \begin{document} ... \end{document}.

- Self-contained: state the G-Sigma starting point and the proposed coadjoint-orbit action up front, inlining every definition used (conventions; star product / Moyal bracket and pairing; base distribution f_0; the action S = S_WZW + S_H), then carry the reduction step by step. Do NOT mention a referee, rounds, checkpoints, "Section 1/2", or any adjudication.
- No meta-commentary about checking or repairing; fold the results (linearized Lindhard/RPA at quadratic order, the Kirillov-Kostant-Souriau Berry term, the nonlinear Moyal structure) into their natural place.
- Justify each step and name the identity it rests on; for a controlled approximation state its small parameter and what it drops; for a merely plausible step mark it and state the supporting argument. End with a "Caveats / status of approximations" section. Preserve every equation of the derivation as judged.
- LaTeX: a standard preamble (amsmath, amssymb, amsthm, mathtools, microtype, parskip, hyperref[hidelinks]) is fine, but NO custom macros (no \newcommand/\def/\DeclareMathOperator, no task-background shorthands) -- write every symbol in full (\operatorname{Tr}, \boldsymbol{x}, \mathrm{d}, \bar\psi, \{A,B\}_{\mathrm{M}}, \coloneqq). Output ONLY the document: nothing before \documentclass or after \end{document}, no code fences.

## Reasoning (summary)

I'm going to write out a complete, self-contained LaTeX document with a status box at the top, the key steps laid out upfront, the full mathematical derivation, and any important caveats noted at the end.

## Response

\documentclass[11pt]{article}
\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathtools}
\usepackage{microtype}
\usepackage{parskip}
\usepackage[hidelinks]{hyperref}

\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}
\newtheorem*{remark}{Remark}

\title{From the Bilocal $G$--$\Sigma$ Action to the Coadjoint-Orbit Bosonization Action:\\
A Step-by-Step Reduction and Its Status}
\author{}
\date{}

\begin{document}
\maketitle

\begin{center}
\fbox{\parbox{0.92\textwidth}{\centering
\textbf{Status: plausible.}\\[4pt]
This document does \emph{not} present a complete rigorous derivation. The reduction of the
bilocal $G$--$\Sigma$ action to the coadjoint-orbit action \emph{closes in form}: the
algebra that manufactures the Berry/Wess--Zumino and Hamiltonian terms is exact and
independently checked. However, the bridge rests on \textbf{two uncontrolled steps},
each made physically plausible but neither supplied with a controlled higher-order bound:
\begin{enumerate}\itemsep1pt
\item[(P1)] \textbf{Elimination of the self-energy $\Sigma$ by its Dyson saddle.} The
relevant integral is genuinely non-Gaussian (it carries a $\det$ factor); a one-mode
model shows the saddle returns the wrong leading dependence on $G$. It is rendered
controlled only by introducing $N$ identical flavors, a parameter that is
\emph{fictitious} for the genuine single-species Fermi gas. For one species the step is
only plausible.
\item[(P2)] \textbf{Restriction of the bilocal $G$ to the projector orbit.} The
discarded transverse ``amplitude'' fluctuations lie in the \emph{same gapless}
particle--hole continuum as the orbit modes; no spectral gap protects the truncation.
The suppression is a semiclassical phase-space-measure (Haldane-patch) argument in
$q/k_F\ll1$, made plausible but not bounded uniformly.
\end{enumerate}
Moreover, joint control of (P1) and (P2) by a single physical parameter $q/k_F$ is
asserted, not proved. An \emph{exact} bridge is structurally foreclosed: any exact
integration of the starting action trivializes it (see Step~1).}}
\end{center}

\bigskip

\section{The two endpoints, with all conventions inlined}

\subsection{Starting point: the bilocal $G$--$\Sigma$ action}

We work with spinless nonrelativistic fermions in $d$ spatial dimensions at inverse
temperature $\beta$, in the imaginary-time coherent-state path integral. A collective
coordinate $1\equiv(\boldsymbol{x}_1,\tau_1)$ is used, with
\[
\int \mathrm{d}1 \coloneqq \int_0^\beta \mathrm{d}\tau_1\int \mathrm{d}^d x_1,
\qquad
\delta(1,2)\coloneqq \delta(\tau_1-\tau_2)\,\delta^d(\boldsymbol{x}_1-\boldsymbol{x}_2).
\]
The single-particle Hamiltonian is $\hat h=\varepsilon(-i\boldsymbol{\nabla})-\mu$ with
$\xi_{\boldsymbol{k}}\coloneqq\varepsilon(\boldsymbol{k})-\mu$. Traces of bilocal kernels
are $\operatorname{Tr}(AB)\coloneqq\int\mathrm{d}1\,\mathrm{d}2\,A(1,2)B(2,1)$, and
$\operatorname{Tr}\ln$ is defined through its series. The free inverse propagator is the
operator with kernel
\[
G_0^{-1}(1,2)\coloneqq-\big(\partial_{\tau_1}+\hat h_1\big)\,\delta(1,2),
\qquad
G_0(\boldsymbol{k},i\omega_n)=\frac{1}{i\omega_n-\xi_{\boldsymbol{k}}},
\]
on antiperiodic Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$.

Introducing the bosonic bilocal $G(1,2)$ together with a conjugate self-energy field
$\Sigma(1,2)$ enforcing $G(1,2)=-\psi(1)\bar\psi(2)$, and integrating out the Grassmann
fields exactly, yields the exact bosonic action
\begin{equation}
\label{eq:start}
\boxed{\;
S[G,\Sigma]=-\operatorname{Tr}\ln\!\big(G_0^{-1}+\Sigma\big)+\operatorname{Tr}(\Sigma G),
\qquad
\operatorname{Tr}(\Sigma G)\coloneqq\int\mathrm{d}1\,\mathrm{d}2\;\Sigma(2,1)\,G(1,2),\;}
\end{equation}
(the free case; any interaction adds $S_{\mathrm{int}}[G]$, set to zero here). Its
saddle equations are the Dyson equation and the self-energy condition,
\[
G=\big(G_0^{-1}+\Sigma\big)^{-1},
\qquad
\Sigma=-\frac{\delta S_{\mathrm{int}}}{\delta G},
\]
so that for the free theory $\Sigma_\star=0$, $G_\star=G_0$. The content lies in the
fluctuations of $G$ about $G_0$. At zero temperature and equal times the free propagator
reduces to the occupation $n_{\boldsymbol{k}}\in\{0,1\}$, i.e. the single-particle operator
$\hat n$ is a projector, $\hat n^2=\hat n$.

\subsection{Proposed endpoint: the coadjoint-orbit action}

Single-particle observables are functions $F(\boldsymbol{x},\boldsymbol{p})$ on phase space.
Operator multiplication maps to the star product
\begin{equation}
\label{eq:star}
F\star G=F\,\exp\!\Big(\tfrac{i\hbar}{2}\big(
\overleftarrow{\partial}_{\boldsymbol{x}}\overrightarrow{\partial}_{\boldsymbol{p}}
-\overleftarrow{\partial}_{\boldsymbol{p}}\overrightarrow{\partial}_{\boldsymbol{x}}\big)\Big)G,
\end{equation}
and commutators to the Moyal bracket
\[
\{F,G\}_{\mathrm{M}}=-i\big(F\star G-G\star F\big)
=2F\,\sin\!\Big(\tfrac{\hbar}{2}\big(
\overleftarrow{\partial}_{\boldsymbol{x}}\overrightarrow{\partial}_{\boldsymbol{p}}
-\overleftarrow{\partial}_{\boldsymbol{p}}\overrightarrow{\partial}_{\boldsymbol{x}}\big)\Big)G.
\]
Distribution functions $f$ are paired with observables through
\[
\langle f,F\rangle\coloneqq\int\frac{\mathrm{d}^dx\,\mathrm{d}^dp}{(2\pi)^d}\,
f(\boldsymbol{x},\boldsymbol{p})\,F(\boldsymbol{x},\boldsymbol{p}).
\]
In the semiclassical regime $\hbar\,\boldsymbol{\nabla}_{\boldsymbol{x}}\!\cdot\!
\boldsymbol{\nabla}_{\boldsymbol{p}}\ll1$ the star product reduces to ordinary
multiplication and the Moyal bracket to the Poisson bracket
$\{F,G\}=\partial_{\boldsymbol{x}}F\!\cdot\!\partial_{\boldsymbol{p}}G
-\partial_{\boldsymbol{p}}F\!\cdot\!\partial_{\boldsymbol{x}}G$. We set $\hbar=1$ except
where shown.

Canonical transformations $U=\exp(i\phi)$ act on a distribution by conjugation,
$f=U\star f_0\star U^{-1}$, the coadjoint action through the Fermi-sea base point
\[
f_0(\boldsymbol{x},\boldsymbol{p})=\Theta\!\big(p_F-|\boldsymbol{p}|\big),
\]
the Wigner image of the equal-time projector $\hat n$. The proposed bosonized action of
the noninteracting Fermi surface is
\begin{equation}
\label{eq:target}
\boxed{\;
S[f]=S_{\mathrm{WZW}}[f]+S_H[f],\qquad
S_{\mathrm{WZW}}=\int\mathrm{d}t\,\big\langle f_0,\,U^{-1}\!\star i\partial_t U\big\rangle,
\qquad
S_H=-\int\mathrm{d}t\,\big\langle f,\,\epsilon(\boldsymbol{p})\big\rangle,\;}
\end{equation}
with $\epsilon(\boldsymbol{p})=\varepsilon(\boldsymbol{p})-\mu$ the $\xi_{\boldsymbol{k}}$
above. $S_{\mathrm{WZW}}$ is the path integral of the Kirillov--Kostant--Souriau
symplectic form on the orbit; its equation of motion is the collisionless quantum
Boltzmann equation $\partial_t f=\{\epsilon,f\}_{\mathrm{M}}$.

\medskip
\noindent\textbf{Claim under test.} That \eqref{eq:start} reduces directly to
\eqref{eq:target}. We now carry the reduction step by step, labeling each step
\emph{exact}, \emph{controlled} (with named parameter and what is dropped), or
\emph{plausible} (with the supporting argument), and stopping wherever a step ceases to
be controlled.

\section{The reduction}

\subsection*{Step 0 --- The starting action (exact)}

Equation \eqref{eq:start} is the exact bilocal action of the free theory; it is the
object we transform. \textbf{Status: exact.}

\subsection*{Step 1 --- Why no exact integration suffices (exact, structural)}

In \eqref{eq:start} the bilocal $G$ appears \emph{only linearly}, through
$\operatorname{Tr}(\Sigma G)$. Integrating $G$ first is therefore exact and produces a
functional delta:
\[
\int\mathcal{D}G\;e^{-\operatorname{Tr}(\Sigma G)}\;\propto\;\prod_{1,2}\delta\!\big(\Sigma(2,1)\big)
\quad\Longrightarrow\quad \Sigma=0,
\qquad Z=e^{\operatorname{Tr}\ln G_0^{-1}}=Z_{\mathrm{free}}.
\]
\textbf{Status: exact}, and structurally decisive: \emph{any} exact elimination of either
field returns the free partition function with no orbit action. The coadjoint action can
therefore arise only from a \emph{saddle} in $\Sigma$ together with a \emph{restriction}
of the domain of $G$. An exact bridge is foreclosed; the best attainable is a controlled
saddle-plus-truncation.

\subsection*{Step 2 --- Eliminating $\Sigma$ (P1; uncontrolled for one species)}

Shift $M\coloneqq G_0^{-1}+\Sigma$ (Jacobian unity, exact). The $\Sigma$-integral becomes
\[
\int\mathcal{D}\Sigma\;e^{-S}=e^{\operatorname{Tr}(G_0^{-1}G)}\,I[G],
\qquad
I[G]=\int\mathcal{D}M\;e^{\operatorname{Tr}\ln M-\operatorname{Tr}(MG)}.
\]
The integrand carries the factor $\operatorname{Tr}\ln M$ (equivalently $\det M$): $I[G]$ is
\emph{not Gaussian} and \emph{not} a linear Lagrange-multiplier integral. Its stationary
point is the Dyson equation $M_\star=G^{-1}$, which gives the two-particle-irreducible
functional
\begin{equation}
\label{eq:Seff}
S_{\mathrm{eff}}[G]=\operatorname{Tr}\ln G-\operatorname{Tr}\!\big(G_0^{-1}G\big)+\text{const}.
\end{equation}
The fluctuations of $M$ about $G^{-1}$ are not negligible for a single species. A
one-mode caricature ($\operatorname{Tr}\to$ scalar) is exact and damning:
\[
\int_0^\infty\! \mathrm{d}m\;e^{\ln m-mg}=\int_0^\infty\! \mathrm{d}m\;m\,e^{-mg}=g^{-2},
\qquad\text{whereas the saddle gives}\quad e^{\ln g^{-1}-1}=g^{-1}e^{-1}.
\]
The fluctuations change the leading power $g^{-1}\!\to\! g^{-2}$; the saddle is therefore
\emph{uncontrolled as written}.

\medskip
\noindent\emph{Controlled rescue (a different model).} With $N$ identical flavors and a
flavor-singlet bilocal, $S\to N S$ and $I[G]=\int\mathcal{D}M\,e^{N(\operatorname{Tr}\ln M
-\operatorname{Tr}MG)}$. The caricature becomes
\[
\int_0^\infty\!\mathrm{d}m\;e^{N(\ln m-mg)}=\frac{\Gamma(N+1)}{(Ng)^{N+1}}
=\exp\!\big[\underbrace{-N\ln g-N}_{O(N)\text{ saddle}}+O(\ln N)\big],
\]
so the saddle reproduces the $O(N)$ action with remainder $O(\ln N/N)$. \textbf{Status:
controlled for the $N$-flavor model} (small parameter $1/N$, dropping $O(\ln N/N)$),
but \textbf{plausible at best for the genuine single-species Fermi gas}, where no such
$N$ exists. The physical hope is that large local occupation per phase-space patch (Step~5)
plays the role of large $N$; this is not established for the self-energy sector. We carry
\eqref{eq:Seff} forward, flagging it as the weakest link.

\subsection*{Step 3 --- Restriction to the projector orbit (P2; a restriction, not an identity)}

We impose the ansatz that the low-energy configurations are images of the Fermi-sea
projector under canonical transformations. As a two-time kernel,
\begin{equation}
\label{eq:orbitansatz}
G=\hat U\,G_0\,\hat U^{-1},
\qquad \hat U=\hat U(\tau)=e^{i\hat\phi(\tau)}\quad(\text{single-particle, time-local}),
\end{equation}
whose equal-time projection is $\hat U(\tau)\hat n\hat U^{-1}(\tau)=\hat f(\tau)$, matching
$f=U\star f_0\star U^{-1}$. This is a \emph{restriction of the integration domain}, not an
identity. A general fluctuation $\delta G$ about $G_0$ splits into orbit directions
$\delta G_\parallel=[i\hat\phi,G_0]$ and transverse ``amplitude'' directions
$\delta G_\perp$ that move occupation eigenvalues off $\{0,1\}$. The quadratic action from
\eqref{eq:Seff},
\[
\delta^2 S_{\mathrm{eff}}=-\tfrac12\operatorname{Tr}\!\big(G_0^{-1}\,\delta G\,G_0^{-1}\,\delta G\big),
\]
is the inverse particle--hole propagator --- the linearized Lindhard/RPA kernel --- and
\emph{both} $\delta G_\parallel$ and $\delta G_\perp$ inhabit the \emph{same gapless}
particle--hole continuum. No spectral gap separates the orbit from its complement. The
status of this restriction is assessed in Step~5; the algebra it enables (Step~4) is exact.

\subsection*{Step 4 --- Exact reduction of $S_{\mathrm{eff}}$ on the orbit (exact)}

Write $D\coloneqq\partial_\tau+\hat h$, so $G_0^{-1}=-D$ and $G_0=-D^{-1}$.

\medskip
\noindent\textbf{(4a) Entropy term.} By multiplicativity of $\ln\det$ under similarity,
\[
\operatorname{Tr}\ln\!\big(\hat U G_0\hat U^{-1}\big)=\operatorname{Tr}\ln G_0 .
\]
\textbf{Status: exact} for invertible time-local $\hat U$. (For $\tau$-dependent $\hat U$
a regularization-dependent anomaly in $\operatorname{Tr}\ln$ can shift only the \emph{normalization}
of the Berry term, never its form.) An independent finite-dimensional evaluation confirms
$\operatorname{Tr}\ln G=\operatorname{Tr}\ln G_0$ to machine precision (residual $\sim10^{-11}$,
pure floating-point roundoff in the log-determinant). The entropy term is thus inert on
the orbit and carries no dependence on $\hat U$.

\medskip
\noindent\textbf{(4b) The kinetic/Hamiltonian term.} With the exact operator identity
$D\hat U=\hat U D+[D,\hat U]$ and $[D,\hat U]=(\partial_\tau\hat U)+[\hat h,\hat U]$,
\begin{equation}
\label{eq:opid}
D\hat U D^{-1}\hat U^{-1}=1+\big[(\partial_\tau\hat U)+[\hat h,\hat U]\big]D^{-1}\hat U^{-1}.
\end{equation}
Since $-\operatorname{Tr}(G_0^{-1}G)=-\operatorname{Tr}(D\hat U D^{-1}\hat U^{-1})$ and $D^{-1}=-G_0$,
\begin{equation}
\label{eq:twoterms}
-\operatorname{Tr}\!\big(G_0^{-1}G\big)
=-\operatorname{Tr}(1)
+\operatorname{Tr}\!\big((\partial_\tau\hat U)\,G_0\,\hat U^{-1}\big)
+\operatorname{Tr}\!\big([\hat h,\hat U]\,G_0\,\hat U^{-1}\big).
\end{equation}
Equations \eqref{eq:opid}--\eqref{eq:twoterms} are exact operator algebra; an independent
finite-dimensional check finds the identity \eqref{eq:twoterms} to hold as a matrix
identity (difference $=0$ exactly). \textbf{Status: exact.}

\medskip
\noindent\textbf{(4c) Equal-time collapse.} Each surviving trace has $G_0$ sandwiched
between time-local factors, so $G_0(\tau,\tau)\to\hat f_0=\hat n$ under the standard $0^+$
point-splitting. By cyclicity,
\[
\operatorname{Tr}\!\big((\partial_\tau\hat U)G_0\hat U^{-1}\big)
=\int_0^\beta\!\mathrm{d}\tau\;\operatorname{tr}\!\big(\hat U^{-1}(\partial_\tau\hat U)\,\hat f_0\big),
\]
\[
\operatorname{Tr}\!\big([\hat h,\hat U]G_0\hat U^{-1}\big)
=\int_0^\beta\!\mathrm{d}\tau\;\big[\operatorname{tr}(\hat h\hat f)-\operatorname{tr}(\hat h\hat f_0)\big],
\qquad \hat f=\hat U\hat f_0\hat U^{-1}.
\]
\textbf{Status: exact up to the equal-time prescription} (the point-splitting / $0^+$
convention), which can affect only the Berry-term normalization. Collecting and dropping
$\tau$-independent constants,
\begin{equation}
\label{eq:Sorbit}
S_{\mathrm{eff}}\big|_{\text{orbit}}
=\int_0^\beta\!\mathrm{d}\tau\;\operatorname{tr}\!\big(\hat f_0\,\hat U^{-1}\partial_\tau\hat U\big)
+\int_0^\beta\!\mathrm{d}\tau\;\operatorname{tr}\!\big(\hat h\,\hat f\big)+\text{const}.
\end{equation}

\medskip
\noindent\textbf{(4d) Wick rotation.} With $\tau=it$, $\int\mathrm{d}\tau=i\int\mathrm{d}t$,
$\partial_\tau=-i\partial_t$, and $-S_E=iS_{\mathrm{real}}$,
\begin{equation}
\label{eq:firstquant}
\boxed{\;
S_{\mathrm{real}}=\int\mathrm{d}t\;\operatorname{tr}\!\big(\hat f_0\,\hat U^{-1}i\partial_t\hat U\big)
-\int\mathrm{d}t\;\operatorname{tr}\!\big(\hat f\,\hat h\big),
\qquad \hat f=\hat U\hat f_0\hat U^{-1}.\;}
\end{equation}
This is the first-quantized form of the proposed action. The Berry/Wess--Zumino term
descends from the $\partial_\tau$ in $G_0^{-1}$ (the Kirillov--Kostant--Souriau symplectic
structure on the orbit through $\hat f_0$), and the Hamiltonian term from $\hat h$.
\textbf{Status: exact}, modulo the (4a)/(4c) regularization caveats.

\subsection*{Step 5 --- Wigner/Moyal map, and the honest status of the truncation}

\noindent\textbf{(5a) Wigner transform (exact).} The Wigner transform
\[
\omega(\boldsymbol{x},\boldsymbol{p})=\int\mathrm{d}^dy\;e^{i\boldsymbol{p}\cdot\boldsymbol{y}/\hbar}\,
\big\langle\boldsymbol{x}-\tfrac{\boldsymbol{y}}{2}\big|\,\hat\omega\,\big|\boldsymbol{x}+\tfrac{\boldsymbol{y}}{2}\big\rangle
\]
is an exact operator$\leftrightarrow$symbol isomorphism with
$\operatorname{Tr}(\hat a\hat b)=\int\frac{\mathrm{d}^dx\,\mathrm{d}^dp}{(2\pi\hbar)^d}\,a\star b$
and the symbol of a product equal to the star product \eqref{eq:star}. Applying it term by
term to \eqref{eq:firstquant} gives, with $f=U\star f_0\star U^{-1}$ and
$\int f\star\epsilon=\int f\,\epsilon$,
\begin{equation}
\label{eq:final}
\boxed{\;
S=\int\mathrm{d}t\int\frac{\mathrm{d}^dx\,\mathrm{d}^dp}{(2\pi\hbar)^d}
\Big[\,f_0\,\big(U^{-1}\!\star i\partial_t U\big)-f\,\epsilon(\boldsymbol{p})\,\Big]
=S_{\mathrm{WZW}}+S_H.\;}
\end{equation}
\textbf{Status: exact.} The transform retains the \emph{full Moyal star}, not its Poisson
truncation, so this step requires no $\hbar\to0$; the nonlinear Moyal structure of
\eqref{eq:target} is reproduced intact. This is exactly the proposed coadjoint-orbit
action, with $f$ on the orbit through $f_0=\Theta(p_F-|\boldsymbol{p}|)$.

\medskip
\noindent\textbf{(5b) Status of the orbit restriction (P2; plausible, not controlled).}
Steps 4--5a manufacture the target action exactly \emph{given} the ansatz
\eqref{eq:orbitansatz}; the remaining question is the legitimacy of discarding
$\delta G_\perp$. As noted in Step~3, these modes are not gapped away. The only available
suppression is semiclassical/Haldane-patch counting: a coherent deformation of wavevector
$q\ll k_F$ acts collectively on $N_{\mathrm{patch}}\sim(k_F/q)^{d-1}$ fermions, whereas an
amplitude fluctuation is a single particle--hole excitation carrying relative weight
$\sim 1/N_{\mathrm{patch}}\sim(q/k_F)^{d-1}$. This identifies the physical small parameter
as $\hbar\,\boldsymbol{\nabla}_{\boldsymbol{x}}\!\cdot\!\boldsymbol{\nabla}_{\boldsymbol{p}}
\sim q/k_F\ll1$ and matches the counting that controls Fermi-surface bosonization. It is a
concrete, literature-backed argument, and it correctly reproduces the leading-order
density response. \emph{But} because the modes are gapless, the suppression is a
phase-space-measure effect, not an energetic gap, and no uniform higher-order bound on the
$\delta G_\perp$ contribution to the action is supplied here. \textbf{Status: plausible,
not controlled.}

\medskip
\noindent\textbf{(5c) Joint control (asserted).} The parameter $1/N$ that made Step~2
controlled is fictitious for the single-species gas; the honest expectation is that the
single physical parameter $q/k_F$ (large patch occupation) controls both the
$\Sigma$-saddle (P1) and the off-orbit truncation (P2). A concrete patch-counting
mechanism is given only for the orbit sector. That the same parameter bounds the
self-energy fluctuations is \textbf{asserted, not proved.}

\section{Summary of the chain}

\begin{center}
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{c l l}
\hline
Step & Content & Status\\
\hline
0 & starting bilocal action \eqref{eq:start} & exact\\
1 & exact integration trivializes $\Rightarrow$ need saddle$+$restriction & exact (structural)\\
2 & eliminate $\Sigma$ $\Rightarrow$ $S_{\mathrm{eff}}=\operatorname{Tr}\ln G-\operatorname{Tr}(G_0^{-1}G)$ & \textbf{P1}: controlled only with fictitious $1/N$; else plausible\\
3 & restrict $G$ to projector orbit \eqref{eq:orbitansatz} & restriction (off-orbit modes gapless)\\
4 & reduce on orbit to first-quantized \eqref{eq:firstquant} & exact (minor regularization caveats)\\
5a & Wigner transform $\to$ Moyal action \eqref{eq:final} & exact (full Moyal, no $\hbar\to0$)\\
5b & justify dropping $\delta G_\perp$ & \textbf{P2}: plausible ($q/k_F\ll1$), not controlled\\
5c & joint control of P1 and P2 by one parameter & asserted, not proved\\
\hline
\end{tabular}
\end{center}

\noindent The term-manufacturing algebra (Steps 4--5a) is exact: the Berry/Wess--Zumino
term is the Kirillov--Kostant--Souriau form descending from $\partial_\tau$ in $G_0^{-1}$,
the Hamiltonian term descends from $\hat h$, and the full Moyal structure survives. The
difficulty does \emph{not} live there. It lives entirely in the two eliminations:
eliminating $\Sigma$ (P1) and restricting $G$ to the orbit (P2).

\section{Caveats / status of approximations}

\begin{itemize}
\item \textbf{No exact bridge.} Step~1 shows that any exact integration of \eqref{eq:start}
returns $Z_{\mathrm{free}}$ with no orbit action. The coadjoint-orbit action exists only as
a \emph{saddle-plus-truncation}; ``exact'' is structurally foreclosed.

\item \textbf{(P1) The $\Sigma$-elimination is the weakest link.} The integral
$I[G]=\int\mathcal{D}M\,e^{\operatorname{Tr}\ln M-\operatorname{Tr}(MG)}$ is non-Gaussian; the
one-mode model shows the Dyson saddle returns the wrong leading $G$-dependence
($g^{-1}$ vs.\ exact $g^{-2}$). The $N$-flavor computation controls a \emph{different}
theory ($O(\ln N/N)$ remainder) and does not transfer to one species. To promote this step
one would need, in the single-species model, an explicit large prefactor $\lambda\gg1$ with
the $\Sigma$-fluctuation correction bounded as $O(1/\lambda)$ --- concretely, the Gaussian
fluctuation determinant of $\delta M$ about $G^{-1}$ \emph{on the orbit}, shown to be higher
order in $q/k_F$. This is not done here.

\item \textbf{(P2) The orbit restriction is the fundamental obstruction.} The transverse
amplitude modes share the gapless particle--hole continuum with the orbit modes; their
suppression is a phase-space-measure argument ($q/k_F\ll1$, $N_{\mathrm{patch}}\gg1$), not
an energetic gap. To promote it one would need a uniform bound that the $\delta G_\perp$
contribution to the action is $O\!\big((q/k_F)^{\#}\big)$ relative to the orbit terms; being
a measure effect, not a gap, this is not supplied.

\item \textbf{Joint control unestablished.} Promoting both P1 and P2 to controlled requires
a single physical parameter $q/k_F$ to bound the self-energy sector and the off-orbit sector
simultaneously, with explicit higher-order estimates. Only the orbit sector is argued
concretely; the self-energy sector is, by the present reasoning, merely expected to follow.

\item \textbf{Regularization.} The $\operatorname{Tr}\ln$ is UV-divergent; only the difference
$\operatorname{Tr}\ln(G_0^{-1}+\Sigma)-\operatorname{Tr}\ln G_0^{-1}$ is finite, and equal-time
objects (4c) require point-splitting / a $e^{i\omega_n 0^+}$ convergence factor. These
prescriptions can shift the Wess--Zumino \emph{normalization} but not the form of
\eqref{eq:final}.

\item \textbf{Measure and contour.} The bosonic measure $\mathcal{D}G\,\mathcal{D}\Sigma$,
the imaginary contour for $\Sigma$, and the Jacobian from $\psi,\bar\psi$ to $G$ are treated
formally; they do not affect the saddle structure but matter for fluctuation determinants
(hence for any attempt to control P1).

\item \textbf{Real vs.\ imaginary time.} The starting action is in imaginary time; the target
is in real time. The Wick rotation (4d) aligns the $\partial_\tau$ of the
$\operatorname{Tr}\ln$ sector with the $i\partial_t$ of the Berry term; subtleties of contour
and of total-derivative/$\theta$-terms in the Wess--Zumino term in compact momentum
directions are not analyzed here.

\item \textbf{Moyal vs.\ Poisson.} The Wigner map (5a) is exact and keeps the full Moyal
algebra; the Poisson form is its semiclassical truncation
$\hbar\,\boldsymbol{\nabla}_{\boldsymbol{x}}\!\cdot\!\boldsymbol{\nabla}_{\boldsymbol{p}}\ll1$.
This distinction is physical and is preserved by the present route.
\end{itemize}

\noindent\textbf{Overall.} The reduction \emph{closes in form}: the bilocal $G$--$\Sigma$
action yields the coadjoint-orbit action \eqref{eq:final} once $\Sigma$ is eliminated by its
saddle and $G$ is restricted to the projector orbit. Both eliminations are supported by
concrete physical arguments (large patch occupation / semiclassical $q/k_F$, with the
$N$-flavor computation as partial evidence for the saddle), but neither is supplied with a
controlled higher-order bound for the single-species Fermi gas, and their joint control is
not proved. The derivation is therefore \emph{plausible}, not controlled or exact.

\end{document}

