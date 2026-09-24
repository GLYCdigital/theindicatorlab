---
title: "Macro_Candles_M1D Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/macro-candles-m1d.png"
tags:
  - "macro candles m1d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Macro_Candles_M1D review: how this higher-timeframe trend overlay works, the settings that matter, entry logic, and where it falls short."
tv_script_url: "https://www.tradingview.com/script/G0Y5c2yI-Macro-Candles-M1D/"
sources: ["https://www.tradingview.com/script/G0Y5c2yI-Macro-Candles-M1D/"]
---
Most "macro" indicators are just an EMA with a fancy name. Macro_Candles_M1D isn't that — but it isn't the trend oracle its name might suggest either. Here's what the script actually does, per its own documentation.

## What it actually does

Macro_Candles_M1D colours the candles that print inside each ICT macro window and grades every macro against the one before it. A macro runs from ten minutes before the hour to ten minutes after it, New York time. Inside the window the candles take the macro's colour; outside it the chart's own candles show untouched.

It draws nothing else: one dotted line at each macro's open and one dot carrying the reading. There's no banded backdrop, no higher-timeframe body projection, no daily framing. The "macro" here is a twenty-minute session window, not a daily candle.

## Key features that actually matter

The core mechanic is the **grade**. Each macro opens against the previous macro's high and low. Opening above that high grades it bullish, opening below that low grades it bearish, and opening inside the range grades it consolidation. The grade is set on the opening candle and held.

Then there's the **re-grade**. A macro can change its grade once. One that opened above the previous high turns bearish on the first candle that closes back below that high, and one that opened below the previous low turns bullish on the first close back above it. A consolidation macro turns bearish on the first close below the previous low and bullish on the first close above its high. Candles already printed keep the colour they had, so the candle where the grade changed stays visible. One change per macro, then it holds to the close.

On the **method**: the opening grade is read from the opening candle's open and never revised. A re-grade evaluates on confirmed candles only, so a colour change is never undone by a later tick. The previous macro's high and low are its full range, wick to wick, and the first macro on a loaded chart has no previous range to read against, so it stays uncoloured.

One practical limitation worth knowing up front: on one-hour and higher charts a twenty-minute window has no candle to colour. The script draws nothing and says so in a small corner note. This is a sub-hourly tool.

## Settings and How to Tune Them

The settings cover colour mode, the bullish, bearish and consolidation colours, the re-grade switch, candle colouring on or off, and wick colour. The wick can be set to its own colour instead of inheriting the body's. Two other colour modes are available: each candle in its own up or down colour, or every macro candle in one colour.

The open line has its own colour and width settings — by default a neutral grey dotted line of width one.

The bias dot has a cushion from price and a size setting. The dot sits above price for a bearish or consolidation macro, below price for a bullish one, at a set distance clear of the surrounding candles, and it steps away from any candle that later reaches it. Hovering the dot shows the reading in words; a re-grade recolours the dot, moves it to the other side of price and rewrites the reading.

Which macros print is controlled by spacing and hour switches. Every hour is on by default. Spacing shows a macro every two, three or up to twelve hours, counted from midnight New York, and each of the twenty-four opening hours has its own switch on top of that. History in days is also configurable.

The script's own visual grammar: bullish is blue, bearish is red, consolidation is a dark grey — all three adjustable. Nothing carries a background or a text label; the dot is the only marker, and its reading lives in the hover.

## How the pieces fit together

The logic is narrow and that's the point. A macro's grade gives you the directional read for that twenty-minute window; the re-grade flags the single moment it flips; the coloured candles show you exactly which candles belonged to the window and which didn't; the dot carries the current reading so you don't have to infer it from colour alone.

The script is explicit that a macro exists only if its opening candle printed. Around a session close the last candles of one hour can run straight into the first candles of a later one with nothing between them; those candles belong to a window that never opened and are left alone. So gaps in colouring are meaningful, not glitches.

## Pros and cons

**Pros:**
- The opening grade is read once and never revised, and re-grades evaluate on confirmed candles only — so a printed colour isn't undone by a later tick
- The previous macro's full wick-to-wick range is the reference, not a smoothed average
- One re-grade per macro, with the change candle left visible — you can see where the flip happened rather than just its end state
- The dot carries the reading in words on hover, including after a re-grade
- Per-hour switches plus spacing give fine control over which windows are active

**Cons:**
- Draws nothing on one-hour and higher charts — the window has no candle to colour at those resolutions
- The first macro on a loaded chart stays uncoloured, since it has no previous range to read against
- Only the dot carries a reading; no text labels or backgrounds anywhere
- Documentation is limited to the description itself

## Who it's for

Traders working sub-hourly charts who want the ICT macro windows marked and graded without drawing them by hand. If your chart is one hour or higher, this script has nothing to show you. If you want signals handed to you, look elsewhere — this is window colouring and a grade, not a strategy.

## FAQ

**Does it repaint?** The opening grade is read from the opening candle's open and never revised. A re-grade evaluates on confirmed candles only, so a colour change is never undone by a later tick. Candles already printed keep the colour they had.

**Which markets?** The window is resolved through the exchange-independent time zone so it stays true across daylight saving on any symbol.

**What chart timeframe do I need?** Sub-hourly. On one-hour and higher charts the twenty-minute window has no candle to colour, and the script draws nothing and notes this in a corner.

**Can I turn off the re-grade?** Yes — there's a re-grade switch in the settings.

## Verdict

Macro_Candles_M1D does one job: it colours the candles inside each ICT macro window and grades each macro against the previous one, with a single permitted re-grade per window. It's a narrow, well-defined tool rather than a broad trend filter, and its usefulness depends entirely on whether you trade the sub-hourly windows it's built around.

Built by M1D. For education and study of price delivery — not financial advice.

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
