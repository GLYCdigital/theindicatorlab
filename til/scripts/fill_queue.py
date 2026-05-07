#!/usr/bin/env python3
"""
Fill the indicator queue with TradingView indicators to review.
Run when the queue starts running low (<5 remaining).

Usage:
    python3 fill_queue.py           # Interactive mode — picks categories
    python3 fill_queue.py --auto    # Auto-fills 20 new indicators

Format added:  slug|Indicator Name|chart_type|Category
"""
import os, sys, random

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE_FILE = os.path.join(WORKSPACE, "indicator_queue.txt")
REVIEWS_DIR = os.path.join(WORKSPACE, "../theindicatorlab/content/reviews")

# ── Indicator database ──────────────────────────────────────────────────────
# Format: (slug, "Display Name", "chart_type", "Category")
# chart_type must match generate_chart.py supported types
# Category determines where it appears in review cards

INDICATORS = [
    # Momentum
    ("aroon", "Aroon Indicator", "rsi", "Momentum"),
    ("commodity-channel-index", "Commodity Channel Index (CCI)", "rsi", "Momentum"),
    ("elder-ray-index", "Elder Ray Index", "macd", "Momentum"),
    ("detrended-price-oscillator", "Detrended Price Oscillator (DPO)", "macd", "Momentum"),
    ("rate-of-change", "Rate of Change (ROC)", "rsi", "Momentum"),
    ("coppock-curve", "Coppock Curve", "macd", "Momentum"),
    ("klinger-oscillator", "Klinger Oscillator", "macd", "Momentum"),
    ("force-index", "Force Index", "macd", "Momentum"),
    ("ultimate-oscillator", "Ultimate Oscillator", "macd", "Momentum"),
    ("chande-momentum", "Chande Momentum Oscillator", "rsi", "Momentum"),
    ("relative-vigor-index", "Relative Vigor Index", "rsi", "Momentum"),
    
    # Volume
    ("accumulation-distribution", "Accumulation Distribution Line", "macd", "Volume"),
    ("negative-volume-index", "Negative Volume Index", "macd", "Volume"),
    ("positive-volume-index", "Positive Volume Index", "macd", "Volume"),
    ("ease-of-movement", "Ease of Movement", "macd", "Volume"),
    ("volume-ratio", "Volume Ratio", "macd", "Volume"),
    ("volume-flow", "Volume Flow Indicator", "macd", "Volume"),
    
    # Trend
    ("average-directional-index", "Average Directional Index (ADX)", "rsi", "Trend"),
    ("triple-ema", "Triple EMA (TEMA)", "bollinger-bands", "Trend"),
    ("price-channel", "Price Channel", "supertrend", "Trend"),
    ("mass-index", "Mass Index", "macd", "Volatility"),
    ("linear-regression", "Linear Regression", "bollinger-bands", "Trend"),
    ("moving-average-ribbon", "Moving Average Ribbon", "ema", "Trend"),
    ("qstick", "QStick", "macd", "Momentum"),
    
    # Volatility
    ("chandelier-exit", "Chandelier Exit", "supertrend", "Volatility"),
    ("chaikin-volatility", "Chaikin Volatility", "bollinger-bands", "Volatility"),
    ("projection-oscillator", "Projection Oscillator", "macd", "Momentum"),
    
    # Support / Resistance
    ("fibonacci-retracement", "Fibonacci Retracement", "bollinger-bands", "Support & Resistance"),
    ("camarilla-pivots", "Camarilla Pivots", "bollinger-bands", "Support & Resistance"),
    ("woodie-pivots", "Woodie Pivots", "bollinger-bands", "Support & Resistance"),
    
    # Additional classics
    ("waddah-attar", "Waddah Attar Explosive", "macd", "Momentum"),
    ("vortex", "Vortex Indicator", "macd", "Momentum"),
    ("know-sure-thing", "Know Sure Thing (KST)", "macd", "Momentum"),
    ("arnaud-legoux", "Arnaud Legoux Moving Average", "ema", "Trend"),
    ("hull-moving-average", "Hull Moving Average", "ema", "Trend"),
    ("least-squares", "Least Squares Moving Average", "ema", "Trend"),
    ("variable-index-dynamic", "VIDYA", "ema", "Trend"),
]

def get_already_reviewed():
    """Check which indicators already have reviews."""
    reviewed = set()
    if os.path.exists(REVIEWS_DIR):
        for f in os.listdir(REVIEWS_DIR):
            if f.endswith('.md'):
                reviewed.add(f.replace('.md', ''))
    return reviewed

def get_already_queued():
    """Check which indicators are already in the queue."""
    queued = set()
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    slug = line.split('|')[0].strip()
                    if slug:
                        queued.add(slug)
    return queued

def fill(auto=False, count=20):
    reviewed = get_already_reviewed()
    queued = get_already_queued()
    
    available = []
    for slug, name, ctype, cat in INDICATORS:
        if slug not in reviewed and slug not in queued:
            available.append((slug, name, ctype, cat))
    
    print(f"Indicators already reviewed: {len(reviewed)}")
    print(f"Already in queue: {len(queued)}")
    print(f"Available to add: {len(available)}")
    
    if not available:
        print("✅ Queue is full! No new indicators to add.")
        return 0
    
    if auto:
        random.shuffle(available)
        to_add = available[:count]
    else:
        print("\nAvailable indicators:")
        for i, (slug, name, ctype, cat) in enumerate(available, 1):
            print(f"  {i:3d}. {name} ({cat})")
        print(f"\nEnter numbers to add (e.g. '1 3 5-10'), or 'all':")
        choice = input("> ").strip()
        if choice == 'all':
            to_add = available
        else:
            to_add = []
            for part in choice.split():
                if '-' in part:
                    start, end = part.split('-')
                    for i in range(int(start)-1, int(end)):
                        if i < len(available):
                            to_add.append(available[i])
                else:
                    idx = int(part) - 1
                    if idx < len(available):
                        to_add.append(available[idx])
    
    if not to_add:
        print("No indicators selected.")
        return 0
    
    # Append to queue
    with open(QUEUE_FILE, 'a') as f:
        for slug, name, ctype, cat in to_add:
            f.write(f"{slug}|{name}|{ctype}|{cat}\n")
    
    print(f"✅ Added {len(to_add)} indicators to queue!")
    print(f"   Queue now has {queued.__len__() + len(to_add)} items pending")
    return len(to_add)

if __name__ == "__main__":
    auto = '--auto' in sys.argv
    fill(auto=auto)
