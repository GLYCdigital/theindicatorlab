---
title: "Sector_Rotation_Leadership_Persistence_Dots3Red Review: Settings, Strategy & How to Use It"
date: 2026-09-13
draft: false
type: reviews
image: "/screenshots/sector-rotation-leadership-persistence-dots3red.png"
tags:
  - "sector rotation leadership persistence dots3red"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Sector_Rotation_Leadership_Persistence_Dots3Red: what the dots actually show, best settings, entry logic, and who should install it."
tv_script_url: "https://www.tradingview.com/script/pVIAaEEY-Sector-Rotation-Leadership-Persistence-Dots3Red/"
sources: ["https://www.tradingview.com/script/pVIAaEEY-Sector-Rotation-Leadership-Persistence-Dots3Red/"]
---
Most "sector rotation" scripts on TradingView are repackaged relative-strength lines with a gradient slapped on top. This one takes a different angle, and the difference is stated right in the title: **leadership persistence**. It doesn't just show which sector is leading — it tracks how long that leadership tends to last, and how often a new leader is still leading a set number of bars later.

## What it actually plots

The core is a normalized comparison of all eleven US SPDR Select Sector ETFs — Technology, Financials, Energy, Health Care, Industrials, Discretionary, Staples, Utilities, Materials, Real Estate, and Communication Services. Each is plotted as cumulative percentage return from a common anchor point, so every line starts at zero and diverges from there. The spread between the best and worst performer is the visual story.

Leadership is defined mechanically: the sector with the highest normalized return at any moment is the current leader, marked with a star in both the end-of-chart label and the dashboard legend. Every time leadership changes hands, the duration the previous leader held the top spot is recorded, building a running average across every changeover the chart has produced. Separately, each new leader is checked again a set number of bars later to see whether it is still leading. That running percentage is the persistence statistic.

The script reports both figures directly on the chart. In the published example, the dashboard shows an average leadership of 14 bars and a persistence rate of 58%, both with a sample size of 8 changeovers. Those numbers are measured from the chart's own rotation history, not from a general rule about how sectors should behave — and the sample is small, which the script itself acknowledges.

## Settings and How to Tune Them

**Rotation Anchor — Week / Month / Quarter.** All lines reset to zero at the start of each new period. The documentation describes Month as the standard window for rotation analysis, since it is long enough to show a real trend without letting early leadership become irrelevant. Week gives a faster, more tactical view; Quarter gives a slower, more structural read. Match the anchor to your own time horizon.

**Leadership Check Window.** This controls how many bars ahead a new leader is graded for persistence. It is the input that defines what "still leading" means for the persistence statistic; a longer window asks a stricter question, a shorter one a looser one.

**Dashboard — show/hide and position.** The dashboard carries the current leader, leadership duration, average leadership length, persistence odds, changeover count, and the full ranked sector legend. The ranked legend sorts all eleven sectors by current performance, showing each one's actual line color and live return percentage. The script's stated rationale for the legend is that on-chart labels at the far right edge can get compressed or pushed off-screen depending on chart sizing, whereas the dashboard legend stays fully readable regardless of zoom or pane width.

## How to read it

The published guidance is to read the spread, not just the top line. A wide gap between the leader and the rest signals strong rotation conviction; a tight cluster near zero signals an indecisive, rotation-less market.

The second read is "Led Since" alongside "Avg Leadership." If the current leader has already held the top spot longer than the historical average changeover duration, that is context worth noting — not a signal to act on.

The persistence percentage is framed as a way to calibrate expectations, not to predict. The script is explicit that a figure like 58% with a sample of 8 is real but still developing, and should be treated with more confidence once the changeover count grows.

The ranked legend doubles as a market-breadth check. Whether the top of the ranking is dominated by cyclical sectors (Discretionary, Industrials, Financials) or defensive ones (Staples, Utilities, Real Estate) is itself a read on broad market risk appetite.

## Pros and cons

**Pros:**
- Puts eleven sectors on one normalized chart, so leadership and lag are visible at a glance rather than pieced together from eleven separate tabs
- The persistence statistic answers a question most rotation tools skip: once a sector takes the lead, how long does that lead typically last
- The ranked dashboard legend stays readable regardless of zoom or pane width, which solves a real limitation of edge-of-chart labels
- Statistics accumulate from the chart's own history rather than applying a generic rule

**Cons:**
- Leadership and persistence statistics only accumulate from when the indicator is added to the chart, so early readings rest on small sample sizes
- Covers the eleven US SPDR Select Sector ETFs specifically — no international markets and no custom sector groupings
- It is an analytical and visualization tool, not a signal generator, and it does not produce trade signals
- No built-in screener mentioned; sector comparison happens on the chart

## Who it's for

Traders who already think in terms of sector rotation and want an objective, chart-based read on whether leadership is persisting. It is a diagnostic and contextual tool rather than an entry trigger. Anyone expecting trade signals or coverage outside the eleven US sector ETFs will need something else.

## FAQ

**Does it generate trade signals?** No. The script states plainly that it is an analytical and visualization tool that does not generate trade signals and does not constitute financial advice.

**Does it cover international markets or custom sector lists?** No. It covers the eleven US SPDR Select Sector ETFs specifically.

**Why are the sample sizes so small?** The leadership and persistence statistics start accumulating from the moment the indicator is added to the chart. They become more meaningful as more changeovers occur, and the script warns to expect small samples early on.

**Can I rely on the persistence rate as a forecast?** The script frames it as a calibration tool, not a prediction. Historical leadership duration and persistence rates do not guarantee how sector rotation will behave going forward.

## Verdict

This is a focused tool that answers a narrower question than most rotation scripts attempt, and answers it honestly — with its own sample sizes and caveats displayed alongside the numbers. The normalized eleven-sector view and the ranked legend make leadership and breadth readable at a glance, and the persistence statistic adds context that a plain relative-strength line does not provide. The limitations are structural rather than fixable: a growing sample, US ETFs only, and no signals. Traders already working a rotation framework will find it useful as a contextual layer.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
