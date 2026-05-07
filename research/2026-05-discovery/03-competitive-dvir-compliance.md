# 03 — Competitive Landscape: Lightweight DVIR + Roadside-Inspection Prep (C1)

**Candidate:** Carrier-side DVIR + roadside-inspection prep + CSA score visibility for SMB and mid-market (10–500 power units) NA fleets.
**Geography:** US + Canada.
**Method:** Category-deep, NOT MDM-bounded. Covers pure-plays, ELD-bundled, OEM-bundled, compliance-services giants, and status quo.

---

## Category map

### 1. ELD-bundled DVIR (the default)
The carriers that already pay for ELD compliance get DVIR as a checkbox feature. This is the dominant status quo for any carrier above ~10 power units.

| Vendor | DVIR posture | Pricing signal | Notes |
|---|---|---|---|
| Motive (KeepTruckin) | Configurable checklists, defect alerts in driver app | ~$35/truck/mo all-in (2025) [Trucker Credit Hub](https://credittruckusa.com/2025/08/31/best-eld-devices-for-truckers-in-2025-motive-vs-samsara-vs-garmin-vs-geotab/) | DVIR functionally adequate; UX criticized by drivers |
| Samsara | All-in-one Driver App with ePOD-quality DVIR | starts ~$27/truck/mo | Expanding toward AI dash cam + safety scoring suite [Samsara FAQ](https://www.samsara.com/guides/fleet-faq) |
| Geotab | Geotab Drive — ELD + DVIR + driver ID + messaging | $30–40/truck/mo, 36-mo commitment | Marketplace ecosystem; OEM-embedded telematics partnerships [Geotab DVIR](https://www.geotab.com/fleet-management-solutions/dvir/) |
| Solera/Omnitracs | Bundled in IVG/XRS | per-truck monthly + hardware | Legacy fleets, slower modernization |
| Solera/Spireon | LoJack/Spireon for trailer tracking + DVIR add-on | bundled | Trailer-anchored |
| Garmin Fleet | DVIR app modules | Hardware-driven | Smaller share |

**Take:** ELD-bundled DVIR is "free" if you already have the ELD. The functional weakness is in workflow depth (defect routing, mechanic handoff, inspection-prep) — but it's good enough that displacing it is a switching-cost battle, not a feature battle.

### 2. Standalone DVIR / fleet inspection pure-plays

| Vendor | Position | Customer base | Pricing |
|---|---|---|---|
| **Whip Around** | Mobile-first inspection + maintenance, no hardware | Five Star (1,500 vehicles), trucking, waste, transit. [Whip Around](https://whiparound.com/) | Per-asset/mo, public quotes ~$5–7/asset/mo for DVIR-only |
| **Fleetio** | Maintenance management with DVIR | Strong mid-market presence | Per-asset/mo |
| **HVI (Heavy Vehicle Inspection)** | Inspection-first, no hardware | DOT-focused | Per-asset/mo |
| **Zonar EVIR** | RFID-anchored verifiable inspection (patent moat) | Transit, large fleets, regulated environments [Zonar EVIR](https://www.zonarsystems.com/articles/where-dvir-and-edvir-stop-evir-ensures-compliance/) | Hardware + SaaS, premium |
| **Lytx DVIR** | Bundled with safety camera platform | Mid-market+ | Bundled |
| **BigRoad** (Fleet Complete) | DVIR + ELD + IFTA bundle | Mid-market | Per-truck/mo |
| **SafetyCulture / iAuditor** | Generic inspection app, configurable | Cross-industry | Per-user/mo |

**Take:** Whip Around won the SMB no-hardware niche; Zonar EVIR owns the verifiable-inspection premium niche. The middle is contested.

### 3. Compliance-services giants

| Vendor | Position | Notes |
|---|---|---|
| **J.J. Keller Encompass** | DVIR + driver file + CSA + drug/alcohol clearinghouse + training | Consultative compliance brand; trucking-default for compliance officers |
| **EBE Technologies** | Driver compliance lifecycle | Dispatcher/safety director sale |
| **Idelic** | Driver risk + CSA + telematics integration | Enterprise carriers |

**Take:** Compliance-services giants own the multi-workflow buyer relationship; DVIR is one of N modules they sell. Hard to displace on a single workflow.

### 4. OEM-bundled / aftermarket

| Vendor | Position |
|---|---|
| **PACCAR Connected Services / TruckTech+** | OEM truck-data driven |
| **Daimler/Detroit Connect** | OEM telematics with DVIR |
| **Volvo Dynafleet** | OEM-bundled |

**Take:** OEM bundles are growing but optional; carriers with mixed fleets typically use one of the cross-OEM ELD platforms instead.

### 5. Status quo: paper

Sub-30-truck carriers and a meaningful share of 30–100-truck carriers still run paper DVIRs. The FMCSA Final Rule (Docket FMCSA-2025-0115, effective March 23, 2026) clarifies eDVIR acceptance which removes a regulatory excuse to stay paper but doesn't mandate digital. Source: [Heavy Vehicle Inspection / FMCSA docket coverage](https://heavyvehicleinspection.com/article/top-fleet-inspection-software-comparison-features-pricing).

---

## Where the category leaves customers underserved

1. **Roadside-inspection prep is universally weak.** Vendors generate the DVIR record; almost none give the driver a "what to show the inspector right now" workflow tied to the carrier's CSA exposure.
2. **CSA score visibility for the driver and dispatcher** is fragmented. SafeStat scores live on the FMCSA portal; ELDs don't surface them at the moment of decision.
3. **Defect-to-mechanic handoff** is paper or email at most carriers. Whip Around and Fleetio do this; ELDs largely don't.
4. **Sub-30-truck carriers that can't justify $35/truck/mo ELD bundles.** A meaningful share of NA carriers run cheap ELD-only solutions (BlueArrow, Garmin) and paper DVIR. Whip Around's no-hardware pitch addresses this but adoption is uneven.
5. **Multi-vendor reconciliation.** A carrier with mixed Motive + Samsara + Geotab fleets (acquisition history) has no single DVIR pane.

---

## Status quo cost / friction

- ELD subscription: $25–40/truck/month
- Standalone DVIR add-on (if needed): $3–8/asset/month
- Paper DVIR: ~$0 direct cost, but CSA exposure cost is hidden
- Mid-market carrier with 200 trucks spending on DVIR: ~$60K–$192K/year all-in if standalone; closer to $0 marginal if ELD-bundled

---

## Switching costs

- Driver retraining: meaningful for any change
- Integration with maintenance system / DOT files: moderate
- Hardware: minimal for app-based; high for Zonar EVIR

---

## Sources

- [Heavy Vehicle Inspection vendor comparison](https://heavyvehicleinspection.com/article/top-fleet-inspection-software-comparison-features-pricing)
- [Whip Around platform](https://whiparound.com/)
- [Whip Around no-defect rule guide](https://whiparound.com/blog/the-fmcsa-no-defect-dvir-final-rule-what-it-means-for-all-motor-carriers/)
- [Geotab DVIR](https://www.geotab.com/fleet-management-solutions/dvir/)
- [Samsara fleet FAQ](https://www.samsara.com/guides/fleet-faq)
- [Trucker Credit Hub ELD comparison 2025](https://credittruckusa.com/2025/08/31/best-eld-devices-for-truckers-in-2025-motive-vs-samsara-vs-garmin-vs-geotab/)
- [Zonar EVIR](https://www.zonarsystems.com/articles/where-dvir-and-edvir-stop-evir-ensures-compliance/)
