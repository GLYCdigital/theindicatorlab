#!/usr/bin/env python3
"""
P&L Dashboard — generates daily Trading Signal report with charts.
Reads bot state/logs, plots P&L, posts to Telegram.

Run: python3 til/scripts/pnl_dashboard.py
"""

import json, datetime, os, re, sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

TRADE_DIR = "/Users/Gabriel 1/.openclaw/workspace/trade"
TIL_DIR = "/Users/Gabriel 1/.openclaw/workspace/til"
OUTPUT_DIR = "/Users/Gabriel 1/.openclaw/workspace/til/dashboard"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Token and chat ID read from env only — Gemma's old token was revoked
# Set via cron sourcing ~/.openclaw/secrets/env.sh
TELEGRAM_TOKEN = os.environ.get('TIL_PNL_BOT_TOKEN', '')
TELEGRAM_CHAT = os.environ.get('TIL_PNL_CHAT_ID', '-1003250348876')

if not TELEGRAM_TOKEN:
    print("WARNING: TIL_PNL_BOT_TOKEN not set — Telegram disabled")

NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# ── Color scheme ────────────────────────────────────────────────────────────
BG = '#1a1b2e'
CARD = '#232544'
GREEN = '#00e6b0'
RED = '#ff6b6b'
TEXT = 'white'
MUTED = '#8888aa'

plt.style.use('dark_background')
plt.rcParams.update({
    'figure.facecolor': BG,
    'axes.facecolor': BG,
    'axes.edgecolor': '#333',
    'axes.labelcolor': MUTED,
    'xtick.color': MUTED,
    'ytick.color': MUTED,
    'grid.color': '#2a2a44',
    'grid.alpha': 0.3,
    'text.color': TEXT,
    'font.size': 11,
})


def load_json(name):
    try:
        with open(os.path.join(TRADE_DIR, name)) as f:
            return json.load(f)
    except:
        return {}


def parse_log(name):
    """Extract buy/sell trades from bot log files."""
    trades = []
    path = os.path.join(TRADE_DIR, name)
    if not os.path.exists(path):
        return trades
    with open(path) as f:
        for line in f:
            m = re.search(r'Paper fill: (buy|sell) ([\d.]+) @ \$?([\d.]+)', line)
            if m:
                side, amount, price = m.groups()
                trades.append({
                    'side': side,
                    'amount': float(amount),
                    'price': float(price),
                })
    return trades


def calc_pnl(trades):
    """Calculate cumulative P&L from trade list."""
    position = 0
    cost_basis = 0
    realized_pnl = 0
    pnl_history = [(0, 0)]  # (trade_num, cumulative_pnl)
    
    for i, t in enumerate(trades):
        if t['side'] == 'buy':
            position += t['amount']
            cost_basis += t['amount'] * t['price']
        else:  # sell
            if position > 0:
                avg_cost = cost_basis / position
                trade_pnl = t['amount'] * (t['price'] - avg_cost)
                realized_pnl += trade_pnl
                # Reduce position
                sell_ratio = t['amount'] / position if position > 0 else 0
                cost_basis *= (1 - sell_ratio)
                position -= t['amount']
                pnl_history.append((i + 1, realized_pnl))
    
    return realized_pnl, pnl_history


def make_pnl_chart(grid_pnl, dca_pnl, trend_pnl, grid_history, dca_history, trend_history):
    """Generate the P&L chart."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 10), gridspec_kw={'height_ratios': [3, 2]})
    
    # ── Top: Combined P&L ──
    ax = axes[0, 0]
    ax.set_title('Cumulative P&L', fontsize=15, fontweight='bold', color=TEXT, pad=12)
    
    for history, label, color in [
        (grid_history, 'Grid (ETH/USDT)', GREEN),
        (dca_history, 'DCA (ETH/BTC)', '#4dabf7'),
        (trend_history, 'Trend (BTC/USDT)', '#fcc419')
    ]:
        if len(history) > 1:
            xs = [h[0] for h in history]
            ys = [h[1] for h in history]
            ax.plot(xs, ys, label=label, color=color, linewidth=2, alpha=0.9)
            ax.fill_between(xs, ys, alpha=0.1, color=color)
    
    ax.axhline(y=0, color='#555', linewidth=0.5)
    ax.set_ylabel('P&L ($)', color=MUTED)
    ax.legend(loc='upper left', framealpha=0.3)
    ax.grid(True, alpha=0.2)
    
    # ── Top Right: Summary cards ──
    ax = axes[0, 1]
    ax.axis('off')
    
    total_pnl = grid_pnl + dca_pnl + trend_pnl
    
    summary_lines = [
        ("Trading Dashboard", NOW, 18, True),
        ("", "", 8, False),
        ("Total P&L", f"${total_pnl:+.2f}", 24, True),
        ("", "", 16, False),
        ("Grid Bot (ETH/USDT)", f"${grid_pnl:+.2f}", 14, False),
        ("DCA Bot (ETH/BTC)", f"${dca_pnl:+.2f}", 14, False),
        ("Trend Bot (BTC/USDT)", f"${trend_pnl:+.2f}", 14, False),
        ("", "", 24, False),
        ("Mode: Paper Trading", "", 12, False),
    ]
    
    y_pos = 0.92
    for label, value, size, bold in summary_lines:
        if bold and value:
            ax.text(0.1, y_pos, f"{label} {value}", fontsize=size, fontweight='bold',
                   color=GREEN if '+' in str(value) and '$' in str(value) else TEXT,
                   transform=ax.transAxes)
        elif value:
            ax.text(0.1, y_pos, f"{label}  {value}", fontsize=size, color=TEXT,
                   transform=ax.transAxes)
        else:
            ax.text(0.1, y_pos, f"{label}", fontsize=size, color=MUTED,
                   transform=ax.transAxes)
        y_pos -= 0.06 * (size / 12)
    
    # ── Bottom: Bot status ──
    ax = axes[1, 0]
    ax.axis('off')
    
    bots = [
        ("Grid Bot", "ETH/USDT", "$500", "grid_bot.pid", grid_pnl),
        ("DCA Bot", "ETH/BTC", "$200", "dca_bot.pid", dca_pnl),
        ("Trend Bot", "BTC/USDT", "$300", "trend_bot.pid", trend_pnl),
    ]
    
    status_lines = [("Bot Status", "", 16, True), ("", "", 8, False)]
    for name, pair, invest, pid_file, pnl in bots:
        pid_path = os.path.join(TRADE_DIR, pid_file)
        running = False
        try:
            pid = int(open(pid_path).read().strip())
            os.kill(pid, 0)
            running = True
        except:
            pass
        
        status = "✅ Running" if running else "❌ Stopped"
        status_lines.append((f"{name} ({pair})", f"{status} | Invest: {invest} | P&L: ${pnl:+.2f}", 12, False))
    
    y_pos = 0.85
    for label, value, size, bold in status_lines:
        if bold:
            ax.text(0.1, y_pos, label, fontsize=size, fontweight='bold', color=TEXT, transform=ax.transAxes)
        elif value:
            ax.text(0.1, y_pos, f"{label}  {value}", fontsize=size, color=TEXT, transform=ax.transAxes)
        y_pos -= 0.07
    
    # ── Bottom Right: Recent trades ──
    ax = axes[1, 1]
    ax.axis('off')
    
    all_trades = []
    for log_file in ['grid_bot.log', 'dca_bot.log', 'trend_bot.log']:
        for t in parse_log(log_file):
            all_trades.append(t)
    latest = all_trades[-10:] if all_trades else []
    
    ax.text(0.1, 0.92, "Recent Trades", fontsize=14, fontweight='bold', color=TEXT, transform=ax.transAxes)
    if latest:
        y_pos = 0.78
        for t in reversed(latest):
            icon = 'BUY' if t['side'] == 'buy' else 'SELL'
            label = f"{icon} {t['side'].upper()} {t['amount']:.4f} @ ${t['price']:.2f}"
            ax.text(0.1, y_pos, label, fontsize=10, color=TEXT, transform=ax.transAxes, family='monospace')
            y_pos -= 0.07
    else:
        ax.text(0.1, 0.78, "No recent trades", fontsize=12, color=MUTED, transform=ax.transAxes)
    
    plt.tight_layout(pad=2)
    path = os.path.join(OUTPUT_DIR, "pnl_dashboard.png")
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    return path


def post_to_telegram(image_path, caption):
    """Post dashboard image to Telegram group."""
    import urllib.request
    
    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="chat_id"\r\n\r\n'
        f'{TELEGRAM_CHAT}\r\n'
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="caption"\r\n\r\n'
        f'{caption}\r\n'
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="photo"; filename="pnl.png"\r\n'
        f'Content-Type: image/png\r\n\r\n'
    ).encode() + image_data + f'\r\n--{boundary}--\r\n'.encode()
    
    req = urllib.request.Request(
        f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto',
        data=body,
        headers={'Content-Type': f'multipart/form-data; boundary={boundary}'}
    )
    
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except Exception as e:
        print(f"Telegram post failed: {e}")
        return None


def main():
    print("Loading bot states...")
    
    # Parse trades from logs
    grid_trades = parse_log("grid_bot.log")
    dca_trades = parse_log("dca_bot.log")
    trend_trades = parse_log("trend_bot.log")
    
    print(f"  Grid trades: {len(grid_trades)}")
    print(f"  DCA trades: {len(dca_trades)}")
    print(f"  Trend trades: {len(trend_trades)}")
    
    # Calculate P&L
    grid_pnl, grid_history = calc_pnl(grid_trades)
    dca_pnl, dca_history = calc_pnl(dca_trades)
    trend_pnl, trend_history = calc_pnl(trend_trades)
    
    print(f"  Grid P&L: ${grid_pnl:+.2f}")
    print(f"  DCA P&L: ${dca_pnl:+.2f}")
    print(f"  Trend P&L: ${trend_pnl:+.2f}")
    print(f"  Total P&L: ${grid_pnl + dca_pnl + trend_pnl:+.2f}")
    
    # Generate chart
    print("Generating chart...")
    chart_path = make_pnl_chart(
        grid_pnl, dca_pnl, trend_pnl,
        grid_history, dca_history, trend_history
    )
    print(f"  Chart saved: {chart_path}")
    
    # Post to Telegram
    print("Posting to Telegram...")
    caption = f"📊 Daily Trading Dashboard — {NOW.split()[0]}\nAll bots in paper mode"
    result = post_to_telegram(chart_path, caption)
    
    if result and result.get('ok'):
        print("✅ Dashboard posted to Telegram!")
    else:
        print("⚠️  Telegram post had an issue")
    
    print("\nDone!")


if __name__ == "__main__":
    main()
