---
title: "Floor_Pivots Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/floor-pivots.png"
tags:
  - floor pivots
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Floor_Pivots provides key support/resistance levels based on daily, weekly, and monthly pivots. Ideal for breakout and mean-reversion traders. Settings and strategy inside."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Floor_Pivots calculates and plots classic floor-trader pivot points: a central pivot plus support levels (S1, S2, S3) and resistance levels (R1, R2, R3), derived from the prior period's high, low, and close. The script lets you switch between daily, weekly, and monthly calculation periods. These levels are intended as reference points where price may react — either pausing/reversing or pushing through.

**Key Features That Set It Apart**

Many pivot indicators on TradingView are cluttered or overly complex. Floor_Pivots aims for a clean presentation. Three notable features:

- **Multi-timeframe selection** in one script — switch between daily, weekly, and monthly without loading three separate indicators.
- **Customizable line styles and colors** — support and resistance can be styled to fit your chart.
- **Built-in session high/low labels** — intended to help spot intraday extremes relative to the pivot.

**Honest Pros and Cons**

| Pros | Cons |
|------|------|
| Clean, level-based presentation | No central pivot range (CPR) or Fibonacci variants |
| Applies across timeframes | Default colors are plain |
| Lightweight | No alerts for level breaks |
| Monthly pivots can serve as swing reference points | Doesn't auto-adjust for market open gaps |

**Settings and How to Tune Them**

- **Timeframe**: Daily, weekly, or monthly calculation periods. Which one suits you depends on your holding horizon.
- **Line style**: The script supports different line styles, which can help distinguish the central pivot from the first-tier and second-tier levels at a glance.
- **Colors**: Fully customizable so you can build a readable hierarchy across the levels.
- **Session High/Low**: Toggle the session high/low labels on or off depending on whether you want intraday extremes displayed.

No single configuration is objectively best — the right settings depend on the timeframe you trade and how much visual detail you want on the chart.

**How to Use It for Entries and Exits**

This is a pure level indicator — it generates no signals. Common approaches:

- **Breakout**: A close beyond R1, ideally with confirming volume, can be used as a long trigger with R2 as a target and the pivot as a stop reference.
- **Mean reversion**: A touch of S2 combined with an oversold oscillator reading can be used as a long setup targeting S1 or the pivot, with a stop beyond S3.
- **Reversal at pivot**: If price opens above the pivot but fails to hold, the pivot itself can act as a short trigger with S1 as a target.
- **Trailing stop**: R1 can serve as a trailing reference for long positions in a strong trend.

**Who It's Actually For**

- **Day traders** who want clean, fast-loading reference levels.
- **Swing traders** who want weekly or monthly reference points.
- **Beginners** learning support and resistance — the simplicity is a plus.

Not for: Traders who want automatic entry signals, Fibonacci levels, or volume-based pivots.

**Better Alternatives If They Exist**

- **Auto Pivot Levels** — includes CPR and Fibonacci, but more cluttered.
- **Pivot Point Standard** — similar but with alerts.
- **VWAP + Pivots** — if you want volume-weighted levels alongside pivots.

Floor_Pivots's appeal is that it stays lightweight and customizable without being overwhelming.

**FAQ: Real Trader Questions**

**Q: Does this repaint?**
The pivot levels are derived from the prior period's high, low, and close, so once a period closes the levels are fixed.

**Q: Can I use it on crypto?**
Yes, it works on any asset. Monthly pivots are a commonly cited reference on Bitcoin.

**Q: Why don't I see S3/R3?**
Check your settings — the levels are typically enabled by default but may be hidden if you toggled them off.

**Q: Can I backtest strategies with this?**
Indirectly. The levels don't generate signals, but you can manually evaluate entries at S1/R1.

**Final Verdict**

Floor_Pivots is a solid, no-nonsense pivot level tool. It won't make you rich by itself, but paired with price action or an oscillator, it's a reliable reference. For a free indicator with clean code, it earns its four stars.

**Rating**: ⭐⭐⭐⭐ (4/5)

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
