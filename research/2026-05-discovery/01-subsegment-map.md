# 01 — North America T&L Sub-Segment Map

**Scope:** US + Canada. Today: 2026-05-07. Regulatory anchors: FMCSA, FDA FSMA 204, DOT, OSHA, AAR, CBP.
**Internal data dependency:** SOTI CRM customer counts, attach rates, ACV by sub-segment are NOT available to this analysis. All "SOTI presence" calls use public case studies, third-party reviews (G2, Capterra, PeerSpot), and trade press. Estimates are flagged "directional, public-source-derived."

---

## 1. LTL / FTL Trucking

**Size & shape (NA only)**
- ~2.09M USDOT-registered active motor carriers per FMCSA MCMIS snapshot Aug 2025; ~91.5% operate ≤10 power units; single-truck operators ~1.16M. Source: [maxdispatchservice.com / FMCSA MCMIS](https://maxdispatchservice.com/how-many-trucking-companies-in-the-us/), [FMCSA Pocket Guide 2024](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/FMCSA%20Pocket%20Guide%202024-v6%20508%20.pdf).
- Concentration: extreme long-tail. Top 10 for-hire carriers (Knight-Swift, Schneider, Werner, J.B. Hunt, etc.) hold a single-digit share by power units. Mid-market (50–500 power units) is the practical sweet spot — large enough to buy software, small enough to not build their own.
- Regulatory anchors: FMCSA HOS (ELD mandate fully phased), FMCSA CSA scoring, DVIR (49 CFR 396.11/13), drug & alcohol clearinghouse, hazmat 49 CFR for the subset.

**Operational workflow profile**
1. Driver pre/post-trip DVIR (mobile/rugged today, but a meaningful share still on paper at small carriers)
2. HOS/ELD logging (mobile — mandated)
3. Dispatch & load tendering (mobile + cab-mounted tablet)
4. POD capture at delivery (mobile/rugged for shippers that demand it; paper still common in dry van)
5. Roadside inspection prep & CSA management (mobile + back office)
6. IFTA fuel tax reporting (mostly back-office, fed by ELD telematics)
7. Detention & demurrage tracking (manual / spreadsheet at most carriers)

**SOTI presence:** **Strong**. Ruan Transportation (~5,000 devices managed by MobiControl) is the flagship reference. Source: [SOTI Ruan case study PDF](https://soti.net/media/3459/ruan_customer_snapshot_2020.pdf). The unnamed "logistics provider" case (3,000 vehicles, 1M+ packages/day, 1,000+ shipping agents) is the second anchor — hybrid LTL/last-mile profile. Source: [SOTI Logistics Provider use case](https://soti.net/resources/customer-stories-and-use-cases/logistics-provider/).

**Buyer landscape**
- IT director / VP IT (device buyer); Fleet ops / safety director (workflow buyer); CFO sign-off at mid-market
- Procurement: VAR/MSP-led for sub-50-unit fleets; direct + Zebra/Honeywell partner channel for mid-market
- Budget: split between IT (devices, MDM) and operations (TMS, ELD subscription)

**Workflow whitespace flags**
- Detention & demurrage tracking — universally manual, drives carrier P&L. No vendor owns this workflow end-to-end.
- Cross-platform DVIR + HOS + roadside-inspection-prep bundle for sub-50-unit carriers — fragmented; ELD vendors solve HOS but DVIR is a checkbox feature, not a workflow.
- POD/exception capture in dry van LTL — gap between TMS and shipper's WMS.

---

## 2. Last Mile Delivery

**Size & shape (NA only)**
- NA was largest regional last-mile market in 2025; share ~36–38% of a global market growing at ~8–10% CAGR. Source: [Precedence / Coherent / Technavio compilations](https://www.technavio.com/report/last-mile-delivery-market-size-in-north-america-industry-analysis), [The Business Research Company](https://www.thebusinessresearchcompany.com/report/last-mile-delivery-global-market-report).
- Operator structure: Amazon DSP network (~3,000+ small Delivery Service Partners in NA, each running 20–40 vans); FedEx Ground ISP network (~5,000+ contracted ISPs); UPS in-house; Walmart Spark; OnTrac, LaserShip/OnTrac merger; thousands of regional/local last-mile carriers. Source: [TheBusinessResearchCompany last-mile market report](https://www.thebusinessresearchcompany.com/report/last-mile-delivery-global-market-report).
- Regulatory anchors: FMCSA HOS for vehicles ≥10,001 lbs; state-level cargo theft laws; PROVE It Act–style emerging legislation; OSHA for warehouse-side handoff.

**Operational workflow profile**
1. Route assignment & turn-by-turn navigation (mobile, often consumer-grade Android)
2. Multi-stop sequence + dynamic re-routing
3. POD: signature, photo, geo-stamp (mobile)
4. Failed-delivery exception capture & customer notification
5. Pre-trip vehicle check (light DVIR — paper or simple form for non-CDL drivers)
6. Returns / undelivered handling
7. Settlement & gig pay (driver-app fed)

**SOTI presence:** **Moderate.** The "Logistics Provider" case study (3,000 vehicles, 1M+ packages/day) sits here. Source: [SOTI Logistics Provider use case](https://soti.net/resources/customer-stories-and-use-cases/logistics-provider/). DSP/ISP segment is largely Amazon Mentor / FedEx-mandated tech stack; SOTI penetration is structural minority.

**Buyer landscape**
- Operations director at the carrier (workflow); IT manager (devices); franchise/contractor often forced into platform-of-record by the brand they deliver for
- Procurement: heavy OEM-bundled (Zebra TC family is dominant rugged hardware)
- Budget: operations primary, IT secondary

**Workflow whitespace flags**
- POD-quality scoring & shipper-grade evidence trail for non-Amazon/FedEx/UPS carriers — fragmented, often custom-built per shipper.
- Last-mile route optimization for sub-200-vehicle regional carriers — Routific, OptimoRoute, Onfleet exist but adoption is uneven; many still use Excel + driver knowledge.
- Returns / RMA capture at the doorstep — almost universally a paper or call-center fallback.

---

## 3. Courier / Same-Day

**Size & shape (NA only)**
- Highly fragmented. Major networks: TFI International (Canada-anchored, US ops with thousands of vehicles), OnTrac, Dropoff, Senpex, Roadie (UPS-owned), regional medical/pharma couriers (Dash Courier, USA Couriers). Source: [SwiftERM courier roundup](https://swifterm.com/top-10-courier-companies-in-the-usa-and-canada/), [DC Velocity / company sites](https://www.fleetcouriers.com/).
- Estimate: 15,000–25,000 NA courier operators of varying scale (directional, public-source-derived; flagged as internal data dependency for refinement).
- Regulatory anchors: FMCSA only for vehicles ≥10,001 lbs; HIPAA for medical couriers; chain-of-custody for pharma & legal documents.

**Operational workflow profile**
1. Dynamic dispatch (high task density, short legs)
2. Multi-pickup multi-drop optimization
3. Real-time customer ETA / live tracking
4. POD with chain-of-custody (especially medical/legal/pharma)
5. Driver settlement (often 1099 / gig)
6. Vehicle / driver onboarding & background check

**SOTI presence:** **Minimal-to-Moderate.** K&S Couriers is referenced in SOTI's blog/case-study material, with operational savings claims around device management. Source: [SOTI T&L recap blog (K&S, Ruan, et al.)](https://hsm.soti.net/resources/blog/2021/want-to-save-30-hours-each-day-add-60-000-usd-to-your-bottom-line-easily-push-48-000-app-updates-per-year-these-three-tl-companies-did-with-soti-find-out-how/), [SOTI K&S case study PDF](https://soti.net/media/1837/kands-casestudy-a4.pdf). Most couriers run consumer Android, dispatcher-built apps, or vendor-bundled (Bringg, OnFleet, Tookan).

**Buyer landscape**
- Owner-operator or ops director at sub-100-vehicle outfits; IT thin or outsourced
- Procurement: VAR-led, often bundled with rugged-hardware refresh
- Budget: operations

**Workflow whitespace flags**
- Chain-of-custody capture for pharma/medical/legal — fragmented; some use Bringg, some use custom forms, many use scanned signatures + email.
- Gig driver onboarding & device provisioning — a real pain (1099 churn is high), no clear vendor owns it.
- Cross-tenant dispatch for couriers handling overflow from multiple shippers.

---

## 4. Warehousing / 3PL

**Size & shape (NA only)**
- US 3PL market: $323.4B in 2025, +5.0% YoY. Source: [Armstrong & Associates](https://www.3plogistics.com/3pl-market-info-resources/3pl-market-information/us-3pl-market-size-estimates/).
- Armstrong's 3PL guide profiles 750+ companies; the Who's Who guide spans 889 NA providers. Source: [Armstrong press release](https://www.einpresswire.com/article/656921670/armstrong-s-who-s-who-in-logistics-3pl-guide-expands-to-over-750-3pls).
- Top-50 control disproportionate revenue but the long-tail of regional 3PLs / warehouse operators numbers in the thousands.
- Regulatory anchors: OSHA (warehouse safety), FDA FSMA 204 for any 3PL touching FTL items (effective compliance Jan 2026, FDA enforcement discretion through July 2028 per Aug 2025 Federal Register extension), C-TPAT for cross-border 3PLs. Source: [FDA FSMA 204 page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods), [Federal Register Aug 2025 extension](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension).

**Operational workflow profile**
1. Inbound receiving + put-away (rugged scanner — Zebra TC52/TC73 dominant)
2. Picking, packing, shipping (rugged + voice + sometimes wearables)
3. Cycle counting & inventory accuracy
4. Yard management — gate-in, trailer location, dock assignment
5. Dock scheduling / appointment management
6. Cross-docking
7. Labor / shift productivity tracking

**SOTI presence:** **Strong** at the device-management layer. Zebra holds >50% of warehouse rugged scanner market and SOTI MobiControl is Zebra-validated for 2025.0. Source: [SOTI/Zebra validation blog](https://soti.net/resources/blog/2025/soti-mobicontrol-soti-xsight-20250-are-now-zebra-validated/), [Tera Digital warehouse scanner overview](https://tera-digital.com/blogs/barcodes/warehouse-scanner). Honeywell's mobile computing/scanner business sale to Brady (announced 2025, $1.4B) is a noteworthy disruption to the OEM landscape. Source: [DC Velocity Honeywell-Brady article](https://www.dcvelocity.com/technology/automatic-data-capture/honeywell-to-sell-off-its-mobile-computers-barcode-scanners-division-for-1-4-billion).

**Buyer landscape**
- VP Operations / DC manager (workflow); Director IT / WMS owner (devices); often joint
- Procurement: VAR/integrator-led (Lowry, Peak-Ryzex, Barcoding Inc.) — strong SOTI channel match
- Budget: operations (WMS, labor) > IT (devices, MDM)

**Workflow whitespace flags**
- **Yard management for mid-market 3PLs** — large operators run YMS (Blue Yonder, PINC, Kaleris/Navis); mid-market and regional 3PLs run paper/whiteboard.
- **Dock scheduling** — Opendock, FourKites Appointment, Loadsmart Opendock now dominant but penetration in regional 3PLs is uneven.
- **FSMA 204 KDE / CTE capture at receive/ship** — most 3PLs scrambling; spreadsheet workarounds widespread.
- **Cycle count + slotting analytics on top of rugged-device telemetry** — XSight has partial signal here but not productized as a 3PL workflow.

---

## 5. Cold Chain (refrigerated transport + storage)

**Size & shape (NA only)**
- Top reefer carriers: Prime Inc., C.R. England, Marten Transport, Schneider National, Swift; mid-tier KLLM, Stevens, Hill Brothers, Leonard's Express, Erb (Canada). Source: [Transport Topics 2025 reefer ranking](https://www.ttnews.com/for-hire/refrigerated/2025), [FleetOwner reefer outlook](https://www.fleetowner.com/refrigerated-transporter/reefer-operations/article/55131813/reefer-outlook-refrigerated-outlook-carriers-cautiously-optimistic-about-2025).
- Combined NA reefer fleet: estimated 200,000+ refrigerated tractors/trailers; cold-storage warehouse footprint includes Lineage, Americold, US Cold Storage, Tippmann.
- Regulatory anchors: **FDA FSMA 204** (compliance Jan 2026, enforcement July 2028); FSMA Sanitary Transportation Rule; USDA for meat/poultry; HOS/CSA carry over from trucking.

**Operational workflow profile**
1. Reefer temperature compliance & exception management (telematics-fed: Carrier Transicold Lynx, Thermo King ConnectedSuite)
2. Pre-cool & set-point verification at pickup (driver-side rugged or paper)
3. KDE/CTE capture at receive/ship (FSMA 204 — new, mostly unsolved)
4. Lot-level traceability through put-away (cold-storage WMS)
5. DVIR / HOS / load securement (same as trucking)
6. Door-open event tracking & temperature-excursion alarms
7. Customs/cross-border documentation (US-Canada-Mexico cold-chain flows)

**SOTI presence:** **Minimal-to-Moderate.** No flagship reefer-specific SOTI case study identified. Carrier/Thermo King telematics own the reefer hardware integration. SOTI's role is device-management for the driver tablet/handheld, not the reefer telematics ecosystem.

**Buyer landscape**
- Compliance officer / VP food safety (FSMA 204 buyer); fleet ops (HOS/DVIR); IT (devices)
- Three buying centers — slow purchase cycle but each can stall a deal

**Workflow whitespace flags**
- **FSMA 204 KDE/CTE capture across the chain** — single biggest near-term whitespace; vendors like Trustwell, Wherefour, FoodLogiQ exist but penetration is low at carrier+3PL+receiver intersection.
- **Temperature-excursion exception workflow** — telematics generate alerts; the WORKFLOW for documenting, contesting, and resolving claims is mostly email + spreadsheet.
- **Driver-side reefer pre-trip verification** — paper at most carriers; could be a Snap form.

---

## 6. Port / Intermodal

**Size & shape (NA only)**
- Major NA terminal operators: Ports America (70+ locations), SSA Marine, APM Terminals, ITS, Maher Terminals, Yusen Terminals, GCT (Canada). Source: [Ports America](https://www.portsamerica.com/), [Tideworks state of intermodal](https://info.tideworks.com/state-industry-report-intermodal-terminals).
- Largest container ports: LA/LB, NY/NJ, Savannah, Houston, Norfolk, Vancouver, Montreal.
- ~200+ inland intermodal terminals run by Class I rails or 3PLs. Source: [Intermodal Association of North America](https://www.intermodal.org/).
- Regulatory anchors: CBP (ACE, in-bond), C-TPAT, OSHA, USCG, FMC.

**Operational workflow profile**
1. Gate-in / gate-out (OCR cameras + handheld backup)
2. Yard moves & equipment assignment (rugged vehicle-mount in tractors, RF terminals)
3. Container inspection (light DVIR-equivalent for chassis)
4. Crane / RTG operator workflows (fixed displays, not mobile)
5. Reefer monitoring on the yard
6. Customs / in-bond / chain-of-custody (CBP touchpoints)

**SOTI presence:** **Minimal.** No SOTI port case studies surfaced. Tideworks, Navis (Kaleris), TOS Mainsail dominate the TOS layer; Cisco Industrial IoT for hardened comms. Devices in port operations skew vehicle-mount (Zebra VC8300) and ruggedized tablets — a place SOTI MobiControl could land but the workflow software is owned.

**Buyer landscape**
- Terminal operations director, IT/OT manager, unionized labor environment (ILWU/ILA) constrains workflow change
- Procurement: long sales cycles, often capital-project-driven

**Workflow whitespace flags**
- Port/yard handheld worker workflow (chassis inspection, container exception capture) is fragmented; TOS owns gate, but worker mobile workflow is often paper or built-in-house.
- Drayage driver app at the port-truck boundary (PortPro, Compcare exist; adoption uneven).

---

## 7. Rail Freight

**Size & shape (NA only)**
- Six Class I railroads: BNSF, Union Pacific, CSX, Norfolk Southern, CN, CPKC. Combined ~140,000+ employees; ~140K route miles. Source: [Wikipedia List of US Class I railroads](https://en.wikipedia.org/wiki/List_of_Class_I_railroads), [FRA Freight Rail Overview](https://railroads.dot.gov/rail-network-development/freight-rail-overview).
- ~600 short-line/regional railroads (Class II + III).
- Regulatory anchors: FRA, AAR interchange rules, PTC mandate (already deployed).

**Operational workflow profile**
1. Crew assignment & lineup management (mostly proprietary RR systems)
2. Conductor / engineer eOTD and authority workflows (proprietary mobile apps + ruggedized tablets)
3. Mechanical inspection & defect reporting
4. Intermodal terminal yard moves (overlap with Sub-segment 6)
5. Hazmat documentation
6. Maintenance-of-way crew dispatch (more like field service)

**SOTI presence:** **Minimal / None visible.** Class I railroads run heavily customized ecosystems (Wabtec, Trimble Rail, in-house). Short-lines and shippers/private fleets are a more realistic SOTI target.

**Buyer landscape**
- Class Is buy capital systems through long RFP cycles; not a near-term SOTI motion.
- Short-lines + private fleet/captive rail (e.g., chemical shippers running their own switching) buy more like trucking.

**Workflow whitespace flags**
- Short-line conductor mobile workflow is often paper.
- Mechanical defect reporting at private rail fleets is a paper/spreadsheet gap.
- Generally low-priority for SOTI in 12–24 month horizon.

---

## 8. Field Service Logistics

**Size & shape (NA only)**
- US FSM market: $1.81B in 2025, ~85% NA share of region revenue. Source: [GMI Insights field service management market](https://www.gminsights.com/industry-analysis/field-service-management-market).
- Mobile workforce: utility, telecom, HVAC, parts-delivery technicians; estimated 5–7M field workers in NA across these verticals (directional, public-source-derived; internal data dependency).
- Regulatory anchors: OSHA, NFPA, EPA refrigerant tracking; sub-vertical specific.

**Operational workflow profile**
1. Dispatch & route to job (FSM platforms — ServiceTitan, IFS, Salesforce FSL, Oracle, ServiceNow, Microsoft Dynamics)
2. Parts inventory on the truck (mobile)
3. Work-order completion + signature/photo POW (proof of work)
4. Customer signature & invoicing
5. Vehicle inspection (light DVIR for service vans)
6. Time/labor capture

**SOTI presence:** **Moderate.** SOTI publishes field-service mobility content and some SMB/MSP customers. Source: [SOTI field services blog](https://soti.net/resources/blog/2020/5-field-services-mobility-challenges-and-how-soti-solves-them/?tags=SOTI+MobiControl&pageNo=1&c=IoT). FSM platforms (ServiceTitan, IFS, etc.) typically dictate the device stack and bundle their own MDM-lite — SOTI competes harder here.

**Buyer landscape**
- Operations director / dispatch manager (workflow); IT (devices)
- Procurement: FSM-platform-led (the FSM vendor often dictates devices), VAR for hardware

**Workflow whitespace flags**
- Inventory accuracy on service trucks (truck-stock cycle counts) — chronic gap.
- Cross-system handoff between FSM platform and the warehouse fulfilling parts — fragmented.
- Less interesting for this T&L discovery; tagged as adjacency, not core.

---

## Summary table

| Sub-segment | NA fleet/operator count (directional) | SOTI presence | Workflow whitespace flags | Top regulatory pressure |
|---|---|---|---|---|
| LTL / FTL Trucking | ~2.09M USDOT carriers; mid-market 50–500 trucks the sweet spot | **Strong** (Ruan ~5K devices) | Detention/demurrage; integrated DVIR+HOS+CSA for SMB; POD in dry van | FMCSA HOS/CSA, DVIR rule |
| Last Mile Delivery | DSP/ISP networks ~8K+ contractors; thousands of regionals | **Moderate** (Logistics-Provider case 3K vehicles) | POD evidence trail for non-major shippers; route optimization for sub-200-vehicle regionals; doorstep returns | FMCSA HOS for ≥10K lb; state cargo theft |
| Courier / Same-Day | 15K–25K operators (directional) | **Minimal-to-Moderate** (K&S referenced) | Chain-of-custody for pharma/medical; gig driver onboarding | HIPAA, chain-of-custody |
| Warehousing / 3PL | $323.4B market; 750+ profiled 3PLs + long-tail | **Strong** (device-mgmt layer; Zebra-validated) | Yard management for mid-market; dock scheduling; FSMA 204 KDE capture; cycle-count analytics | OSHA, FSMA 204 |
| Cold Chain | 200K+ reefer assets; major carriers + cold-storage giants | **Minimal-to-Moderate** | FSMA 204 traceability; temp-excursion exception workflow; driver pre-trip reefer verification | **FSMA 204 (Jan 2026 / July 2028)** |
| Port / Intermodal | 70+ marine terminal sites; 200+ inland intermodal | **Minimal** | Drayage app; chassis/container exception capture | CBP, OSHA, FMC |
| Rail Freight | 6 Class I + ~600 short-lines | **Minimal / None** | Short-line conductor mobile; private-fleet defect reporting | FRA, AAR |
| Field Service Logistics | 5–7M field workers across verticals (directional) | **Moderate** | Truck-stock inventory; FSM-warehouse handoff | OSHA, EPA refrigerant |

---

## What surprised the analysis (vs. v1 assumptions)

1. **FSMA 204's enforcement clock is later than the headline date.** The Aug 2025 Federal Register notice extended enforcement to July 2028; the Jan 2026 "compliance date" still holds for record-keeping but the enforcement runway gives SOTI a real 12–24 month window before customers panic-buy. v1 likely treated FSMA as a now-now urgency; the realistic urgency curve peaks in late 2026 / early 2027.
2. **Honeywell's exit from rugged mobile computing** (sale to Brady, $1.4B) is a structural shift in SOTI's OEM ecosystem. v1 framed Zebra/Honeywell as a duopoly. By 2026 the duopoly is effectively a Zebra monopoly with Brady as a wildcard. SOTI's Zebra-validated status is more strategic than v1 captured.
3. **The long-tail of trucking is more accessible than v1 implied.** With ~91.5% of carriers running ≤10 trucks and 99.3% running <100, the SOTI value-segment angle has real depth — but reaching it requires VAR/MSP channel scale, not direct sales motion.
4. **Rail and Port are not "moderate" SOTI opportunities.** They are minimal in the 12–24 month horizon. v1's catch-all listing inflated their priority. Class Is buy through capital cycles; ports are union/political-constrained. Short-lines and private-rail fleets are the only realistic foothold.
5. **Last-mile last-mile is more fragmented than the marquee names suggest.** Amazon DSPs and FedEx ISPs are tech-mandated, but the regional last-mile carriers (especially big-and-bulky, pharma, medical) have meaningful technology gaps and procurement freedom.

**Internal data dependencies flagged:**
- SOTI customer counts by sub-segment (CRM pull required)
- Attach rates for XSight and Snap inside T&L install base
- ACV by sub-segment and by product
- Win/loss data against Workspace ONE, Intune, Hexnode in T&L deals
- Churn by sub-segment

These should be pulled in parallel with Phase 2 of the pipeline so the sizer (06) and the brief (07) can replace public-source estimates with real numbers.
