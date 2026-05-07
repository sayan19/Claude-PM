# SOTI T&L Market Discovery — Agent Pipeline
 
This project rebuilds SOTI's Transportation & Logistics market discovery research, replacing the v1 pipeline that had structural blind spots in its competitive scoping and aperture framing.
 
## How to use this
 
The entry point is the `tl-research-orchestrator` agent. From a Claude Code session in this project root, invoke it explicitly:
 

```
Use the tl-research-orchestrator subagent on a fresh T&L market discovery for North America.
```


 
The orchestrator will fan out to the seven specialist agents in the right order. Do not invoke the specialists directly unless you're rebuilding a single phase — the orchestrator enforces evidence standards and the three-aperture frame across the whole pipeline.
 
## Pipeline architecture
 

```
                tl-research-orchestrator
                          |
     ┌────────────────────┼────────────────────┐
     |                    |                    |
PHASE 1 — DISCOVERY (sequential)
     |                    |
     v                    v
tl-subsegment-mapper  →  tl-workflow-discoverer
     |                    |
     └─────────┬──────────┘
               |
               v
PHASE 2 — PER-CANDIDATE DEEP-DIVE (parallel fan-out, one set per top candidate)
     ┌────────────────────┼────────────────────┐
     v                    v                    v
category-competitive-  whitespace-          soti-right-to-win-
analyst                synthesizer          evaluator
               |
               v
PHASE 3 — SIZING & SYNTHESIS (sequential)
     |
     v
opportunity-sizer  →  discovery-brief-synthesizer
```


 
## The three-aperture frame
 
Every candidate opportunity gets evaluated against three apertures, not one. This is the central design decision of this rebuild — the v1 pipeline collapsed everything into Aperture 1 by framing the question as "what attaches to MobiControl?" That's a defensive frame and it pre-constrained the answer.
 
| Aperture | Bet | Build cost | Distribution | Examples |
|----------|-----|-----------|--------------|----------|
| 1 — Adjacent | Extend MobiControl/XSight/Snap | Low (months) | MDM install base | Lightweight DVIR via Snap, warehouse shift analytics in XSight |
| 2 — Platform-extension | New SOTI capability, MDM-base distribution | Medium (12–24 mo) | Existing T&L customers as early adopters | Predictive device lifecycle, T&L compliance reporting layer |
| 3 — Net-new SaaS | Standalone T&L product | High (multi-year) | Channel + direct, separate motion | Yard management, last-mile routing, freight-matching for value segment |
 
The right-to-win evaluator scores candidates against all three. The honest verdict can be Aperture 3 even when Aperture 1 looks more comfortable.
 
## Documented failure modes (the orchestrator enforces these)
 
These are mistakes from v1 that every agent must avoid:
 
1. **MDM-bounded competitive scans.** Competitive analysis must cover the full category (pure-plays, fleet platforms, TMS/WMS modules, OEM-bundled, status quo), not just SOTI's MDM peers.
2. **TAM as decision-driver.** TAM is reference only. The headline numbers are install-base × attach × ACV (Apertures 1, 2) or addressable × share × ACV (Aperture 3).
3. **Overclaiming.** State validation honestly. No AI-flavored phrasing. Customer signal that doesn't exist gets flagged as a research gap.
4. **MobiControl backgrounded.** MobiControl is the platform anchor. XSight and Snap layer on top. Never let an opportunity write-up over-index on the layers and lose the foundation.
5. **Geographic drift.** This research is North America only. FMCSA, FDA FSMA, DOT are the regulatory anchors.
6. **Customer signal hand-waving.** Every "we know" claim has a source URL. Every "we don't know" appears in the customer-interview agenda.
 
## Output artifacts
 
The pipeline produces these files in the working directory (in order):
 

```
01-subsegment-map.md
02-workflow-candidates.md
03-competitive-<candidate-slug>.md         (one per top candidate, fan-out)
04-whitespace-<candidate-slug>.md          (one per top candidate, fan-out)
05-rtw-<candidate-slug>.md                 (one per top candidate, fan-out)
06-sizing-<candidate-slug>.md              (one per surviving candidate)
07-discovery-brief.md                      (final synthesis)
```

 
The `07-discovery-brief.md` is the artifact that goes to leadership. Everything else is the audit trail.
 
## When to invoke specialists directly
 
The orchestrator is the default entry point. Direct invocation of specialists is useful in two cases:
 
- **Rebuilding a single phase** when new evidence comes in. Example: an internal CRM pull arrives mid-research; invoke `opportunity-sizer` directly on the affected candidates.
- **Pressure-testing a verdict.** Example: orchestrator concluded a candidate is Aperture 1; invoke `soti-right-to-win-evaluator` directly with explicit framing to score Aperture 3 harder.
 
In both cases, hand the prior artifacts to the specialist as input. Don't run them blind.
 
## Models and tool access
 
Each agent's frontmatter specifies model and tools deliberately:
 
- **Opus** for orchestrator, workflow discoverer, RTW evaluator, brief synthesizer (judgment-heavy)
- **Sonnet** for sub-segment mapper, competitive analyst, whitespace synthesizer, sizer (research-heavy, well-defined contract)
- **WebSearch + WebFetch** for any agent that needs primary-source verification
- **Read/Write/Edit** for all (they all produce or consume markdown artifacts)
 
## Conventions
 
- Plain language over corporate prose. Senior PM audience.
- Source URL for every factual claim. No claim without a source.
- Paraphrase aggressively, never quote longer than 15 words from any single source.
- Validation honesty: "directional market signal" vs. "validated customer signal" are different and should be labeled.
- North America scope throughout. If a source is global, find the NA carve-out or note it explicitly.