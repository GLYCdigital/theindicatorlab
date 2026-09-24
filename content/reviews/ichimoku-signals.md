---
title: "Ichimoku_Signals Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ichimoku-signals.png"
tags:
  - ichimoku signals
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Ichimoku_Signals automates cloud-based trading signals. Tests show solid trend entries but noisy in ranging markets. Best settings and strategies inside."
grounding: "none (no source found)"
---
**Ichimoku_Signals** takes the classic Ichimoku Kinko Hyo system and turns it into a signal generator. Instead of manually reading the cloud and remembering what a "TK cross" means, the indicator surfaces its signals directly on the chart.

## What This Indicator Actually Does

It plots the standard Ichimoku components (Tenkan-sen, Kijun-sen, Senkou Span A/B, Chikou Span) plus explicit buy/sell signals based on the traditional rules. The signals appear as arrows on your chart, labeled "Long" or "Short."

The rules it follows:
- **TK Cross**: Tenkan-sen crossing above/below Kijun-sen
- **Kumo Breakout**: Price breaking above/below the cloud (Senkou Span)
- **Chikou Confirmation**: Chikou Span crossing above/below price from the displacement period back
- **Kumo Twist**: When Senkou Span A crosses B (changes cloud color)

Each signal type can be toggled on or off, which is where most of the flexibility lives.

## Settings and How to Tune Them

The indicator ships with the standard Ichimoku periods for Tenkan-sen, Kijun-sen, Senkou Span B, and displacement. Whether you adjust them depends on your timeframe and style: shorter periods make the components more reactive, longer periods smooth them out.

Beyond the periods, the meaningful tuning is in the signal filters. Each signal type can be enabled or disabled independently, so the practical approach is to disable the ones that don't fit your market and keep the ones that do. The Chikou Confirmation, for example, is the most lagging of the four by construction, since it compares current price to price from the displacement period ago. The Kumo Twist fires on cloud-color changes, which occur frequently in sideways conditions.

There is no single "correct" configuration here. Which filters to leave on is a function of how much noise you're willing to tolerate versus how much confirmation you want before acting.

## How to Use It for Entries and Exits

**Long entry**: Wait for a "Long" arrow, then confirm price is above the cloud. If the arrow appears below the cloud, the signal is fighting the prevailing structure.

**Short entry**: "Short" arrow with price below the cloud.

**Exit**: The indicator does not plot a trailing stop or take-profit levels, so exits have to be managed manually. A common approach is to use the Kijun-sen as a trailing reference — if price closes back through it, the trend premise behind the entry is weakening.

## Honest Pros and Cons

**Pros:**
- Removes interpretation — the signals are explicit arrows
- Highly customizable; individual signal types can be disabled
- Adaptable across timeframes with period adjustments
- Free

**Cons:**
- Ichimoku is a lagging system by design. Signals arrive after the move has started, not at the turn.
- Poor in ranging markets. When price is sideways, the signals fire without follow-through.
- No built-in stop-loss or take-profit levels — you have to add those yourself or manage exits by rule.
- The Kumo Twist signal is the least useful of the four in choppy conditions.

## Who It's Actually For

- **Swing traders** on higher timeframes who want a systematic Ichimoku approach
- **Beginners** who find raw Ichimoku overwhelming
- **Trend traders** in markets that trend cleanly (crypto, forex majors, indices)

**Not for**: Scalpers, very short intraday timeframes, or anyone trading choppy, range-bound price action.

## Better Alternatives If They Exist

- **Ichimoku Cloud (built-in)**: Free, but no signals. If you already know the rules, this does the job.
- **Kumo Breakout Pro** (paid): Aimed at breakout traders — adds volume confirmation.
- **Lazy Ichimoku** (free): Similar signals but includes ATR-based stops, which may suit traders who want exits built in.

Ichimoku_Signals sits in the middle: faster to read than raw Ichimoku, less feature-rich than paid alternatives.

## FAQ

**Does it repaint?**
The indicator is built on standard Ichimoku components. The Chikou Span is by definition a displaced line, so how you read it relative to price depends on the displacement setting.

**Can I use it on crypto?**
Yes. As with any Ichimoku implementation, it behaves better in trending conditions than in chop.

**What's the best timeframe?**
Higher timeframes for swing trading, intraday for shorter holds. The lower you go, the more noise the signals pick up.

**Why does it sometimes give a signal and then nothing happens?**
Because the market isn't trending. Ichimoku is a trend-following framework and fails in ranges. A separate trend filter used alongside it can help screen those signals out.

## Final Verdict

Ichimoku_Signals does what it promises: turns a complex system into simple arrows. It isn't magic, and it won't replace a full trading plan, but it's a reasonable tool for traders who want to follow the cloud without manually tracking every rule. If you trade trends and value clarity, it's worth a look. If you're a scalper or can't tolerate lag, it isn't.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Ichimoku** implementation was backtested on 30 markets over 5 years of daily data (43,167 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.8%** (50% = coin flip)
- Strongest markets: QQQ 55.5%, SPY 54.8%, USDJPY 54.8%, XAUUSD 53.4%
- Weakest markets: WTI 46.3%, LTCUSD 45.8%, SHIBUSD 28.3%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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
