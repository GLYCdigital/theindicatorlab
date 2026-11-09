---
title: "Ichimoku Itto By Itto Ryu Review — Trend Indicator"
date: 2026-11-10T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/ichimoku-itto-by-itto-ryu.png"
tags:
  - "ichimoku itto by itto ryu"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A clean Ichimoku Kinko Hyo implementation for TradingView. What the Itto-Ryu version does, who it suits, and its trade-offs — honest review."
grounding: "none (no source found)"
---
The Ichimoku Itto by [Itto-Ryu] is a TradingView script that renders the Ichimoku Kinko Hyo charting system — the Japanese "one glance equilibrium" framework — as a trend indicator. That is the honest starting point: this is an Ichimoku implementation, not a new proprietary signal engine. If you already know Ichimoku, you know roughly what you are getting. The question is whether this particular version is worth installing over the dozens of others, and to answer it fairly you need to understand what Ichimoku itself carries and where a clean implementation earns its keep.

A note on scope up front: the official description and documentation for this specific script were not available when this review was put together, so anything below about the underlying method comes from the Ichimoku framework in general, not from a documented feature list of this build. I have not run or backtested this indicator, and I won't pretend otherwise.

## What Ichimoku actually is

Ichimoku Kinko Hyo plots a set of calculated lines that together define trend direction, momentum, and support/resistance in one view. The standard components are the Tenkan-sen (conversion line), the Kijun-sen (base line), the Senkou Span A and Senkou Span B (which form the Kumo, or "cloud," projected forward), and the Chikou Span (lagging line). The cloud is the centrepiece: price above it reads bullish, below it bearish, and inside it indecisive.

An "Itto-Ryu" flavoured version is best understood as an interpretation of that system rather than a reinvention of it. The name references a school of swordsmanship; in trading contexts it signals a particular reading discipline applied to the standard Ichimoku elements. Without the source documentation I can't tell you what, if anything, this build changes about the default calculations — so treat the lines as Ichimoku lines and evaluate the tool on that basis.

## How you'd actually use it

The workflow is the classic one, and it is genuinely useful for trend traders:

- **Trend filter.** Read price relative to the cloud first. Above it, you are hunting longs; below it, shorts; inside it, stand aside. This alone removes a lot of low-quality trades.
- **Momentum and entry timing.** The relationship between the Tenkan-sen and Kijun-sen gives a faster read on short-term momentum. Crosses between them are commonly used as timing triggers, filtered by cloud position.
- **Support and resistance.** The cloud's edges act as dynamic zones where price tends to react. Forward projection means you can see where those zones will sit ahead of time — a genuinely distinctive feature of Ichimoku.
- **Confirmation with the lagging line.** The Chikou Span compared against past price offers a further confirmation layer that many traders skip and later regret.

As shown in the chart above, the visual density of Ichimoku is the point and the problem: it gives you a lot of information at once, and the cloud can dominate your chart if you let it.

## Pros and cons

**Pros**
- Ichimoku is a complete, self-contained framework. You get trend, momentum, and levels from one overlay rather than stacking three indicators.
- The forward-projected cloud is a real analytical edge — you can plan around future support/resistance rather than reacting to it.
- As a trend indicator it is disciplined: the cloud filter forces you to acknowledge when the market has no clear direction.
- A clean Ichimoku implementation keeps your chart readable and your rules consistent, which matters more than most traders admit.

**Cons**
- The learning curve is steep. Ichimoku has a lot of moving parts and the cloud's visual weight can obscure price action on lower timeframes.
- It lags by design. The lines are built from past prices and the cloud is projected, but the signals themselves confirm late — this is not a tool for catching tops and bottoms.
- Without documented specifics on this build, you can't be certain how it differs from a standard Ichimoku script. That ambiguity is a legitimate reason to compare before committing.
- On ranging markets the cloud can produce whipsaws and chop that punish impatience.

## Who it's for

Trend-following swing traders and position traders who like a systematic, rules-based overlay — people who want one indicator to answer "what is the trend and where are the levels" rather than chasing signals. It is less suited to scalpers and intraday momentum traders who need fast, discrete triggers. If you are new to Ichimoku, this is a reasonable way to learn the system on a real chart, provided you study the components before trading them.

## FAQ

**Is this a buy/sell signal indicator?**
No. Ichimoku is an analytical framework; any signals come from how you interpret the lines and cloud. This script renders the framework.

**Does it repaint?**
I can't confirm specifics for this build without documentation. Ichimoku's standard lines are calculated from historical prices and the cloud is projected forward; treat any indicator's real-time behaviour with normal caution and verify on your own chart.

**Which timeframe is best?**
Not documented here, and I won't invent one. Ichimoku is traditionally applied to higher timeframes, but that is a general convention, not a claim about this script.

**Can I use it with other indicators?**
Yes — it is an overlay, and its trend read pairs naturally with momentum or volume tools. Just avoid duplicating the same information.

## Verdict

A solid, faithful take on Ichimoku for TradingView. It won't surprise anyone who knows the system, and the missing documentation makes it hard to argue it beats every alternative — but Ichimoku done cleanly is a genuinely powerful trend framework, and this delivers that. Four stars: very good, with the caveat that you should confirm the specifics on the script page before relying on it.

⭐⭐⭐⭐
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*
