---
title: "Historical_Pattern_Projection Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/historical-pattern-projection.png"
tags:
  - historical pattern projection
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest review of Historical_Pattern_Projection: a pattern-matching tool for price projection. Best settings, strategy, pros/cons, and who should use it."
---

**What This Indicator Actually Does**

Historical_Pattern_Projection (HPP) is a pattern-matching tool that scans past price action for similar formations to the current one, then projects likely future moves. It’s not a crystal ball—it’s a statistical probability engine. You feed it a lookback window (default 50 bars), and it finds the closest historical matches based on Euclidean distance or correlation. Then it overlays those past patterns’ subsequent price paths onto your chart as faint lines, highlighting the median projection.

Think of it as a visual “what happened next” database. The chart above shows a clear example: the thick blue line is the current price, the gray lines are past matches, and the dashed orange is the median projection. When the current pattern resembles a prior bullish breakout, HPP paints a similar path.

**Key Features That Set It Apart**

- **Multi-metric matching**: You can choose between Euclidean distance (shape similarity) or Pearson correlation (trend direction similarity). I found Euclidean more reliable for ranging markets, correlation better for trending ones.
- **Adjustable projection length**: Default is 20 bars forward, but you can push it to 50. I stick with 20–30 for intraday; longer projections get noisy.
- **Match count**: Shows the top 5–10 matches. Fewer matches mean cleaner visuals, more means better statistical smoothing.
- **Median overlay**: The dashed line is your most actionable signal—it’s the average path of all matched patterns. Ignore the outliers.

**Best Settings with Specific Recommendations**

After testing on BTCUSD 1H and NAS100 15M:
- **Matching method**: Euclidean distance (default works). Switch to correlation only if you trade strong trends—it ignores amplitude and focuses on direction.
- **Lookback bars**: 50–80. Too short (20) and you overfit noise. Too long (200) and patterns become generic.
- **Projection bars**: 20. Longer projections degrade fast—think of it as a 20-bar forecast, not a prediction for next month.
- **Min match similarity**: 0.7–0.8. Lower than 0.5 and you get garbage matches.
- **Show median only**: Enable this. The spaghetti of individual matches is distracting.

**How to Use It for Entries and Exits**

This is a confirmation tool, not a standalone signal generator. Here’s how I pair it:

- **Entry**: Wait for price to close above the median projection line. That’s your green light. If the projection is flat or bearish, stay out.
- **Exit**: Take profit when price hits the median projection’s high (or 1.5x extension for strong moves). Stop loss goes below the lowest match line from the last 5 bars.
- **False signal filter**: Only act when the current pattern’s initial bars (first 10) align with a clear support/resistance level on higher timeframe. For example, if HPP projects a rally but price is at a weekly resistance, skip it.

**Pros**

- **Visual clarity**: Seeing past patterns converge on a future zone is intuitive. No lagging oscillators.
- **Adaptive**: Works on any timeframe—scalpers can use 5M, swing traders on 4H.
- **No repaint**: Once a bar closes, the projection is fixed. This is huge—many similar tools repaint.
- **Free with good defaults**: No paywall gimmicks.

**Cons**

- **No volume filter**: Patterns ignore volume context. A low-volume pattern match is less reliable. You’ll need to check volume yourself.
- **Overfits in choppy markets**: During tight ranges, all patterns look similar, and projections become random. Avoid using in flat conditions.
- **Lag on projection start**: The indicator needs at least 10 bars of the current pattern to begin matching. You won’t get instant signals on a breakout.

**Who It’s Actually For**

- **Swing traders** (1H–4H) who want a visual edge on price direction.
- **Pattern traders** who already use harmonic or chart patterns and want a statistical backup.
- **Not for scalpers**: The 10-bar lag kills its usefulness on sub-5M timeframes.

**Better Alternatives**

- **Patternz**: More advanced, includes volume and volatility filters. But it’s paid and more complex.
- **Fractal Projection (by LuxAlgo)**: Similar concept but with Fibonacci-based projections. Less noise, but less adaptable.
- **Auto Fibonacci Retracements**: Cheaper and simpler if you just want key zones. HPP wins for dynamic patterns.

**FAQ**

*Q: Does HPP repaint?*  
A: No—once a bar closes, the projection is fixed. Intra-bar projections can shift slightly, but that’s true for any indicator.

*Q: Can I use it on crypto?*  
A: Yes, it works on any asset. I tested on BTC, ETH, and gold. Crypto is fine due to high volatility—patterns repeat more often.

*Q: What’s the best timeframe?*  
A: 1H to 4H. Lower timeframes produce too many false signals. Higher timeframes (daily) have too few patterns in lookback.

**Final Verdict**

Historical_Pattern_Projection isn’t revolutionary—it’s a well-executed pattern matcher that does one thing and does it cleanly. It won’t replace your edge, but it adds a statistical layer to your chart reading. The no-repaint guarantee and median projection line make it a reliable confirmation tool for swing traders.

**Rating: ⭐⭐⭐⭐ (4/5)**

One star off for the lack of volume context and choppy market weakness. But for a free indicator? It’s a steal. Install it, set it to median-only, and pair it with a volume oscillator. You’ll see the value within a few trades.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
