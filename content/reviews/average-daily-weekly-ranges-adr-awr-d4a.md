---
title: "Average_Daily_Weekly_Ranges_Adr_Awr_D4A Review: Settings, Strategy & How to Use It"
date: 2026-08-22
draft: false
type: reviews
image: "/screenshots/average-daily-weekly-ranges-adr-awr-d4a.png"
tags:
  - "average daily weekly ranges adr awr d4a"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Average Daily Weekly Ranges (ADR/AWR D4A): settings, entry/exit logic, pros/cons, and who should actually use this volatility tool."
tv_script_url: "https://www.tradingview.com/script/1SpBdC7v-Average-Daily-Weekly-Ranges-ADR-AWR-D4A/"
sources: ["https://www.tradingview.com/script/1SpBdC7v-Average-Daily-Weekly-Ranges-ADR-AWR-D4A/"]
---
The Average Daily Weekly Ranges (ADR/AWR) indicator is a study that calculates Average Daily Range and Average Weekly Range and displays them directly on the chart. It is not a moving average rebranded as a volatility tool — it reads exchange daily and weekly bars and projects range levels relative to the current price.

The core function: the script derives ADR from the daily candle's high-low range and AWR from the weekly candle's high-low range, averaged over a user-selected lookback period. It then plots the current day's and current week's range as marker lines on the right side of the chart, with the position customizable. High/low and one-third high/low levels can each be toggled for both the daily and weekly projections. The lines move with price, so you are always seeing where the expected move ends for the current day or week.

## Key Features

The headline feature is the dual-range calculation. ADR and AWR are handled separately, and each can display current marker lines plus historical levels as full-length lines when enabled. That gives four potential reference levels to work with: daily high/low projection and weekly high/low projection.

- **Session context**: you can see whether the current day's range is already extended relative to its historical average, or whether room remains.
- **Volatility comparison**: the widget shows ADR and AWR metrics as a percentage of the average range over the selected lookback period, with a tooltip showing the average range size for that period.
- **Range sizing in native units**: the current day and week range are shown in the asset's own metrics — points for indices, pips for forex, and so on.
- **Color-coded widget**: background colors reflect the current day's range as a percentage of average — low, average, high, or very high — unless you disable color grading and use a single color.

The script uses `request.security()` to read the official exchange or data-vendor daily bar, the same high/low you would see on a Daily timeframe. It is timeframe-independent, so it is accurate whether you are viewing 1-minute or 1-hour bars, and it reflects whatever session scope the data feed uses to build its daily candle. For continuous futures and forex, that is typically the full ~23–24 hour session including the overnight/electronic session, not just regular trading hours.

## Settings and How to Tune Them

- **Lookback Range (Days & Weeks)** — selects the period the script uses for calculation. The description cites 5, 10, or 20 days (or weeks) as examples, and notes that normally five days is used for ADR and five weeks for AWR.
- **Low, Average, High, Very High** — widget background colors reflecting the current day's range as a percentage of average: low is under 50%, average is under 100%, high is under 150%, and anything at or above 150% is marked very high.
- **BG Transparency** — background transparency of the widget.
- **Don't Color Grade, Use One Color** — uses a single color independent of the size of the current ADR.
- **Show Today's Price %** — shows the asset's current gain or loss percentage.
- **Show Week's Price %** — shows the asset's current gain or loss compared to the price at the weekly open.
- **Up, Down, Even** — the colors symbolizing gain, loss, or unchanged price.
- **Widget location** — defines where the widget sits on the chart.
- **Show current Average Day Range Marker Lines (ADR)** — displays current ADR lines as markers on the right side of the chart.
- **Show Historical Daily Lines (true day extent)** — displays current and historical ADR levels as full-length lines.
- **High/Low** — defines the ADR+ and ADR− lines.
- **1/3 High/Low** — defines the one-third ADR+ and one-third ADR− lines.
- **Offset left and Right** — defines the beginning and end of the ADR marker lines.
- **Show current Average Week Range Marker Lines (AWR)** — displays current AWR lines as markers on the right side of the chart.
- **Show Historical Weekly Lines (true week extent)** — displays current and historical AWR levels as full-length lines.
- **High/Low** — defines the AWR+ and AWR− lines.
- **1/3 High/Low** — defines the one-third AWR+ and one-third AWR− lines.
- **Offset left and Right** — defines the beginning and end of the AWR marker lines.
- **Labels** — enables labels for the current day and week; you can define the label size and right offset.

There is no single "best" configuration. The lookback period trades off responsiveness against smoothness, and the appropriate value depends on the asset and the strategy. The color and location settings are purely presentational.

## How to Use It

The script's stated purpose is to let you see how the current day or week's price behavior compares to previous days and weeks. The official description gives one concrete example: if it is Wednesday and the weekly range is still below 30%, you can expect — though it is not guaranteed — that Thursday and Friday will try to catch up with the historical average and offer larger price movements.

That framing supports two general approaches:

**Range or mean-reversion trading:** when price approaches an ADR or AWR extreme, the projection lines mark where the average move would be exhausted. A reversal signal at one of those levels, in the context of a neutral or ranging higher-timeframe trend, is the setup the tool is built to inform. Opposite-side bands are natural reference points for targets.

**Breakout trading:** when price pushes through a range band, the average range is being exceeded for that period, which the description frames as consistent with larger-than-average movement. The next larger-period band becomes the relevant reference.

The indicator does not generate signals. It is a reference overlay, and any entry, stop, or target decision is yours.

## Pros & Cons

**Pros:**
- Clean visual output with toggleable marker lines, historical lines, and labels.
- Uses official exchange daily and weekly bars via `request.security()`, so it is timeframe-independent.
- Works across asset types and on any timeframe below daily for ADR and below weekly for AWR.
- Range values are expressed in the asset's native units, which avoids mental conversion.
- The widget's color grading gives an at-a-glance read on whether the current day's range is low, average, high, or very high.

**Cons:**
- No alert functionality is described, so band touches cannot trigger notifications from the script itself.
- No multi-instrument dashboard; ranges are shown for the chart's current symbol only.
- The weekly bands are redundant for traders who only work intraday.

## Alternatives

If alerts are the priority, an ADR tool built around touch notifications covers that need but would not include the weekly range. For a multi-pair dashboard view, a broader volatility dashboard is more suitable, though typically more complex than this script. For a simpler intraday range reference, standard-deviation bands around VWAP cover related ground.

## FAQ

**Does this indicator repaint?**
The source material does not make a repainting claim. The script reads the official exchange daily bar via `request.security()` and calculates ranges from historical high-low data, so the values are derived from completed daily and weekly bars.

**What assets does it work on?**
The description states it should work on all asset types and all timeframes below the daily timeframe for ADR and below the weekly timeframe for AWR.

**What is the minimum lookback period?**
The description does not specify a minimum. It cites 5, 10, or 20 periods as examples, with five days and five weeks given as the normal intervals.

**Does it work on crypto?**
The description states the script should work on all asset types. It does not make a specific claim about crypto behavior.

## Final Verdict

The Average Daily Weekly Ranges (ADR/AWR) indicator does one job: it calculates average daily and weekly ranges from official exchange bars and displays them as reference lines and a metrics widget. The dual-range approach, the native-unit readout, and the color-graded widget make it a compact volatility reference for intraday and short-term traders. The absence of alerts and any multi-instrument view are real limitations, and the weekly component will be dead weight for purely intraday use. As a range-projection overlay rather than a signal generator, it is a clean, focused tool.

---

*Disclaimer: The content provided in this script is for educational and informational purposes only. It does not constitute financial advice, investment recommendations, or a solicitation to buy or sell any financial instruments. All investments involve risk, and past performance does not guarantee future results.*

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
