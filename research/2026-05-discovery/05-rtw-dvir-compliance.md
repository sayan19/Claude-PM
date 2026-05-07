# 05 — SOTI Right-to-Win: DVIR + Roadside-Inspection Prep (C1)

**Three-aperture scoring (1 = no right-to-win, 5 = strong right-to-win)**

---

## Aperture 1 — Adjacent (extend MobiControl/XSight/Snap)

**Score: 4 / 5**

**Why:**
- DVIR is a paradigmatic Snap workflow: form, photo, signature, geotag, sync. SOTI has already published Snap content for vehicle inspection apps. Source: [SOTI Snap T&L blog](https://soti.net/resources/blog/2025/driving-digital-transformation-in-tl-with-soti-snap/).
- The driver tablet/handheld in the cab is overwhelmingly Zebra rugged Android — SOTI MobiControl is the device manager of record at the install base. SOTI MobiControl is Zebra-validated for 2025.0. Source: [SOTI Zebra validation](https://soti.net/resources/blog/2025/soti-mobicontrol-soti-xsight-20250-are-now-zebra-validated/).
- MobiControl provides the platform anchor: device provisioning, lockdown, OS update, kiosk mode for the DVIR app, remote support if a driver gets stuck mid-inspection.
- Build cost is low — Snap form templates + back-office report. Months, not years.

**Why not 5:**
- ELD-bundled DVIR is "free" to carriers already paying for ELD. Snap-built DVIR has to differentiate beyond "cleaner forms."
- Whip Around's no-hardware proposition is a defensible incumbent for the SMB Snap-natural target.

**Build cost:** Months. ~$200K–$500K to productize.
**Distribution:** Existing T&L install base + VAR/MSP channel.
**ACV signal:** Modest. $3–8/asset/mo per public DVIR add-on pricing.

---

## Aperture 2 — Platform-extension (new SOTI capability, MDM-base distribution)

**Score: 4 / 5**

**Why:**
- Whitespace 2 (roadside-prep) and Whitespace 3 (CSA-score prioritization) require new capability beyond a form: ingest FMCSA SafeStat, violation severity tables, telematics defect data; expose a driver-side decision-support UX.
- This is platform-extension: leverages the device install base for distribution but builds a new compliance layer.
- Strongest argument: NO MDM peer (Workspace ONE, Intune, Hexnode) is in this space. SOTI uniquely sits at the intersection of device-managed driver UX and back-office compliance reporting.

**Why not 5:**
- New capability requires data partnerships (FMCSA APIs are public; ELD data is gated by vendor). Motive and Samsara are unlikely to expose DVIR data to SOTI freely.
- Build cost: 12–24 months to a defensible product.

**Build cost:** 12–18 months. ~$2M–$5M.
**Distribution:** T&L install base, then channel.
**ACV signal:** $10–25/asset/mo for compliance-prep layer (above DVIR baseline).

---

## Aperture 3 — Net-new SaaS (standalone, no MDM dependency)

**Score: 2 / 5**

**Why not:**
- Standalone DVIR is a saturated category. Whip Around, Fleetio, HVI, Zonar EVIR, Motive, Samsara, Geotab, J.J. Keller all serve it.
- SOTI has no DVIR brand recognition outside the device-management buyer.
- The buyer for standalone DVIR is the safety director, not IT — SOTI's commercial motion is built for the IT buyer.
- Whip Around already won the no-hardware niche; Zonar owns the verifiable inspection patent.

**Why not 1:**
- A *vendor-neutral mixed-fleet DVIR reconciliation* (Whitespace 4) is a real net-new wedge with little competition. Not enough to justify a multi-year build, but a real seam.

**Build cost:** Multi-year, $10M+
**Distribution:** Direct + channel, separate motion from MDM.
**ACV signal:** $5–10/asset/mo (ceiling set by Whip Around).

---

## Aperture verdict

**Lead with Aperture 1 (adjacent), build toward Aperture 2 (platform-extension).**

The honest read is: SOTI should ship a Snap-based DVIR template *quickly* (Aperture 1) for the install base — this is defense and protects against ELD vendors expanding into MDM-adjacent device management. The strategic move is the platform-extension layer (roadside-prep + CSA prioritization) that no MDM peer offers and that Whip Around / ELD vendors aren't naturally positioned to build because they don't sit at the device-management substrate.

Aperture 3 is **not recommended**. The category is saturated and SOTI's right-to-win is weak.

---

## What needs to be true for this to work

1. SOTI's T&L install base actually has a meaningful share of carriers running paper DVIR or weak ELD-bundle DVIR. **(Internal data dependency: SOTI must pull DVIR-related Snap usage from the customer base; if Snap-DVIR is already common, the Aperture 1 move is "expand the template," not "build the workflow.")**
2. Customer interviews validate that the roadside-prep + CSA prioritization workflow is a real pain. Currently only directional market signal.
3. SOTI is willing to invest in compliance-data integrations (FMCSA APIs, severity tables, ELD vendor data feeds where possible).

---

## What would kill this opportunity

- Motive or Samsara expanding their device-management capability and bundling DVIR + MDM-lite as a defensive package against SOTI.
- A VAR-channel-led Whip Around marketing push into the SOTI install base.
- Brady Corp (post-Honeywell-acquisition) entering the device-management + workflow software space.

---

## Internal data dependencies flagged

- SOTI T&L customer count
- Snap usage rate inside T&L install base today
- DVIR-specific Snap usage if any
- Win/loss against Motive/Samsara at IT-buyer level
- Average device count per T&L customer (sizing input)

---

## Aperture summary

| Aperture | Score | Build | Recommended |
|---|---|---|---|
| 1 — Adjacent | 4/5 | Low (months) | **Yes — ship fast** |
| 2 — Platform-extension | 4/5 | Med (12–18 mo) | **Yes — strategic build** |
| 3 — Net-new SaaS | 2/5 | High | No |
