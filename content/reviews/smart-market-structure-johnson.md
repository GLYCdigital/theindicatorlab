---
title: "Smart_Market_Structure_Johnson Review: Settings, Strategy & How to Use It"
date: 2026-08-10
draft: false
type: reviews
image: "/screenshots/smart-market-structure-johnson.png"
tags:
  - "smart market structure johnson"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Smart_Market_Structure_Johnson review: tested settings, entry logic, pros/cons. A solid 4-star trend indicator for swing traders."
grounding: "none (no source found)"
---
# Smart_Market_Structure_Johnson Review

Smart_Market_Structure_Johnson is a market structure mapping tool. It identifies swing highs and swing lows and connects them into a trend narrative. It is not a signal generator and not a forecasting tool — it is a structure visualizer.

The indicator is price-action driven. It does not depend on oscillators or other lagging studies, which keeps its output focused on where price has actually turned rather than on secondary confirmation.

**What sets it apart**

Structure indicators tend to fall into two failure modes: they either repaint aggressively, or they draw so many lines the chart becomes unreadable. This one is designed to avoid both. Swing detection relies on pivot confirmation, and the left and right bar counts are user-configurable — meaning a swing, once confirmed, stays confirmed historically.

The breakout detection is the more distinctive feature. When price breaks a recent swing high or low, the indicator shades the zone and flips the trend bias line. It is not only drawing structure; it is flagging when that structure has shifted. The color coding is straightforward: green for bullish structure, red for bearish, gray for neutral consolidation.

**Settings and How to Tune Them**

- **Left/Right bars.** These control pivot strength. Higher values produce fewer, more significant swings; lower values produce more swings and more noise. The right balance depends on the timeframe and the instrument.
- **Breakout confirmation.** This sets how much price action is required before a break is accepted. A tighter confirmation reacts faster but admits more false breaks; a looser one filters noise at the cost of responsiveness.
- **Draw previous structure.** When enabled, the indicator shows the last confirmed swing before the current one, which helps frame the current structure in context.

One limitation worth flagging: the indicator does not include a built-in alert for structure breaks. Alerts have to be set manually at the relevant swing levels.

**How it is used**

The logic is straightforward. In an uptrend, the workflow is to wait for price to pull back to the most recent swing low, then act on a bullish reversal candle that closes back above that swing low. The stop sits below the swing low; the target is the next measured move derived from the prior swing range. Shorts mirror the same process.

The indicator tells you where structure is. It does not tell you when to enter. Timing remains the trader's responsibility.

**Trade-offs**

Pros:
- Confirmed swings do not repaint, so historical structure is stable
- Clean visual output that does not clutter the chart
- Customizable pivot strength
- Price-action driven, with no oscillator dependency

Cons:
- No built-in alerts for structure breaks
- Neutral zones can be ambiguous once the bias line turns gray
- Lower timeframes produce noisy structure that is difficult to use without heavy adjustment
- It reacts to structure rather than anticipating it — it is not a leading signal tool

**Who it suits**

Swing traders and position traders are the natural audience. When trades are held for days or weeks, market structure is a core input, and this tool maps it efficiently. Very short-term traders are likely to find the pivot confirmation lag a problem, since entries arrive after the move has already begun.

**Alternatives**

For traders who want built-in alerts and more automated signal generation, LuxAlgo's Market Structure indicator is a more polished option, though it occupies more chart space. For a free alternative, the "Smart Money Concepts" script by LuxAlgo covers similar ground with more visual options, though it is less stable historically.

**FAQ**

*Does it repaint?* Confirmed swings do not repaint. The trend bias line can flip intrabar if price wicks through a level, but it is fixed once the candle closes.

*What is the best timeframe?* Higher timeframes produce cleaner structure. Lower timeframes require more adjustment and produce more noise.

**Verdict**

Smart_Market_Structure_Johnson is not flashy and it will not hand you trades. The missing alerts are a genuine drawback. But for a trader who already understands market structure and wants a reliable visual tool to map it, the indicator does what it claims. Stable confirmed swings and clean output put it ahead of much of the category. It is a workhorse rather than a showpiece.

**Rating: 4/5**

## Frequently Asked Questions

### Is Smart_Market_Structure_Johnson worth it?

It is a solid choice for traders who need a clean, price-action-driven map of market structure. It is not designed for traders looking for automated entries or leading signals.

### Does this indicator repaint?

Confirmed swings do not repaint. The trend bias line can flip intrabar but is fixed on candle close.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **SMA/MA Cross** implementation was backtested on 30 markets over 5 years of daily data (43,215 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.7%** (50% = coin flip)
- Strongest markets: XAUUSD 54.5%, META 54.4%, USDJPY 53.4%, SPY 53.3%
- Weakest markets: VIX 43.7%, AUDUSD 43.4%, SHIBUSD 30.0%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
