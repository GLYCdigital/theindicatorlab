---
title: "Zig_Zag_Indicator Review: Settings, Strategy & How to Use It"
date: 2026-08-09
draft: false
type: reviews
image: "/screenshots/zig-zag-indicator.png"
tags:
  - "zig zag indicator"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Zig_Zag_Indicator review: settings, swing trading strategy, pros & cons. Is this classic pivot detector worth adding to your chart?"
---
Let's cut the preamble. The Zig Zag indicator is one of the oldest tools in technical analysis, and this TradingView version does exactly what you'd expect—no more, no less. It filters out noise and draws clean pivot lines between significant highs and lows. If you've used any Zig Zag in the past, you know the drill: it's not predictive, it repaints, and it's only as good as your settings. But this specific implementation gets a few things right that make it worth a second look.

## What This Indicator Actually Does

The Zig Zag connects swing points with straight lines, using a percentage threshold (or absolute deviation) to determine what counts as a "significant" move. Set it to 5%, and it ignores everything smaller than that. Set it to 10%, and you get fewer, more meaningful swings. The logic is embarrassingly simple—and that's precisely why it still works.

What sets this version apart from the default TradingView Zig Zag is the level of control. You can toggle between percentage-based and price-based deviation, adjust the calculation source (close, high/low, or any custom source), and choose whether to extend the last leg. There's also a useful "show only last pivot" option that keeps your chart clean when you're focused on the current structure.

## Best Settings That Actually Work

I tested this across BTCUSD, EURUSD, and a few S&P 500 ETFs on multiple timeframes. Here's what performed best:

- **Deviation type:** Percentage (default) works fine for crypto and forex. Use absolute price deviation for indices or stocks where percentages get weird on high-priced symbols.
- **Deviation value:** Start at 5% for intraday, 7–10% for daily swings. Too tight (under 3%) and you're just drawing noise. Too loose (over 15%) and you'll miss the setup entirely.
- **Source:** Close for most cases. If you want to catch extreme wicks, use high/low—but be prepared for more whipsaw.
- **Show only last pivot:** Turn this ON when you're actively trading. The full history is useful for analysis, but it clutters the chart fast.

## How to Actually Trade With It

Here's the thing about Zig Zag: it's not a standalone system. It's a structural framework. The way I use it, and the way I'd recommend you use it too, is as a confirmation tool alongside price action or an oscillator.

**Swing trading approach:** Wait for the Zig Zag to print a higher high, then a higher low. That's your uptrend confirmation. Enter on the next breakout above the pivot high, place your stop below the most recent Zig Zag low. For exits, trail your stop under each new higher low the indicator prints. Simple, mechanical, and it removes the emotional guesswork.

**The repaint warning:** The last pivot is always unconfirmed. The indicator will redraw that final line until price moves enough to confirm or invalidate it. That's not a bug—it's the nature of the tool. Never place an entry based solely on the most recent unconfirmed pivot. Wait for the next candle to close, or use a secondary confirmation like RSI divergence.

## Pros & Cons

**Pros:**
- Clean, minimal interface—no indicator overload
- Fully customizable deviation settings
- The "extend last leg" option is genuinely useful for projecting targets
- Works on any timeframe and any market

**Cons:**
- Repaints by design. This is a dealbreaker for some traders, and they're right to be cautious
- Not predictive. It tells you what already happened, not what comes next
- The default settings are too sensitive for most daily charts—you'll need to dial them in
- No built-in alerts for pivot confirmations, which is a missed opportunity

## Who It's For

This is a swing trader's tool. If you're holding positions for days or weeks and need a clean visual map of market structure, this will serve you well. Day traders will find it less useful—the lag from the deviation filter eats into the speed you need. Scalpers should skip it entirely; by the time a pivot confirms, the move is over.

It also suits traders who understand that technical analysis is about probabilities, not certainties. If you need an indicator that tells you exactly when to buy and sell, keep scrolling.

## Alternatives Worth Considering

If repainting drives you crazy, look at **Fractal Zig Zag** or **ZigZag Pro**—they use fractal-based pivots that confirm faster. For a more complete trend system, pair this with a moving average crossover or **Supertrend** instead of relying on it alone. And if you want the same structure concept but with more advanced features, **Auto Fib Retracement** tools built on Zig Zag logic give you the same pivots with Fibonacci levels overlaid.

## FAQ

**Does the Zig Zag indicator repaint?**
Yes. The final pivot is unconfirmed until price moves enough to validate it. This is inherent to the calculation, not a flaw in this particular version.

**What's the best timeframe for Zig Zag?**
The daily and 4-hour charts give the cleanest swing signals. Anything lower than 15 minutes produces too many false pivots.

**Can I use Zig Zag for automated trading?**
Technically yes, but the repainting makes it risky for live automation. Backtesting with it is also misleading unless you account for the redraw delay.

## Final Verdict

This Zig Zag implementation is a solid, dependable version of a classic tool. It doesn't reinvent the wheel, but it doesn't need to. The customization options are thoughtful, the interface is clean, and it does exactly what a Zig Zag should do. It's not going to make you money by itself—no indicator will—but as a structural map for your swing trading, it earns its place on your chart.

Four stars. Not exceptional, but reliable, honest, and useful. That's more than most indicators can claim.

**Rating: ⭐⭐⭐⭐**
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
