---
title: "Impulse_Rsi_Tobbysimard Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/impulse-rsi-tobbysimard.png"
tags:
  - impulse rsi tobbysimard
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A custom RSI with smoothed momentum and divergence detection. Not revolutionary, but cleaner signals than default RSI. Good for trend-confirmation scalping."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) — A practical RSI variant that cuts through noise, but don't expect magic.**

## What This Indicator Actually Does

Impulse_Rsi_Tobbysimard is a modified RSI oscillator that applies additional smoothing and impulse logic to the classic Relative Strength Index. Where the default TradingView RSI can whip you around in choppy markets, this version attempts to filter out low-probability moves using a secondary momentum calculation and a custom smoothing filter.

On the chart, you'll see a single line oscillating between 0 and 100 with overbought/oversold zones. The line changes color when it detects a "confirmed impulse" — a rapid shift in momentum beyond a user-defined threshold. It also plots small arrows when divergence occurs between price and the indicator.

## Key Features That Set It Apart

- **Impulse confirmation logic**: The line only changes color after RSI breaks and holds beyond a threshold (adjustable via the "Impulse Strength" input). This is intended to filter out fakeouts.
- **Built-in divergence detection**: The indicator automatically marks hidden and regular divergences with up/down arrows.
- **Smoothing control**: A "Signal Smoothing" parameter applies a moving average to the RSI line. Raising it produces slower, cleaner swings on higher timeframes.
- **Custom overbought/oversold levels**: You can set separate thresholds for bullish/bearish impulses — tighter levels for more conservative reads, looser levels for more aggressive ones.

## Settings and How to Tune Them

The main parameters are:

- **Timeframe**: The indicator is designed for intraday and swing use; the smoothing and impulse confirmation introduce lag that becomes more noticeable as you drop to very short timeframes.
- **RSI Length**: The standard RSI length input. Longer lengths produce a slower, smoother line; shorter lengths react faster.
- **Impulse Strength**: A multiplier on the RSI's rate of change. Higher values mean fewer, stronger signals; lower values mean more frequent but weaker signals. This is the parameter most responsible for how often the line flips color.
- **Signal Smoothing**: Applies a moving average to the RSI line. Higher values smooth the line further and suit higher timeframes; lower values keep it responsive for intraday work.
- **Overbought/Oversold**: Adjustable thresholds for bullish and bearish impulses. Tighter levels reduce signals in trending markets; wider levels produce more.

There is also a "Show Divergence Labels" option in the settings panel, which displays text labels rather than arrow-only markers.

No single combination is objectively best — the right values depend on the instrument, timeframe and how much lag you're willing to accept.

## How It's Typically Used for Entries and Exits

This isn't a standalone system. It's best treated as a confirmation tool alongside price action or a trend filter.

**Long entry concept**:
1. Price makes a higher low while the indicator makes a lower low (hidden bullish divergence).
2. Wait for the RSI line to change color (impulse confirmed) and cross back above the oversold level.
3. Enter on a subsequent candle close, with a stop below the recent swing low.

**Partial exit concept**:
- If already long and the RSI line flips color (impulse lost) while still in overbought territory, some traders take partial profits on the idea that the impulse logic gives early warning before a full reversal.

**False signal filter**: One common approach is to only act on impulse signals that appear within a few bars of crossing the overbought/oversold zone, rather than acting on every color change.

## Honest Pros and Cons

**Pros**:
- Cleaner than default RSI — less whip in choppy ranges.
- Divergence detection is serviceable, though not perfect.
- Simple color-coding makes it easy to scan multiple pairs quickly.
- The smoothing parameter genuinely helps on higher timeframes.

**Cons**:
- Lags on lower timeframes. The smoothing and impulse confirmation add delay, so you'll miss the early portion of a move.
- The Impulse Strength parameter is sensitive. At low values it catches nearly every blip; it often needs to be raised to avoid noise.
- Divergence arrows can repaint — they may appear and then disappear a few bars later, which is a problem if you're not using alerts.
- No native alert for divergence. You'll need custom Pine Script alerts.

## Who It's Actually For

- **Swing traders** on higher intraday and daily timeframes who want a less jittery RSI.
- **Scalpers** only on liquid pairs, and only if they can tolerate the lag.
- **Trend traders** using it as a filter — waiting for the impulse signal to confirm on a pullback before entering.

**Not for**: Very short timeframe day traders, pure reversal traders (the lag works against you), or anyone who can't tolerate repainting divergence markers.

## Better Alternatives

- **RSI Divergence Indicator** by LuxAlgo — better divergence detection, no repaint, and multi-timeframe support. Paid.
- **Smoothed RSI** by TradeSmart — simpler, no impulse logic, but zero lag and no repaint. Free.
- **Momentum RSI** by LonesomeTheBlue — uses a different smoothing algorithm that responds faster. Free.

If you're on a budget, this one is solid for the price (free).

## FAQ

**Q: Does this indicator repaint?**
A: The divergence arrows can repaint. The RSI line itself is calculated on close, so the impulse color is stable after the bar closes.

**Q: Can I use it for crypto?**
A: Yes. It works best on intraday to hourly timeframes; on lower timeframes the lag becomes more noticeable.

**Q: What's the "Impulse Strength" doing?**
A: It's a multiplier on the RSI's rate of change. Higher values mean fewer, stronger signals; lower values mean more frequent but weaker signals.

**Q: How do I set alerts?**
A: You'll need to create a custom alert with a Pine Script condition. The indicator doesn't have native alert triggers.

## Final Thoughts

Impulse_Rsi_Tobbysimard won't turn you into a millionaire, but it's a genuinely useful refinement of the classic RSI. The smoothing and impulse logic cut through noise better than the default oscillator, and the divergence detection is a nice bonus — even if it isn't perfect.

**4/5 stars**. It's free, it works, and it offers a clear alternative to default RSI for swing trading. If you're tired of RSI whipsawing you in and out of trades, it's worth a look. Just don't rely on it alone — pair it with price action or a trend filter.

**Rating**: ⭐⭐⭐⭐ (4/5) — Reliable RSI variant for swing traders who want fewer false signals.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
