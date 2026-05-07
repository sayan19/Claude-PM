# 04 — Whitespace: FSMA 204 KDE / CTE Capture (C7)

## Where customers are genuinely underserved

### Whitespace 1: Reefer carrier-side KDE capture
**The gap:** A reefer carrier moving FTL items is a CTE actor (Ship event from origin, Receive event at destination). Their TMS doesn't emit KDE-formatted records. Today they pass through paper or PDF BOLs and hope downstream systems reconcile.
**Why nobody owns it:** TMS vendors prioritize revenue features (rating, dispatch); FSMA 204 carrier-side is too narrow for them to invest deeply. Trustwell et al. focus shipper/receiver.
**Customer signal:** Directional. Trade press (Food Logistics, FleetOwner) flags this as a known gap; no validated SOTI customer signal.
**SOTI fit:** Strong. Driver-side rugged Android + Snap form to capture KDEs at pickup/dropoff is a clean fit. SOTI's reefer-carrier customers (if any in install base — needs validation) are direct prospects.

### Whitespace 2: Wrap-around KDE capture for non-enterprise WMS
**The gap:** A regional cold-storage 3PL on Datex, Made4Net, or a customized WMS doesn't have native KDE schema export. Replacing the WMS is unrealistic; wrapping it isn't well-served.
**Why nobody owns it:** Trustwell and FoodLogiQ plug in but at enterprise pricing and integration complexity.
**Customer signal:** Directional.
**SOTI fit:** Moderate. The capture happens on the rugged scanner at receive/ship; SOTI is the device manager. A Snap KDE form at receive/ship could emit FDA-format records that flow alongside (not through) the WMS.

### Whitespace 3: Receiver-side scan-and-confirm with carrier handoff
**The gap:** When a reefer pulls into a receiver DC, the receiver scans lot codes into their WMS but the carrier doesn't get a confirmation record. Carriers can't prove their CTE participation.
**Why nobody owns it:** Cross-system handoffs are nobody's commercial priority.
**Customer signal:** Directional.
**SOTI fit:** Moderate. SOTI as the substrate across both sides (carrier driver app + receiver warehouse scanner) could close this loop — but only if SOTI is on both sides, which is not always.

### Whitespace 4: Driver-side reefer temperature attestation tied to KDE
**The gap:** FSMA 204 doesn't mandate temperature in KDE schema, but FSMA Sanitary Transportation Rule does require records, and shippers often demand temperature attestation on the BOL. A driver-side Snap form that captures temperature, set point, door-open events, and KDE-relevant lot data in one workflow is unmet.
**Why nobody owns it:** Reefer telematics and FSMA software don't talk to each other.
**Customer signal:** Directional. Cold-chain trade press flags this consistently.
**SOTI fit:** Strong. Snap-natural workflow that bundles regulatory exposure into one driver-side capture.

### Whitespace 5: Audit-pack export for FDA 24-hour requests
**The gap:** When FDA requests records in 24 hours, the covered entity has to assemble KDEs in a sortable electronic format. Many today would scramble.
**Why nobody owns it:** Most platforms generate reports; few productize the FDA-format export.
**Customer signal:** Directional.
**SOTI fit:** Moderate. Requires a back-office layer beyond Snap.

---

## Buyer frustration themes

- "We don't even know if we're a covered entity for some SKUs."
- "Our WMS captures lot but not in the KDE format."
- "Our reefer carrier has no idea what FSMA 204 means for them."
- "If FDA showed up tomorrow, we'd have 24 hours to assemble something we can't assemble."

Synthesized from food-safety trade press and consultancy content; **directional market signal, not validated customer signal.**

---

## Implication

The strongest SOTI-aligned wedges are:

1. **Reefer carrier-side KDE capture** (Whitespace 1) — driver-side Snap form on the device SOTI manages. Greenfield. Distinctive.
2. **Wrap-around KDE capture for non-enterprise cold-storage 3PL** (Whitespace 2) — receive/ship Snap form on the rugged scanner. Augments the WMS without replacing it.
3. **Driver-side temperature + KDE bundled attestation** (Whitespace 4) — extends Whitespace 1 with the SST cross-reference.

The Aug 2025 FDA enforcement extension to July 2028 dampens urgency. Customers buying *now* are early movers; the curve peaks late 2026 / early 2027. SOTI has a 6–12 month window to ship a credible Snap-FSMA template before the field consolidates.
