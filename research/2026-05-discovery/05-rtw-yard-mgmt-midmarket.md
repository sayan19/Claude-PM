# 05 — SOTI Right-to-Win: Yard Management for Mid-Market 3PLs (C2)

## Aperture 1 — Adjacent (extend MobiControl/XSight/Snap)

**Score: 3 / 5**

**Why:**
- Hostler tablet, gate-guard handheld, driver check-in form are all rugged Android workflows that MobiControl already manages.
- Snap-buildable: gate-in form, trailer position update, dock assignment confirm.
- XSight already collects device telemetry that could fuel yard analytics (hostler productivity, gate throughput).

**Why not 5:**
- The *workflow logic* of YMS (trailer state machine, dock assignment, appointment integration) is non-trivial. Snap forms alone don't make a YMS.
- A "Snap yard forms" play helps a customer who already has a YMS — narrow value.
- Without a YMS partnership or a SOTI YMS layer, this is "forms theater" not yard management.

**Build cost:** Months for forms templates; the value proposition is limited without backend orchestration.
**Distribution:** Existing T&L install base.
**ACV signal:** Snap incremental ACV unclear without bundled YMS feature.

---

## Aperture 2 — Platform-extension (new SOTI capability, MDM-base distribution)

**Score: 4 / 5**

**Why:**
- Combine Snap-built hostler/gate UX with an XSight-fed yard analytics overlay and a lightweight workflow orchestrator (trailer state, dock assignment, appointment ingest).
- Distribution leverages the rugged install base: any 3PL or carrier already managing devices via SOTI is a direct prospect.
- The "device-telemetry + yard workflow" combination is genuinely distinctive — no MDM peer offers it; YMS vendors don't have the device telemetry side.
- Buyer is the operations director — adjacent to the IT/devices buyer SOTI already sells to. Joint sale is plausible.

**Why not 5:**
- Buyer mismatch is real. SOTI's IT-buyer motion needs adaptation to operations-buyer.
- Mid-market YMS is consolidating (Vector-YardView). SOTI would be a late entrant.
- Hardware moats at the high end (RFID, computer vision) are real; SOTI can't match them.
- 12–24 month build.

**Build cost:** 12–24 months. ~$3M–$8M for a defensible MVP.
**Distribution:** T&L install base first; channel via VARs (Lowry, Peak-Ryzex, Barcoding).
**ACV signal:** $20K–$50K/site/year for a light-touch YMS layer (mid-market price discipline).

---

## Aperture 3 — Net-new SaaS (standalone, no MDM dependency)

**Score: 2 / 5**

**Why not:**
- Vector, Velostics, Terminal Industries, Kaleris, Datex own the category. SOTI has no YMS brand.
- Standalone YMS sale is operations-buyer, deep WMS/TMS integration — SOTI's commercial muscle is built elsewhere.
- The category has been growing 12% CAGR with well-funded entrants; the window for a new entrant is narrow.

**Why not 1:**
- The mid-market light-touch wedge (Whitespace 2) is real and could support a new entrant. But SOTI is not the obvious one.

**Build cost:** Multi-year, $10M+
**Distribution:** Direct + channel
**ACV signal:** $30K–$100K/site/year (matching YardView/Velostics)

---

## Aperture verdict

**Lead with Aperture 2 (platform-extension) IF customer interviews confirm the hostler-UX + yard-analytics whitespace. Aperture 1 alone is not enough.**

The most distinctive bet for SOTI is the device-telemetry-fed yard analytics layer — XSight extended into operational intelligence for the yard. This is a credible differentiator no incumbent has, and the install-base distribution advantage is real. But it must be paired with at least light yard-workflow orchestration to be more than analytics theater.

Aperture 3 net-new YMS is **not recommended** — category is consolidating against new entrants.

---

## What needs to be true

1. Mid-market 3PLs in SOTI's install base actually run yard ops on whiteboards / paper / spreadsheets (validate via interviews).
2. Hostler-UX is a known pain that customers will pay to fix.
3. SOTI is willing to make the operations-buyer commercial pivot (or sell joint with the IT buyer).
4. **Internal data dependency: How many SOTI T&L customers operate multi-DC yards? What share already use a YMS? What share use whiteboards?**

---

## What would kill this opportunity

- Vector/Velostics launching a Zebra-validated hostler app that closes the device-UX gap.
- Kaleris democratizing pricing (e.g., a "Kaleris Lite" for mid-market).
- A SOTI customer interview that says "we have a YMS, the device UX is fine, leave us alone."

---

## Internal data dependencies flagged

- T&L customer count by sub-segment, especially 3PL count
- Multi-site customer count (proxy for yard relevance)
- XSight attach rate in 3PL segment
- Existing yard-related Snap usage if any

---

## Aperture summary

| Aperture | Score | Build | Recommended |
|---|---|---|---|
| 1 — Adjacent (Snap forms only) | 3/5 | Low | Insufficient on its own |
| 2 — Platform-extension (UX + analytics + light orchestration) | 4/5 | Med (12–24 mo) | **Yes, if validated** |
| 3 — Net-new YMS SaaS | 2/5 | High | No |
