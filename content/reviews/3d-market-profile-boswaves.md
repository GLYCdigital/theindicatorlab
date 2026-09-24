---
title: "3D_Market_Profile_Boswaves Review: Settings, Strategy & How to Use It"
date: 2026-08-25
draft: false
type: reviews
image: "/screenshots/3d-market-profile-boswaves.png"
tags:
  - "3d market profile boswaves"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "3D_Market_Profile_Boswaves review: honest take on settings, entry logic, pros/cons, and who should actually use this trend indicator."
tv_script_url: "https://www.tradingview.com/script/QdfnWDjO-3D-Market-Profile-BOSWaves/"
sources: ["https://www.tradingview.com/script/QdfnWDjO-3D-Market-Profile-BOSWaves/"]
---
# 3D Market Profile [BOSWaves] Review

The 3D Market Profile [BOSWaves] is a TPO (Time Price Opportunity) market profile system that aggregates chart bars into complete TPO periods, builds a per-row distribution of letters and print counts, and renders the result as a three-dimensional extruded structure using polyline geometry. As the name suggests, the "3D" element is not a gimmick — it refers to extruded top faces and side caps that follow the profile contour row by row, plus a rear glass plane and wireframe bounding box. If you've used traditional market profile tools, the analytical framework (POC, Value Area, Initial Balance) will feel familiar, but the spatial rendering is a different approach to the same underlying data.

It's worth being clear about what this indicator is and isn't. It is a structural visualization and reference tool, not a signal generator. It builds a distribution from recent chart history, derives standard market profile levels from that distribution, and renders them as extending reference lines. It does not produce discrete entry or exit signals.

## What Actually Sets It Apart

Most market profile indicators render flat row boxes where the only visual difference between a high-density and low-density row is bar width — something that gets hard to compare once a profile has many rows or is viewed on a smaller screen. This indicator adds two more visual dimensions on top of width: extruded top and side faces that follow the profile contour, and density-gradient coloring that progresses from a configured low-density color to a high-density color with a power-transformed gradient.

The design principles behind it are specific:

- TPO distribution is built from complete timeframe periods, not individual bars, so each period contributes exactly one letter print to each price row it trades through regardless of how many chart bars compose it.
- The 3D extrusion follows the profile contour row by row rather than applying a uniform rectangular extrusion, preserving the shape of the distribution in the depth geometry.
- POC, VAH, VAL, and Initial Balance are all derived from the same TPO count data that drives the visual rendering.

The POC tiebreaking rule is also worth noting: when multiple rows share the maximum print count, the row closest to the profile mid-range is selected. That's a consistent rule favoring centrally located levels rather than an arbitrary pick.

## Settings and How to Tune Them

The source material provides a suggested baseline configuration, which is a reasonable starting point rather than a recommendation of optimal values:

- **Length:** 180
- **Rows:** 24
- **Value Area %:** 70
- **Placement:** Right of Price
- **TPO Timeframe:** 30
- **Show TPO Letters:** Enabled
- **Initial Balance Periods:** 2
- **3D Depth (Bars):** 6
- **3D Height (Rows):** 0.42
- **Show 3D Frame:** Enabled
- **Show POC / VA:** Enabled
- **Show Initial Balance:** Enabled
- **Show Level Labels:** Enabled

Tuning guidance from the source material:

- **Rows:** Adjust to increase or decrease vertical price resolution. The goal is to calibrate row height to the instrument's typical daily range so rows represent meaningful price increments rather than noise-level or excessively large bands.
- **TPO Cell Width:** Controls the horizontal space allocated to each letter. Increase for wider, more readable letter display, or decrease to fit more prints within the same profile width.
- **Length and Cell Width:** Profile width scales automatically with the maximum row print count multiplied by cell width, so these two settings together determine the resulting profile width.
- **3D Depth (Bars) and 3D Height (Rows):** Control horizontal perspective extent and vertical depth respectively. Calibrate to the chart's aspect ratio and current zoom level.
- **Right Offset / Placement:** If the profile overlaps price action, use Right of Price with a larger Right Offset to push it further from current price, or switch to On Range placement to anchor it to the beginning of the analyzed window.
- **Initial Balance Periods:** Adjust to include more or fewer opening TPO periods in the IB calculation. Two periods represents the conventional first trading hour using thirty-minute TPOs; increase for a wider opening range definition.
- **TPO Timeframe:** Match to the session type being analyzed. Using a thirty-minute timeframe on a daily chart produces very few periods and minimal distribution differentiation, so choose a timeframe appropriate to the chart timeframe and session length.

Adjustments should be incremental and evaluated across multiple session types rather than isolated market conditions.

## How It's Meant to Be Used

The indicator is built around conventional market profile and auction theory approaches rather than a proprietary signal model:

1. **POC reversion framework:** Use the POC line as a mean reversion reference when price has extended to or beyond the Value Area boundaries. The POC represents the price where the distribution's greatest acceptance occurred.
2. **Value Area boundary trading:** Monitor price behavior at VAH and VAL for acceptance or rejection. Price accepting above VAH or below VAL with multiple closes beyond the boundary suggests genuine range extension; rejection at the boundaries and return inside the Value Area suggests reversion continuation.
3. **Initial Balance range extension:** Price establishing acceptance above IBH with sustained closes is framed as potential bullish range extension; acceptance below IBL as potential bearish extension. Price remaining within IB is framed as balanced auction conditions.
4. **Single print targeting:** Single print rows are treated as potential return targets for incomplete auction areas, on the market profile principle that incomplete auctions tend to be revisited.
5. **Placement selection:** Right of Price keeps the profile in forward chart space as a live reference; On Range anchors it to the historical window for post-session analysis.
6. **Timeframe and length calibration:** The source material maps timeframe choices to session types — shorter timeframes for intraday micro-profiles, thirty-minute TPOs for conventional daily profiles, and longer timeframes for multi-day macro profiles.

Note that this is a visualization and reference framework. The indicator does not generate discrete entry or exit signals.

## Pros & Cons

**Strengths:** The multi-timeframe spatial rendering is the core differentiator — extruded geometry and gradient coloring communicate density through width, shape, and color simultaneously. The analytical framework follows conventional market profile methodology (POC via max count with mid-range tiebreaking, outward Value Area expansion from the POC with alternating upper/lower priority, IB derived from the opening periods). Level rendering is differentiated by type: dual glow and core lines for POC, dotted lines for VAH/VAL, dashed lines for IBH/IBL, with price readout labels at the right extent.

**Weaknesses:** The source material lists reduced effectiveness in several conditions — markets with highly variable daily ranges where a fixed row count produces inconsistent row heights, instruments without clear session structure where few complete periods form, very short profile lengths producing too few TPO periods for a meaningful distribution, compressed consolidation where all rows get similar counts and the distribution flattens, and markets with frequent large gaps where the profile range is dominated by gap space. The performance profile also notes full object cleanup and rebuild on the last bar, which is relevant for anyone running this on lower-end hardware with multiple charts. The source material does not describe repainting behavior, alert functionality, or resource consumption beyond the cleanup-and-rebuild note, so I won't make claims either way on those fronts.

## Who Should Use This

The source material positions this for market profile and auction theory-based approaches. High effectiveness is claimed for session-structured markets with a defined trading window, instruments with consistent daily range, and workflows where POC, Value Area, and IB are the primary structural reference. Reduced effectiveness is noted for markets without clear session structure, highly variable daily ranges, very short profile lengths, compressed consolidation, and gap-dominated markets.

If you're new to market profile concepts, the indicator will not teach you what POC and Value Area mean — those are prerequisites, not features. The visualization assumes you already read a distribution.

## Common Questions

**Does it generate signals?** No. It provides continuous structural reference (POC, VAH, VAL, IBH, IBL) but no discrete entry or exit signals. The source material states this explicitly.

**What does the "3D" actually do?** It constructs polyline quadrilateral top faces following each row's width contour, side end cap faces at the outer edge of each row, and a rear glass plane bounding box, using configurable depth bar and depth row offsets. It's a spatial rendering of the same distribution data, not a separate indicator.

**Can I use it on any timeframe?** The source material gives timeframe guidance rather than a hard restriction: shorter timeframes for intraday micro-profiles, mid-range timeframes for session profiles, and higher timeframes for multi-session macro profiles. It warns that mismatching the TPO timeframe to the chart timeframe (e.g., thirty-minute TPOs on a daily chart) produces very few periods and minimal differentiation.

## Final Verdict

3D Market Profile [BOSWaves] is a structurally sound implementation of conventional TPO market profile analysis with an unusually elaborate rendering layer. The analytical core — period aggregation, row-level print counting, POC selection with mid-range tiebreaking, outward Value Area expansion, and IB derivation — follows standard methodology, and the 3D geometry is driven by the same count data rather than being decorative. The caveats are real: it's a reference tool, not a signal generator, and its effectiveness degrades in the specific conditions the source material calls out. For traders already fluent in market profile concepts who want a more spatially readable distribution, it's a coherent addition to a broader analytical framework.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
