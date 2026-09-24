---
title: "Uptrick_Band_Flow Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/uptrick-band-flow.png"
tags:
  - "uptrick band flow"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Uptrick Band Flow review: a smoothed WMA baseline with ATR bands, close-confirmed trend flips, single-position signals and a fixed ATR target ladder."
tv_script_url: "https://www.tradingview.com/script/QqSFhZiX-Uptrick-Band-Flow/"
sources: ["https://www.tradingview.com/script/QqSFhZiX-Uptrick-Band-Flow/"]
---
Most "trend" indicators on TradingView are a moving average with a color change. Uptrick: Band Flow is more deliberate than that. It's a trend overlay built from a smoothed moving-average baseline and ATR bands, where the trend state only flips when a bar closes outside the opposite band. Nothing changes while price sits inside the envelope. That one design decision shapes everything else about the tool.

As shown in the chart above, the output is a colored envelope with occasional Up or Down labels and a set of target markers extending from the entry bar.

## What's actually under the hood

The calculation chain is documented clearly, and it's worth walking through because the parts depend on each other.

The baseline is a weighted moving average of close over the **Trend Length** (default 30), which weights recent closes more heavily than a simple average so the center line reacts sooner at the same length. An EMA smoothing pass (**Trend Smoothing**, default 4) then reduces bar-to-bar noise. Set it to 1 and the smoothing is switched off.

The bands are baseline ± ATR times a multiplier. **Band ATR Length** defaults to 14, and the upper and lower multipliers default to 1.50 each. They're independent, so you can run an asymmetric envelope if you want. ATR is floored at the symbol's minimum tick, which prevents the band width from collapsing to zero on quiet instruments.

Then comes the part that matters: trend state with memory. A close above the upper band turns it bullish. A close below the lower band turns it bearish. Price inside the bands keeps the previous state. Trend changes are evaluated on confirmed bar closes only. So touching the baseline does nothing — you need a full breakout of the opposite band.

## The signal and target engine

Signals are single-position. An Up label appears on a bullish break when the script isn't already long. A Down label appears on a bearish break when it isn't already short. Repeated breakouts in the same direction don't stack labels.

That signal bar does two things: its close becomes the entry price, and its ATR is captured and frozen. The five take-profit levels are then fixed distances from that entry — entry plus (long) or minus (short) the stored ATR times each level's multiplier. Defaults are 1.0, 2.0, 3.0, 4.0 and 5.0 ATR. Each level marks once per signal with a small cross when a bar's high (long) or low (short) reaches it, and everything resets on the next signal.

Freezing the ATR at entry is the interesting choice here. A live ATR ladder would drift as volatility changes after you're in the trade; this one stays put. Whether that's better depends on how you use targets, but it's a coherent decision rather than an accident.

## Using it

Three overlay modes change the visual without changing the logic. **Center** gives you the baseline with a gradient fill to price. **Trail** shows a one-sided trail — lower trail in an uptrend, upper in a downtrend — with an outer edge expanded by extra ATR. **Bands** shows the full envelope with a gradient strongest near the baseline. The default is Bands.

Signal labels have two anchor modes. **Bands** places them on the outer trail edge; **ATR** places them beyond the candle low or high. This is label positioning only — it does not change when signals fire. That separation is a small thing that speaks well of the design.

There's a dashboard in the top-right, two columns by six rows, showing script name and trend state, trend direction, overlay mode, signal anchor mode, entry price, and take-profit progress as five dots. Seven alert conditions exist: Up, Down, and TP1 through TP5.

One practical note straight from the documentation: Up and Down alerts are only true on bar close, but take-profit conditions can become true while a bar is still forming. Choose your alert frequency with that in mind.

Also worth repeating because it's easy to ignore: use standard candlestick or bar charts. Heikin Ashi, Renko, Kagi, Point and Figure and Range charts don't show real traded prices, so signals and targets on them wouldn't be realistic.

## Pros and cons

**Pros:**
- Trend state with memory removes the constant flip-flopping you get from a plain baseline cross. Touching the center line does nothing.
- Single-position signal logic prevents label clutter on repeated breakouts.
- Entry-frozen ATR ladder gives fixed, measurable distances rather than a moving target.
- Independent upper and lower multipliers allow an asymmetric envelope.
- Three overlay modes and two anchor modes cover a lot of visual preferences without touching the logic.
- ATR floored at minimum tick is a small robustness detail that prevents degenerate band widths.
- Pine Script v6, chart data only, no `request.security` calls.

**Cons:**
- It's a lagging tool by construction. Signals confirm a close outside the envelope, not an early turn. The documentation says this outright.
- The five ATR targets are reference distances, not orders or predictions. If you treat them as a system, you're using it wrong.
- Trend Length moves where the bands sit, and the documentation explicitly declines to say which direction is "better" — you have to test on your own markets.
- No short-side nuance beyond the mirror of the long logic. If you trade both directions, the tool is symmetric whether your markets are or not.
- It's an overlay, not a complete system. No position sizing, no stop logic beyond the band structure.

## Who it's for

Swing and position traders who want a clean trend-state read and a structured way to measure ATR distances from a breakout. It suits people who prefer confirmation over anticipation and who already have their own entry and risk framework. If you scalp or want early signals, this will frustrate you.

## FAQ

**Does it repaint?** Trend changes are evaluated on confirmed bar closes only, so the trend state doesn't shift intrabar. Take-profit markers are different — they can trigger while a bar is still forming.

**Can I use it on Heikin Ashi?** The documentation advises against it. Those chart types don't show real traded prices.

**Do the take-profit levels move after entry?** No. ATR is captured on the signal bar, so the five levels stay fixed until the next signal.

**Can I get alerts?** Yes — seven conditions: Up, Down, TP1 through TP5.

## Verdict

Band Flow is a well-assembled trend overlay. The pieces are standard — WMA, EMA smoothing, ATR — but the assembly is thoughtful: trend state with memory, single-position signals, frozen targets, and clean separation between signal logic and label placement. It doesn't pretend to be a system, and the documentation is honest about what it is and isn't.

The ceiling is that it's still a lagging, confirmation-based tool with no edge beyond disciplined trend reading. That's fine. It's not trying to be more.

**Rating: ⭐⭐⭐⭐ (4/5)** — a solid, coherent trend tool that does exactly what it says, held back only by the inherent limits of close-confirmed breakout logic.
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
