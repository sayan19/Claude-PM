# 03 — Competitive Landscape: FSMA 204 KDE / CTE Capture (C7)

**Candidate:** Device-side capture of FDA-mandated Key Data Elements at Critical Tracking Events for Food Traceability List items, across cold-storage 3PLs and reefer carriers.
**Geography:** US + Canada (FDA jurisdiction is US; Canadian operators serving US destinations are in scope).
**Method:** Category-deep across enterprise traceability, cold-chain SaaS, WMS/TMS modules, IoT sensor platforms, and status quo.

---

## Regulatory anchor

- **FSMA 204 final rule** (21 CFR Part 1, Subpart S) requires KDE capture at CTEs (Receive, Ship, Transform, Initial Packing, First Land-Based Receiver, Cooling) for foods on the FDA Food Traceability List. Source: [FDA FSMA 204 page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods).
- **Compliance date Jan 20, 2026** for record-keeping; FDA enforcement extended to **July 20, 2028** by Federal Register notice Aug 7, 2025. Source: [Federal Register 2025-14967](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension).
- Records must be producible to FDA within 24 hours in sortable electronic format.
- Covered entities: anyone who manufactures, processes, packs, or holds an FTL item — meaningfully includes cold-storage 3PLs, reefer carriers in the chain, distribution centers, and retailers.

---

## Category map

### 1. Enterprise food traceability platforms (the leaders)

| Vendor | Position | Notes |
|---|---|---|
| **Trustwell (FoodLogiQ + Genesis Foods)** | End-to-end traceability + recall + supplier compliance. 250M+ CTEs captured to date. [Trustwell](https://www.trustwell.com/), [Trustwell traceability](https://www.trustwell.com/products/foodlogiq/traceability/), [Trustwell FSMA 204 guide](https://www.trustwell.com/resources/guide-to-fsma-204-compliance/) | Tier-1 food brands, retailers, 3PLs |
| **iTradeNetwork** | Supply chain traceability + supplier collaboration | Foodservice and retail |
| **ReposiTrak** | Compliance + traceability for retailers/grocery | Retail-anchored |
| **TraceGains** | Supplier compliance + traceability + ingredients | Manufacturer focus |

**Take:** Enterprise platforms own the upper market. Implementation costs $100K–$500K+; built for tier-1 brands, not 3PLs.

### 2. Mid-market food traceability + ERP

| Vendor | Position |
|---|---|
| **Wherefour** | Cloud ERP + traceability for mid-market food makers; bakes lot tracking into inventory moves. [Wherefour](https://wherefour.com/best-food-traceability-software-for-fsma-compliance/) |
| **Icicle** | Food safety + traceability mid-market |
| **FoodReady** | SMB food safety + FSMA compliance |
| **Trace One** | EU origin, NA presence |

**Take:** Mid-market plays are food-manufacturer-oriented; less coverage of cold-storage 3PLs and carriers.

### 3. Cold-storage 3PL / WMS-bundled traceability

| Vendor | Position |
|---|---|
| **Kӧrber Supply Chain (HighJump)** | Cold-storage WMS with lot tracking |
| **Manhattan Active Warehouse** | Lot/serial; FSMA 204 KDE capture in roadmap |
| **Datex** | 3PL-focused WMS with lot tracking |
| **Tecsys** | Distribution WMS with FSMA-capable workflows |
| **Made4Net** | Mid-market WMS |
| **Extensiv (3PL Central)** | Cloud WMS for 3PLs |

**Take:** WMS layer captures lot+location at receive/ship — but the FSMA 204 KDE schema (specifically Traceability Lot Code, location identifier, dates, quantities, supplier reference) requires either WMS upgrade or wraparound capture.

### 4. Carrier-side / TMS

- Most TMS (McLeod, MercuryGate, Trimble) do NOT natively capture FSMA 204 KDEs at the carrier level. Carriers typically pass through a BOL but don't emit KDE-formatted records.
- This is an unsolved gap for reefer carriers — they're a CTE actor under FSMA 204 but lack tooling.

### 5. IoT / sensor-anchored traceability

| Vendor | Position |
|---|---|
| **Wiliot** | Battery-free Bluetooth sensors at item level — emerging |
| **TempTale (Sensitech)** | Temperature loggers, FSMA-aligned |
| **Tive** | Real-time sensors with KDE-adjacent metadata |
| **Carrier Lynx, Thermo King ConnectedSuite** | Reefer telematics |

**Take:** Sensors generate the temperature record but not the FSMA 204 KDE record itself. Pairing required.

### 6. Status quo: spreadsheets

Widespread. The Aug 2025 FDA enforcement extension to 2028 has reduced panic-buying but not solved the problem. Many cold-storage 3PLs and reefer carriers are running spreadsheet workarounds.

---

## Where the category leaves customers underserved

1. **Cold-storage 3PLs that aren't on Manhattan / Blue Yonder.** A regional cold-storage 3PL on Datex or Made4Net needs a wrap-around KDE capture without replacing their WMS. Trustwell and similar plug in but at enterprise pricing.
2. **Reefer carriers.** The carrier is a CTE actor (Ship event) but TMS doesn't emit KDE records. No clean carrier-side FSMA 204 product exists.
3. **Receiver-side handoff.** When a reefer arrives at a retailer DC, the receiver captures lot info into their WMS — but the carrier doesn't get a confirmation record back. Reconciliation is messy.
4. **Mid-market 3PLs lacking compliance budget.** Trustwell starts at enterprise pricing; small 3PLs need a $10K–$30K/year solution.
5. **Driver-side reefer pre-trip + arrival temperature attestation.** Paper at most carriers; FSMA 204 doesn't *require* this but FSMA Sanitary Transportation Rule cross-references it.

---

## Status quo cost / friction

- Trustwell / FoodLogiQ enterprise: $100K–$500K implementation + $50K–$200K/year subscription
- Wherefour mid-market: $30K–$100K/year typical
- Spreadsheet: ~$0 direct, FDA exposure cost is asymmetric (recall events, regulatory action)

---

## Switching costs

- WMS replacement (if going for embedded): very high
- Wrap-around KDE capture: low to moderate
- Carrier-side: greenfield (low switching cost from "nothing")
- Process / training: meaningful

---

## Sources

- [FDA FSMA 204 page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods)
- [Federal Register Aug 7 2025 enforcement extension](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension)
- [Trustwell FSMA 204 guide](https://www.trustwell.com/resources/guide-to-fsma-204-compliance/)
- [Wherefour FSMA traceability](https://wherefour.com/best-food-traceability-software-for-fsma-compliance/)
- [Food Logistics on FSMA 204 cold chain](https://www.foodlogistics.com/safety-security/food-safety/article/22926779/food-drug-administration-fda-fsma-204-compliance-to-fundamentally-change-how-the-cold-chain-works)
- [Digit Software top 7 traceability vendors 2026](https://www.digit-software.com/blog/best-food-traceability-software)
