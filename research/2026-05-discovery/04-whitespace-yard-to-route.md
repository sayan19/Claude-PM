# 04 — Whitespace: Yard-to-Route Handoff (C6c)

## Where customers are genuinely underserved

This entire candidate is whitespace. The competitive landscape (03 artifact) showed no incumbent owns the seam. The whitespace question becomes "which sub-pain inside the seam is most acute and addressable."

### Whitespace 1: Driver-side awareness of yard reality
**The gap:** The driver in the cab doesn't know the trailer is being repositioned and won't be ready until 14:50. The driver burns 20 minutes idling at the gate.
**Who half-solves it:** No one cleanly. Some YMS push to dispatcher; dispatcher manually messages driver.
**SOTI fit:** The driver device is SOTI-managed. A push to the driver from a yard event is a Snap + MobiControl notification surface — natural fit.
**Customer signal status:** Directional. No validated SOTI customer signal.

### Whitespace 2: Real-time ETA recalculation when yard delays propagate
**The gap:** The route plan was built at 06:00 assuming 14:30 departure. At 14:42 the trailer is still at the dock. The customer ETA, sent at 14:00 in good faith, is now wrong. No vendor recalculates and notifies the customer in real time.
**Who half-solves it:** FourKites and Project44 do this for shippers; OptimoRoute and Locus recalculate within the route plan; the cross-system loop closure is rare.
**SOTI fit:** Indirect. SOTI doesn't own the routing engine or the customer-notification layer. SOTI's contribution is the device-side data that reflects yard reality.
**Customer signal status:** Directional.

### Whitespace 3: Detention reconciliation with device-captured timestamps
**The gap:** Carriers want to bill detention; shippers contest because the timestamps are imprecise. Geofence-based ELD timestamps are noisy; manual driver entry is unreliable.
**Who half-solves it:** Vector, FourKites, some TMS dwell-tracking modules.
**SOTI fit:** The driver device generates a clean timestamp when the driver opens the dispatch app, scans the gate-in barcode, signs the bill, etc. SOTI-managed device + Snap-captured events are an audit-grade timestamp source.
**Customer signal:** Directional.

### Whitespace 4: Mid-market carrier without shipper-paid visibility
**The gap:** A 200-truck mid-market carrier doesn't have FourKites because their shipper didn't pay for it. They want carrier-side visibility for their own ops. No clean offering at $5K–$20K/month for their scale.
**Who half-solves it:** Vector, McLeod, MercuryGate carrier modules — partial.
**SOTI fit:** Plausible carrier-priced "yard + driver app" thin wedge. Doesn't compete with FourKites on shipper visibility; competes with status quo on carrier ops.
**Customer signal:** Directional.

### Whitespace 5: Multi-handoff visibility for cross-dock and intermodal
**The gap:** Loads moving through cross-dock or intermodal handoffs (rail to truck, truck to truck) lose visibility at every transfer.
**Who half-solves it:** Project44 + IANA partnerships.
**SOTI fit:** Weak — multi-actor coordination beyond SOTI's substrate.

---

## Buyer frustration themes

- "Our dispatchers spend their day on the phone reconciling yard and route."
- "Detention disputes are 50/50 because our timestamps don't hold up."
- "I can see where my truck is but not whether the load is ready when the truck gets there."
- "Customer ETAs are based on a plan, not reality."

Synthesized; **directional market signal, not validated customer signal.** This is the candidate where the customer-signal gap is largest — the workflow is real but no one has packaged the pain narrative for it yet.

---

## Implication

This is the highest-uncertainty, highest-distinctiveness candidate. SOTI is uniquely positioned to be the substrate (device-managed across hostler, gate, driver) but the *product wedge* is unclear:

1. **Wedge A: Driver-side delay-awareness** — push notifications to driver app from yard events. Snap + MobiControl-natural. Small but defendable.
2. **Wedge B: Detention timestamp authority** — productize SOTI-device-captured timestamps as audit-grade detention evidence. Distinctive; requires a back-office reconciliation layer.
3. **Wedge C: Mid-market carrier-side yard+driver visibility** — a thin product that gives the carrier their own visibility independent of shipper-paid FourKites. Larger market but more category competition.

Wedge B is the most SOTI-distinctive. Wedge A is the easiest to ship. Wedge C is the biggest market but most competitive.

The honest read: this seam is real but customer pain hasn't crystallized into a buyer with a budget line. The customer interviews must validate that the seam pain is *funded* — i.e., someone is willing to write a PO for it.
