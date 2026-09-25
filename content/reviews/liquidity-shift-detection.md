---
title: "Liquidity_Shift_Detection Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/gdVgCcCT-Liquidity-Shift-Detection-LSD-Zeiierman/"
date: 2026-09-03
draft: false
type: reviews
image: "/screenshots/liquidity-shift-detection.png"
tags:
  - "liquidity shift detection"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Liquidity_Shift_Detection review: settings, pros/cons, and how to trade liquidity sweeps & BOS signals on TradingView."
grounding: "none (no source found)"
---
# Liquidity_Shift_Detection Review

Liquidity_Shift_Detection is a trend indicator that flags moments when price takes out a recent swing high or low — what institutional traders call a liquidity sweep — and then confirms whether the move actually holds. It's not a crystal ball; it's a structural tool that tells you when a key level has been broken and whether momentum agrees with the breakout.

**What Sets It Apart**

Most liquidity indicators just draw zones and leave you guessing. This one does the detection work for you. When price sweeps a recent high or low, it plots a marker and then — crucially — waits for confirmation before painting a shift signal. That confirmation filter is what separates it from a dozen similar tools that fire off signals on every wick.

The visual output is clean. You get a baseline color shift on the chart background or candle highlights when a shift is confirmed, plus distinct markers for the initial sweep versus the confirmed change in character. No clutter, no hundred lines of zones you'll never use. The indicator also repaints, and that needs to be stated upfront: the marker that appears at the sweep can disappear if the confirmation fails. That's a dealbreaker for some, but for those who understand the concept, it's actually the point.

**Settings and How to Tune Them**

The swing length setting controls how far back the indicator looks for the high or low being swept. A shorter lookback catches more sweeps but also more noise; a longer lookback filters micro-sweeps that happen every few candles but responds more slowly to genuine structural shifts.

The confirmation period setting matters more than most people realize. A shorter period gets you in earlier but increases false shifts. A longer period sacrifices some of the move but improves reliability. The tradeoff is timing versus accuracy, and the right balance depends on your holding period.

The ATR-based volatility filter is best left at its defaults for standard forex and crypto pairs. It exists to normalize the sweep threshold against prevailing volatility, so adjusting it is only worthwhile if you're trading something with unusual range characteristics.

**Trading Logic That Makes Sense**

The setup requires a sweep first. Price makes a new high or low that takes out visible liquidity — usually above a prior swing high. The indicator marks this. The entry is not here. The trigger is the confirmation candle close, which flips the indicator into a shift state.

For longs: price sweeps below a swing low, then closes back above that low. That's the shift. The entry is on the confirmation close with a stop below the sweep low (or the candle low, whichever is tighter). The target is the next liquidity pool to the upside — often prior equal highs or a session high. For shorts, reverse it.

The logic aligns with how price actually moves. It's not a lagging moving average crossover; it's identifying where stop losses cluster and how price reacts when those stops get run. Combining it with a simple trend filter — only taking longs above a longer moving average and shorts below it — is a reasonable way to reduce counter-trend signals.

**Pros and Cons**

The honest breakdown:

*Pros:*
- Clear, actionable signals with confirmation built in
- Works across timeframes and asset classes
- Visual design is clean and doesn't clutter your chart
- Good at catching trend reversals early

*Cons:*
- Repainting is real and you need to understand it before trading
- In ranging markets, it will chop you up — no indicator fixes a flat market
- The confirmation filter means you miss the absolute bottom or top
- No alert functionality built into the base version (you'll need to set your own)

**Who Should Use This**

This is for traders who already understand liquidity concepts — smart money concepts, order blocks, sweep-and-reverse patterns. If you're just starting out, this might confuse more than help because the signals need context. You need to know what a swing high is, why liquidity pools matter, and how institutional orders move price.

It's also aimed at traders who are tired of lagging indicators. This one reacts to price action in near real-time. If you're a swing trader looking for entries at trend reversals, or a day trader who wants to align with higher-timeframe shifts, it's worth a look.

**Alternatives Worth Considering**

If the repainting bothers you, look at Smart Money Concepts by LuxAlgo — it provides similar liquidity detection without repainting, though it's more complex. For a simpler approach, the classic Supply Demand Zones indicator gives you the zones without the shift confirmation. And if you want pure trend without the liquidity angle, Supertrend combined with a momentum oscillator does a decent job.

**Frequently Asked Questions**

*Does this indicator repaint?* Yes. The sweep marker and shift signal can update as new candles form. It's designed that way to confirm shifts, not to give you perfect entries.

*What timeframe works best?* It functions on all of them. Very low timeframes generate more noise, and very high timeframes produce fewer signals, so the practical range sits somewhere in the middle depending on how frequently you want to trade.

*Can I use it for crypto?* Yes. Crypto's 24/7 market creates more liquidity sweeps than traditional markets, which means more signals — and more of them to filter.

*Does it work for scalping?* Possible, but the confirmation delay makes entries slower than pure price action scalping. You'll miss some moves.

**Final Verdict**

Liquidity_Shift_Detection is a solid structural tool. It won't make you a profitable trader by itself — nothing will — but it does one thing well: it identifies when liquidity gets swept and whether the shift is real. The repainting is a legitimate concern, but it's inherent to the indicator's logic. If you understand what you're looking at and pair it with proper risk management, this is one of the better structural indicators available on TradingView right now.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
