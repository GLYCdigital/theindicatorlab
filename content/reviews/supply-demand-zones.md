---
title: "Supply Demand Zones Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/supply-demand-zones.png"
tags:
  - supply demand zones
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Supply Demand Zones review: how it plots key levels, best settings, entry/exit tactics, and who should use it. No fluff."
---

**Final Verdict: ⭐⭐⭐⭐ (4/5)**  
A solid, no-nonsense tool for spotting institutional zones. Not perfect, but effective if you use it right.

---

## What This Indicator Actually Does

Supply Demand Zones automatically identifies areas where price previously reversed sharply—what most traders call "support and resistance on steroids." It draws rectangular boxes around these zones based on aggressive price moves away from a range. The idea is simple: price left these zones fast, so it'll likely react there again.

I tested it on BTC/USD 1H and 4H, plus some ES futures on 15M. The zones it draws are clean—no overlapping clutter like some other scripts. As the chart above shows, the indicator highlights zones with a slight transparency, making them easy to spot without hiding price action.

---

## Key Features That Set It Apart

- **Auto-zone detection** – No manual drawing. The indicator finds both supply (sell) and demand (buy) zones based on swing highs/lows and momentum.
- **Zone freshness labels** – It marks zones as "Fresh" (untested) or "Tested." Fresh zones are more reliable; tested ones get weaker.
- **Customizable lookback** – You can adjust the sensitivity. I found a lookback of 20–30 bars works best on 1H, while 10–15 is better for scalping.
- **Drop-down zone filtering** – You can disable old zones or show only the last 5–10. Keeps the chart readable.

---

## Best Settings with Specific Recommendations

After a week of tweaking, here's what I settled on:

- **Zone detection sensitivity:** 25 (default is 20). This catches medium-strength moves without drawing every blip.
- **Max zones shown:** 8. More than that and the chart looks like a Jackson Pollock painting.
- **Zone extension:** 2 bars left. This gives you a buffer—price often wicks into the zone before reversing.
- **Color scheme:** Green for demand, red for supply. Keep transparency at 40% so you still see candlestick patterns inside the zone.

**For scalpers (5M/15M):** Drop sensitivity to 15, max zones to 5.  
**For swing traders (1H/4H):** Sensitivity 30, max zones 10. Let the bigger picture play out.

---

## How to Use It for Entries and Exits

I don't just buy at the zone line—I wait for confirmation.

**Entry setup (long example):**
1. Price enters a fresh demand zone.
2. Wait for a bullish rejection candle (long wick, close near high).
3. Enter on the next candle's break above that rejection candle's high.
4. Stop loss: 2–3 pips below the zone's lowest point.

**Exit strategy:**
- Take partial profits at the nearest supply zone (or 1:2 risk-to-reward).
- Move stop to breakeven after price moves one zone width away.

**The trap:** Don't fade every zone. Fresh zones with a strong prior impulse move work best. Old, tested zones get chopped up—skip those.

---

## Honest Pros and Cons

**Pros:**
- Saves hours of manual drawing. Zones are consistent, not subjective.
- Fresh zone labels are genuinely useful—untested zones have a higher probability of holding.
- Works across timeframes. I've used it from 5M to 1D without issues.

**Cons:**
- Can't adjust zone strength based on volume or order flow. It's purely price-based.
- Sometimes draws zones on minor swings that aren't significant. You'll need to ignore about 20% of them.
- No multi-timeframe alignment built in. You have to add the indicator to each chart manually.

---

## Who It's Actually For

- **Swing traders** who want a quick, reliable way to map key levels.
- **Beginners** who struggle with drawing zones consistently.
- **Not for** pure price action purists who prefer manual analysis—this tool is a shortcut, not a replacement.

---

## Better Alternatives If They Exist

If you want more granularity, try **Order Flow Imbalance** or **Volume Profile** indicators. They show real supply/demand based on traded volume, not just price moves. But for a simple, clean zone-drawing tool, this is one of the best on TradingView.

---

## FAQ

**Q: Does it repaint?**  
No. Once a zone is drawn, it stays. The "fresh" label updates to "tested" when price revisits, but the zone itself doesn't move.

**Q: Can I use it for crypto?**  
Yes. Works fine on BTC/ETH. Just adjust sensitivity—crypto moves are choppier, so a higher sensitivity (30+) helps.

**Q: How many zones should I keep visible?**  
Max 8–10. More than that and you're just guessing.

**Q: What timeframe is best?**  
1H to 4H for swing trading. 15M for scalping. Avoid 1M—it draws too many false zones.

---

**Final Verdict: ⭐⭐⭐⭐ (4/5)**  
A reliable, time-saving indicator for zone-based trading. It doesn't predict the future, but it maps the battlefield well. If you understand that zones are areas of interest, not hard lines, you'll get solid value from it.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
