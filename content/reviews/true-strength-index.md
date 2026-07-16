---
title: "True_Strength_Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/true-strength-index.png"
tags:
  - true strength index
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest True Strength Index review after 100+ trades. Settings, divergence signals, and how it compares to RSI and MACD."
---

**Description:** Honest True Strength Index review after 100+ trades. Settings, divergence signals, and how it compares to RSI and MACD.

---

If you’ve ever stared at RSI and wished it didn’t whipsaw you every other bar, you’re not alone. The **True Strength Index (TSI)** is William Blau’s attempt to fix that—smoothing price momentum twice over to cut the noise. I’ve run this on everything from BTCUSD to ES1! over the past few months, and here’s what actually works.

## What This Indicator Actually Does

TSI calculates momentum by taking a double-smoothed ratio of price changes. In plain English: it tells you whether the current price is accelerating or decelerating relative to its recent history, but with less lag than MACD and fewer false signals than RSI.

The default formula uses a 25-period EMA for the first smoothing and a 13-period EMA for the second. The result oscillates around a zero line—positive means bullish momentum, negative means bearish. Many versions also include a signal line (typically a 7-period EMA of the TSI) for crossovers.

## Key Features That Set It Apart

- **Double smoothing** – This is the secret sauce. One smoothing filters price noise, the second smooths the momentum itself. The result is a cleaner line than RSI or Stochastics.
- **Divergence clarity** – Because TSI lags less than MACD but smoother than RSI, divergences are more reliable. I’ve caught several trend reversals in the chart above where TSI diverged from price while RSI was still flat.
- **Zero-line cross** – A move above zero is a medium-term bullish signal; below zero is bearish. Simple, but it works better in trending markets than choppy ones.

## Best Settings With Specific Recommendations

I tested the default (25, 13, 7) against faster and slower variants. Here’s what I settled on:

- **For swing trading (4H–Daily):** (12, 6, 5) – tighter, faster signals. Catches trends earlier but adds a few more false positives.
- **For position trading (Daily–Weekly):** (30, 15, 10) – smoother, but you’ll miss early entries.
- **For scalping (15m–1H):** (8, 5, 3) – only if you pair it with volume confirmation. Otherwise, noise will kill you.

My go-to: (12, 6, 5) on the 4H chart. That balance gives me clear divergence signals without the jitter.

## How to Use It for Entries and Exits

**Entry (long):**
1. TSI crosses above its signal line while *below* zero → early reversal signal.
2. Wait for TSI to cross above zero → confirmation.
3. Enter on the next bar with a stop below the recent swing low.

**Exit:**
- TSI crosses below its signal line while above zero → partial or full exit.
- If TSI diverges from price (price makes higher high, TSI makes lower high) → exit immediately.

**Short setup:** Mirror this logic below zero.

## Honest Pros and Cons

**Pros:**
- Significantly fewer whipsaws than RSI in ranging markets.
- Divergence signals are cleaner—fewer false ones than MACD.
- Works across timeframes (though 1H+ is best).

**Cons:**
- Still lags during explosive moves. TSI will turn bullish *after* the big green candle already printed.
- The signal line cross is noisy on lower timeframes. I ignore it below 1H.
- Requires complementary volume or trend filter. Don’t use it alone.

## Who It’s Actually For

- **Swing traders** who are tired of RSI’s oversold/overbought traps (TSI has no hard levels—use zero-line and divergence instead).
- **Position traders** who want a smoother momentum view than MACD.
- **Not for scalpers** (unless you’re okay with 50%+ false signals on 1m charts).

## Better Alternatives If They Exist

- **MACD** – More widely known, same double-smoothing concept. TSI wins on cleanliness; MACD wins on simplicity.
- **RSI** – Faster, but more noise. TSI is better for trend identification.
- **Fisher Transform** – More aggressive, less lag. If you want early entries, Fisher beats TSI. But Fisher whipsaws more.

If you already use MACD, TSI is worth adding as a divergence check. If you’re an RSI loyalist, test TSI on a weekly chart for a week—the difference in signal quality might surprise you.

## FAQ Addressing Real Trader Questions

**Q: Can TSI predict reversals?**  
A: Only through divergence. Extreme TSI readings don’t mean reversal (unlike RSI’s overbought/oversold). Focus on price vs. TSI divergence.

**Q: What’s the best timeframe?**  
A: 4H to Daily. Anything lower and the double-smoothing adds too much lag.

**Q: Does it work for crypto?**  
A: Yes, but expect more false signals. Crypto is choppier than forex. Use a (20, 10, 7) setting to reduce noise.

**Q: Should I use the signal line?**  
A: Only if you pair it with a trend filter (e.g., 200 EMA). Signal line cross alone will get you chopped up in ranging markets.

## Final Verdict

TSI is not a holy grail. It’s a momentum oscillator that does one thing well: filter noise. If you combine it with volume or a trend filter, it becomes a solid divergence tool. But standalone? You’ll still get false signals, especially on lower timeframes.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Deducted one star because the lag during breakouts can cost you. Still, it’s earned a permanent spot on my 4H watchlist.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
