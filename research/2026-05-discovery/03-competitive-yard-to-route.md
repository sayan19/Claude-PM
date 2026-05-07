# 03 — Competitive Landscape: Yard-to-Route Handoff (C6c)

**Candidate:** The seam between yard exit (load departed dock 7 at 14:32) and route execution (driver picks up load at 15:10) — making sure the route plan, ETA, and driver workflow stay coherent across the handoff.
**Geography:** US + Canada.
**Method:** Category-deep across YMS, TMS, last-mile platforms, visibility platforms, and status quo. This is a *seam* candidate — no incumbent owns it cleanly; the competitive frame is "who covers part of it."

---

## Category map (covers-part-of-the-seam)

### 1. YMS owns the yard exit side

| Vendor | Owns | Doesn't own |
|---|---|---|
| Kaleris (PINC), Blue Yonder, Manhattan, YardView, Velostics | Trailer at dock; gate-out timestamp | Once the truck leaves the gate, YMS hands off and visibility ends |

### 2. Visibility platforms own the in-transit side

| Vendor | Owns | Doesn't own |
|---|---|---|
| FourKites Dynamic Yard + visibility | In-yard dwell + over-the-road tracking — closest end-to-end | The driver-app workflow at handoff (driver still uses TMS or carrier-built app) [FourKites Dynamic Yard](https://www.fourkites.com/platform/yard-management/) |
| Project44 | Multi-modal visibility | Yard-side workflow |
| Tive | Sensor-anchored visibility | Yard workflow |

### 3. TMS owns the route plan

| Vendor | Owns | Doesn't own |
|---|---|---|
| McLeod, Trimble, MercuryGate, Descartes | Dispatch plan, route optimization | Real-time replan when yard delays propagate |
| Loadsmart, Convoy/DAT, Uber Freight | Tendering | Yard-side coordination |

### 4. Last-mile platforms own the driver app

| Vendor | Owns | Doesn't own |
|---|---|---|
| OptimoRoute, Routific, Onfleet, Bringg, Locus | Driver navigation, POD, multi-stop | Origin-yard coordination |

### 5. Carriers' internal-built solutions

Many large carriers (J.B. Hunt, Werner, Schneider) have built internal driver apps that ingest from their own dispatch + yard systems. These work for the carrier that built them but don't transfer.

### 6. Status quo: dispatcher phone calls + email

The most common "solution" at mid-market and below. A driver waiting for a trailer texts dispatch; dispatch radios the yard; the yard checks; the chain wastes 20–60 minutes per handoff.

---

## What the seam looks like in operational reality

A T&L example:
1. Carrier dispatches Driver D for Load L; planned departure 14:30.
2. Yard hostler still re-positioning trailer at 14:42; dock-out at 14:51.
3. Driver D arrives at gate 14:55, gate-out at 15:08.
4. Route plan assumed 14:30 departure; ETA at first stop is now 38 minutes late.
5. Customer-facing ETA was sent at 14:00 based on the plan; never updated.

The data exists in three systems (YMS, TMS, driver app). No vendor reliably reconciles in real time; the carrier eats the variance as detention and customer dissatisfaction.

---

## Where the category leaves customers underserved

1. **Cross-system real-time reconciliation.** No vendor today natively reconciles yard-side reality with TMS plan and driver-app execution in a way that re-broadcasts a corrected ETA without manual intervention.
2. **Mid-market carriers without enterprise visibility.** FourKites, Project44 are shipper-funded; carrier-side visibility is incidental. A 200-truck carrier doesn't get FourKites unless their shipper paid for it.
3. **The driver-side moment.** The driver doesn't know the trailer is delayed until they arrive at the gate. A "trailer not ready, ETA 14:50" push to the driver app is rare.
4. **Detention reconciliation tied to driver-side data.** Carriers who could prove detention with timestamped data lose disputes because the data is fragmented.

---

## Status quo cost / friction

- Lost detention recovery at mid-market: ~$30K–$80K/month per 200-truck fleet (carrier estimates from trade press; directional)
- Customer ETA accuracy penalty: shipper-of-choice impact, hard to quantify
- Hostler / dispatcher phone time: significant but unmeasured

---

## Switching costs

- This is a NEW workflow rather than a replacement. Switching cost = adoption friction + integration cost.
- Integrating with existing YMS, TMS, driver app: meaningful.
- Single-vendor pitch ("we replace YMS + TMS + driver app") is a non-starter for mid-market.
- Pitch must be "we sit between your existing systems."

---

## Sources

- [FourKites Dynamic Yard](https://www.fourkites.com/platform/yard-management/)
- [Velostics on YMS trends 2025 / Redwood TMS partnership](https://www.velostics.com/blog/yms-trends-to-watch-for-2025)
- [DC Velocity Vector-YardView](https://www.dcvelocity.com/technology/warehouse-it/yard-management-yms/vector-acquires-yardview-to-improve-dock-visibility)
- [Velostics 2025 yard checklist](https://www.velostics.com/blog/yms-checklist)
- [DataDocks YMS comparison](https://datadocks.com/posts/best-yard-management-options)

---

## Competitive read

There is no incumbent at this seam. There are *partial* solutions on each side. The closest end-to-end is FourKites Dynamic Yard + visibility — but FourKites is a shipper-paid platform, leaves the carrier-driver-app side largely unaddressed, and is enterprise-priced.

This is the most distinctive whitespace in the candidate set, but it's also the one where the question "is the customer pain real and acute enough to pay" is most uncertain.
