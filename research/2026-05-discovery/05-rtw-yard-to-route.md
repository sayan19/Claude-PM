# 05 — SOTI Right-to-Win: Yard-to-Route Handoff (C6c)

## Aperture 1 — Adjacent (extend MobiControl/XSight/Snap)

**Score: 3 / 5**

**Why:**
- Driver-side notifications when yard events occur are MobiControl-native (push to managed device).
- Snap forms can capture gate-in / gate-out / dock-pickup events on the driver device.
- Hostler-side trailer-position update on a Snap form can feed the system that pushes to the driver.

**Why not higher:**
- Adjacent alone delivers "device-side events flowing into existing systems" — useful but not a product wedge by itself.
- The value emerges only when the events drive a workflow (notify driver, recalculate ETA, generate detention pack). That's beyond Snap.

**Build cost:** Low (months) for forms + notifications; the value is gated on the platform-extension layer.
**Distribution:** Existing T&L install base.
**ACV signal:** Modest standalone.

---

## Aperture 2 — Platform-extension

**Score: 4 / 5**

**Why:**
- This seam is genuinely empty. No incumbent owns it. SOTI's distinctive substrate (rugged devices on every actor in the workflow — hostler, gate guard, driver) is exactly what's needed.
- Wedge B (detention timestamp authority) productizes SOTI-device data into audit-grade detention evidence — a real new capability.
- Wedge A (driver-side delay-awareness) layered with Wedge B becomes a meaningful platform extension.
- Distribution leverages T&L install base.
- No MDM peer is positioned to build this. No YMS/TMS vendor sits at the device-management substrate.

**Why not 5:**
- Customer-pain validation is weakest of all candidates. The seam is real but the *funded buyer* is uncertain.
- Build requires real workflow orchestration beyond MobiControl/XSight/Snap.
- 12–24 month build to defensible MVP.

**Build cost:** 18–24 months. ~$4M–$8M (this is the most ambitious build of any candidate).
**Distribution:** T&L install base; channel; partnership with a TMS or YMS vendor likely required.
**ACV signal:** Speculative. Could be $30K–$100K/site/year if the detention-recovery story holds.

---

## Aperture 3 — Net-new SaaS

**Score: 2 / 5**

**Why not:**
- Standalone "yard-to-route handoff" SaaS would compete with FourKites visibility on the high end and Vector+Velostics on the integrated side.
- SOTI has no brand in either positioning.
- Buyer is operations director or CFO (detention recovery); SOTI's commercial muscle is IT-buyer.

**Why not 1:**
- The wedge is real — but in net-new packaging, SOTI loses the distribution advantage that makes the bet attractive.

**Build cost:** Multi-year, $10M+
**Distribution:** Direct + channel
**ACV signal:** Speculative

---

## Aperture verdict

**Lead with Aperture 2 (platform-extension), but ONLY after customer interviews confirm a funded buyer for the seam pain. This is the highest-uncertainty candidate in the set.**

The honest read: this candidate has the most distinctive whitespace and the strongest theoretical SOTI right-to-win, BUT it has the weakest current customer-signal validation. Three customer interviews confirming a funded budget for the seam pain would change this from "interesting bet" to "leading bet."

Aperture 1 (just Snap forms + notifications) is too thin a product without the platform-extension layer. Ship the Aperture 1 capability as a no-regrets foundation, but the strategic bet is Aperture 2.

Aperture 3 net-new SaaS: not recommended. Loses SOTI's distribution advantage.

---

## What needs to be true

1. Mid-market carriers (200–500 trucks) feel detention recovery as a CFO-level pain.
2. The seam pain crystallizes into a budget line (not just an operational annoyance).
3. SOTI is willing to make an 18–24 month build investment in workflow orchestration.
4. **Internal data dependency:** What share of SOTI T&L customers operate yards (vs. drop-and-hook only)? What share have multi-system pain on the yard-route handoff? Likely 30–50% but unverified.

---

## What would kill this opportunity

- Customer interviews reveal the pain is real but no one is funded to fix it.
- FourKites pushes down-market with carrier-priced visibility.
- Vector or Velostics launches a Zebra-validated yard+driver bundle that closes the seam.
- TMS vendor (McLeod, MercuryGate) builds it as a free module.

---

## Internal data dependencies flagged

- Share of T&L customers operating yards vs. drop-and-hook
- Share of T&L customers with detention as a CFO-level concern
- Existing partnerships with YMS or TMS vendors
- Snap usage in yard contexts today

---

## Aperture summary

| Aperture | Score | Build | Recommended |
|---|---|---|---|
| 1 — Adjacent | 3/5 | Low | Yes — no-regrets foundation |
| 2 — Platform-extension | 4/5 | High (18–24 mo) | **Yes — strategic bet contingent on customer validation** |
| 3 — Net-new SaaS | 2/5 | Very high | No |
