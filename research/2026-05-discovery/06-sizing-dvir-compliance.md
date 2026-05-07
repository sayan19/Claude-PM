# 06 — Sizing: DVIR + Roadside-Inspection Prep (C1)

**Method:** install-base × attach × ACV (Aperture 1 + 2). TAM is reference only.

---

## Reference TAM (NA only)

- DVIR software market: $1.32B in 2024 at 12.6% CAGR. Source: [Heavy Vehicle Inspection (citing market data)](https://heavyvehicleinspection.com/article/top-fleet-inspection-software-comparison-features-pricing). NA share ~50% directional → ~$660M NA DVIR software 2024.
- Underlying NA fleet: ~2.09M USDOT carriers; ~3M+ commercial power units. Source: [FMCSA / Max Dispatch Service](https://maxdispatchservice.com/how-many-trucking-companies-in-the-us/).

TAM is reference. The relevant headline is install-base × attach × ACV.

---

## Aperture 1 — Adjacent (Snap DVIR template)

**Install-base assumptions (DIRECTIONAL — internal data dependency)**

- SOTI T&L customer count NA: estimated 200–400 enterprise/mid-market customers based on public case studies and channel scale (no SOTI CRM access). **Flagged as internal data dependency.**
- Average device count per T&L customer: 500–1,500 (Ruan ~5K is upper end; Logistics-Provider 3K vehicles is upper end; small T&L customers can be 50–200 devices).
- Total addressable T&L devices in SOTI install base: estimated 150K–500K. **Internal data dependency.**

**Attach-rate assumptions**

- Snap DVIR template attach in T&L install base: 15–30% over 18 months (those running paper or weak ELD-bundled DVIR).
- Per-asset Snap DVIR ACV: $3–6/asset/month → $36–72/asset/year.

**Headline math (Aperture 1)**

| Scenario | T&L devices | DVIR-relevant share | ACV/device/yr | Annual revenue |
|---|---|---|---|---|
| Conservative | 150K | 15% (22.5K assets) | $36 | **~$0.8M/yr** |
| Base | 300K | 20% (60K assets) | $48 | **~$2.9M/yr** |
| Aggressive | 500K | 30% (150K assets) | $60 | **~$9.0M/yr** |

The Aperture 1 economics are real but modest. They protect existing customers and add bolt-on revenue, but they don't drive a multi-segment growth story by themselves.

---

## Aperture 2 — Platform-extension (compliance layer with CSA + roadside-prep)

**Install-base assumptions**

- Layer attach restricted to mid-market and above (≥50 power units). Estimate 80–150 SOTI T&L customers fit this profile.
- Average power units per qualified customer: 200–800.
- Addressable power units across qualified base: 30K–100K.

**ACV assumptions**

- Compliance layer ACV: $10–25/asset/month above Snap baseline → $120–300/asset/year.

**Headline math (Aperture 2)**

| Scenario | Qualified power units | Win share | ACV/unit/yr | Annual revenue |
|---|---|---|---|---|
| Conservative | 30K | 20% (6K) | $120 | **~$0.7M/yr** |
| Base | 60K | 30% (18K) | $180 | **~$3.2M/yr** |
| Aggressive | 100K | 40% (40K) | $300 | **~$12M/yr** |

Aperture 2 layered on top of Aperture 1 = potential combined NA revenue $1.5M (conservative) to $21M (aggressive) within 24–36 months of platform-extension launch.

---

## Aperture 3 — Net-new SaaS (not recommended)

Reference math only. Addressable NA mid-market carriers (50–500 power units): ~30K–50K carriers. Win share at year-3: <5% realistic for new entrant. ACV $5–10/asset/mo standalone. Combined revenue scenarios:
- Aggressive: 50K × 5% × 200 avg power units × $90/yr = **~$45M/yr**, but this requires multi-year investment, separate go-to-market, and a brand the install base of Whip Around et al. is already buying. The win-share assumption is generous.

Not recommended.

---

## Sensitivity / risks

- **Internal data dependency:** SOTI T&L customer count and device count by sub-segment. Aperture 1 base case ($2.9M/yr) could be off by 2–3x in either direction.
- **Attach rate is the most sensitive variable.** ELD-bundled DVIR being "good enough free" is the biggest risk. If attach is 5% instead of 20%, base case drops to $0.7M/yr.
- **Channel motion:** the long-tail SMB carriers are reachable only via VARs and insurance brokers. Aperture 2 economics depend on that motion working.

---

## Internal data dependencies flagged

- T&L customer count NA, by sub-segment (especially trucking)
- Average power units per T&L customer
- Existing Snap usage and any DVIR-specific Snap deployments
- Win/loss data for compliance-adjacent deals
