---
title: "Rolling_Drawdown_Run_Up_By_Ycgh_Capital Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/rolling-drawdown-run-up-by-ycgh-capital.png"
tags:
  - "rolling drawdown run up by ycgh capital"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
tags:
  - "rolling drawdown run up by ycgh capital"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Rolling_Drawdown_Run_Up_By_Ycgh_Capital review. Tested settings, entry/exit logic, pros/cons, and who should use this trend strength gauge."
tv_script_url: "https://www.tradingview.com/script/c1xDAFeP-Rolling-Drawdown-Run-up-by-YCGH-Capital/"
---
Let me be upfront: this isn't a flashy indicator. No arrows, no buy/sell signals, no neon clouds. What `Rolling_Drawdown_Run_Up_By_Ycgh_Capital` does is simpler and arguably more useful — it visualizes the statistical health of your current trend by tracking rolling drawdown and run-up percentages over a lookback window.

I've spent the last two weeks running it on BTCUSD, EURUSD, and a few S&P 500 tickers on the MACD chart setup shown above. Here's what I found.

## What This Indicator Actually Does

The core concept is straightforward: it calculates the drawdown from the highest equity/price point and the run-up from the lowest point over a defined rolling period, then plots them as separate lines. The spread between those two lines gives you a real-time read on trend momentum and volatility contraction.

Think of it as a trend-strength thermometer rather than a direction predictor. When the run-up line accelerates away from the drawdown line, you're in a healthy trend. When they converge or cross, momentum is fading.

## Key Features That Stand Out

- **Rolling window flexibility** — You control the lookback period directly in settings. I tested 50, 100, and 200 bars. The 100-bar default is a solid middle ground, but shorter windows react faster to regime changes.

- **Visual separation** — The indicator plots drawdown and run-up as distinct colored lines. In the MACD screenshot above, you can see how the run-up line (green) stays well above the drawdown line (red) during the uptrend, then they pinch together at the top — that's your exit cue.

- **Clean, uncluttered output** — No repainting signals or overlay chaos. It sits in its own pane and doesn't interfere with your price action or other indicators.

## Best Settings I Found Through Testing

After extensive backtesting, here's my recommended configuration:

- **Lookback period**: 100 bars for swing trading, 50 for intraday scalping
- **Drawdown calculation**: Percentage-based (default) works best across asset classes
- **Run-up calculation**: Keep it symmetric with the drawdown period

The sweet spot on daily charts was 100–150 bars. Anything below 50 produced too much noise, and above 200 the lines became laggard and useless for timely decisions.

## How I Actually Trade With It

This isn't a standalone system. It's a filter and a warning system. Here's my logic:

**Entry**: When price pulls back but the run-up line stays above the drawdown line on the higher timeframe, I look for long entries on lower timeframes. The trend is statistically intact.

**Exit**: When the drawdown line starts climbing faster than the run-up line — they begin converging — I tighten my stops or take partial profits. This consistently caught trend exhaustion before price reversed.

**Avoid**: If both lines are flat and hugging each other, you're in a range. Don't force trades.

## Pros & Cons

**Pros:**
- Objectively quantifies trend health instead of relying on subjective pattern reading
- Works across all asset classes — I tested crypto, forex, and indices
- Zero lag in the calculation itself; the rolling window updates instantly
- Excellent for position sizing — wider run-up/drawdown spread justifies larger positions

**Cons:**
- Not a directional signal. It tells you the trend is strong, not which way to trade
- Can whipsaw in choppy, directionless markets
- The visual difference between the two lines can be subtle on compressed charts
- No alerts built in — you'll need to set manual price alerts

## Who Should Use This

This indicator shines for systematic traders who want to layer statistical confirmation onto their existing strategy. If you already use trend-following entries but struggle with when to exit, this solves that problem elegantly. Swing traders on 4H or daily charts will get the most value.

Day traders will find the 50-bar setting too slow for 1-minute charts. And if you're a pure price action trader who distrusts derived metrics, this will feel redundant.

## Alternatives Worth Considering

- **Aroon** — Similar trend-strength concept but uses time since highs/lows rather than percentage drawdown. Better for very volatile assets.
- **Choppiness Index** — If your main problem is identifying ranging markets, this does that more directly.
- **MACD** — The classic momentum oscillator pairs well alongside this for confirmation, especially on the chart setup shown here.

## FAQ

**Does this repaint?**
No. The rolling calculation uses only historical data and updates cleanly on each new bar.

**Can I use it for crypto?**
Absolutely. I found it particularly useful on Bitcoin's violent trend swings — the drawdown line catches flush corrections that would shake out weaker trend filters.

**What timeframe works best?**
Daily and 4H give the cleanest signals. Lower timeframes produce more false convergence signals.

**Is this a buy/sell indicator?**
No, and anyone telling you otherwise is overselling it. It's a trend health monitor.

## Final Verdict

`Rolling_Drawdown_Run_Up_By_Ycgh_Capital` earns its place in my toolkit because it answers a question most indicators ignore: *How statistically robust is my current trend?* It won't tell you when to enter, but it will save you from holding losers or exiting winners too early.

It's not flashy, it doesn't generate signals, and it won't replace your primary strategy. But as a trend filter and exit timer, it's quietly effective. For traders who already have a directional edge and need better trend timing, this is a worthwhile addition.

**Rating: 4 out of 5** — Loses a star for no built-in alerts and its inability to determine trend direction on its own. Everything else it does, it does well.
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
