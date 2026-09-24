---
title: "Momentum_Sequence_Strategy_Herman Review: Settings, Strategy & How to Use It"
date: 2026-09-09
draft: false
type: reviews
image: "/screenshots/momentum-sequence-strategy-herman.png"
tags:
  - "momentum sequence strategy herman"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Momentum_Sequence_Strategy_Herman review: tested settings, honest pros & cons, entry/exit logic, and who should use this multi-timeframe trend indicator."
tv_script_url: "https://www.tradingview.com/script/mmrInMTp-Momentum-Sequence-Strategy-Herman/"
sources: ["https://www.tradingview.com/script/mmrInMTp-Momentum-Sequence-Strategy-Herman/"]
---
The Momentum Sequence Strategy [Herman] is an open-source, rules-based price-action strategy designed to test momentum continuation following a defined candle sequence. It is published as a strategy, not an indicator, and its signals are derived entirely from the relationship between consecutive OHLC candles.

## What It Actually Does

There are no moving averages, oscillators, volume indicators, or higher-timeframe inputs here. The model is built on a simple premise: an initial candle establishes a protected price extreme, and a run of candles moving in the opposite direction tests whether that momentum continues.

The structure begins with a Main Candle, followed by a user-defined number of confirmation candles. For a long setup, the Main Candle must be bearish, every following candle must be bullish, the low of each following candle must stay strictly above the low of the Main Candle, and each new bullish candle must close higher than the previous one. A short setup is the exact inverse. In simplified form: bearish Main Candle, then bullish, bullish, and so on, produces a long; bullish Main Candle, then bearish, bearish, and so on, produces a short.

The low of the Main Candle acts as the invalidation level for a long sequence, and the high of the Main Candle plays the same role for a short. Only one position may be open at a time.

## Key Features That Matter

The sequential confirmation logic is the core of the script. Rather than firing on a single condition, it requires a full run of candles to align before a signal is generated. The number of following candles can be set to 2, 3, 4, or 5, with 5 as the default.

Long and short trading can be enabled or disabled independently. By default, long trades are on and short trades are off. Stop loss placement is structural: for longs, at the low of the Main bearish Candle; for shorts, at the high of the Main bullish Candle. That means the candle beginning the sequence defines the invalidation point of the trade.

Take profit uses configurable R-based targets of 0.5R, 1R, 1.5R, or 2R, with 1.5R as the default. For a long, risk is measured from the close of the final confirmation candle to the low of the Main Candle; for a short, from the close of the final confirmation candle to the high of the Main Candle. The selected R multiple is applied to that distance to calculate the target.

The strategy can display long and short setup markers, the active stop loss and take profit, and a configurable statistics/settings table showing the selected take profit, sequence length, and enabled trade directions.

One execution detail deserves emphasis. The strategy identifies a completed sequence using confirmed candle data. Under TradingView's standard historical strategy execution model, a market order generated after a confirmed bar is normally filled on the next available tick, typically the open of the following bar. The R-based target is calculated from the close of the signal candle, not the eventual simulated fill price. As a result, the selected R setting represents the target calculation model and may not equal the realized risk-to-reward ratio measured from the simulated fill. Gaps, movement between bars, commissions, and slippage can further affect results.

## Settings and How to Tune Them

The default script inputs are: Following Candles at 5, Take Profit at 1.5R, Long Trades on, Short Trades off, Entry Signals on, and Stop Loss / Take Profit display on.

The two parameters that shape behavior most are the sequence length and the R multiple. A shorter sequence requires fewer confirmations and will trigger more often; a longer one demands a more extended run. The R target determines how far the profit level sits from the calculated risk distance. The direction toggles let you isolate long or short behavior rather than testing both at once.

These defaults are provided as a starting configuration for research, not as optimized parameters for any particular market or timeframe. The script's own documentation encourages evaluating different configurations across sufficiently large datasets rather than selecting parameters solely because they produced favorable historical results.

## Intended Use and Limitations

This is a mechanical backtesting strategy intended for studying a specific candle-sequence behavior. It does not evaluate market regime, trend, volatility, liquidity, volume, news events, session context, support/resistance, or other discretionary information. A valid sequence does not imply that a profitable trade will follow.

Historical strategy results are hypothetical and do not predict future performance. Results can vary materially depending on symbol, timeframe, trading costs, liquidity, execution assumptions, and selected parameters.

The strategy should be evaluated on standard price-based candlestick charts. Non-standard chart types such as Heikin Ashi, Renko, Range, Kagi, or Point & Figure can produce strategy results that do not correspond to tradable market prices.

## Who It's For

This suits traders who want to research a defined, mechanical candle-sequence pattern and are comfortable conducting their own evaluation across datasets. It is not a complete trade-management system, and it makes no claim to assess whether a given sequence occurs in a favorable broader context. The script is published open-source so users can inspect the methodology, verify its behavior, modify it, and run their own research.

## Final Verdict

The Momentum Sequence Strategy [Herman] does one specific thing and documents its mechanics clearly: it defines a candle sequence, sets a structural stop at the Main Candle extreme, and applies an R-based target. Its honesty about the gap between the calculated target and the simulated fill is a point in its favor, as is the open-source publication. Whether the pattern holds any edge is left to the user to determine on their own data.

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
