---
title: "Guppy Multiple Moving Average Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/guppy-multiple-moving-average.png"
tags:
  - guppy multiple moving average
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Guppy Multiple Moving Average on TradingView: settings, strategy, and real trades. A 4/5 review from a trader who's used it for trend shifts."
---

**Guppy Multiple Moving Average Review: Settings, Strategy & How to Use It**

I’ve been trading with moving averages for years, and the Guppy Multiple Moving Average (GMMA) is one of those rare indicators that actually makes you *think* about market structure rather than just blindly following lines. It’s not perfect, but it’s earned its place in my toolkit. Here’s my honest take after weeks of testing it on TradingView.

## What This Indicator Actually Does

The GMMA plots two groups of exponential moving averages (EMAs) on your chart: a **short-term group** (usually 3, 5, 8, 10, 12, 15) and a **long-term group** (30, 35, 40, 45, 50, 60). The idea is simple: the short-term group represents traders, the long-term group represents investors. When they converge, you’re looking at indecision. When they diverge, you’re seeing conviction.

Don’t let the simplicity fool you—this isn’t a laggy mess like a single moving average. The multiple layers give you a visual “compass” for trend strength.

## Key Features That Set It Apart

- **Trend strength gauge**: The distance between the two groups tells you if a move has legs. Tight = consolidation. Wide = strong trend.
- **Early reversal signals**: When the short-term group crosses through the long-term group, you get a heads-up *before* price confirms. This is the real edge.
- **Customizable EMAs**: You can adjust the periods and even switch to SMAs if you prefer. I keep the defaults—they’re well-tested.

## Best Settings with Specific Recommendations

I’ve tested dozens of combinations. Here’s what works:

- **Timeframe**: 1-hour or 4-hour. Anything lower and you get too much noise. Daily works for swing trading.
- **EMA periods**: Stick with the default (3,5,8,10,12,15 for short; 30,35,40,45,50,60 for long). They’re based on Guppy’s original research. Don’t mess with them unless you have a strong reason.
- **Color scheme**: Make short-term EMAs blue and long-term ones red. The visual contrast matters when you’re scanning multiple charts.

Pro tip: Overlay it on a clean chart—no other indicators. The GMMA is already busy enough.

## How to Use It for Entries and Exits

**Long entries**:
1. Wait for the short-term group to compress tightly (convergence).
2. Look for price to break above the long-term group.
3. Enter when the short-term group starts to expand away *above* the long-term group. That’s the “green light.”
4. Place your stop just below the nearest long-term EMA (typically the 30).

**Short entries**:
Reverse the logic—short-term group compresses below the long-term group, then expands downward.

**Exits**:
Exit when the short-term group compresses again. That means momentum is fading. Don’t wait for a full cross—by then, you’ve given back half your profit.

## Honest Pros and Cons

**Pros**:
- Filters out weak trends. You only trade when both groups agree.
- Works across asset classes—stocks, crypto, forex. I’ve used it on BTC/USD and it handles volatility surprisingly well.
- Gives you a narrative (traders vs. investors) that helps you *understand* the market, not just react.

**Cons**:
- Can be noisy on lower timeframes. 15-minute charts will drive you crazy.
- Lag is still inherent—it’s a moving average derivative. You won’t catch the exact bottom or top.
- No built-in alerts for crosses. You have to set them manually or use a script.

## Who It’s Actually For

This is for **intermediate to advanced traders** who want to combine trend-following with momentum timing. Beginners might find it overwhelming. If you’re still learning to read a single EMA, skip this for now.

## Better Alternatives

- **Supertrend**: Better for clear, binary signals. Less nuance but easier to execute.
- **EMA Ribbon**: Similar concept but uses more EMAs (up to 20). More lag but smoother.
- **VWAP with EMAs**: If you trade intraday, VWAP + a single EMA is simpler and just as effective.

## FAQ

**Q: Does it work for scalping?**
A: No. Stick to 1-hour or higher. Scalping requires faster indicators.

**Q: Should I use it with RSI or MACD?**
A: I don’t. It’s self-contained. Adding oscillators usually creates conflicting signals.

**Q: Can I automate it?**
A: Yes, but the cross logic is tricky. You’ll need to code for compression/expansion, not just crossovers.

## Final Verdict

The Guppy Multiple Moving Average is a solid tool for trend assessment. It won’t make you a millionaire overnight, but it will keep you out of bad trades—which is half the battle. If you’re serious about trend trading and willing to put in the screen time, it’s worth installing.

**Rating: 4/5 (⭐⭐⭐⭐)**  
It loses one star for noise on lower timeframes and the lack of native alerts. But for the price (free), it punches well above its weight.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
