---
title: "Auto_Harmonic_Patterns_Afd Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/auto-harmonic-patterns-afd.png"
tags:
  - "auto harmonic patterns afd"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Auto_Harmonic_Patterns_Afd review: how this TradingView indicator auto-detects Gartley, Bat and Butterfly patterns, best settings, entry logic and honest limits."
tv_script_url: "https://www.tradingview.com/script/2MvG5H7T-Auto-Harmonic-Patterns-AFD/"
---
Most harmonic pattern indicators on TradingView are either so eager they paint a butterfly on every three-bar pullback, or so strict you see one setup a month. Auto_Harmonic_Patterns_Afd sits closer to the middle of that range, and after running it on the 4H and daily across FX majors and a few large-cap charts, that's the honest headline: it detects legitimately, it labels cleanly, and it makes you do the final filtering yourself. That's a fair trade, but it's not a free ride.

## What it actually does

The script scans price action for classic harmonic structures — Gartley, Bat, Butterfly, Crab, and the usual XABCD family — and draws the completed leg set with point labels, Fibonacci ratio annotations, and a projected reversal zone around the D point. When a structure completes inside its tolerance band, you get an alert. That's the whole mechanism. No repainting tricks, no "AI prediction" language, no buy/sell arrows pretending to be a system.

It's filed under Trend, which is a slight misnomer. Harmonics are mean-reversion tools by nature — you're trading the reaction off point D back toward B and C. Where the trend category does apply is the filtering: the better setups in my testing were the ones where the pattern pointed in the direction of the higher-timeframe trend, not against it.

## Detection quality and the settings that matter

The defaults are usable but loose. Two inputs changed my results more than anything else:

- **Error tolerance / ratio deviation.** Tighten this from the default to roughly 0.05–0.08 on the 4H. The D-point zone shrinks noticeably and you stop getting patterns that "sort of" qualify. On the daily I'd push it slightly looser, around 0.10, because daily swings rarely nail the 0.786 to the tick.
- **Pattern selection.** Turn off the patterns you don't trade. Crab and Butterfly have wide D zones and produce more false completions than Gartley or Bat. If you're new to harmonics, run Gartley and Bat only for a month.

One thing worth knowing: the indicator does not repaint completed patterns, but it *does* redraw the in-progress XABCD leg as price moves. If you're watching a forming pattern, treat the D projection as a zone, not a level. I got burned once treating a forming Bat's D as a hard limit — the leg extended, the pattern invalidated, and the label vanished. That's correct behavior, but it's a behavior you need to expect.

## How I traded it

The logic that worked:

1. Wait for the completed pattern alert. Do not front-run the D point.
2. Check the higher timeframe. Long from a bullish Gartley only if the daily isn't in a clean downtrend.
3. Entry on the first rejection candle inside the D zone — a wick, an engulfing close, whatever your trigger is.
4. Stop beyond X. Not beyond D. Beyond X. If the pattern fails, it fails there, and that's where your invalidation lives.
5. First target at point C, second at point B. The measured move back to B is where most of the edge is; holding past C for the full retracement dropped my win rate meaningfully.

As the chart above shows, the completed structures cluster around swing extremes, which is exactly where you want a reversal tool firing. The MACD panel underneath is useful here — I only took D-point entries where momentum was already diverging against the prior leg. That single filter cut my losing trades more than any setting tweak.

## Pros and cons

**Pros**
- Clean XABCD labeling with visible ratio annotations — you can audit every pattern instead of trusting a black box
- Adjustable tolerance, which most free harmonic scripts don't expose
- Alerts fire on completion, not on formation, so you're not chasing ghosts
- No repainting on confirmed patterns
- Works across timeframes without needing separate versions

**Cons**
- The in-progress leg redraws, and new users will get faked out by it
- No built-in trend or volume filter — you supply that context yourself
- Crab and Butterfly completions are noisy at default tolerance
- Documentation is thin; you're reverse-engineering the ratio bands from the labels
- The "Trend" categorization is misleading for anyone browsing by category

## Who it's for

Discretionary swing traders who already understand harmonic ratios and want the drawing done for them. If you know what a 0.786 retracement means, this saves you 20 minutes of manual measuring per setup. If you don't, this indicator will generate confident-looking labels you can't evaluate, and you'll lose money politely.

It is not for scalpers. On the 5-minute chart the tolerance bands are meaningless — spread and noise swallow the D zone entirely. And it's not for anyone wanting a turnkey signal; there are no arrows and no strategy tester hook.

## Alternatives

If you want harmonics with a built-in trend filter, look at the Scott Carney-style scripts that gate patterns by EMA slope. If you want automated entries and backtesting, you're better off with a strategy-script version of harmonic detection — this is a visual tool, not a system. And if you just want reversal zones without the XABCD overhead, a plain Fibonacci retracement tool plus divergence does 80% of the job for free.

## FAQ

**Does Auto_Harmonic_Patterns_Afd repaint?**
Completed patterns do not repaint. Forming patterns redraw the projected D point as price develops, which is expected but can mislead.

**What timeframe works best?**
4H and daily. Below 1H the ratio tolerances produce too many marginal completions.

**Does it give buy and sell signals?**
No. It draws the pattern and fires a completion alert. Entry, stop, and target decisions are yours.

**Is it free?**
Check the current listing — pricing on community scripts changes, and the feature set here is closer to a solid free tool than a paid suite.

**Can I use it for crypto?**
Yes, and it handles crypto's wider swings reasonably well on the 4H, though you'll want tolerance closer to 0.10.

## Verdict

Auto_Harmonic_Patterns_Afd does one job — finding and drawing harmonic structures — and does it without theatrics. The adjustable tolerance and honest labeling put it above most of the harmonic clutter on TradingView. What holds it back from five stars is the missing context layer: no trend filter, no volume confirmation, thin docs, and a redraw behavior that will cost beginners real money before they learn it. Bring your own filter and it's a genuinely useful swing tool.

**Rating: ⭐⭐⭐⭐ (4/5)** — Recommended for traders who already speak harmonic, with a caveat for everyone else.
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
