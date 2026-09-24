---
title: "Auto_Pitchfork Trade Levels AFD Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/auto-pitchfork-trade-levels-afd.png"
tags:
  - "auto pitchfork trade levels afd"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Auto_Pitchfork_Trade_Levels_Afd review: an honest look at this automated Pitchfork trend indicator, the settings that matter, and how to trade it."
tv_script_url: "https://www.tradingview.com/script/qaZnLWji-Auto-Pitchfork-Trade-Levels-AFD/"
---
Andrew's Pitchfork used to be a manual chore. You'd eyeball three pivots, drag the tines around, and inevitably second-guess whether you picked the right swing points. Auto_Pitchfork_Trade_Levels_Afd does the pivot-picking for you and draws the fork, the median line, and a set of trade levels automatically. That's the whole pitch, and it mostly delivers.

This is a trend tool, not a signal generator. It doesn't tell you to buy or sell. It tells you where price sits relative to a structured channel — and that distinction matters a lot when you decide whether to keep it on your chart.

## What it actually does

The indicator scans price for pivot highs and lows, selects a dominant swing sequence, and projects a three-tine pitchfork from it. From there it plots what the name promises: trade levels — typically the median line, the outer parallel tines, and intermediate warning lines where reactions tend to happen.

As shown in the chart above, the fork anchors to a clean impulse leg and fans outward. Price respects the median line surprisingly often, and the outer tines act as the "don't chase here" zones. If you've traded manual forks, the behavior will feel familiar — you just skip the drawing step.

The auto-selection is the real feature. On liquid instruments with clear swings (think EURUSD on 4H, ES on 15m), it picks sensible anchors. On choppy, ranging messes, it picks garbage. More on that below.

## Settings that actually matter

I tested this across timeframes and settled on a configuration that keeps it useful without turning the chart into spaghetti.

**Pivot lookback / sensitivity.** This is the one dial that changes everything. Lower values make the fork snap to every minor wiggle and redraw constantly. Higher values produce a stable fork that holds its shape for dozens of bars. I'd start at a lookback that captures the last 5–10 significant swings on your timeframe and leave it there.

**Show median line.** Always on. The median line is the tradeable feature. Without it you're just looking at a decorative channel.

**Show outer tines.** On, but treat them as context, not entries.

**Show trade levels / warning lines.** Useful on higher timeframes (4H+). On the 5-minute it adds clutter for marginal value.

**Extend fork right.** Enable it if you're trading the current structure. Disable it if you only want historical context.

The biggest complaint I have: there's no clean "lock the fork" option. When a new pivot forms, the whole thing can shift. That's inherent to any auto-pitchfork, but a manual override would make this a 5-star tool.

## How to trade it

The logic is straightforward once you accept the fork is a map, not a trigger.

- **Trend continuation:** In an uptrend, buy pullbacks into the median line or the lower tine, ideally with a rejection candle. Stop goes below the tine. Target the upper tine.
- **Trend reversal watch:** When price breaks and closes beyond the outer tine, the structure that generated the fork is failing. That's your cue to stop trusting the fork, not to fade it blindly.
- **Median line as the bias gauge:** Price above the median line = bullish bias. Below = bearish. This alone is a decent filter for other strategies you already run.

Pair it with a momentum read — RSI divergence into an outer tine, or a MACD cross back toward the median — and the win rate improves noticeably. The fork on its own is directional context. The fork plus confirmation is a system.

## Pros and cons

**Pros:**
- Removes the subjectivity of drawing pitchforks manually
- Median line and tines are genuinely useful reaction zones
- Works well on trending FX pairs and index futures
- Clean, uncluttered default output
- Free and lightweight on the chart

**Cons:**
- Auto pivot selection is unreliable in ranging or news-driven chop
- The fork can redraw when new pivots form — no lock feature
- No alerts built in for tine touches or median crosses
- "Trade levels" are somewhat generic; not instrument-specific
- No multi-timeframe awareness

## Who it's for

Discretionary trend traders who already think in channels and want automation to handle the drawing. If you trade breakouts of structure, pullbacks to dynamic support, or you're learning pitchfork theory, this is a solid training-wheels-plus tool. Scalpers on the 1-minute will find it too twitchy. Pure indicator-signal traders who want buy/sell arrows should look elsewhere.

## Alternatives

If you want a pitchfork with manual anchor control, the built-in **Pitchfork** drawing tool plus a pivot indicator gives you more precision. For automated trend channels, **Linear Regression Channel** or **Auto Trendlines** scratch a similar itch. If you specifically want trade levels with alerts, a **Pivot Points**-based script will fire notifications this one won't.

## FAQ

**Does it repaint?** The fork redraws when new pivots qualify. Historical tine touches don't vanish, but the projection can shift. Treat the current fork as provisional until the anchor leg is confirmed.

**Which timeframe is best?** 4H and Daily for swing trading, 15m for intraday on liquid instruments. Avoid below 5m.

**Can I get alerts?** Not natively. You'd need to add alert conditions manually or use it alongside an alert-capable script.

**Does it work on crypto?** Yes, but only on pairs with clean swing structure. Low-cap altcoins produce noise forks.

**Is it a buy/sell signal?** No. It's context. You supply the trigger.

## Final verdict

Auto_Pitchfork_Trade_Levels_Afd does one job well: it turns a fiddly manual drawing exercise into a consistent, automatic overlay. The median line and outer tines are tradeable, and on trending markets the tool earns its chart space. It stumbles on chop, lacks alerts, and the redraw behavior will annoy precision traders — but for the price of free and a few minutes of setup, it's a worthwhile addition to a trend-following toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)** — Solid, useful, and honest about what it is. A lock feature and alerts would make it essential.
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
