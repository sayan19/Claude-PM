# T&L Monetization Gap Research

## Gap Summary Table

| Gap Name | Sub-Segments Affected | Category | Evidence Strength | Currently Solved By | Source |
|---|---|---|---|---|---|
| Digital DVIR and Pre-Trip Inspection Workflows | LTL and FTL trucking and freight, Courier and same-day delivery | Digitization, Compliance | Strong | Geotab, Samsara, Verizon Connect, Driveroo, TruckX | [FMCSA DVIR Rule](https://www.fmcsa.dot.gov/regulations/inspection-repair-and-maintenance-driver-vehicle-inspection-report-dvir) |
| FDA FSMA 204 Cold Chain Traceability and Temperature Logging | Cold chain and temperature-controlled logistics, Warehousing and distribution centers (3PL) | Compliance | Strong | IoT sensor vendors (Milesight, Sonicu, Telit), Samsara condition monitoring | [FDA FSMA 204 Rule](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods) |
| CSA Safety Scoring and Driver Behavior Compliance | LTL and FTL trucking and freight, Last-mile and final-mile delivery | Compliance | Strong | Samsara, Geotab, Lytx | [FMCSA CSA Scoring Changes](https://www.iatinsurancegroup.com/resources/blog/2025/changes-to-fmcsa-csa-scoring/) |
| Warehouse Shift Productivity and Device Utilization Analytics | Warehousing and distribution centers (3PL) | Analytics | Medium | JASCI LMS, OneTrack, Easy Metrics ProTrack | [OneTrack Productivity](https://www.onetrack.ai/solutions/productivity) |
| MDM to WMS, TMS, and ERP Integration | Warehousing and distribution centers (3PL), LTL and FTL trucking and freight | Integration | Medium | No single vendor; manual integration or middleware | [ExploreWMS Challenges](https://www.explorewms.com/biggest-wms-challenges.html) |
| Device Lifecycle Management: Staging, Refresh, and End-of-Life | All sub-segments | Lifecycle | Medium | SHI, MCPC, PiiComm, vMOX, Datex | [Unduit DLM Guide](https://www.unduit.com/blog/device-lifecycle-management-best-practices/) |
| Reporting and Dashboard Customization | All sub-segments | Analytics | Medium | Complaint about SOTI; competitors not clearly better | [G2 SOTI Reviews](https://www.g2.com/products/soti-mobicontrol/reviews) |

---

## Gap 1: Digital DVIR and Pre-Trip Inspection Workflows

**What the gap is:**
Drivers of commercial vehicles are required by FMCSA regulations (49 CFR 396.11 and 396.13) to complete Driver Vehicle Inspection Reports before and after each trip. Many fleets still use paper forms for this. Paper DVIRs are prone to "rubber-stamping" where drivers check every item without performing the actual inspection. FMCSA's May 2025 NPRM (docket FMCSA-2025-0115) proposes explicit eDVIR authorization language, accelerating the shift to digital. SOTI Snap could be used to build digital inspection forms, but SOTI does not offer a purpose-built DVIR workflow product.

**Sub-segments affected:**
LTL and FTL trucking and freight. Courier and same-day delivery. Last-mile and final-mile delivery.

**How customers handle it today:**
Several fleet management vendors offer integrated eDVIR solutions. Geotab streamlines DVIR reporting with its Geotab Drive app, combining it with ELD compliance, driver ID, and messaging in a single app.
Source: [Geotab DVIR](https://www.geotab.com/fleet-management-solutions/dvir/)

Verizon Connect offers a digital DVIR tool that reduces burden on drivers and improves mechanic communication.
Source: [Verizon Connect DVIR](https://www.verizonconnect.com/solutions/dvir/)

Teletrac Navman pushes failure notifications from DVIRs straight into the TN360 maintenance platform.
Source: [Teletrac Navman DVIR](https://www.teletracnavman.com/fleet-management-software/compliance/dvir)

Driveroo Fleet offers a mobile app for pre and post-trip DVIRs with instant web platform visibility.
Source: [Driveroo Fleet](https://www.driveroo.com/fleet-edvir-app/)

TruckX automates DVIR creation, completion, and retention with live defect monitoring.
Source: [TruckX DVIR](https://truckx.com/glossary/fleet-maintenance/driver-vehicle-inspection-report/)

**What customers are actually saying:**
No direct customer quotes found comparing SOTI to DVIR-specific tools. Needs primary research.

**Regulatory or compliance driver:**
FMCSA 49 CFR 396.11 and 396.13 require DVIRs for commercial motor vehicles over 10,000 pounds. Penalties for missing or incomplete DVIRs can reach $1,270 per day. Falsifying a DVIR can result in fines up to $12,695. FMCSA's May 2025 NPRM (FMCSA-2025-0115) proposes explicit eDVIR authorization language. DVIR violations remain among the most frequent citations during DOT audits; only 7% of motor carriers pass a focused compliance review without a single violation.
Source: [FMCSA DVIR Regulations](https://www.fmcsa.dot.gov/regulations/inspection-repair-and-maintenance-driver-vehicle-inspection-report-dvir)
Source: [Heavy Vehicle Inspection DVIR Guide](https://heavyvehicleinspection.com/article/dvir-guide-driver-vehicle-inspection-report)

**Budget signal:**
Multiple dedicated DVIR vendors exist with standalone products (Driveroo, TruckX, Simply Fleet), indicating a market where customers pay separately for this capability. Fleet management platforms (Geotab, Samsara, Verizon Connect) bundle DVIR with broader fleet solutions. FMCSA estimates that proper DVIRs prevent approximately 14,000 accidents every year, creating a strong insurance and liability cost justification.
Source: [Heavy Vehicle Inspection DVIR Guide](https://heavyvehicleinspection.com/article/dvir-guide-driver-vehicle-inspection-report)

**Which SOTI product is closest to addressing this gap:**
SOTI Snap (no-code digital forms and app builder) could be used to create custom DVIR inspection forms on rugged devices. However, Snap does not include DVIR-specific features such as GPS verification of driver location, photo capture requirements for key components, quality scoring for suspiciously fast inspections, or automated maintenance workflow triggers.

**What was not found:**
No evidence found of SOTI customers using Snap for DVIR workflows specifically. Needs primary research.
No direct customer quotes comparing SOTI to DVIR competitors. Needs primary research.
No pricing data found for standalone DVIR solutions. Needs primary research.

---

## Gap 2: FDA FSMA 204 Cold Chain Traceability and Temperature Logging

**What the gap is:**
The FDA's FSMA 204 Food Traceability Final Rule requires companies that manufacture, process, pack, or hold foods on the Food Traceability List to maintain records with Key Data Elements at Critical Tracking Events, and provide that data to the FDA within 24 hours on request. Records must be retained for 24 months. This creates new technology spending on continuous temperature monitoring, digital chain-of-custody records, and traceability data integration. SOTI manages the devices used in cold chain operations but does not capture or store temperature, humidity, or traceability data itself.

**Sub-segments affected:**
Cold chain and temperature-controlled logistics. Warehousing and distribution centers (3PL), specifically those handling food.

**How customers handle it today:**
IoT sensor vendors provide continuous temperature monitoring solutions separate from MDM. Milesight offers IoT-based cold chain temperature monitoring with connected sensors.
Source: [Milesight Cold Chain](https://www.milesight.com/iot/solution/cold-chain-temperature-monitoring)

Telit provides IoT-enabled monitoring that creates connected, intelligent environments for cold chain logistics.
Source: [Telit Cold Chain IoT](https://www.telit.com/blog/iot-enabled-monitoring-changing-cold-chain-logistics-forever/)

Samsara offers temperature, humidity, door, and cargo sensors for trailer tracking and condition monitoring as part of its fleet management platform.
Source: [Samsara ELD Features](https://www.empwrtrucking.com/freight-technology/samsara-eld-a-comprehensive-guide-to-features-benefits-and-pricing/)

Paper logs and spreadsheets remain in use at some operations but cannot provide the precision, speed, or accuracy the rule demands.
Source: [SFL Companies FSMA 204](https://www.sflcompanies.com/post/how-the-fdas-fsma-204-rule-is-changing-cold-chain-logistics)

**What customers are actually saying:**
No direct customer quotes found from T&L cold chain operators about MDM and temperature logging gaps. Needs primary research.

**Regulatory or compliance driver:**
FDA FSMA 204 (Food Traceability Final Rule). Original compliance date: January 20, 2026. On March 20, 2025, FDA announced a 30-month extension, pushing the compliance deadline to July 20, 2028. Formal rulemaking in the Federal Register is underway.
Source: [FDA FSMA 204 Final Rule](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods)
Source: [Federal Register Compliance Extension](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension)

Foods covered: fresh produce, seafood, dairy, ready-to-eat deli items, soft cheeses, and other perishable products requiring temperature control.
Source: [Lindner Logistics FSMA 204 Guide](https://www.lindnerlogistics.com/fsma-204-cold-chain-compliance)

**Budget signal:**
Technology enablers required include connected sensors for real-time temperature, humidity, vibration, and location monitoring, plus API integrations between brokers, shippers, and carriers. Multiple IoT vendors (Milesight, Sonicu, Telit, Pyliot) have purpose-built cold chain monitoring products, indicating active spending in this area.
Source: [SFL Companies FSMA 204](https://www.sflcompanies.com/post/how-the-fdas-fsma-204-rule-is-changing-cold-chain-logistics)

**Which SOTI product is closest to addressing this gap:**
SOTI Connect manages IoT endpoints including printers and sensors. SOTI XSight provides device-level diagnostics. Neither product captures or stores temperature traceability data in the format required by FSMA 204. SOTI Snap could be used to build temperature logging forms, but it would not replace continuous IoT sensor monitoring.

**What was not found:**
No evidence found of SOTI customers using any SOTI product for FSMA 204 compliance. Needs primary research.
No evidence found for how much cold chain operators spend on temperature monitoring technology. Needs primary research.
No direct customer quotes about the gap between MDM and cold chain compliance. Needs primary research.
No evidence found for GDP (Good Distribution Practice) pharma logistics spending in connection with MDM. Needs primary research.

---

## Gap 3: CSA Safety Scoring and Driver Behavior Compliance

**What the gap is:**
FMCSA is overhauling its Compliance, Safety, Accountability (CSA) scoring system. Starting February 2026, "BASICs" become "Compliance Categories," the violation window shortens to 12 months, and the Utilization Factor expands to carriers with up to 250,000 vehicle miles traveled per average power unit. The system is shifting from documentation-based compliance to a data-first model where carrier interventions are triggered by data trends, not just inspections. Fleets need technology to track driver behavior, safety events, and compliance data. SOTI MobiControl manages the devices drivers use but does not capture driver safety scores, braking events, or compliance metrics.

**Sub-segments affected:**
LTL and FTL trucking and freight. Last-mile and final-mile delivery. Courier and same-day delivery.

**How customers handle it today:**
Samsara offers AI dash cams, driver safety scoring, and compliance dashboards. Ranked #1 on G2 for Fleet Management across all of 2025 with a 99 average customer satisfaction score.
Source: [Samsara G2 Rankings](https://www.samsara.com/company/news/press-releases/Samsara-Ranks-No-1-in-Fleet-Management-on-G2-for-2025)

Geotab provides ELD, fleet tracking, and compliance reporting with advanced telematics and IoT integration. Analyst rating of 77 on SelectHub, tied with Samsara.
Source: [SelectHub Samsara vs Geotab](https://www.selecthub.com/fleet-management-software/samsara-vs-geotab/)

Lytx provides AI-driven driver safety tools. Considered one of the best for advanced features alongside Geotab.
Source: [Dataconomy ELD Devices](https://dataconomy.com/2025/09/18/best-eld-devices-and-fleet-management-tools-2025-top-picks-for-trucking-companies/)

**What customers are actually saying:**
No direct customer quotes found about gaps between MDM and driver safety scoring. Needs primary research.

**Regulatory or compliance driver:**
FMCSA CSA scoring overhaul with full enforcement starting February 2026. New compliance categories, shorter violation windows, and expanded utilization factor. More than 100,000 violations reported in FMCSA enforcement data from 2025. Most issues involved missed Clearinghouse queries, incomplete driver qualification files, and gaps in maintenance records. Some fines exceeded $125,000.
Source: [IAT Insurance CSA Scoring Changes](https://www.iatinsurancegroup.com/resources/blog/2025/changes-to-fmcsa-csa-scoring/)
Source: [FreightWaves FMCSA Compliance Reviews](https://www.freightwaves.com/news/what-fleets-need-to-know-about-fmcsa-compliance-reviews-in-2025)

**Budget signal:**
Fleet management is 38% of the telematics market share as of 2025, indicating substantial existing spend.
Source: [Keystonecorp IoT Fleet Guide](https://keystonecorp.com/logistics/a-detailed-guide-to-iot-in-fleet-management/)

Samsara, Geotab, Lytx, Verizon Connect, and Motive all have dedicated fleet safety and compliance products, indicating a large addressable market where customers are paying for these capabilities.
Source: [Dataconomy ELD Devices](https://dataconomy.com/2025/09/18/best-eld-devices-and-fleet-management-tools-2025-top-picks-for-trucking-companies/)

**Which SOTI product is closest to addressing this gap:**
SOTI XSight provides device-level analytics (battery, app, signal, OBDII telemetry) but does not track driver behavior, safety events, or CSA compliance metrics. SOTI MobiControl manages the ELD and fleet management apps on the device but does not replace the ELD or telematics platform itself.

**What was not found:**
No evidence found of SOTI customers using XSight OBDII data for CSA compliance purposes. Needs primary research.
No direct customer quotes about wanting MDM and safety scoring in the same platform. Needs primary research.
No evidence found for fleet spending specifically on driver safety scoring tools as distinct from ELD spend. Needs primary research.

---

## Gap 4: Warehouse Shift Productivity and Device Utilization Analytics

**What the gap is:**
Warehouse operations managers want to see how productive each shift is and how devices are being utilized across shared-device environments. The gap is between what MDM shows (device health, battery, app usage) and what operations needs (picks per hour, idle time, gap time, worker-level performance by shift). Dedicated Labor Management Systems (LMS) exist for this, but they sit outside MDM and do not integrate with device-level data.

**Sub-segments affected:**
Warehousing and distribution centers (3PL).

**How customers handle it today:**
JASCI offers a Labor Management System built into its WMS. Visual dashboards show individual, team, and shift performance. As soon as an employee logs in, the system tracks their activity.
Source: [JASCI Labor Management](https://www.jascicloud.com/products/labor-management)

OneTrack identifies idle time, gap time, and indirect time, and alerts when a process takes longer than expected or when an operator falls behind goal.
Source: [OneTrack Productivity](https://www.onetrack.ai/solutions/productivity)

Easy Metrics ProTrack allows floor managers to run their operation in real time from one screen, with a Kiosk for tracking production hours for activities that do not use RF, voice, or terminal systems.
Source: [Easy Metrics ProTrack](https://www.easymetrics.com/protrack-labor-management-software/)

**What customers are actually saying:**
No direct customer quotes found about wanting productivity analytics from their MDM platform. Needs primary research.

**Regulatory or compliance driver:**
No regulatory driver identified.

**Budget signal:**
Multiple dedicated LMS vendors exist (JASCI, OneTrack, Easy Metrics), indicating warehouses pay separately for shift-level productivity analytics. Finding enough workers for manual and repetitive tasks remains a major challenge for warehouses in 2025, increasing the value of analytics that optimize existing labor.
Source: [Cyzerg Warehouse Automation Trends](https://cyzerg.com/blog/5-warehouse-automation-trends-2025/)

**Which SOTI product is closest to addressing this gap:**
SOTI XSight provides device-level analytics including app usage, battery health, and signal strength. The iDC Logistics case study shows XSight App Usage Dashboards in use at a 3PL. However, XSight does not correlate device activity with worker identity, shift schedules, or operational KPIs like picks per hour.
Source: [SOTI iDC Logistics Case Study](https://soti.net/resources/customer-stories-and-use-cases/idc-logistics/?csc=)

**What was not found:**
No evidence found of SOTI customers requesting worker-level productivity features from XSight. Needs primary research.
No evidence found for pricing of warehouse LMS tools. Needs primary research.
No evidence found for how warehouse operators currently bridge the gap between MDM device data and LMS productivity data. Needs primary research.

---

## Gap 5: MDM to WMS, TMS, and ERP Integration

**What the gap is:**
T&L operations run on multiple disconnected systems: WMS for warehouse execution, TMS for transportation planning, ERP (SAP, Oracle) for business logic, and MDM for device management. These systems do not talk to each other in real time. When a palletizer goes down, the TMS planning engine does not know that. When a driver's device fails mid-route, the dispatch system does not automatically reroute. The gap is that MDM sits in its own silo, managing devices without awareness of the operational context those devices support.

**Sub-segments affected:**
Warehousing and distribution centers (3PL). LTL and FTL trucking and freight.

**How customers handle it today:**
Manhattan Associates argues that data-centric integration between TMS and WMS is only a "stop gap" on the road to a holistic execution platform; the real goal is making TMS aware of warehouse-level constraints in real time.
Source: [Logistics Management TMS-WMS](https://www.logisticsmgmt.com/article/logistics_technology_tms_gets_more_warehouse_aware)

Many warehouses struggle to connect WMS with external platforms like e-commerce, CRM, and ERP systems. When integration is broken, teams face manual tasks and redundancies.
Source: [ExploreWMS Challenges](https://www.explorewms.com/biggest-wms-challenges.html)

SAP WM mainstream support ends in 2027, forcing migrations to SAP EWM. SAP Logistics Management (SAP LGM) is SAP's cloud solution bridging warehouse and transport.
Source: [Qinlox SAP WM to EWM](https://www.qinlox.eu/en/insights/von-sap-wm-zu-sap-ewm)

**What customers are actually saying:**
No direct customer quotes found about wanting MDM to integrate with WMS or TMS. Needs primary research.

**Regulatory or compliance driver:**
No regulatory driver identified. However, SAP WM end-of-mainstream-support in 2027 (extendable to 2030 with fees) creates a technology migration trigger.
Source: [Qinlox SAP WM to EWM](https://www.qinlox.eu/en/insights/von-sap-wm-zu-sap-ewm)

**Budget signal:**
WMS and TMS are described as the "backbone of transportation and logistics operations" with declining acquisition and integration costs driving more warehouses to invest.
Source: [ALS WMS/TMS Selection Guide](https://www.als-int.com/insights/posts/wms-tms-selection-guide-strategic-framework-2025/)

SOTI published a January 2026 blog on MDM benefits in the warehouse that references WMS integration.
Source: [SOTI Warehouse MDM Blog](https://soti.net/resources/blog/2026/what-are-the-key-benefits-of-mdm-in-the-warehouse/)

**Which SOTI product is closest to addressing this gap:**
SOTI MobiControl provides APIs and can push device status data to external systems. SOTI XSight provides analytics data. However, no evidence was found of a published SOTI integration with any major WMS (Manhattan, Blue Yonder, SAP EWM) or TMS vendor.

**What was not found:**
No evidence found of SOTI customers integrating MobiControl with WMS, TMS, or ERP systems. Needs primary research.
No evidence found of competitor MDM vendors offering pre-built WMS or TMS integrations. Needs primary research.
No evidence found for what customers pay for MDM-to-WMS integration middleware. Needs primary research.

---

## Gap 6: Device Lifecycle Management: Staging, Refresh, and End-of-Life

**What the gap is:**
Managing the full lifecycle of rugged devices (procurement, staging, deployment, maintenance, refresh, end-of-life disposal) is painful for T&L companies. Devices sit in closets waiting to be deployed, returned equipment piles up, sensitive data rides around on unwiped drives, and IT teams spend time on logistics instead of higher-value work. By 2028, Gartner projects 70% of organizations will adopt managed device lifecycle services, up from fewer than 35% in 2025. 80% of organizations say outdated or inadequate technology holds back innovation.

**Sub-segments affected:**
All sub-segments. This is a cross-cutting problem wherever rugged device fleets exist.

**How customers handle it today:**
SHI provides IT lifecycle services including device lifecycle management.
Source: [SHI Device Lifecycle Management](https://www.shi.com/IT-Lifecycle-Services/Device-Lifecycle-Management)

PiiComm offers a device lifecycle management guide covering procurement through disposal for enterprise fleets.
Source: [PiiComm DLM Guide](https://piicomm.ca/device-lifecycle-management-guide/)

MCPC provides device lifecycle management services.
Source: [MCPC Device Lifecycle](https://www.mcpc.com/services/device-lifecycle-management/)

vMOX offers complete forward and reverse mobile device logistics automation from request to delivery to return, including end-of-life management.
Source: [vMOX Deploy](https://www.vmox.com/deploy)

Datex offers outsourced MDM for supply chain businesses including lifecycle management.
Source: [Datex MDM](https://www.datexcorp.com/mobile-device-management-mdm/)

**What customers are actually saying:**
No direct customer quotes found about device lifecycle pain specifically in T&L. Needs primary research.

**Regulatory or compliance driver:**
No regulatory driver identified. However, data security requirements mean devices with customer delivery data must be properly wiped at end-of-life. SOTI's Road Ahead report found that 61% of T&L workers fear for customer data safety if devices get lost or stolen, and 58% are concerned about data on shared devices.
Source: [SOTI Road Ahead Newsroom](https://soti.net/resources/newsroom/2024/soti-research-reveals-digital-dilemmas-in-the-transportation-and-logistics-industry/)

**Budget signal:**
Multiple managed device lifecycle providers exist (SHI, MCPC, PiiComm, vMOX), indicating enterprises pay for this service. Consumer-grade tablets have an 89% failure rate in the first year of fleet deployment versus below 5% for rugged devices, showing the cost penalty of poor lifecycle decisions.
Source: [Topicon Rugged Tablets](https://www.topicon.hk/blog-detail/rugged-tablets-improve-fleet-management.html)

Drops, screen damage, battery failures, and software malfunctions are described as "inevitable" in logistics environments, requiring spare pool programs and managed repair logistics.
Source: [Unduit DLM Guide](https://www.unduit.com/blog/device-lifecycle-management-best-practices/)

**Which SOTI product is closest to addressing this gap:**
SOTI MobiControl supports zero-touch enrollment and remote provisioning. SOTI Stage enables barcode and NFC-based enrollment. SOTI XSight provides battery health analytics that can inform refresh timing. However, SOTI does not offer procurement management, spare pool management, repair logistics, or end-of-life disposal services.

**What was not found:**
No evidence found for how much T&L companies spend on device lifecycle management services. Needs primary research.
No evidence found of SOTI partnering with lifecycle management service providers. Needs primary research.
No evidence found for typical device refresh cycles in T&L. Needs primary research.

---

## Gap 7: Reporting and Dashboard Customization

**What the gap is:**
SOTI MobiControl users report that the platform's reporting capabilities are limited. Users want customizable reports and dashboards that can be tailored to what their organization actually needs to see, rather than the default views. This gap is not unique to T&L but is relevant because T&L operations managers need specific views (battery health by shift, device failure rates by route, app performance by depot) that the current reporting does not easily produce.

**Sub-segments affected:**
All sub-segments where SOTI is deployed.

**How customers handle it today:**
Users work with the default reports or export data for manual analysis. Some use SOTI XSight dashboards (Battery, App Usage) for specific views, but customization remains limited.

**What customers are actually saying:**
A Capterra reviewer identified as a License Manager in Warehousing who used MobiControl for 1 to 2 years noted the software manages devices well remotely but wanted a lower price.
Source: [Capterra SOTI Reviews](https://www.capterra.com/p/133554/Soti-MobiControl/reviews/)

PeerSpot reviews note that report customization needs improvement and currently does not provide adequate filtering or customizable options.
Source: [PeerSpot SOTI MobiControl Reviews](https://www.peerspot.com/products/soti-mobicontrol-reviews)

G2 reviewers note the reporting section could be more detailed and that updates take too much time.
Source: [G2 SOTI MobiControl Reviews](https://www.g2.com/products/soti-mobicontrol/reviews)

**Regulatory or compliance driver:**
No regulatory driver identified.

**Budget signal:**
No budget signal found. This gap is about feature completeness within the existing product, not about a separate spending category. Needs primary research to understand if customers are exporting data to third-party BI tools and paying for that separately.

**Which SOTI product is closest to addressing this gap:**
SOTI XSight provides analytics dashboards. SOTI MobiControl provides reporting. Both are cited in reviews as needing more customization options.

**What was not found:**
No evidence found for how many T&L customers supplement SOTI reporting with external BI tools. Needs primary research.
No evidence found for competitor MDM reporting capabilities that are specifically better for T&L use cases. Needs primary research.

---

## Verbatim MobiControl Customer Feedback (T&L Reviewers)

**IT Specialist Section Head, Logistics and Supply Chain (used 2+ years), Capterra:**
Noted that SOTI MobiControl helps with asset management, easy report extraction, remote access to enrolled devices, application management, and device location.
Source: [Capterra SOTI Reviews](https://www.capterra.com/p/133554/Soti-MobiControl/reviews/)

**License Manager, Warehousing (used 1 to 2 years), Capterra:**
Noted the software remotely manages the devices well but they would be happy to buy it for a lower price.
Source: [Capterra SOTI Reviews](https://www.capterra.com/p/133554/Soti-MobiControl/reviews/)

**iDC Logistics (3PL), SOTI Case Study:**
"Without SOTI, iDC would not be where it is today. The capabilities of SOTI MobiControl XS allow our team to address issues quicker and more efficiently."
Source: [SOTI iDC Logistics Case Study](https://soti.net/resources/customer-stories-and-use-cases/idc-logistics/?csc=)

**PeerSpot reviewer (industry not specified):**
Reported that MobiControl had an agent version not compatible with Android Oreo that bricked 100 phones, and SOTI's response was "nothing we can do, sorry."
Source: [PeerSpot SOTI Reviews](https://www.peerspot.com/products/soti-mobicontrol-reviews)

**PeerSpot reviewers (mixed industries):**
Support shows mixed feedback. Some find customer service good with quick responses. Others experience inconsistency in technical assistance, with some level-one agents lacking deep product knowledge.
Source: [PeerSpot SOTI Reviews](https://www.peerspot.com/products/soti-mobicontrol-reviews)

No additional T&L-specific reviews found on G2 or Gartner Peer Insights beyond the above. G2 reviews are behind a login wall. Gartner Peer Insights for SOTI MobiControl exists but individual reviews were not accessible in this research.
Source: [Gartner Peer Insights SOTI MobiControl](https://www.gartner.com/reviews/market/unified-endpoint-management-tools/vendor/soti/product/soti-mobicontrol)

---
