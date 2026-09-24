---
title: "Smc_Confluence_Suite Review: Settings, Strategy & How to Use It"
date: 2026-09-10
draft: false
type: reviews
image: "/screenshots/smc-confluence-suite.png"
tags:
  - "smc confluence suite"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Smc_Confluence_Suite review: A smart-money concepts tool that maps order blocks, FVGs, and liquidity. Tested settings, entry logic, and honest trade-offs."
tv_script_url: "https://www.tradingview.com/script/6Y4Q2ogX-SMC-Confluence-Suite/"
sources: ["https://www.tradingview.com/script/6Y4Q2ogX-SMC-Confluence-Suite/"]
---
Most Smart Money Concept indicators are a pile of rectangles drawn after the fact, looking brilliant in hindsight and useless in real time. The SMC Confluence Suite is a more serious attempt to codify the institutional footprint into a single pane. Here is an honest picture of what it does well and where it falls short.

## What This Indicator Actually Does

At its core, the SMC Confluence Suite aggregates the major SMC pillars—order blocks, fair value gaps (FVGs), and liquidity zones—into one overlay. But the key differentiator is the word "confluence." It doesn't just draw every structure it finds; it scores zones based on how many SMC elements align at the same price level. A zone with an order block, an FVG, and a liquidity sweep nearby gets highlighted as a high-probability area, while isolated structures fade into the background.

The script maps structure across two timeframes and condenses nine separate confirmations into a single 0-100 score, so you can tell a high-quality setup from a mediocre one at a glance.

## Key Features That Stand Out

The confluence scoring engine is the star. Nine weighted factors are each scored on a gradient rather than pass/fail, and the score is color-coded so a stacked confluence stands out from a weaker single-factor area. This creates a visual hierarchy that is genuinely useful for scanning multiple charts quickly.

The scoring factors themselves are worth listing, because the value of the tool lives in them:

1. Fresh BOS/CHoCH on TF1 in the bias direction
2. TF2 trend alignment
3. Order Blocks overlapping the OTE zone
4. Fair Value Gaps overlapping the OTE zone
5. Depth on the correct side of equilibrium
6. A liquidity sweep supporting the bias
7. Price located inside the OTE zone
8. Reward-to-risk versus your target
9. Untouched zones still available

Every weight is adjustable, and setting one to zero removes that factor without distorting the scale. The breakdown table shows exactly where points were lost, so the number is auditable instead of being a black box. Grades run A+ at 85, A at 75, B at 60, C at 45, and D below.

The built-in liquidity sweep detection is another plus. Instead of manually hunting for equal highs/lows that got wicked out, the indicator flags these events and maps the subsequent displacement move. It uses a minimum ATR penetration and an optional "close back inside" requirement, plus EQH/EQL clustering.

I also appreciate the structure handling. Order Blocks are anchored to the actual structural break rather than to an arbitrary displacement candle, with configurable mitigation (touch / 50% / full). Fair Value Gaps are filtered by absolute size and/or ATR so micro-gaps are ignored. Premium/Discount is drawn from the current TF1 swing pair with an equilibrium line, and zones on the wrong side are dimmed or filtered out. The OTE component marks the 0.62 / 0.705 / 0.79 retracement zone with entry, stop, TP1, TP2, R:R, and a position size derived from your account balance and risk percentage.

The settings menu is deep, but not overwhelming. You can toggle individual SMC elements on/off, adjust the lookback period for structure detection, and set minimum confluence thresholds.

## Settings and How to Tune Them

The parameters worth understanding:

- **TF1 and TF2**: The two timeframes the structure engine references. Set them to timeframes equal to or higher than your chart.
- **Confluence threshold**: The minimum score you require before acting on a zone.
- **Lookback period**: How far back the structure detection reaches.
- **Order block mitigation**: Choose touch, 50%, or full mitigation depending on how conservatively you want a zone invalidated.
- **FVG filters**: Absolute size and/or ATR filtering to drop micro-gaps.
- **Liquidity sweep requirements**: Minimum ATR penetration and the optional "close back inside" requirement.
- **Factor weights**: Each of the nine scoring factors can be weighted, and zeroing one removes it from the scale.

There is no single correct configuration here—the right values depend on the instrument and the timeframe you trade. Test any settings on your own instruments and timeframes before risking capital.

## How to Actually Use It

The intended workflow is a simple sequence:

1. Set TF1 and TF2 to timeframes equal to or higher than your chart.
2. Wait for a BOS or CHoCH to project a new OTE zone.
3. Check the score panel—B or better means the supporting factors are present.
4. Enter inside the OTE zone, ideally where an OB or FVG overlaps it.
5. Size the position with the lot value shown on the dashboard.

The exit is where many traders struggle. The indicator does not have an auto-target feature. The convention is to mark the opposing liquidity pool manually and take partial profits there, letting the remaining position run until price creates a new structure break.

## Pros & Cons

**Pros:**
- Confluence scoring genuinely filters out low-quality zones
- Visual hierarchy makes chart reading faster
- Auditable breakdown table shows where points were lost
- Works across asset classes without heavy re-tuning

**Cons:**
- Live bars update until they close, which is normal for structure-based tools but still worth knowing
- Higher timeframe zones can overlap heavily, creating visual clutter
- The learning curve is steeper than a simple moving average crossover, obviously
- It assumes you already understand SMC concepts—it won't teach you the *why* behind the zones

## Who This Is For

This is for the trader who already understands SMC concepts but wants to streamline their analysis. If you're new to order blocks and FVGs, this indicator won't teach you the *why* behind the zones—it just shows you *where* they are. You'll need to pair it with some SMC education first.

It's also well-suited for traders who scan multiple markets daily. The color-coded confluence zones let you quickly identify which charts have the clearest institutional structure without deep-diving into each one.

## A Note on Repainting

Higher-timeframe pivots are requested with lookahead enabled but referenced with a one-bar offset, so only closed higher-timeframe values are used. Structure levels themselves are confirmed on bar close. Live bars will still update until they close, which is normal behaviour for any structure-based tool. The practical implication is that you should trade zones that are currently active rather than historical ones that may have been invalidated.

## Alternatives Worth Considering

If you find this too heavy, **Smart Money Concepts by LuxAlgo** offers a cleaner visual presentation but lacks the confluence scoring. For a more automated approach, **LuxAlgo's SMC Suite** includes entry and exit signals, though those are generally less reliable than manual execution.

If you're on a budget, **Supply Demand Zones** by CyberMind is a simpler, repaint-free option that covers basic zone identification without the SMC framework.

## FAQ

**Does this indicator repaint?**
Higher-timeframe pivots are referenced with a one-bar offset so only closed values are used, and structure levels are confirmed on bar close. Live bars will still update until they close, which is normal for any structure-based tool.

**Can I use it for crypto?**
The script is a visualization and analysis tool and is not instrument-specific. Liquidity sweeps are especially relevant in crypto's volatile sessions, but you should test it on your own instruments and timeframes before risking capital.

**Does it work for scalping?**
The indicator is designed around structure and confluence rather than a specific timeframe. Whether it suits scalping depends on your instrument and how you configure TF1, TF2, and the confluence threshold—test it yourself before committing capital.

## Final Verdict

The SMC Confluence Suite takes the messy, subjective nature of SMC analysis and imposes a disciplined structure on it. The confluence scoring is auditable rather than a black box, and the breakdown table tells you exactly why a setup scored the way it did.

The live-bar updating and the lack of an auto-target hold it back. But if you're already trading SMC concepts and want to elevate your zone selection game, this is one of the better tools in this category.

*This script is a visualisation and analysis tool. It does not predict price and it is not financial advice. Test any settings on your own instruments and timeframes before risking capital.*

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
