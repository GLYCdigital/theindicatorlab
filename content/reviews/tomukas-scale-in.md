---
title: "Tomukas_Scale_In Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/tomukas-scale-in.png"
tags:
  - tomukas scale in
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Scale into positions systematically with Tomukas_Scale_In. Honest review of its entry logic, risk management, and best settings for trend-following traders."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Tomukas_Scale_In is a position scaling tool for TradingView that automates the process of adding to a winning trade. It is not a buy/sell signal generator in the traditional sense—it does not predict reversals or trend changes. Instead, it is designed to help traders pyramid into positions as price moves in their favor, based on predefined levels or percentage increments.

The core idea is to reduce average entry price risk while letting winners run. The indicator plots entry zones and scale-in levels directly on the chart, so the trader is not manually marking where to add size.

**Key Features That Set It Apart**

- **Customizable Scale-In Levels:** The indicator supports multiple scaling tiers, defined either by percentage distance from initial entry or by fixed price intervals. This removes the need to manually mark levels.
- **Dynamic Position Size Display:** It shows suggested lot size or contract count for each tier based on account balance and risk percentage. Useful for traders who want strict risk management.
- **Visual Entry Zones:** The indicator paints colored bands showing where to add. Green for the first scale, blue for the second, and so on.
- **Trailing Stop Integration:** Optional trailing stop for each tier. This is uncommon for a scaling tool—most just show entries. It is intended to help lock profits on partial positions during pullbacks.

**Settings and How to Tune Them**

The indicator exposes several parameters, including scale count, scale increment, initial risk, and an optional trailing stop. The source material offers the following starting points:

- **Scale count:** 3 (fewer tiers reduce complexity; 5 is described as overkill for most retail traders)
- **Scale increment:** 2% (described as working well for trending markets like crypto; 1% for forex)
- **Initial risk:** 1% of account per full setup
- **Trailing stop:** Enable with a 0.5% trail for each tier

These are presented as a starting configuration, not as an optimal one. The default settings are described as too aggressive—specifically, a 5% increment default on a volatile stock is characterized as damaging to an account.

**How to Use It for Entries and Exits**

**Entry:** Wait for price to reach the first scale level (often a pullback or breakout retest). Enter with 50% of the intended total position. Then, if price moves to the second level, add 30%. At the third level, add 20%. The indicator marks these levels clearly.

**Exit:** Each tier gets its own stop loss. One approach is to set stops at 1.5x the scale increment below each entry. The trailing stop feature is intended to manage partial exits. For the final tier, a manual trendline break can serve as the exit trigger.

**Honest Pros and Cons**

**Pros:**
- Removes emotional guesswork from scaling
- Works well in strong trends; the visual bands support discipline
- Trailing stop integration is a genuine time-saver
- Lightweight—described as having no lag even on 1-minute charts

**Cons:**
- Useless in choppy or ranging markets. The indicator will signal entries that get stopped out immediately.
- No backtesting engine built-in. Historical testing must be done manually.
- Default settings are too aggressive. The 5% increment default on a volatile stock is described as account-wrecking.

**Who It's Actually For**

Trend-following traders who already have a strategy and need execution help. Swing traders and position traders will get the most value. Day traders may find the scale increments too slow—unless trading on higher timeframes.

Not for scalpers or reversal traders. If you fade moves, this tool will work against you.

**Better Alternatives If They Exist**

- **Pyramiding Strategy** (free, simpler): For basic scale logic, this is lighter.
- **Fractal Scale** (paid, more complex): Offers auto-optimization of scale levels based on volatility, but the interface is cluttered.
- **Manual scaling with Excel:** If you are only scaling twice, an indicator may not be necessary.

Tomukas_Scale_In sits in a middle ground—more features than free tools, less bloat than paid alternatives.

**FAQ Addressing Real Trader Questions**

**Q: Does it work on crypto?**
A: Yes. It is described as working best on daily or 4-hour charts.

**Q: Can I use it with futures?**
A: Yes, it supports contracts. Contract size is set in the settings.

**Q: Does it repaint?**
A: No. Levels are based on current price, not future data.

**Q: Can I automate with it?**
A: No, it is manual only. No alert or API integration.

**Final Verdict with Star Rating**

Tomukas_Scale_In is a practical tool for trend traders who want systematic scaling without the mental overhead. It is not a magic bullet—bad market conditions will expose its weaknesses—but for its intended use, it delivers.

**Rating: ⭐⭐⭐⭐ (4/5)**

One star off for no backtesting and poor defaults. But if you adjust the settings and use it in trending markets, it is a solid 4-star addition to your toolkit.

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
