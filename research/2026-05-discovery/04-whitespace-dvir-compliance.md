# 04 — Whitespace: DVIR + Roadside-Inspection Prep (C1)

## Where customers are genuinely underserved

### Whitespace 1: Sub-30-truck carrier with paper DVIR + cheap ELD
**The gap:** ~91.5% of NA carriers run ≤10 trucks; many run cheap ELD-only services (no DVIR module) and paper inspections. Whip Around is the natural buyer's choice but penetration is uneven; the long-tail is real and unaddressed by ELD bundles. Source: [FMCSA fleet distribution / max dispatch](https://maxdispatchservice.com/how-many-trucking-companies-in-the-us/).
**Why nobody owns it:** The unit economics of selling $5–7/asset/mo into a 10-truck carrier are tough for direct sales; channel via VARs/MSPs/insurance brokers is the path.
**Customer signal status:** Directional market signal (carrier surveys, FMCSA data); no validated SOTI customer signal in this segment from public sources.

### Whitespace 2: Roadside-inspection prep at the moment of pull-over
**The gap:** When a driver is pulled over for a Level 1 inspection, the workflow is "fumble for paperwork." No incumbent provides a one-tap "inspector mode" that surfaces the carrier's last 8 days of HOS, current DVIR record, registration, IRP, IFTA, hazmat (if applicable), insurance card, and CSA-score-relevant signals.
**Why nobody owns it:** ELD vendors focus on the data plane, not the field UX. Compliance-services giants (J.J. Keller) sell the back-office; the driver-side moment is unmet.
**Customer signal status:** Directional — driver forums and trade press complain about it; no validated SOTI customer signal.

### Whitespace 3: CSA-score-driven defect prioritization
**The gap:** A defect logged on a DVIR could be a CSA-score-impacting violation if found at roadside. No vendor surfaces "this defect, if found by an inspector, would cost you 5 BASIC points and trigger an intervention." A carrier's safety director would pay for this prioritization layer.
**Why nobody owns it:** Cross-system synthesis (DVIR + FMCSA SafeStat + violation severity tables) is hard; FMCSA data APIs exist but few vendors weave them.
**Customer signal status:** Directional only.

### Whitespace 4: Mixed-fleet carrier reconciliation
**The gap:** Acquired carriers running a Motive + Samsara + Geotab patchwork need a single DVIR pane. Whip Around and Fleetio do this for inspection but don't ingest from each ELD's DVIR data.
**Why nobody owns it:** Vendor-neutral integration is unfashionable; Project44 and FourKites do it for visibility but not compliance.
**Customer signal status:** Directional (M&A frequency in trucking creates this profile).

### Whitespace 5: CDL trainee → solo driver DVIR confidence
**The gap:** New drivers complete DVIRs poorly (industry-known). Vendors don't gate, score, or coach the inspection.
**Why nobody owns it:** Coaching workflow requires content + judgement; J.J. Keller could but bundles training and inspection separately.
**Customer signal status:** Directional.

---

## Buyer frustration themes (synthesized from G2/Capterra/trade press)

- "DVIR module in our ELD is fine, but defects don't route to the shop on time."
- "We failed an audit because the paper records weren't legible."
- "Drivers pencil-whip the inspection in 30 seconds and we have no way to know."
- "Roadside inspections always feel like a scramble — we should be ready, we're not."

These are *not* SOTI customer quotes — they're synthesized from public review sites and trade-press anecdotes. Treat as **directional market signal, not validated customer signal**. The customer-interview agenda in 07 needs to convert these to validated SOTI signal.

---

## Implication

The category whitespaces map to two distinct wedges:

1. **Driver-side roadside-prep + CSA defect prioritization** — workflow that runs on the rugged tablet/handheld already deployed in the cab. Plays to SOTI's device-management footprint; no incumbent owns the field UX.
2. **Mid-market mixed-fleet DVIR reconciliation** — a vendor-neutral compliance pane on top of Motive/Samsara/Geotab data feeds. Less tied to SOTI's device footprint; more like a compliance SaaS bet.

Wedge #1 is the more SOTI-natural angle. Wedge #2 is more like Aperture 3 net-new SaaS.
