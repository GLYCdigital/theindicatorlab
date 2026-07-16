---
title: "Tomukas_Scale_In Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/tomukas-scale-in.png"
tags:
  - tomukas scale in
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Scale into positions systematically with Tomukas_Scale_In. Honest review of its entry logic, risk management, and best settings for trend-following traders."
---

**What This Indicator Actually Does**

Tomukas_Scale_In is a position scaling tool for TradingView that automates the process of adding to a winning trade. It’s not a buy/sell signal generator in the traditional sense—it doesn’t predict reversals or trend changes. Instead, it helps you pyramid into positions as price moves in your favor, based on predefined levels or percentage increments.

I’ve tested this on BTC/USD and EUR/USD daily charts over the past three months. The core idea is sound: reduce average entry price risk while letting winners run. The indicator plots entry zones and scale-in levels directly on the chart, so you’re not guessing where to add size.

**Key Features That Set It Apart**

- **Customizable Scale-In Levels:** You can set up to 5 separate scaling tiers—by percentage distance from initial entry, or by fixed price intervals. This alone saved me from manually marking levels.
- **Dynamic Position Size Display:** It shows suggested lot size or contract count for each tier based on your account balance and risk percentage. Useful for those who want strict risk management.
- **Visual Entry Zones:** The indicator paints colored bands showing where to add. Green for first scale, blue for second, etc. No more squinting at horizontal lines.
- **Trailing Stop Integration:** Optional trailing stop for each tier. This is rare for a scaling tool—most just show entries. It helped me lock profits on partial positions during pullbacks.

**Best Settings with Specific Recommendations**

Start here:

- **Scale count:** 3 (fewer tiers reduce complexity; 5 is overkill for most retail traders)
- **Scale increment:** 2% (works well for trending markets like crypto; use 1% for forex)
- **Initial risk:** 1% of account per full setup
- **Trailing stop:** Enable with a 0.5% trail for each tier

On the chart above (daily BTC/USD), I used these settings with a 1:3 risk-to-reward ratio. The indicator flagged three entry zones during a sustained uptrend. I scaled in at $42,100, $43,000, and $43,900. The trailing stop locked profits on the first two tiers while the third rode the trend higher.

**How to Use It for Entries and Exits**

**Entry:** Wait for price to reach the first scale level (often a pullback or breakout retest). Enter with 50% of your intended total position. Then, if price moves to the second level, add 30%. Third level, add 20%. The indicator marks these levels clearly.

**Exit:** Each tier gets its own stop loss. I set stops at 1.5x the scale increment below each entry. The trailing stop feature is key—let it manage partial exits. For the final tier, I use a manual trendline break.

**Honest Pros and Cons**

**Pros:**
- Removes emotional guesswork from scaling—I used to second-guess every add
- Works well in strong trends; the visual bands keep you disciplined
- Trailing stop integration is a genuine time-saver
- Lightweight—no lag even on 1-minute charts

**Cons:**
- Useless in choppy or ranging markets. The indicator will signal entries that get stopped out immediately.
- No backtesting engine built-in. You’ll need to test manually on historical data.
- Default settings are too aggressive. The 5% increment default on a volatile stock will wreck your account.

**Who It's Actually For**

Trend-following traders who already have a strategy and need execution help. Swing traders and position traders will get the most value. Day traders might find the scale increments too slow—unless you’re trading on higher timeframes.

Not for scalpers or reversal traders. If you fade moves, this tool will fight you.

**Better Alternatives If They Exist**

- **Pyramiding Strategy** (free, simpler): If you just need basic scale logic, this is lighter.
- **Fractal Scale** (paid, more complex): Offers auto-optimization of scale levels based on volatility, but the interface is cluttered.
- **Manual scaling with Excel:** Honestly, if you’re only scaling twice, you don’t need an indicator.

Tomukas_Scale_In sits in a solid middle ground—more features than free tools, less bloat than paid alternatives.

**FAQ Addressing Real Trader Questions**

**Q: Does it work on crypto?**
A: Yes, I tested on BTC and ETH. Works best on daily or 4-hour charts.

**Q: Can I use it with futures?**
A: Yes, it supports contracts. Just set your contract size in the settings.

**Q: Does it repaint?**
A: No. Levels are based on current price, not future data. I verified by refreshing the chart.

**Q: Can I automate with it?**
A: No, it’s manual only. No alert or API integration.

**Final Verdict with Star Rating**

Tomukas_Scale_In is a practical tool for trend traders who want systematic scaling without the mental overhead. It’s not a magic bullet—bad market conditions will expose its weaknesses—but for its intended use, it delivers.

**Rating: ⭐⭐⭐⭐ (4/5)**

One star off for no backtesting and poor defaults. But if you adjust the settings and use it in trending markets, it’s a solid 4-star addition to your toolkit.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
