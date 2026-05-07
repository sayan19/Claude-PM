# 04 — Whitespace: POD Evidence-Grade Capture (C4)

## Where customers are genuinely underserved

### Whitespace 1: Multi-shipper POD configuration
**The gap:** A regional last-mile carrier serving 12 shippers needs 12 distinct POD workflows. Most ePOD vendors are one-config-per-tenant. Carriers stitch by building separate driver apps or using SafetyCulture-style generic forms with shipper-specific templates.
**Why nobody owns it:** Multi-tenant POD is harder than it looks (audit trails, separated reporting, evidence-pack export per shipper). Bringg approaches it for enterprise; SMB/mid-market gap.
**Customer signal:** Directional (carrier forums, carrier ops director interviews in trade press); no validated SOTI customer signal.
**SOTI fit:** Snap is form-driven and naturally multi-tenant. Direct fit.

### Whitespace 2: Evidence-grade dispute pack auto-assembly
**The gap:** When a shipper disputes a delivery, the carrier wants to send an evidence pack: photo + GPS + timestamp + signature + scan-of-label + driver ID, sealed and tamper-evident. Manual today.
**Why nobody owns it:** Vendors store the data; few productize the export workflow.
**Customer signal:** Directional. Big-and-bulky carriers (Wayfair vendors, AGS, Pilot Freight) feel this acutely.
**SOTI fit:** Plausible — but requires a back-office layer beyond Snap.

### Whitespace 3: On-device photo quality coaching
**The gap:** Driver takes a blurry photo, or a photo of the wrong door. Some vendors detect missing-signature; almost none score photo quality with ML and re-prompt.
**Why nobody owns it:** Edge ML is non-trivial; consumer photo apps do this for portrait, but logistics vendors haven't productized.
**Customer signal:** Directional only.
**SOTI fit:** Plausible Snap + edge ML extension. Distinctive.

### Whitespace 4: Doorstep returns / refused-delivery capture
**The gap:** Driver attempts delivery, customer refuses. Capture: reason, condition, photo, RMA. Today: a phone call back to dispatch.
**Why nobody owns it:** Major carriers built it in-house; SMB has no off-the-shelf option.
**Customer signal:** Directional. Big-and-bulky and pharma sectors feel this.
**SOTI fit:** Snap-natural form; pairs well with main POD workflow.

### Whitespace 5: Chain-of-custody for medical/legal couriers
**The gap:** HIPAA-grade and legal-grade chain-of-custody requires every handoff (driver to gate guard to facility to recipient) to be captured with timestamp + identity + signature. Few couriers have a polished workflow; many use paper.
**Why nobody owns it:** Specialized requirement; pharma-courier-specific platforms (e.g., MedSpeed-built tools) are private.
**Customer signal:** Directional (HIPAA pressure, FDA chain-of-custody expectations); no validated SOTI customer signal.
**SOTI fit:** Snap-natural; SOTI's K&S Couriers footprint is a foothold to validate.

---

## Buyer frustration themes

- "Every shipper wants a different POD format and we can't support them all."
- "We lost $80K last quarter to chargebacks because our drivers' photos were unusable."
- "When a customer disputes, I spend 45 minutes pulling together evidence."
- "Drivers don't capture refused deliveries — they just call dispatch."

Synthesized; **directional market signal, not validated customer signal.**

---

## Implication

The whitespaces map cleanly onto SOTI's Snap + edge capabilities:

1. **Multi-shipper POD with edge photo coaching** — Snap-natural; differentiates against single-tenant ePOD vendors.
2. **Evidence-pack auto-assembly** — back-office layer beyond Snap, but with the device-side data.
3. **Doorstep refused-delivery + returns capture** — Snap-natural extension.
4. **Chain-of-custody for medical/legal couriers** — a specialized but defendable niche aligned with SOTI's existing courier customers (e.g., K&S Couriers reference).

These are largely Aperture 1/2 plays. Aperture 3 standalone is hard because the ePOD category is competitive and many last-mile platforms bundle POD into a wider routing/dispatch suite — competing on ePOD alone is a thin proposition.
