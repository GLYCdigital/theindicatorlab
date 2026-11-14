---
title: "Percentile Momentum Nal Review — Momentum Indicator"
date: 2026-11-15T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/percentile-momentum-nal.png"
tags:
  - "percentile momentum nal"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Percentile Momentum/NAL review: a distribution-based oscillator that measures price displacement from a rolling percentile instead of fixed lookback differences."
tv_script_url: "https://www.tradingview.com/script/iBLlArkY-Percentile-Momentum-NAL/"
sources: ["https://www.tradingview.com/script/iBLlArkY-Percentile-Momentum-NAL/"]
---
Most momentum indicators ask a simple question: how far has price moved from where it was N bars ago? Percentile Momentum/NAL throws that reference point out and replaces it with a different one — the price level sitting at a chosen percentile of the recent price distribution. If that sounds like a subtle distinction, it changes the entire character of the reading.

## What it actually measures

The core calculation is straightforward once you strip away the framing. The script builds a rolling empirical distribution of whatever price source you feed it, extracts a percentile from that distribution (linear interpolation), and subtracts it from the current source value. That difference is the "momentum" number.

So instead of measuring displacement from a past price, you're measuring displacement from a statistical reference — the level below which the chosen percentage of recent prices fall. At the default 70th percentile, that reference sits near the upper end of the observed range, meaning positive momentum means price is trading above a level that most of the recent distribution sits beneath.

Two consequences worth internalising. First, this is not a percentage or normalized oscillator — the values are in the units of the price source, so an ES reading and a BTC reading won't be comparable. Second, it isn't RSI wearing a different hat. There's no bounded 0–100 scale here.

## The two-stage structure is the real idea

The part that separates this from a one-line percentile script is the second layer. The momentum series itself gets run through percentile analysis again, producing adaptive upper and lower bands from its own recent distribution. Defaults are asymmetric — 70th and 10th — which the author explicitly frames as a design choice: up and down momentum don't have to be judged against identical statistical boundaries.

From there, regime classification is a conjunction, not a single trigger. Bullish requires momentum above the upper band **and** close above the percentile price reference. Bearish requires momentum below the lower band. Anything in between, the model holds its previous state.

That persistence mechanism is the most practically significant detail in the whole description. It means the indicator won't flip the moment momentum drifts back toward the middle of its distribution — a new regime needs a threshold breach. Whether you read that as welcome hysteresis or as lag depends entirely on how you trade.

## How you'd actually use it

The workflow is regime-tracking rather than signal-hunting. You watch the oscillator for the coloured state, use the adaptive bands to gauge whether a displacement is statistically unusual or routine, and rely on the trend-coloured candles to see the regime projected onto price. Alerts fire only on confirmed bars when the state changes, which suits swing and position work better than anything intraday.

The gradient shading between momentum and the opposing band is a nice touch — it gives you a sense of how close the current reading sits to flipping, without needing a second pane.

## Pros

- Genuinely different reference frame. Distribution-relative momentum isn't common on TradingView, and the two-stage percentile construction is coherent rather than decorative.
- Asymmetric thresholds are a defensible design. Markets don't distribute symmetrically, and the model reflects that.
- Regime persistence reduces whipsaw on the classification itself, even if it costs responsiveness.
- Alerts are gated to confirmed bars and state changes — no spam on every bar close.
- Configurable source, observation length, price percentile, both momentum percentiles, and three colour presets. The inputs that matter are exposed.

## Cons

- The unbounded, price-unit output is awkward. You can't easily compare momentum magnitude across instruments or even across long time spans on the same chart, and there's no normalization offered.
- Persistence cuts both ways. Holding the last state means the indicator can stay bullish through a meaningful pullback until the lower band is actually breached — or bearish through a recovery. That's the design, but it's a real trade-off, not a free lunch.
- Two layers of rolling percentile calculation mean the behaviour depends heavily on observation length, and the description gives no guidance on how to choose it. You're on your own calibrating.
- The candle colouring on the main chart is convenient but adds visual noise if you already run other regime tools.

## Who it's for

Systematic traders and swing traders who already think in terms of distributions and want a momentum regime filter that doesn't lean on fixed lookback differences. It's also useful for anyone building a rules-based regime layer — the binary bullish/bearish state with confirmed-bar alerts slots cleanly into a broader system. Discretionary scalpers and anyone wanting a fast, bounded oscillator should look elsewhere; this isn't built for that.

## FAQ

**Does it repaint?** The alerts require a confirmed bar, so the alert logic doesn't fire intrabar. The regime classification itself persists between states by design, which is different from repainting.

**Is it a buy/sell signal indicator?** No. It classifies directional regimes. The author frames it as a framework for examining displacement and momentum expansion, not an entry trigger.

**Why asymmetric percentiles?** The description states the model deliberately avoids assuming up and down momentum need identical statistical boundaries. The defaults reflect that, and both are adjustable.

**Can I use it on any market?** The inputs are generic, but the price-unit output means readings aren't portable between instruments. You'd need to re-tune observation length per market.

## Verdict

This is a well-constructed indicator with a clear, non-gimmicky premise. The dual percentile approach — one for the price reference, one for the momentum thresholds — is the kind of idea that rewards thinking about what momentum actually means, and the persistence logic shows the author thought about practical behaviour rather than just plotting a line.

It loses a star for the unbounded output and the lack of guidance on tuning observation length, both of which push real work onto the user. But if you want a momentum model that adapts its reference to the market's own distribution instead of a fixed lookback, this is a solid, honest implementation of that idea.

⭐⭐⭐⭐
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*
