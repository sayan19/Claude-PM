# T&L Competitive Coverage Map

## Coverage Matrix

| Gap | 42Gears | Intune | Workspace ONE / Omnissa | Ivanti | Samsara | Geotab | Status Quo | Source Row |
|---|---|---|---|---|---|---|---|---|
| Digital DVIR | None | None | None | None | Full | Full | Paper forms | See Gap 1 details |
| FSMA 204 Cold Chain | None | None | None | None | Full | Full | Paper logs, spreadsheets | See Gap 2 details |
| CSA Safety Scoring | None | None | None | None | Full | Full | Manual tracking, CSA reports | See Gap 3 details |
| Warehouse Shift Productivity | Partial | Partial | Partial | Partial | None | None | Spreadsheets, standalone LMS | See Gap 4 details |
| MDM to WMS/TMS/ERP Integration | Unknown | Partial | Partial | Unknown | None | None | Manual data transfer | See Gap 5 details |
| Device Lifecycle Management | Partial | Partial | Partial | Partial | None | None | Manual staging, ad hoc refresh | See Gap 6 details |
| Reporting and Dashboard Customization | Partial | Partial | Partial | Partial | N/A | N/A | Exported data, manual analysis | See Gap 7 details |

---

## Gap 1: Digital DVIR and Pre-Trip Inspection Workflows — Detailed Coverage

**42Gears SureMDM**
Coverage level: None
What they do for this gap: 42Gears manages devices on which third-party ELD and DVIR apps run. It does not offer a native DVIR inspection feature within SureMDM. A blog post discusses ELD compliance in the context of managing tablets and rugged handhelds that run ELD apps, but no DVIR workflow product exists.
Source: [42Gears ELD Compliance Blog](https://www.42gears.com/blog/strengthen-your-eld-compliance-with-42gears-mobility-management/)
T&L-specific evidence: Blue Line Transportation uses SureMDM and SureLock for tablet management and lockdown. Victory Transportation Systems is listed as a customer. Neither case study mentions DVIR.
Source: [42Gears T&L Blog](https://www.42gears.com/blog/15-year-recap-of-digital-transformation-successes-with-42gears-mdm-transportation-logistics/)
Customer quote: No T&L-specific customer quotes found for this gap on 42Gears.
Pricing signal: SureMDM plans range from USD 3.99 to USD 7.99 per device per month.
Source: [42Gears Pricing](https://www.42gears.com/pricing/mobile-device-management/)
Switching cost from 42Gears to SOTI for this gap: Not found. Neither vendor offers native DVIR.

**Microsoft Intune**
Coverage level: None
What they do for this gap: Intune manages rugged devices in warehouse and logistics environments, including Zebra and Honeywell handhelds. It supports kiosk mode, OEMConfig, and remote support. It does not offer DVIR inspection workflows.
Source: [Microsoft Tech Community Warehouse Devices](https://techcommunity.microsoft.com/blog/intunecustomersuccess/from-the-frontlines-managing-warehouse-devices-with-microsoft-intune/4428928)
T&L-specific evidence: Microsoft published a blog on managing warehouse devices with Intune, covering vehicle-mounted scanners and rugged handhelds. No DVIR feature mentioned.
Source: [MS AI Insider Intune Warehouse](https://ailonalab.com/2025/07/01/how-microsoft-intune-enhances-warehouse-device-management-with-role-based-android-configurations-and-oemconfig-integration/)
Customer quote: No T&L-specific customer quotes found for this gap on Intune.
Pricing signal: Intune Plan 1 Device license is USD 2.70 per device per month. Plan 2 (specialty devices) is USD 4.00 per user per month add-on.
Source: [Microsoft Intune Pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing)
Switching cost from Intune to SOTI for this gap: Not applicable. Neither offers native DVIR.

**VMware Workspace ONE / Omnissa**
Coverage level: None
What they do for this gap: Workspace ONE UEM manages rugged devices including Zebra and Honeywell hardware. It supports zero-touch enrollment, kiosk mode, and shared device management. No DVIR inspection feature found.
Source: [Omnissa Workspace ONE UEM](https://www.omnissa.com/products/workspace-one-unified-endpoint-management/)
T&L-specific evidence: No transportation or logistics case studies found. No DVIR feature referenced.
Customer quote: No T&L-specific customer quotes found for this gap on Workspace ONE.
Pricing signal: Not publicly available on Omnissa website. Needs primary research.
Switching cost from Workspace ONE to SOTI for this gap: Not found.

**Ivanti UEM**
Coverage level: None
What they do for this gap: Ivanti manages rugged devices across logistics and manufacturing environments with automated workflows and zero-trust security. System4u offers Ivanti-based services for logistics and road transport. No DVIR feature found.
Source: [Ivanti Enterprise Mobility](https://www.ivanti.com/enterprise-mobility)
Source: [System4u Logistics](https://www.system4u.com/industries/logistics-and-road-transport/)
T&L-specific evidence: No DVIR-specific case studies or features found.
Customer quote: No T&L-specific customer quotes found for this gap on Ivanti.
Pricing signal: Ivanti MobileIron Secure UEM Bundle perpetual license is available but pricing is not publicly listed on vendor site.
Source: [HSSL Ivanti Pricing](https://hssl.us/ivanti-mobileiron-secure-uem-bundle-per-device-includes-help-work-perpetual-license-mi-uem-d-pl/)
Switching cost from Ivanti to SOTI for this gap: Not found.

**Samsara (adjacent vendor)**
Coverage level: Full
What they do for this gap: Samsara offers a dedicated DVIR product. Drivers submit DVIRs from the Samsara Driver App. The DVIR dashboard eliminates paperwork and creates a maintenance communication loop. DVIR 2.0 adds AI verification (ensures driver is near the vehicle, validates photos are of actual vehicle components), voice-to-text for inspection notes, and one-click work order creation from defects. Vehicles with unsafe DVIRs can be marked out of service.
Source: [Samsara DVIR Product](https://www.samsara.com/products/apps-and-workflows/dvir)
Source: [Samsara DVIR 2.0 Beta](https://kb.samsara.com/hc/en-us/articles/40227269615629-DVIR-2-0-Beta)
T&L-specific evidence: DVIR is a core feature of Samsara's fleet management platform used by trucking and delivery fleets.
Customer quote: No verbatim T&L customer quote found specifically about Samsara DVIR on G2 or Gartner Peer Insights in this research.
Pricing signal: USD 27 to 33 per vehicle per month (base), USD 40 to 60 with advanced features. Three-year minimum contract.
Source: [Tech.co Samsara Review](https://tech.co/fleet-management/samsara-fleet-management-review)
Switching cost from Samsara to SOTI for this gap: High. Samsara's DVIR is tightly integrated with its ELD, maintenance, and fleet management platform. Switching would require replacing the entire fleet management stack, not just the DVIR component. Three-year contracts with early termination fees equal to remaining balance.
Source: [Tech.co Samsara Review](https://tech.co/fleet-management/samsara-fleet-management-review)

**Geotab (adjacent vendor)**
Coverage level: Full
What they do for this gap: Geotab offers electronic DVIRs through the Geotab Drive app, combining DVIR reporting with ELD compliance, driver ID, and messaging. Supports 100+ HOS rulesets and exemptions for U.S. and Canada. Fleet managers receive real-time defect notifications for faster maintenance scheduling.
Source: [Geotab DVIR](https://www.geotab.com/fleet-management-solutions/dvir/)
T&L-specific evidence: DVIR is integrated with Geotab's compliance and fleet management platform.
Customer quote: No verbatim T&L customer quote found specifically about Geotab DVIR in this research.
Pricing signal: Not publicly available. Needs primary research.
Switching cost from Geotab to SOTI for this gap: High. Same dynamics as Samsara. DVIR is part of a broader telematics and compliance platform.

**Status quo (spreadsheets and manual process)**
Drivers complete paper DVIR forms before and after each trip. Forms are collected at depots, filed physically, and sometimes never reviewed unless there is an audit. "Rubber-stamping" is common, where drivers check every item without performing the actual inspection. Only 7% of motor carriers pass a focused compliance review without a single violation.
Source: [Heavy Vehicle Inspection DVIR Guide](https://heavyvehicleinspection.com/article/dvir-guide-driver-vehicle-inspection-report)

**SOTI's current coverage of this gap (factual only):**
SOTI Snap can be used to build custom digital forms on managed devices, which could include a DVIR template.
Source: [SOTI MobiControl Product Page](https://soti.net/products/soti-mobicontrol/)
No evidence found of any SOTI customer using Snap for DVIR workflows.
SOTI does not offer GPS verification of driver location during inspections, AI-assisted photo validation, automated work order creation from defects, or DVIR-specific compliance reporting. These are features Samsara and Geotab both offer.

---

## Gap 2: FDA FSMA 204 Cold Chain Traceability and Temperature Logging — Detailed Coverage

**42Gears SureMDM**
Coverage level: None
What they do for this gap: No cold chain monitoring, temperature logging, or FSMA 204 compliance features found in SureMDM product documentation or marketing.
T&L-specific evidence: No cold chain case studies found for 42Gears.
Customer quote: No T&L-specific customer quotes found for this gap on 42Gears.
Pricing signal: USD 3.99 to USD 7.99 per device per month (general MDM).
Source: [42Gears Pricing](https://www.42gears.com/pricing/mobile-device-management/)
Switching cost from 42Gears to SOTI for this gap: Not applicable. Neither offers native cold chain compliance.

**Microsoft Intune**
Coverage level: None
What they do for this gap: Intune manages devices but does not capture temperature data, provide cold chain monitoring, or offer FSMA 204 compliance features. No cold chain-related documentation found.
T&L-specific evidence: No cold chain case studies found for Intune.
Customer quote: No T&L-specific customer quotes found for this gap on Intune.
Pricing signal: USD 2.70 per device per month (device license).
Source: [Microsoft Intune Pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing)
Switching cost from Intune to SOTI for this gap: Not applicable.

**VMware Workspace ONE / Omnissa**
Coverage level: None
What they do for this gap: No cold chain monitoring or FSMA 204 features found in Workspace ONE documentation.
T&L-specific evidence: No cold chain case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Workspace ONE to SOTI for this gap: Not applicable.

**Ivanti UEM**
Coverage level: None
What they do for this gap: No cold chain monitoring or FSMA 204 features found in Ivanti product documentation.
T&L-specific evidence: No cold chain case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Ivanti to SOTI for this gap: Not applicable.

**Samsara (adjacent vendor)**
Coverage level: Full
What they do for this gap: Samsara offers a comprehensive cold chain monitoring solution. Environmental Monitors provide continuous temperature reporting. Integration with Thermo King and Carrier refrigeration units allows remote control of reefers (on/off, run mode, set-point adjustment, alarm clearing) from the Samsara dashboard. Reefer Temperature Reports are downloadable as PDF or CSV for FSMA compliance. Wireless environmental and door monitors provide additional temperature and humidity tracking for multi-zone or sensitive loads. Real-time temperature alerts via email or text when air temperature deviates from target.
Source: [Samsara Cold Chain Monitoring](https://www.samsara.com/guides/what-is-cold-chain-monitoring)
Source: [Samsara Reefer Temperature Reports](https://www.samsara.com/blog/introducing-reefer-temperature-reports)
Source: [Samsara Thermo King Integration](https://www.samsara.com/blog/samsara-for-thermo-king-refrigeration-units)
T&L-specific evidence: Samsara ranked first for innovation in ABI Research's cold chain monitoring competitive ranking. Acme Smoked Fish is a published case study.
Source: [ABI Research Cold Chain Ranking](https://www.abiresearch.com/press/powerfleet-samsara-and-motive-lead-abi-researchs-cold-chain-monitoring-solutions-competitive-ranking)
Source: [Samsara Acme Smoked Fish Case Study](https://s3-us-west-2.amazonaws.com/corpweb-static/pdf/docs/casestudy-acme-smoked-fish.pdf)
Customer quote: No verbatim T&L customer quote found specifically about Samsara cold chain on G2 or Gartner in this research.
Pricing signal: USD 27 to 60 per vehicle per month (platform pricing; cold chain features included in broader subscription).
Source: [Tech.co Samsara Review](https://tech.co/fleet-management/samsara-fleet-management-review)
Switching cost from Samsara to SOTI for this gap: Very high. Samsara's cold chain solution includes proprietary hardware (Environmental Monitors, Asset Gateway), reefer integrations, and compliance reporting. Replacing this with SOTI would require an entirely different sensor and reporting stack.

**Geotab (adjacent vendor)**
Coverage level: Full
What they do for this gap: Geotab offers a dedicated Cold Chain Solution with near-real-time monitoring, proactive alerts, and audit-ready compliance data. Hardware options include direct integration with Thermo King via TracKing (no extra hardware needed) and IOX Cold / IOX Cold Rugged expanders for non-Thermo King units. Interactive historical data viewer combines graphs, grids, and maps for proof of compliance.
Source: [Geotab Cold Chain Management](https://www.geotab.com/fleet-management-solutions/cold-chain-management/)
Source: [Geotab Cold Chain Solution Launch](https://www.geotab.com/au/press-release/cold-chain-management/)
T&L-specific evidence: Geotab published a 2025 Cold Chain Logistics Guide for fleet managers.
Source: [Geotab Cold Chain Logistics Guide](https://www.geotab.com/blog/cold-chain-logistics/)
Customer quote: No verbatim T&L customer quote found specifically about Geotab cold chain in this research.
Pricing signal: Not publicly available.
Switching cost from Geotab to SOTI for this gap: Very high. Same dynamics as Samsara: proprietary hardware, reefer integrations, compliance documentation.

**Status quo (spreadsheets and manual process)**
Some cold chain operations still use paper temperature logs and manual recording. Workers check temperatures at set intervals and write them on forms. These cannot provide the precision, speed, or accuracy that FSMA 204 demands (data retrievable within 24 hours, retained for 24 months).
Source: [SFL Companies FSMA 204](https://www.sflcompanies.com/post/how-the-fdas-fsma-204-rule-is-changing-cold-chain-logistics)

**SOTI's current coverage of this gap (factual only):**
SOTI Connect manages IoT endpoints including sensors.
Source: [SOTI MobiControl Product Page](https://soti.net/products/soti-mobicontrol/)
STEF (European cold chain logistics provider) is a documented SOTI customer, though the case study does not detail temperature compliance features.
Source: [SOTI STEF Case Study](https://www.soti.net/media/1620/case-study-stef-en.pdf)
SOTI does not offer continuous temperature logging, reefer integration, FSMA 204 compliance reports, or temperature alert workflows. Samsara and Geotab both offer all of these.

---

## Gap 3: CSA Safety Scoring and Driver Behavior Compliance — Detailed Coverage

**42Gears SureMDM**
Coverage level: None
What they do for this gap: No driver safety scoring, CSA compliance, or driver behavior monitoring features found in SureMDM.
T&L-specific evidence: No driver safety case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 3.99 to USD 7.99 per device per month.
Source: [42Gears Pricing](https://www.42gears.com/pricing/mobile-device-management/)
Switching cost from 42Gears to SOTI for this gap: Not applicable. Neither offers driver safety scoring.

**Microsoft Intune**
Coverage level: None
What they do for this gap: Intune manages devices but does not capture driver behavior data, safety scores, or CSA compliance metrics.
T&L-specific evidence: No driver safety features found in Intune documentation.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 2.70 per device per month.
Source: [Microsoft Intune Pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing)
Switching cost from Intune to SOTI for this gap: Not applicable.

**VMware Workspace ONE / Omnissa**
Coverage level: None
What they do for this gap: No driver safety or CSA features found.
Customer quote: No T&L-specific customer quotes found for this gap.
Switching cost: Not applicable.

**Ivanti UEM**
Coverage level: None
What they do for this gap: No driver safety or CSA features found.
Customer quote: No T&L-specific customer quotes found for this gap.
Switching cost: Not applicable.

**Samsara (adjacent vendor)**
Coverage level: Full
What they do for this gap: Samsara provides AI dash cams that detect unsafe driving behaviors (speeding, harsh braking, distracted driving, tailgating). Compliance and ELD features let users view HOS, duty status records, sensor data, and DVIRs. In-built WiFi hotspots provide connectivity in rural areas. Samsara ranked #1 on G2 for Fleet Management across all of 2025 with a 99 average customer satisfaction score.
Source: [Samsara G2 Rankings](https://www.samsara.com/company/news/press-releases/Samsara-Ranks-No-1-in-Fleet-Management-on-G2-for-2025)
Source: [Samsara ELD Features](https://www.empwrtrucking.com/freight-technology/samsara-eld-a-comprehensive-guide-to-features-benefits-and-pricing/)
T&L-specific evidence: 88% of fleets deploy video for safety improvement. Insurers grant double-digit premium discounts for video-verified safety data.
Source: [EzDashcam Fleet Telematics](https://ezdashcam.com/how-dashcams-elevate-fleet-telematics-in-2025/)
Customer quote: No verbatim T&L customer quote found specifically about Samsara safety scoring in this research.
Pricing signal: USD 27 to 60 per vehicle per month.
Source: [Tech.co Samsara Review](https://tech.co/fleet-management/samsara-fleet-management-review)
Switching cost from Samsara to SOTI for this gap: Very high. Requires replacing proprietary dash cam hardware and an entire AI-driven safety analytics platform.

**Geotab (adjacent vendor)**
Coverage level: Full
What they do for this gap: Geotab Vitality combines behavioral science with telematics data to change driver behavior. It identifies speeding, harsh braking, harsh acceleration, harsh cornering, and scores drivers against peer cohorts grouped by vehicle type, driving style (long-haul, middle-mile, local delivery), and contextual area risk. Geotab compliance software addresses FMCSA, DOT, and Canadian MTO rules.
Source: [Geotab Fleet Compliance](https://www.geotab.com/fleet-management-solutions/compliance/)
Source: [CCJ Geotab Vitality](https://www.ccjdigital.com/technology/driver-coaching-and-scorecarding/article/15820573/geotab-vitality-expands-beyond-safety-to-fuel-savings-compliance)
T&L-specific evidence: Richards Building Supply saw a 40% improvement in safe driving in the first 60 days of using Geotab Vitality.
Source: [CCJ Geotab Vitality](https://www.ccjdigital.com/technology/driver-coaching-and-scorecarding/article/15820573/geotab-vitality-expands-beyond-safety-to-fuel-savings-compliance)
Customer quote: No verbatim T&L customer quote found specifically on G2 or Gartner for Geotab safety scoring in this research.
Pricing signal: Not publicly available.
Switching cost from Geotab to SOTI for this gap: Very high. Same dynamics as Samsara.

**Status quo (spreadsheets and manual process)**
Fleets without telematics rely on manual tracking of FMCSA compliance reviews, paper-based incident reports, and reactive responses to CSA score changes. Over 100,000 violations were reported in FMCSA enforcement data in 2025.
Source: [FreightWaves FMCSA Compliance](https://www.freightwaves.com/news/what-fleets-need-to-know-about-fmcsa-compliance-reviews-in-2025)

**SOTI's current coverage of this gap (factual only):**
SOTI XSight provides OBDII vehicle telemetry data. No evidence found that any customer uses this for CSA compliance or driver safety scoring.
SOTI MobiControl manages devices running ELD and fleet management apps but does not replace those apps.
SOTI does not offer dash cams, AI-driven behavior detection, driver safety scores, or CSA compliance reporting.

---

## Gap 4: Warehouse Shift Productivity and Device Utilization Analytics — Detailed Coverage

**42Gears SureMDM**
Coverage level: Partial
What they do for this gap: SureMDM provides device-level analytics including app usage, data consumption, and location tracking. It does not provide worker-level productivity metrics, shift-level performance dashboards, or picks-per-hour tracking.
Source: [42Gears SureMDM Product Page](https://www.42gears.com/products/mobile-device-management/)
T&L-specific evidence: Delhivery uses SureMDM to monitor device health in real time across 20,000+ devices in warehouses. Focus is on device management and security, not worker productivity analytics.
Source: [42Gears Delhivery Case Study](https://www.42gears.com/case-studies/delhivery-accelerates-e-commerce-logistics-workflow-with-42gears-uem/)
Customer quote: No T&L-specific customer quotes found about productivity analytics on 42Gears.
Pricing signal: USD 3.99 to USD 7.99 per device per month.
Source: [42Gears Pricing](https://www.42gears.com/pricing/mobile-device-management/)
Switching cost from 42Gears to SOTI for this gap: Low for the MDM layer. Neither vendor offers shift-level productivity analytics that would replace a standalone LMS.

**Microsoft Intune**
Coverage level: Partial
What they do for this gap: Intune provides Endpoint Analytics including device performance scoring and application reliability metrics. It supports shared device management for multi-user warehouse scenarios. It does not provide worker-level productivity tracking or shift-based analytics.
Source: [Microsoft Tech Community Warehouse Devices](https://techcommunity.microsoft.com/blog/intunecustomersuccess/from-the-frontlines-managing-warehouse-devices-with-microsoft-intune/4428928)
T&L-specific evidence: Microsoft published guidance on managing warehouse devices with role-based configurations. Focus is device management, not operations analytics.
Customer quote: No T&L-specific customer quotes found about productivity analytics on Intune.
Pricing signal: USD 2.70 per device per month (device license). Endpoint Analytics included in Intune Suite at USD 10 per user per month add-on.
Source: [Microsoft Intune Pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing)
Switching cost from Intune to SOTI for this gap: Low to moderate. Organizations in the Microsoft ecosystem get Intune bundled with M365 E3/E5, making the cost comparison favorable for Intune.

**VMware Workspace ONE / Omnissa**
Coverage level: Partial
What they do for this gap: Workspace ONE provides device analytics and shared device support including Windows MultiUser for shift-based operations. It supports multiple users logging into a single device with tailored experiences. Does not provide warehouse operational KPIs.
Source: [Tech Orchard Workspace ONE 2025](https://techorchard.com/workspace-one-uem-2025-a-complete-guide-to-this-years-most-powerful-new-features/)
T&L-specific evidence: No warehouse productivity case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Workspace ONE to SOTI for this gap: Moderate. Migration would involve re-enrolling all devices and reconfiguring policies.

**Ivanti UEM**
Coverage level: Partial
What they do for this gap: Ivanti provides self-healing workflows that detect failing apps and trigger recovery automatically. Supports risk-based access control. Does not provide shift-level productivity analytics.
Source: [Ivanti Enterprise Mobility](https://www.ivanti.com/enterprise-mobility)
T&L-specific evidence: No warehouse productivity case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Ivanti to SOTI for this gap: Moderate.

**Samsara and Geotab**
Coverage level: None
These are fleet and vehicle telematics platforms. They do not manage warehouse devices or provide warehouse shift productivity analytics.

**Status quo (spreadsheets and manual process)**
Warehouse supervisors track productivity manually using spreadsheets, whiteboard tallies, or basic WMS reports. Dedicated LMS tools (JASCI, OneTrack, Easy Metrics ProTrack) exist but sit outside the MDM stack. No evidence found of any MDM vendor integrating with these LMS platforms.
Source: [JASCI Labor Management](https://www.jascicloud.com/products/labor-management)
Source: [OneTrack Productivity](https://www.onetrack.ai/solutions/productivity)

**SOTI's current coverage of this gap (factual only):**
SOTI XSight provides device-level analytics: battery health, app usage, signal strength. The iDC Logistics case study confirms XSight App Usage Dashboards and Battery Dashboards in use at a 3PL.
Source: [SOTI iDC Logistics Case Study](https://soti.net/resources/customer-stories-and-use-cases/idc-logistics/?csc=)
SOTI does not correlate device data with worker identity, shift schedules, or operational KPIs like picks per hour. XSight is closer to this gap than any competitor MDM, but it does not bridge the gap to operational productivity analytics.

---

### Gap 5: MDM to WMS/TMS/ERP Integration

**42Gears SureMDM**
Coverage level: Unknown
What they do for this gap: 42Gears documents API access and integration capabilities but no specific WMS, TMS, or ERP integration connectors were found. Their platform supports REST APIs for device management automation.
Source: [42Gears SureMDM Features](https://www.42gears.com/products/suremdm/)
T&L-specific evidence: No case studies or documentation showing WMS/TMS/ERP integration in T&L environments.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 3.99 to USD 7.99 per device per month depending on tier.
Source: [42Gears Pricing](https://www.42gears.com/pricing/)
Switching cost from 42Gears to SOTI for this gap: Low to moderate. Would require rebuilding any custom API integrations.

**Microsoft Intune**
Coverage level: Partial
What they do for this gap: Intune integrates natively with the Microsoft ecosystem (Azure AD, Dynamics 365, Power Platform). Organizations using Dynamics 365 Supply Chain Management can leverage shared identity and compliance policies. Power Automate enables workflow connections between Intune device events and business applications.
Source: [Microsoft Intune Integration](https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune)
T&L-specific evidence: Microsoft published warehouse device management guidance that includes line-of-business app deployment, but no specific WMS/TMS connector documentation found.
Source: [Microsoft Tech Community Warehouse Devices](https://techcommunity.microsoft.com/blog/intunecustomersuccess/from-the-frontlines-managing-warehouse-devices-with-microsoft-intune/4428928)
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 2.70 per device per month (device license). Microsoft ecosystem lock-in makes integration "free" for organizations already on Dynamics 365.
Source: [Microsoft Intune Pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing)
Switching cost from Intune to SOTI for this gap: High for organizations deeply embedded in the Microsoft ecosystem. Power Automate workflows and Dynamics 365 connections would need to be rebuilt.

**VMware Workspace ONE / Omnissa**
Coverage level: Partial
What they do for this gap: Workspace ONE offers an Integration Broker and REST APIs for connecting device management events to enterprise systems. Supports ServiceNow and other ITSM integrations. No WMS/TMS-specific connectors found.
Source: [Tech Orchard Workspace ONE 2025](https://techorchard.com/workspace-one-uem-2025-a-complete-guide-to-this-years-most-powerful-new-features/)
T&L-specific evidence: No case studies found showing WMS/TMS/ERP integration in logistics environments.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Workspace ONE to SOTI for this gap: Moderate. API integrations would need to be rebuilt.

**Ivanti UEM**
Coverage level: Partial
What they do for this gap: Ivanti offers integration with its broader ITSM platform (Neurons) and supports connectors to ServiceNow and other IT systems. Self-healing automation can trigger workflows based on device events. No WMS/TMS-specific connectors found.
Source: [Ivanti Enterprise Mobility](https://www.ivanti.com/enterprise-mobility)
T&L-specific evidence: No logistics-specific integration case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Ivanti to SOTI for this gap: Moderate.

**Samsara and Geotab**
Coverage level: None
These platforms integrate with fleet and vehicle systems (ELD, GPS, OBDII) but do not manage mobile devices or integrate MDM with WMS/TMS/ERP systems. Samsara offers an open API for fleet data but this is vehicle telematics, not device management integration.
Source: [Samsara Open API](https://www.samsara.com/platform/open-api)

**Status quo (custom development and middleware)**
Most T&L organizations connect MDM to business systems through custom scripts, middleware, or manual processes. IT teams build one-off integrations between their MDM and WMS/TMS systems. This is brittle and expensive to maintain. No evidence found of any MDM vendor offering pre-built connectors for major WMS platforms (Manhattan Associates, Blue Yonder, SAP EWM) or TMS platforms (Oracle TMS, MercuryGate).

**SOTI's current coverage of this gap (factual only):**
SOTI MobiControl provides REST APIs and supports integration through SOTI Connect for IoT device data. The iDC Logistics case study shows MobiControl managing devices that run WMS applications, but the integration is at the app deployment level, not a bidirectional data integration between MobiControl and the WMS.
Source: [SOTI iDC Logistics Case Study](https://soti.net/resources/customer-stories-and-use-cases/idc-logistics/?csc=)
SOTI Connect supports data from IoT endpoints and OBDII devices, which could serve as a bridge to fleet management systems. No pre-built WMS/TMS/ERP connectors were found in SOTI's public documentation.
Source: [SOTI Connect](https://soti.net/products/soti-connect/)

---

### Gap 6: Device Lifecycle Management

**42Gears SureMDM**
Coverage level: Partial
What they do for this gap: 42Gears provides device enrollment, configuration, and remote wipe capabilities. Supports device staging and bulk enrollment. Does not offer device lifecycle cost tracking, refresh cycle planning, or ROI analytics.
Source: [42Gears SureMDM Features](https://www.42gears.com/products/suremdm/)
T&L-specific evidence: 42Gears documents logistics use cases but lifecycle management features are generic, not T&L-specific.
Source: [42Gears Logistics](https://www.42gears.com/solutions/by-industry/logistics/)
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 3.99 to USD 7.99 per device per month depending on tier.
Source: [42Gears Pricing](https://www.42gears.com/pricing/)
Switching cost from 42Gears to SOTI for this gap: Low to moderate.

**Microsoft Intune**
Coverage level: Partial
What they do for this gap: Intune tracks device compliance, OS versions, and hardware inventory. Endpoint Analytics provides device health scores and startup performance data. Autopilot enables zero-touch provisioning. Does not provide T&L-specific lifecycle analytics like ruggedized device replacement cycles or field failure tracking.
Source: [Microsoft Intune Device Management](https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune)
T&L-specific evidence: Microsoft's warehouse device blog covers deployment but not lifecycle cost management.
Source: [Microsoft Tech Community Warehouse Devices](https://techcommunity.microsoft.com/blog/intunecustomersuccess/from-the-frontlines-managing-warehouse-devices-with-microsoft-intune/4428928)
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 2.70 per device per month. Endpoint Analytics included in Intune Suite add-on.
Source: [Microsoft Intune Pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing)
Switching cost from Intune to SOTI for this gap: Low to moderate. Device inventory data would need to be migrated.

**VMware Workspace ONE / Omnissa**
Coverage level: Partial
What they do for this gap: Workspace ONE provides device health dashboards, compliance monitoring, and lifecycle state tracking (enrolled, compliant, retired). Supports automated retirement workflows. Does not offer device cost tracking or refresh cycle optimization.
Source: [Tech Orchard Workspace ONE 2025](https://techorchard.com/workspace-one-uem-2025-a-complete-guide-to-this-years-most-powerful-new-features/)
T&L-specific evidence: No lifecycle management case studies found in T&L.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Workspace ONE to SOTI for this gap: Moderate.

**Ivanti UEM**
Coverage level: Partial
What they do for this gap: Ivanti provides self-healing capabilities and device inventory management. Neurons platform offers predictive analytics for device issues. Does not provide T&L-specific lifecycle cost management.
Source: [Ivanti Enterprise Mobility](https://www.ivanti.com/enterprise-mobility)
T&L-specific evidence: No T&L lifecycle management case studies found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Ivanti to SOTI for this gap: Moderate.

**Samsara and Geotab**
Coverage level: None
These platforms track vehicle lifecycle and maintenance, not mobile device lifecycle. They do not manage handheld or rugged device inventories.

**Status quo (spreadsheets and asset tags)**
T&L operations track device lifecycle through spreadsheets, asset management databases, or general IT asset management (ITAM) tools. Device replacement decisions are reactive (device breaks, then gets replaced) rather than predictive. No evidence found of any MDM vendor offering T&L-specific device lifecycle cost optimization.

**SOTI's current coverage of this gap (factual only):**
SOTI XSight provides battery health analytics, app performance data, and device signal strength monitoring. These inputs could inform device replacement decisions. The SOTI Road Ahead 2024 report found that T&L drivers lose 12 to 16 hours per month to device downtime, establishing the business case for better lifecycle management.
Source: [SOTI Road Ahead 2024](https://soti.net/resources/soti-research/the-road-ahead-2024/)
SOTI MobiControl supports device staging, bulk enrollment, and remote wipe for end-of-life. No evidence found of SOTI offering device lifecycle cost tracking, refresh cycle recommendations, or total cost of ownership analytics.

---

### Gap 7: Reporting and Dashboard Customization

**42Gears SureMDM**
Coverage level: Partial
What they do for this gap: 42Gears provides standard device management reports (compliance, inventory, app usage). Customization options are limited compared to enterprise BI tools. No evidence of T&L-specific report templates.
Source: [42Gears SureMDM Features](https://www.42gears.com/products/suremdm/)
T&L-specific evidence: No T&L-specific reporting capabilities found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 3.99 to USD 7.99 per device per month depending on tier.
Source: [42Gears Pricing](https://www.42gears.com/pricing/)
Switching cost from 42Gears to SOTI for this gap: Low. Report configurations are typically rebuilt during any migration.

**Microsoft Intune**
Coverage level: Partial
What they do for this gap: Intune offers built-in reports for device compliance, app deployment status, and hardware inventory. Advanced reporting through integration with Power BI and Microsoft Graph API. Endpoint Analytics provides performance scoring dashboards. Highly customizable for organizations with Power BI expertise.
Source: [Microsoft Intune Reporting](https://learn.microsoft.com/en-us/mem/intune/fundamentals/reports)
T&L-specific evidence: No T&L-specific report templates found. Customization requires Power BI skills.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: USD 2.70 per device per month. Power BI Pro is an additional USD 10 per user per month.
Source: [Microsoft Power BI Pricing](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing)
Switching cost from Intune to SOTI for this gap: Low for reports, high for Power BI dashboards that took significant investment to build.

**VMware Workspace ONE / Omnissa**
Coverage level: Partial
What they do for this gap: Workspace ONE Intelligence provides custom dashboards and automated reporting. Supports data export and integration with third-party analytics tools. Offers pre-built report templates for common device management metrics.
Source: [Tech Orchard Workspace ONE 2025](https://techorchard.com/workspace-one-uem-2025-a-complete-guide-to-this-years-most-powerful-new-features/)
T&L-specific evidence: No T&L-specific dashboards found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Workspace ONE to SOTI for this gap: Moderate. Custom dashboards would need to be rebuilt.

**Ivanti UEM**
Coverage level: Partial
What they do for this gap: Ivanti Neurons provides analytics dashboards and reporting. Supports custom views and automated report scheduling. No evidence of T&L-specific templates.
Source: [Ivanti Enterprise Mobility](https://www.ivanti.com/enterprise-mobility)
T&L-specific evidence: No T&L-specific reporting found.
Customer quote: No T&L-specific customer quotes found for this gap.
Pricing signal: Not publicly available.
Switching cost from Ivanti to SOTI for this gap: Low to moderate.

**Samsara and Geotab**
Coverage level: N/A
These platforms provide fleet-specific dashboards (safety scores, fuel usage, route analytics) that are not comparable to MDM reporting needs. They do not report on device management metrics.

**Status quo (manual exports and BI tools)**
T&L IT teams export data from their MDM console and build reports manually in Excel or feed data into BI tools (Power BI, Tableau, Looker). This is time-consuming and creates a lag between device events and operational visibility. MobiControl customers on G2 and Gartner Peer Insights have cited reporting limitations as a frustration.
Source: [SOTI MobiControl G2 Reviews](https://www.g2.com/products/soti-mobicontrol/reviews)

**SOTI's current coverage of this gap (factual only):**
SOTI XSight provides pre-built dashboards for battery health, app usage, signal strength, and device performance. MobiControl offers standard compliance and inventory reports. Customer reviews indicate that reporting customization is limited and that creating custom reports requires workarounds.
Source: [SOTI XSight](https://soti.net/products/soti-xsight/)
Source: [SOTI MobiControl G2 Reviews](https://www.g2.com/products/soti-mobicontrol/reviews)
No evidence found of SOTI offering T&L-specific report templates (e.g., DVIR compliance rates, cold chain device uptime, driver device assignment reports).

---

## Patterns Across Gaps

This section documents observable patterns in the competitive data. These are factual observations, not strategic conclusions.

**Pattern 1: MDM competitors cluster at Partial or None for T&L-specific gaps.**
For Gaps 1 (Digital DVIR), 2 (Cold Chain Compliance), and 3 (CSA Safety Scoring), all four direct MDM competitors (42Gears, Intune, Workspace ONE, Ivanti) have None coverage. These gaps are operational and regulatory in nature, falling outside traditional MDM scope. For Gaps 4 through 7, all four MDM competitors have Partial coverage, meaning they offer generic device management features that touch the gap but do not address the T&L-specific workflow.

**Pattern 2: Adjacent competitors dominate the operational gaps but ignore device management.**
Samsara and Geotab have Full coverage for Gaps 1, 2, and 3. These platforms were built for fleet operations and include DVIR, temperature monitoring, and safety scoring as core features. However, they do not manage mobile devices, enroll endpoints, push policies, or control app deployment. The operational gap and the device management gap are solved by different vendors today.

**Pattern 3: No vendor bridges MDM and T&L operations in a single platform.**
Across all seven gaps, no competitor offers both device management and T&L operational capabilities in one product. MDM vendors manage devices. Fleet platforms manage vehicles and drivers. The gap between them is filled by custom integrations, middleware, or manual processes.

**Pattern 4: Pricing signals show two distinct tiers.**
MDM solutions price at USD 2.70 to USD 7.99 per device per month. Fleet telematics platforms (Samsara, Geotab) price at USD 27 to USD 60 per vehicle per month, roughly 5x to 10x higher. This pricing gap suggests that T&L operational capabilities command significantly higher willingness to pay than pure device management.

**Pattern 5: T&L-specific customer evidence is thin across all MDM vendors.**
No MDM competitor (including SOTI) has published extensive T&L-specific case studies, customer quotes, or vertical-specific feature documentation for any of the seven gaps. The T&L vertical appears underserved by the MDM category as a whole.

**Pattern 6: SOTI XSight is closer to the operational gaps than any competitor MDM.**
XSight's device analytics (battery, app, signal, OBDII) provide data points that are adjacent to several gaps (warehouse productivity, device lifecycle, reporting). No competitor MDM offers equivalent device-level operational analytics. This does not mean XSight covers these gaps today; it means the data foundation exists.

---

## Evidence Gaps in This File

The following information was searched for but not found:

1. 42Gears T&L-specific case studies or customer testimonials: Not found on their website or review platforms.
2. VMware Workspace ONE / Omnissa T&L-specific case studies: Not found.
3. Ivanti T&L-specific case studies: Not found.
4. Detailed pricing for Workspace ONE and Ivanti: Not publicly available.
5. Pre-built WMS/TMS/ERP connectors for any MDM vendor: Not found for any vendor.
6. Samsara or Geotab MDM capabilities: Confirmed they do not offer MDM.
7. Customer verbatim quotes about switching from competitors to SOTI for T&L-specific needs: Not found.
