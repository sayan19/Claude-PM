# 02 — Candidate Workflow Opportunity Space

**Scope:** NA T&L, all sub-segments from 01-subsegment-map.md.
**Method:** Walked the operational workflow taxonomy from the customer's POV, NOT from a "what attaches to MobiControl" frame. Seeded candidate (routing + adjacent workflows) is included and analyzed alongside the others, not privileged.

---

## C1. Lightweight DVIR + roadside-inspection prep for SMB / mid-market carriers

**The pain in plain language**
The owner of a 30-truck carrier still has drivers filling out paper inspection sheets at most yards, partly because the ELD vendor's DVIR module is a checkbox feature, partly because the safety director can't get drivers to use it consistently. When a CSA roadside inspection happens, the carrier scrambles for paper. CSA scores creep up; insurance renews higher.

**How it's solved today**
- Paper at sub-30-truck carriers (most common).
- Bundled DVIR module inside ELDs (Motive, Samsara, Geotab, Omnitracs/Solera) — present but functionally weak per practitioner reviews.
- Standalone point solutions: Whip Around, Fleetio, HVI, Zonar EVIR (RFID-anchored, defensible patent), J.J. Keller Encompass, BigRoad.
- Custom-built or SafetyCulture/iAuditor forms.

**Why this might be a SOTI opportunity**
- *Adjacent:* DVIR is a Snap workflow archetype — form, photo, signature, geotag, sync to back-office. Already supported per SOTI's published Snap fleet content. Source: [SOTI Snap T&L blog](https://soti.net/resources/blog/2025/driving-digital-transformation-in-tl-with-soti-snap/).
- *Platform-extension:* Coupling DVIR with HOS exposure, CSA score telemetry, and roadside-inspection prep would extend MobiControl into a compliance layer no MDM peer offers.
- *Net-new:* A standalone DVIR product is a crowded category dominated by Whip Around and the ELD bundles; SOTI would face a moat without an obvious wedge.

**Why this might NOT be a SOTI opportunity**
- Zonar EVIR has a verifiable RFID-anchored patent moat for the high end of the market.
- Whip Around won the SMB no-hardware niche with simple pricing.
- ELD-bundled DVIR, even when weak, is "good enough free" for many carriers.

**Regulatory tailwinds**
- FMCSA Final Rule (Docket FMCSA-2025-0115) effective March 23, 2026 amending 49 CFR 396.11 and 396.13 to formally accept eDVIR. Source: [Heavy Vehicle Inspection comparison citing the docket](https://heavyvehicleinspection.com/article/top-fleet-inspection-software-comparison-features-pricing).
- CSA scoring drives insurance and shipper-of-choice consequences.

**Workflow seam check**
Yes — DVIR sits at the seam between driver mobile, ELD telematics, fleet maintenance system, and back-office compliance. No incumbent owns the full seam.

---

## C2. Yard management for mid-market 3PLs and private fleets

**The pain in plain language**
A 3-DC 3PL has 200 trailers in motion across yards. Where is trailer 4172? Whiteboard says dock 7. Reality is dock 12. Yard hostlers radio each other; gate-in is a paper sheet; appointments overflow because dock scheduling lives in Outlook. Detention bills pile up.

**How it's solved today**
- Whiteboard + radio + spreadsheet at the long-tail.
- Enterprise YMS at large 3PLs: Kaleris (PINC merger), Blue Yonder YMS, FourKites Dynamic Yard, C3 Solutions, SAP YMS module.
- Mid-market: YardView (acquired by Vector in 2024), Velostics, Terminal Industries. Source: [DC Velocity Vector-YardView](https://www.dcvelocity.com/technology/warehouse-it/yard-management-yms/vector-acquires-yardview-to-improve-dock-visibility), [Velostics 2025 trends](https://www.velostics.com/blog/yms-trends-to-watch-for-2025).
- Custom-built / SAP-on-spreadsheets at private manufacturer fleets.

**Why this might be a SOTI opportunity**
- *Adjacent:* Hostler tablet UX, gate-guard handheld, driver check-in form — all run on rugged Android already managed by MobiControl. Snap can capture the workflows.
- *Platform-extension:* SOTI could build a lightweight YMS layer (gate, trailer inventory, dock assignment) that leverages the rugged install base — not as deep as Kaleris, but right-sized for mid-market 3PLs that won't buy enterprise YMS.
- *Net-new:* Standalone YMS is a recognized category ($4.32B dock+yard market in 2025, ~12% CAGR). Source: [Grand View Research dock/yard report](https://www.grandviewresearch.com/industry-analysis/dock-yard-management-systems-market-report). SOTI would compete with category-builders; right-to-win unclear without rugged-device + low-IT-friction wedge.

**Why this might NOT be a SOTI opportunity**
- Camera/RTLS hardware moat at the high end (Kaleris/PINC's YardIQ uses RFID, computer vision).
- Vector's YardView acquisition is consolidating the mid-market.

**Regulatory tailwinds**
- Detention/demurrage cost transparency under FMCSA's Truck Transportation Service Standards (in development).
- FSMA 204 indirectly — a yard losing a reefer is a traceability event.

**Workflow seam check**
Strong yes. YMS sits between TMS, WMS, and dock scheduling. Multiple incumbents own pieces; none owns the rugged-driver-handoff seam well.

---

## C3. Dock scheduling & appointment management

**The pain in plain language**
The 3PL receiver overbooks dock 4 because two TMSs fed appointments without coordinating. Trucks queue for 90 minutes. Detention ensues. Customer service blames operations.

**How it's solved today**
- Outlook / spreadsheets at small operators.
- Standalone dock platforms: Opendock (acquired by Loadsmart), DataDocks, Velostics, Vector.
- Built into TMS/YMS at enterprise.

**Why this might be a SOTI opportunity**
- *Adjacent:* Limited — dock scheduling is browser/mobile-web, not a rugged-device workflow.
- *Platform-extension:* Could pair with C2 yard management for SOTI as a unified "yard + dock" mid-market play.
- *Net-new:* Loadsmart Opendock has the lead; standalone bet weak for SOTI.

**Why this might NOT be a SOTI opportunity**
- Doesn't run on a rugged device — SOTI's distribution advantage is muted.
- Loadsmart, Vector, Velostics are well-capitalized and category-aware.

**Regulatory tailwinds:** weak.

**Workflow seam check:** yes, but SOTI's seam advantage is weaker here.

---

## C4. Proof of Delivery (POD) — evidence-grade capture for non-major shippers

**The pain in plain language**
A regional last-mile carrier delivers for 12 different shippers, each with a different POD requirement: Shipper A wants signature, Shipper B wants photo + GPS pin, Shipper C wants barcode scan + temperature reading. The driver app cobbles 12 forms together; disputes still cost the carrier real money.

**How it's solved today**
- Custom-built driver apps at most regional carriers.
- ePOD modules in TMS (Descartes, MercuryGate, McLeod).
- Standalone: Detrack, Track-POD, Onfleet POD, Bringg, Project44 DriveView. Source: [Descartes ePOD](https://www.descartes.com/solutions/routing-mobile-and-telematics/route-optimization), [Bringg](https://onfleet.com/route-optimization-software).
- Major shipper-mandated apps (Amazon, FedEx, UPS) for their networks.

**Why this might be a SOTI opportunity**
- *Adjacent:* Snap can build configurable POD forms per shipper. The driver device is already managed by MobiControl. This is one of the cleanest Snap fits in the entire taxonomy.
- *Platform-extension:* A "POD evidence vault" with image quality scoring, dispute-pack export, and shipper-grade audit trail is a plausible SOTI net-new on top of the install base.
- *Net-new:* Crowded — Detrack, Track-POD, Onfleet are well-positioned. SOTI net-new bet is weak unless paired with routing (see C5/C6).

**Why this might NOT be a SOTI opportunity**
- Major-shipper-mandated apps (Amazon DSP, FedEx Ground) are walled gardens.
- Bringg and Project44 are aggregators with shipper relationships.

**Regulatory tailwinds:** weak; commercial pressure (chargeback disputes), not regulatory.

**Workflow seam check:** yes — POD sits between driver app, TMS, shipper system, customer service.

---

## C5. Last-mile route optimization for sub-200-vehicle regional carriers

**The pain in plain language**
The 80-vehicle regional last-mile carrier still runs daily route plans in Excel. The dispatcher is the institutional knowledge. When the dispatcher is sick, routes are 12% less efficient. Drivers lose time; CPS (cost per stop) is unmanaged.

**How it's solved today**
- Excel + dispatcher knowledge (most regionals).
- Standalone: OptimoRoute, Routific, Onfleet, Route4Me, Locus, Bringg, Elite EXTRA. Source: [Routific OptimoRoute alternatives](https://www.routific.com/blog/optimoroute-alternatives), [Intel Market Research last-mile route optimization](https://www.intelmarketresearch.com/last-mile-route-optimization-software-market-42577).
- Enterprise: Descartes, Manhattan Active Omni, Oracle.
- Embedded in TMS for some.

**Why this might be a SOTI opportunity**
- *Adjacent:* No — routing is a back-office optimization workflow, not a rugged-device workflow.
- *Platform-extension:* Routing engine paired with the device-managed driver execution layer (POD, exception, returns) — an end-to-end workflow that no incumbent fully closes for the value segment.
- *Net-new:* Standalone routing is crowded. The wedge could be "routing + execution" for the value segment of regional last-mile and big-and-bulky.

**Why this might NOT be a SOTI opportunity**
- Routing optimization is a math/algorithms business; OptimoRoute, Routific, Locus have years of investment in the engine.
- SOTI has no public routing IP.
- Channel: routing is sold to dispatch managers, not to IT — different buyer than SOTI's MDM motion.

**Regulatory tailwinds:** weak; commercial (CPS, on-time delivery SLAs).

**Workflow seam check:** strong — routing sits between TMS, dispatch, driver app, customer notification.

---

## C6. Routing + execution bundles (the seeded candidate)

**Three bundle hypotheses to evaluate distinctly:**

### C6a. Last-mile route + POD
**Pain:** dispatcher plans routes in tool A; driver executes in tool B; POD lives in tool C. Each handoff loses data and adds dispute risk.
**Today:** Routific + custom POD form, OptimoRoute + Onfleet, Bringg as monolith.
**SOTI angle:** Snap-built POD + a routing engine (build, buy, or partner) on the SOTI-managed device fleet. Adjacent + platform extension hybrid. Net-new only if SOTI builds a routing engine.

### C6b. Long-haul route + DVIR/HOS
**Pain:** route assignment happens at dispatch; DVIR happens at the truck; HOS clocks during driving. Three systems. Driver-side device juggles.
**Today:** Motive, Samsara, Geotab — all bundle these. Solera/Omnitracs. So this seam is *already* owned at the high end. Long-tail SMB carriers stitch together cheap ELD + paper DVIR.
**SOTI angle:** Adjacent only — rugged device manager that hosts the ELD + DVIR + dispatch apps cleanly. Hard to win against Motive/Samsara who own the data plane. Net-new is a non-starter without telematics IP.

### C6c. Yard-to-route handoff
**Pain:** The trailer is loaded at dock 7 at 14:32; the driver picks up at 15:10; the route plan was built assuming 15:00 departure. Detention cascades into route delay. Customer ETA is wrong.
**Today:** This seam is owned by *almost no one* well. FourKites Dynamic Yard + visibility helps but doesn't close the driver-app loop. Velostics + Vector partial. Most carriers email or rely on dispatcher phone calls.
**SOTI angle:** Plausible platform-extension play. Ties C2 (yard) to C5 (route) via the rugged device that's in the hostler, the dock guard, and the driver. Genuine seam ownership.

**Bundle-level synthesis**
- C6a is the most accessible (POD is a Snap-natural; routing engine is the build-or-buy question).
- C6b is the least promising (Motive/Samsara own this seam).
- C6c is the most distinctive — it's a workflow no one owns, and SOTI's device-management footprint is the *only* common substrate across the three actors (hostler, gate, driver).

---

## C7. FSMA 204 KDE/CTE capture across cold chain

**The pain in plain language**
A 3PL holds frozen seafood for a major retailer. FSMA 204 demands every Critical Tracking Event (Receive, Ship, Transform) emit Key Data Elements within a 24-hour FDA request window. The 3PL today maintains lot-level data in their WMS but the carrier handoff data lives in the TMS, the inbound BOL is paper, and the receiver's data system doesn't share lot codes back. Compliance officer is panicking.

**How it's solved today**
- Spreadsheet workarounds.
- Trustwell, Wherefour, FoodLogiQ, Ripe.io traceability platforms.
- Built into newer WMS (Manhattan Active, Blue Yonder).
- Carrier-side: nothing dedicated.

**Why this might be a SOTI opportunity**
- *Adjacent:* Snap can build the receive/ship CTE capture form on the rugged device that's already scanning the lot at intake. This is well-aligned with SOTI's existing footprint.
- *Platform-extension:* A SOTI "FSMA 204 capture layer" that emits the FDA-mandated KDE schema regardless of the receiver's WMS would be a real product wedge.
- *Net-new:* Trustwell et al. own the SaaS traceability layer; SOTI's net-new bet is weak unless it productizes the device-side capture.

**Why this might NOT be a SOTI opportunity**
- Compliance officer is the buyer, not IT — different sales motion.
- The Aug 2025 FDA enforcement extension to July 2028 (Source: [Federal Register 2025-14967](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension)) reduces near-term urgency.

**Regulatory tailwinds**
- FSMA 204 (Jan 2026 record-keeping; July 2028 enforcement). Source: [FDA FSMA 204 page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods).
- Strongest single regulatory driver in this candidate set.

**Workflow seam check:** strong — sits across receiver WMS, TMS, carrier app, FDA reporting.

---

## C8. Detention & demurrage tracking for trucking carriers

**The pain in plain language**
A mid-market dry-van carrier eats $40K/month in unrecovered detention because dispatchers forget to bill, drivers don't capture arrival/depart timestamps cleanly, and shippers contest. The data exists across ELD, dispatch notes, and driver memory.

**How it's solved today**
- Manual tracking, dispatcher recall, ELD geofence approximation.
- FourKites D&D dashboards (shipper-side; not carrier-side). Source: [FourKites D&D press release](https://www.fourkites.com/press/fourkites-releases-powerful-new-capabilities-to-manage-runaway-demurrage-and-detention-fees/).
- TMS-bundled dwell-time analytics (McLeod, MercuryGate).
- Custom spreadsheets + factoring company data at small carriers.

**Why this might be a SOTI opportunity**
- *Adjacent:* Driver-side arrival/depart timestamp capture (auto from device geofence + manual confirm) on the SOTI-managed device. Snap-natural.
- *Platform-extension:* "D&D recovery" SaaS that ties device-captured data to invoice-ready dispute packs. Underdeveloped category for carriers.
- *Net-new:* Possible, but FourKites/Vector are positioning. Wedge is "carrier-side D&D recovery" vs. their shipper-side framing.

**Why this might NOT be a SOTI opportunity**
- ELDs already capture some of this; carriers may resist new tooling.
- Buyer is fleet ops or finance, not IT.

**Regulatory tailwinds:** moderate — FMCSA detention transparency rulemaking has been slow but active.

**Workflow seam check:** yes — between driver app, ELD, TMS, dispatch, billing.

---

## C9. CDL driver onboarding & compliance lifecycle

**The pain in plain language**
A 200-truck carrier hires 8–12 drivers a month. Each requires a DOT physical, drug screen, MVR pull, PSP pull, employment verification, and HR onboarding. Speed-to-hire is the differentiator; compliance lapses (e.g., expired med card) create CSA risk.

**How it's solved today**
- Tenstreet (acquired DriverReach March 2025), Idelic, EBE Technologies, J.J. Keller Encompass. Source: [Truckinginfo on Tenstreet/DriverReach](https://www.truckinginfo.com/news/tenstreet-buys-driverreach-to-boost-driver-hiring-and-compliance-tools).
- HRIS bolt-ons.
- Spreadsheet + email at sub-50-truck carriers.

**Why this might be a SOTI opportunity**
- *Adjacent / Platform-extension / Net-new:* All weak. SOTI has no domain expertise in CDL recruiting workflow; the buyer is HR or recruiting, not IT; Tenstreet just consolidated the category.

**Verdict:** Drop. Outside SOTI's domain knowledge and the competitive landscape just consolidated.

---

## C10. IFTA fuel tax reporting

**The pain in plain language**
Quarterly IFTA filing is a per-state miles-and-gallons calculation. ELDs auto-capture jurisdiction miles; carriers reconcile to fuel receipts.

**How it's solved today**
- ELD-vendor IFTA modules (Motive, Samsara, Geotab).
- Standalone: TruckLogics, IFTA Plus, Tax2efile.
- Outsourced to fuel tax services.

**Why this might be a SOTI opportunity**
- All apertures: weak. ELD vendors own the data; tax compliance is a finance-buyer category.

**Verdict:** Drop. Domain mismatch.

---

## C11. Returns / reverse logistics at the doorstep

**The pain in plain language**
A driver delivers a TV; customer says it's the wrong model. Driver has no way to capture the return on the spot; goes back to the warehouse with no documentation; the retailer's system shows it as delivered; customer is angry; chargeback follows.

**How it's solved today**
- Mostly call-center fallback ("we'll send a driver tomorrow").
- Some big-and-bulky carriers (XPO, J.B. Hunt Final Mile) have custom returns apps.
- Returnly, Loop Returns are e-commerce returns platforms (warehouse-side, not doorstep).

**Why this might be a SOTI opportunity**
- *Adjacent:* Snap-buildable doorstep return-capture form. Photo, condition, RMA generation.
- *Platform-extension:* A returns SaaS layer integrated with major retailer return systems.
- *Net-new:* Standalone is a tough sell.

**Verdict:** Interesting Snap opportunity, but customer demand signal is weak in public sources. Demote to medium priority pending customer interviews.

---

## C12. Reefer temperature-excursion exception management

**The pain in plain language**
A reefer trailer's temperature spikes during a 3-hour delay. Carrier Transicold or Thermo King telematics generates an alert. Then what? The driver has paper, the dispatcher has email, the receiver argues the load on arrival, the carrier has no defensible record.

**How it's solved today**
- Carrier/Thermo King reefer telematics generate the alert.
- Email + spreadsheet documentation.
- TempTale / Sensitech standalone temperature data loggers.
- Some 3PLs have built internal exception consoles.

**Why this might be a SOTI opportunity**
- *Adjacent:* Driver-side exception form on the rugged device. Snap-natural.
- *Platform-extension:* Exception management workflow tied to the reefer telematics feed and the device-side documentation.
- *Net-new:* Crowded; Carrier and Thermo King are aggressively expanding into telematics+software.

**Verdict:** Interesting but reefer-telematics moat is real. Demote to medium priority.

---

## C13. Cycle counting & inventory accuracy in 3PL warehouses

**The pain in plain language**
3PL warehouse cycle counts done by warehouse associates with rugged scanners. Variance investigation is mostly tribal. Slotting decisions don't reflect actual pick velocity. WMS reports tell you what happened; nothing tells you what to do about it.

**How it's solved today**
- WMS-native (Manhattan, Blue Yonder, Korber).
- Lucas Systems voice + analytics overlays.
- XSight already collects rugged-device telemetry signal that could feed slotting/labor analytics.

**Why this might be a SOTI opportunity**
- *Adjacent:* XSight extension — labor productivity analytics from device telemetry.
- *Platform-extension:* "Warehouse Operations Intelligence" overlay on top of MobiControl + XSight. Plausible.
- *Net-new:* Lucas, Locus Robotics own pieces; net-new is crowded.

**Verdict:** Interesting XSight extension; carry forward as a Phase 2 candidate.

---

## C14. Hazmat (49 CFR) workflows

**The pain in plain language**
Hazmat shipments require specific placarding, paperwork, driver endorsements, route restrictions. Errors create FMCSA CSA scoring and federal liability.

**How it's solved today**
- TMS hazmat modules (limited).
- J.J. Keller compliance services.
- Carrier-built spreadsheets + paperwork.

**Why this might be a SOTI opportunity**
- All apertures weak. Domain niche; J.J. Keller dominant.

**Verdict:** Drop.

---

## C15. ETA management & customer notifications

**The pain in plain language**
Shippers want predictive ETAs; carriers send "out for delivery" texts; customers want ten-minute precision.

**How it's solved today**
- FourKites, Project44, Tive — visibility platforms.
- Bringg, Onfleet — carrier-side notification.
- Many shipper-built solutions.

**Why this might be a SOTI opportunity**
- All apertures weak. FourKites/Project44 own the visibility category. SOTI lacks the multi-carrier data network that makes these platforms valuable.

**Verdict:** Drop.

---

## Ranking table

| # | Candidate | Sub-segments most affected | Regulatory tailwind | Workflow seam? | First-pass priority |
|---|---|---|---|---|---|
| C1 | Lightweight DVIR + roadside-prep | Trucking, Cold Chain, Field Service | **Strong** (FMCSA eDVIR rule Mar 2026, CSA) | Yes | **High** |
| C2 | Yard management for mid-market 3PL | Warehousing/3PL, Trucking, Cold Chain | Moderate | **Strong** | **High** |
| C3 | Dock scheduling | Warehousing/3PL | Weak | Yes | Medium |
| C4 | POD evidence-grade capture | Last Mile, Courier, Trucking | Weak | Yes | **High** |
| C5 | Last-mile route optimization (sub-200) | Last Mile, Courier | Weak | Strong | Medium |
| C6 | Routing + execution bundles (seeded) | Last Mile, Trucking | Mixed | **Strong** (esp. C6c yard-to-route) | **High** |
| C7 | FSMA 204 KDE/CTE capture | Cold Chain, Warehousing/3PL | **Strongest** (FSMA 204) | Strong | **High** |
| C8 | Detention/demurrage carrier-side | Trucking, Cold Chain | Moderate | Yes | Medium |
| C9 | CDL onboarding | Trucking | Moderate | No | Drop |
| C10 | IFTA | Trucking | None | No | Drop |
| C11 | Doorstep returns | Last Mile | None | Yes | Medium |
| C12 | Reefer exception mgmt | Cold Chain | Moderate (FSMA-adjacent) | Yes | Medium |
| C13 | Warehouse cycle count / labor analytics | Warehousing/3PL | None | Yes | Medium |
| C14 | Hazmat | Trucking | Moderate | No | Drop |
| C15 | ETA & customer notification | Last Mile, Trucking | None | Yes | Drop |

---

## Recommendation to orchestrator

Fan out Phase 2 deep-dives on the **High** priority candidates:
- **C1** — Lightweight DVIR + roadside-inspection prep (slug: `dvir-compliance`)
- **C2** — Yard management for mid-market 3PL (slug: `yard-mgmt-midmarket`)
- **C4** — POD evidence-grade capture (slug: `pod-evidence`)
- **C6c** — Yard-to-route handoff (slug: `yard-to-route`) — this is the seeded-bundle's single most distinctive seam; carry it forward separately from generic routing
- **C7** — FSMA 204 KDE/CTE capture (slug: `fsma-204-capture`)

That's 5 candidates, fitting the 5–8 deep-dive target. C3, C5, C8, C11, C12, C13 are kept as medium-priority for the discovery brief's "broader watchlist." C9, C10, C14, C15 are dropped with rationale.

Note for the orchestrator: C6a (route + POD) and C6b (route + DVIR/HOS) are *implicitly covered* by deep-diving C4 (POD) and C1 (DVIR) respectively, and the Phase 3 brief should weave those bundle hypotheses back together rather than treating them as four separate candidates.
