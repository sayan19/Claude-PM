# 03 — Competitive Landscape: Yard Management for Mid-Market 3PLs (C2)

**Candidate:** YMS for mid-market 3PLs and private fleets (3–20 DC operator scale, 50–500 trailer footprint per DC).
**Geography:** US + Canada.
**Method:** Category-deep, NOT MDM-bounded. Covers enterprise YMS, mid-market YMS, dock-scheduling adjacents, visibility platforms with yard modules, and status quo.

---

## Category map

### 1. Enterprise YMS (large 3PLs, retailers, manufacturers)

| Vendor | Position | Notes |
|---|---|---|
| **Kaleris (formerly PINC)** | Born from PINC YMS + terminal-software brands; "Digital Yard" platform; RFID + computer vision YardIQ. Released enhanced YMS March 2025. [Kaleris yard management](https://kaleris.com/solutions/yard-management/), [DataDocks competitive view](https://datadocks.com/posts/best-yard-management-options) | Asset-intensive supply chains: ports, chemicals, heavy manufacturing. Premium pricing, deep integration. |
| **Blue Yonder YMS** | Module of broader supply chain platform | Tier-1 retailer / 3PL footprint |
| **Manhattan Active Yard Management** | Component of Active Supply Chain | Tightly coupled to Manhattan WMS/TMS install base |
| **C3 Solutions** | Canadian YMS specialist | Mid-to-large 3PL |
| **SAP Extended Warehouse Management YMS** | SAP shops | Enterprise |
| **Oracle Logistics Cloud YMS** | Oracle shops | Enterprise |

**Take:** Enterprise YMS is a deep-integration sale; ACVs $200K–$1M+; multi-month implementations. Not a SOTI-natural buyer.

### 2. Mid-market YMS pure-plays

| Vendor | Position | Pricing signal |
|---|---|---|
| **YardView (Vector-acquired Dec 2024)** | Mid-market focus, fast deployment, trailer tracking. [Vector-YardView via DC Velocity](https://www.dcvelocity.com/technology/warehouse-it/yard-management-yms/vector-acquires-yardview-to-improve-dock-visibility), [YardView 3PL page](https://www.yardview.com/yard-management-software-for-the-3pl-industry) | $30K–$100K/site/year typical |
| **Velostics** | Cloud-native, dock + yard unified, integrates Redwood TMS partnership Apr 2024. [Velostics blog](https://www.velostics.com/blog/yms-trends-to-watch-for-2025) | Subscription + transaction |
| **Terminal Industries** | YMS market entrant 2025. [Terminal Industries 2026 report](https://terminal-industries.com/blog/2026-market-report-leading-yard-management-system-yms-platforms) | Aggressive pricing |
| **Vector** | Yard + dock + driver app + ePOD; consolidation play (acquired YardView) | Multi-product SaaS bundle |
| **Cypress Inland (FreightSnap)** | Asset measurement + yard | Specialized |
| **Datex** | Fully integrated 3PL platform with yard module | Mid-market 3PL |

**Take:** This is the contested middle. Vector's YardView acquisition is consolidation; Velostics is attacking with cloud + dock-first; Kaleris is pushing down-market post-PINC merger.

### 3. Visibility platforms with yard modules

| Vendor | Position |
|---|---|
| **FourKites Dynamic Yard** | Yard layered on top of multi-modal visibility. [FourKites Dynamic Yard](https://www.fourkites.com/platform/yard-management/) |
| **Project44** | Yard-equivalent capability via shipper visibility |
| **Tive** | Sensor-anchored, edge of yard |

**Take:** Visibility-led yard plays are shipper-funded; carrier/3PL adoption is a downstream effect.

### 4. Adjacent dock-scheduling platforms (frequent yard expansion)

| Vendor | Position |
|---|---|
| **Loadsmart Opendock** | Dock scheduling category leader; yard-adjacent |
| **DataDocks** | Dock scheduling, mid-market |
| **PingaLink/Dock411** | Smaller players |

**Take:** Dock scheduling is the sister category; vendors here often expand into yard.

### 5. WMS-bundled yard modules

Manhattan, Blue Yonder, Korber, HighJump (Korber-owned), 3PL Central (Extensiv), CargoWise — most enterprise/mid-market WMS now have a yard module bundled. Adoption depth varies.

### 6. Status quo — whiteboard + radio + spreadsheet

The most common deployment at <5-DC mid-market 3PLs and most regional carriers. Loss: ~5–15% trailer location time, detention exposure, hostler inefficiency. No vendor; estimated to cover the majority of NA mid-market sites.

---

## Where the category leaves customers underserved

1. **Mid-market 3PLs with 3–10 DCs** are too big for whiteboard but balk at $300K Kaleris implementations. YardView/Velostics/Vector address this — but rugged-device-driver/hostler workflow execution is variable across the platforms.
2. **Hostler tablet UX.** Kaleris has its own hostler app; mid-market vendors often use a generic browser UI that's painful on a Zebra TC73 or VC8300.
3. **Driver self-check-in at the gate** (kiosk or driver-phone) is uneven; some YMS have it as a premium add-on.
4. **Yard-to-dock-to-route handoff** — covered separately in the C6c artifact, but every mid-market YMS leaves this seam partial.
5. **Multi-tenant 3PL operations** (multiple shippers' inventory in one yard) are a gap for many YMS that assume single-tenant 3PLs.

---

## Status quo cost / friction

- Enterprise YMS: $200K–$1M+ implementation, $50K–$200K/year subscription
- Mid-market YMS: $30K–$100K/site/year all-in
- Dock + yard bundles: $20K–$60K/site/year
- Whiteboard + radio: ~$0 direct, hidden cost in detention, mis-loads, hostler hours

---

## Switching costs

- Hardware (RFID gates, cameras, RTLS) at the high end: very high
- Integration with WMS/TMS: high
- Hostler/gate-guard retraining: moderate
- For sites currently on whiteboard, no switching cost (just adoption cost)

---

## Sources

- [Kaleris yard management](https://kaleris.com/solutions/yard-management/)
- [Velostics 2025 YMS trends](https://www.velostics.com/blog/yms-trends-to-watch-for-2025)
- [DC Velocity Vector-YardView acquisition](https://www.dcvelocity.com/technology/warehouse-it/yard-management-yms/vector-acquires-yardview-to-improve-dock-visibility)
- [YardView 3PL focus](https://www.yardview.com/yard-management-software-for-the-3pl-industry)
- [DataDocks YMS comparison](https://datadocks.com/posts/best-yard-management-options)
- [Terminal Industries 2026 YMS market report](https://terminal-industries.com/blog/2026-market-report-leading-yard-management-system-yms-platforms)
- [FourKites Dynamic Yard](https://www.fourkites.com/platform/yard-management/)
- [Grand View dock+yard market $4.32B 2025](https://www.grandviewresearch.com/industry-analysis/dock-yard-management-systems-market-report)
