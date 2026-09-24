---
title: "Htf_3_Candle_System Review: Settings, Strategy & How to Use It"
date: 2026-09-19
draft: false
type: reviews
image: "/screenshots/htf-3-candle-system.png"
tags:
  - "htf 3 candle system"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Htf_3_Candle_System review: how the higher-timeframe 3-candle trend confirmation works, best settings, entry rules, pros, cons and who it suits."
tv_script_url: "https://www.tradingview.com/script/rHOFeLwn-HTF-3-Candle-System-Zeiierman/"
sources: ["https://www.tradingview.com/script/rHOFeLwn-HTF-3-Candle-System-Zeiierman/"]
---
Most "3 candle" indicators are repackaged candlestick patterns that fire on every doji and call it a signal. The HTF 3-Candle System (Zeiierman) is not that. It is a higher-timeframe market structure indicator that evaluates the relationship between three consecutive HTF candles and identifies which price pattern currently best describes the developing structure. Instead of hunting for one fixed candlestick formation, it scores multiple bullish and bearish three-candle structures simultaneously.

The "HTF" in the name matters. This is a top-down tool: the indicator reads a higher timeframe than your chart and reconstructs that structure on the right side of price.

## What the chart actually shows

The three higher-timeframe candles are defined as:

- **C1** = the completed HTF candle two periods back
- **C2** = the previous completed HTF candle
- **C3** = the current live HTF candle

C1 and C2 are completed; C3 updates continuously while the higher-timeframe candle is forming, so the pattern ranking and projected levels evolve with current price action.

The System evaluates 12 three-candle structures: Bullish and Bearish Sweep Reversal, Bullish and Bearish FVG Displacement, Bullish and Bearish PO3 Sequence, Bullish and Bearish Expansion, Bullish and Bearish Compression Break, and Morning Star and Evening Star Reversal.

Each pattern receives a quality score built from structural conditions plus softer proximity measurements, so a setup can begin ranking before every condition is fully completed. Factors include liquidity sweeps, candle direction, body strength, range, displacement, FVGs, compression, expansion, and recovery or rejection around key levels. The three highest-ranked structures appear in the 3-CANDLE SYSTEM table with their current scores; the top-ranked pattern controls the live state message and the projected structural levels.

The live state text describes where the active pattern currently stands — sweep or reclaim developing, FVG live, breakout or breakdown developing, compression, PO3 distribution, reversal developing.

Projected levels depend on the active structure and can include sweep levels, breakout levels, FVG boundaries, CE 50%, equilibrium, recovery levels, and invalidation. Nearby levels can merge automatically to reduce clutter.

C1, C2 and C3 are also reconstructed to the right of price using their actual HTF OHLC values, with C3 updating live. The System can additionally map C1, C2 and C3 directly over the lower-timeframe candles that formed them, with high and low dots identifying the exact lower-timeframe candles behind each HTF extreme. Completed C1 and C2 levels can change from Active to Mitigated after being traded through.

## Settings and How to Tune Them

- **Higher Timeframe:** selects the higher timeframe used to construct C1, C2 and live C3. It must be higher than the chart timeframe.
- **Strong Match Threshold:** the minimum quality score required for the highest-ranked pattern to be treated as a strong match.
- **Show Projected HTF Candles:** shows or hides the reconstructed C1, C2 and C3 candles to the right of current price.
- **Offset:** how far the projected candle structure appears from current price.
- **Candle Spacing:** horizontal spacing between projected C1, C2 and C3.
- **Merge:** how close two projected levels can be before they are combined.
- **Spacing:** horizontal spacing between pattern level labels.

The relationship between the Higher Timeframe and your chart timeframe is the setting that changes the tool's character most — a wider gap means slower, more structural reads, a narrower one keeps it closer to current price action.

## How the states read in practice

The examples in the source material show how the ranking and the live state interact, and they are worth understanding before trading off the table.

In a Bearish Expansion example, Bearish Expansion ranks first and the state reads BEARISH EXPANSION LIVE, with C1, C2 and C3 shifting progressively lower and C3 extending through the previous structure. Projected levels identify the Breakdown, the level price should Hold Below, and the Invalidation above.

A Bearish FVG Displacement example reaches the top score with a BEARISH FVG LIVE state; strong downside movement leaves C3 separated below C1, creating the imbalance, and the System projects FVG Upper, CE 50%, C3 High and Invalidation. A related example shows the FVG Upper and CE 50% close enough to merge into a single projected level.

A Bearish Compression Break example is instructive: the pattern ranks first but the state still reads COMPRESSION - WATCH RANGE LOW, because the bearish break has not yet confirmed. C2 is contained within the C1 range and C3 is pressing toward the lower boundary. The Range Low / Breakdown level marks where confirmation would occur, with Equilibrium and Range High defining the rest of the structure. The bullish equivalent reads COMPRESSION - WATCH RANGE HIGH, with confirmation only on a push through the Range High / Breakout level.

A Bullish PO3 Sequence example shows a downside manipulation followed by strong bullish C3 expansion, with the Manipulation Low, the Distribution level above, and the structural Invalidation highlighted.

The reversal examples show earlier-stage states. A Bearish Sweep Reversal can rank first while the state reads HIGH SWEPT - NEED RECLAIM, with the next requirement being C3 moving back below the projected C3 Close level. A Bullish Sweep Reversal can rank first while the state reads WATCHING C1 LOW, before the C1 low has been swept. An Evening Star Reversal can rank first with the state AWAITING REJECTION BELOW C1 MID, showing 50% Rejection, Full Rejection and Invalidation levels.

The takeaway: a high rank is not the same as a confirmed setup. The state message is the part that tells you whether the structure is still developing or has actually triggered.

## Pros and cons

**Pros**
- Evaluates many structures at once rather than forcing one fixed candlestick pattern
- Pattern ranking and projected levels evolve with the live third candle
- Projected levels are structure-specific rather than generic
- HTF mapping ties each HTF extreme back to the lower-timeframe candles that created it

**Cons**
- By design, a setup can rank highly before it is confirmed, which requires reading the state text carefully
- C3 is live, so ranking and levels shift while the HTF candle forms
- No backtest statistics or win-rate display in the source material
- The interplay between ranking, state, and projected levels takes time to learn

## Who it's for

Traders who already work top-down and want a structured read of higher-timeframe price action rather than a single candlestick signal. It suits someone who wants to see which three-candle structure is developing and where that structure's key levels sit. Traders looking for a fast trigger will find the live-state logic requires patience.

## Alternatives worth a look

- **MTF moving averages**: lighter on screen, but no multi-pattern scoring or structural levels.
- **Plain candlestick pattern scanners**: simpler, but typically evaluate one formation at a time rather than ranking a dozen.
- **Manual HTF markup**: full control, but no automated scoring, ranking, or projected levels.

The multi-pattern scoring with a live third candle is what makes this distinct. If you want a single fixed formation, the alternatives are simpler.

## FAQ

**Does it repaint?**
The source material does not make a repainting claim. C3 is explicitly live and updates continuously while the HTF candle forms, and C1 and C2 are completed candles.

**What timeframe should I use it on?**
The source material does not specify a chart timeframe. The only constraint given is that the selected higher timeframe must be higher than the chart timeframe.

**Does it work on crypto or specific markets?**
The source material does not state market coverage.

**Are the projected levels buy/sell signals?**
No. They are the structural references most relevant to the active pattern — sweep levels, breakout levels, FVG boundaries, CE 50%, equilibrium, recovery levels, and invalidation.

## Verdict

The HTF 3-Candle System does one job: it reads three consecutive higher-timeframe candles, scores twelve possible structures against them, and surfaces the top three with the levels that matter to the leader. The live third candle means the read evolves rather than waiting for a closed bar, which is both the appeal and the thing to understand before using it. If you want a mechanical higher-timeframe structure layer with explicit states and projected levels, this is a coherent implementation of that idea.

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
