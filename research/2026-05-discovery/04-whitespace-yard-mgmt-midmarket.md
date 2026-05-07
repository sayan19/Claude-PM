# 04 — Whitespace: Yard Management for Mid-Market 3PLs (C2)

## Where customers are genuinely underserved

### Whitespace 1: Hostler / gate-guard rugged UX
**The gap:** Most mid-market YMS were built browser-first. Hostlers run them on a Zebra VC8300 vehicle-mount or a tablet that's vibrating in a yard truck. The UX is poor; latency is poor; the workflow steps don't match the physical task.
**Why nobody owns it:** YMS vendors are software-led and treat the device as "any browser will do." Kaleris partially solves it at the high end with a hostler-specific app.
**Customer signal:** Directional (G2 reviews complain about field UX); no validated SOTI customer signal.
**SOTI fit:** Direct. Snap can build a hostler UX optimized for Zebra rugged Android, with offline-first sync, large hit-targets, and OS-level lockdown via MobiControl. This is a SOTI-natural play.

### Whitespace 2: Light-touch YMS for 1–3-DC mid-market 3PLs
**The gap:** A 3PL with 3 DCs (each 50–150 trailers) is too small to justify Kaleris and skeptical of YardView/Velostics ACVs. Many such 3PLs run on whiteboard + radio. The whitespace is a $15K–$30K/site/year YMS that focuses on the 80% workflow (gate-in, trailer location, dock assignment, gate-out) without the enterprise depth.
**Why nobody owns it:** Vendors aspire upward, not downward. The economics of selling $15K/site to a 3-DC 3PL through a direct sales motion are weak; channel is required.
**Customer signal:** Directional (Armstrong's 750+ 3PL guide implies a long-tail). No validated SOTI customer signal.
**SOTI fit:** Plausible — but requires SOTI to build YMS workflow IP it doesn't have today.

### Whitespace 3: Multi-tenant 3PL yard
**The gap:** A 3PL operating a single yard with inventory from 4 shippers needs tenant-aware reporting (shipper A's trailer count, shipper B's dock dwell). Most YMS assume single-tenant.
**Why nobody owns it:** Tenant data isolation is a feature most 3PLs build into WMS, not YMS. Few YMS have done it.
**Customer signal:** Directional — Datex and 3PL Central market this; demand is real but penetration low.
**SOTI fit:** Indirect — SOTI's MDM tenancy model could be leveraged but doesn't deliver YMS tenant features by itself.

### Whitespace 4: Yard analytics on top of device telemetry
**The gap:** XSight already collects device telemetry (location, battery, app usage) from the rugged hostler / gate-guard / driver devices. That data could feed a yard analytics layer (hostler productivity, gate throughput, dock dwell). No vendor combines device telemetry with yard workflow analytics in a unified pane.
**Why nobody owns it:** YMS vendors aren't device-management companies; MDM vendors aren't yard-workflow companies.
**Customer signal:** Directional only. This is a "build it because it's natural to SOTI" not "customers asking for it."
**SOTI fit:** Direct — XSight extension. Strongest distinctive angle.

### Whitespace 5: Yard-to-route handoff
Covered in C6c (yard-to-route) artifact. The seam between yard exit (load departed dock 7) and route execution (driver picks up at 15:10) is owned by no one well.

---

## Buyer frustration themes

- "We bought a YMS and the hostlers won't use it because the screen is unusable on their truck."
- "Kaleris is too much; YardView gets us 80% there but the integrations cost more than the SaaS."
- "We track trailers on a whiteboard because it's faster than logging into the system."
- "Detention bills get to me weeks after the fact and I can't reconstruct the timeline."

Synthesized from public review sites and trade-press; **directional market signal, not validated customer signal.**

---

## Implication

The whitespace splits into two SOTI-natural wedges:

1. **Hostler-UX + device-telemetry-fed yard analytics overlay** — a thin product on top of MobiControl/XSight that pairs with an existing YMS *or* covers the 80%-case for 3PLs without one. This is Aperture 1/2 hybrid.
2. **Light-touch standalone YMS for 1–3-DC mid-market 3PLs** — a real net-new SaaS bet. Bigger build, real category competition (Vector, Velostics, Terminal Industries). Aperture 3.

The first wedge plays to SOTI's substrate (rugged devices in the yard); the second is a category bet with category competition.
