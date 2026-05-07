#!/usr/bin/env python3
import yfinance as yf, mplfinance as mpf, matplotlib, pandas as pd, os, sys, argparse
matplotlib.use('Agg')

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../../theindicatorlab/static/screenshots')
os.makedirs(OUTPUT_DIR, exist_ok=True)

TICKERS = {
    "awesome-oscillator":"AAPL","rsi":"TSLA","macd":"MSFT","bollinger-bands":"AMZN",
    "supertrend":"GOOGL","ichimoku-cloud":"BTC-USD","volume-profile":"AAPL",
    "vwap":"MSFT","parabolic-sar":"TSLA","stochastic-rsi":"AMZN","keltner":"GOOGL",
    "ema":"AAPL","donchian":"TSLA","atr":"MSFT","money-flow":"AMZN",
}

mc = mpf.make_marketcolors(up='#26a69a', down='#ef5350', edge='inherit', wick='inherit', volume='inherit')
style = mpf.make_mpf_style(marketcolors=mc, gridstyle='', figcolor='#1a1b2e', facecolor='#1a1b2e')

def gen(slug, itype, ticker=None):
    ticker = ticker or TICKERS.get(itype, "AAPL")
    raw = yf.download(ticker, period="4mo", interval="1d", progress=False)
    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)
    df = raw.copy()
    for c in ['Open','High','Low','Close','Volume']:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df = df.dropna()
    apds = []

    if itype == "awesome-oscillator":
        df['m'] = (df['High']+df['Low'])/2; df['a']=df['m'].rolling(5).mean()-df['m'].rolling(34).mean()
        c = ['#26a69a' if v>=0 else '#ef5350' for v in df['a'].values]
        apds = [mpf.make_addplot(df['a'], type='bar', panel=1, color=c, ylabel='AO', alpha=0.7)]
    elif itype == "rsi":
        d=df['Close'].diff(); g=d.where(d>0,0).rolling(14).mean(); l=(-d.where(d<0,0)).rolling(14).mean()
        df['r']=100-(100/(1+g/l))
        apds=[mpf.make_addplot(df['r'],panel=1,color='#7c4dff',ylabel='RSI')]
        mpf.plot(df,type='candle',style=style,addplot=apds,volume=True,
                hlines=dict(hlines=[70,30],colors=['#ef5350','#26a69a'],linestyle='--'),
                savefig=f"{OUTPUT_DIR}/{slug}.png",tight_layout=True,figsize=(12,7)); return
    elif itype == "macd":
        e1=df['Close'].ewm(span=12).mean(); e2=df['Close'].ewm(span=26).mean()
        df['m']=e1-e2; df['s']=df['m'].ewm(span=9).mean(); df['h']=df['m']-df['s']
        c=['#26a69a' if v>=0 else '#ef5350' for v in df['h'].values]
        apds=[mpf.make_addplot(df['m'],panel=1,color='#2979ff',ylabel='MACD'),
              mpf.make_addplot(df['s'],panel=1,color='#ff6d00'),
              mpf.make_addplot(df['h'],type='bar',panel=1,color=c,alpha=0.5)]
    elif itype == "bollinger-bands":
        df['s']=df['Close'].rolling(20).mean(); std=df['Close'].rolling(20).std()
        df['u']=df['s']+2*std; df['l']=df['s']-2*std
        apds=[mpf.make_addplot(df['s'],color='#ff6d00',width=0.8),
              mpf.make_addplot(df['u'],color='#7c4dff',linestyle='--',width=0.5),
              mpf.make_addplot(df['l'],color='#7c4dff',linestyle='--',width=0.5)]
        mpf.plot(df,type='candle',style=style,addplot=apds,volume=True,
                fill_between=dict(y1=df['u'].values,y2=df['l'].values,alpha=0.1,color='#7c4dff'),
                savefig=f"{OUTPUT_DIR}/{slug}.png",tight_layout=True,figsize=(12,7)); return
    elif itype == "supertrend":
        hl=(df['High']+df['Low'])/2; atr=df['High'].rolling(10).max()-df['Low'].rolling(10).min()
        df['u']=hl+3*atr; df['l']=hl-3*atr
        apds=[mpf.make_addplot(df['u'],color='#ef5350',linestyle='--',width=0.8,alpha=0.6),
              mpf.make_addplot(df['l'],color='#26a69a',linestyle='--',width=0.8,alpha=0.6)]
    elif itype == "ichimoku-cloud":
        h9=df['High'].rolling(9).max(); l9=df['Low'].rolling(9).min()
        h26=df['High'].rolling(26).max(); l26=df['Low'].rolling(26).min()
        h52=df['High'].rolling(52).max(); l52=df['Low'].rolling(52).min()
        t=(h9+l9)/2; k=(h26+l26)/2; sa=((t+k)/2).shift(26); sb=((h52+l52)/2).shift(26); c=df['Close'].shift(-26)
        apds=[mpf.make_addplot(t,color='#ef5350',width=0.8),
              mpf.make_addplot(k,color='#2979ff',width=0.8),
              mpf.make_addplot(c,color='#ff6d00',width=0.8,alpha=0.5)]
        mpf.plot(df,type='candle',style=style,addplot=apds,volume=True,
                fill_between=dict(y1=sa.values,y2=sb.values,alpha=0.2,color='#26a69a'),
                savefig=f"{OUTPUT_DIR}/{slug}.png",tight_layout=True,figsize=(12,7)); return
    elif itype == "volume-profile":
        df['v']=(df['Close']*df['Volume']).rolling(20).sum()/df['Volume'].rolling(20).sum()
        apds=[mpf.make_addplot(df['v'],color='#7c4dff',width=1.2,ylabel='VP')]
    elif itype == "vwap":
        df['v']=(df['Close']*df['Volume']).cumsum()/df['Volume'].cumsum()
        apds=[mpf.make_addplot(df['v'],color='#ff6d00',width=1.2,ylabel='VWAP')]
    elif itype == "parabolic-sar":
        atr=df['High'].rolling(10).max()-df['Low'].rolling(10).min()
        df['s']=df['Close'].rolling(5).min()-atr*0.02
        apds=[mpf.make_addplot(df['s'],type='scatter',color='#2979ff',ylabel='SAR',marker='.',markersize=20)]
    elif itype == "stochastic-rsi":
        d=df['Close'].diff(); g=d.where(d>0,0).rolling(14).mean(); l=(-d.where(d<0,0)).rolling(14).mean()
        df['s']=100-(100/(1+g/l)); df['s']=df['s'].rolling(3).mean()
        apds=[mpf.make_addplot(df['s'],panel=1,color='#e17055',ylabel='Stoch RSI')]
        mpf.plot(df,type='candle',style=style,addplot=apds,volume=True,
                hlines=dict(hlines=[80,20],colors=['#ef5350','#26a69a'],linestyle='--'),
                savefig=f"{OUTPUT_DIR}/{slug}.png",tight_layout=True,figsize=(12,7)); return
    elif itype == "keltner":
        df['s']=df['Close'].rolling(20).mean(); atr=df['High'].rolling(10).max()-df['Low'].rolling(10).min()
        df['u']=df['s']+2*atr; df['l']=df['s']-2*atr
        apds=[mpf.make_addplot(df['s'],color='#ff6d00',width=0.8),
              mpf.make_addplot(df['u'],color='#7c4dff',linestyle='--',width=0.5),
              mpf.make_addplot(df['l'],color='#7c4dff',linestyle='--',width=0.5)]
    elif itype == "ema":
        df['e12']=df['Close'].ewm(span=12).mean(); df['e26']=df['Close'].ewm(span=26).mean()
        apds=[mpf.make_addplot(df['e12'],color='#2979ff',width=0.8),
              mpf.make_addplot(df['e26'],color='#ff6d00',width=0.8)]
    elif itype == "donchian":
        df['u']=df['High'].rolling(20).max(); df['l']=df['Low'].rolling(20).min(); df['m']=(df['u']+df['l'])/2
        apds=[mpf.make_addplot(df['u'],color='#7c4dff',width=0.5,linestyle='--'),
              mpf.make_addplot(df['m'],color='#ff6d00',width=0.5),
              mpf.make_addplot(df['l'],color='#7c4dff',width=0.5,linestyle='--')]
    elif itype == "atr":
        df['a']=df['High'].rolling(14).max()-df['Low'].rolling(14).min()
        apds=[mpf.make_addplot(df['a'],panel=1,color='#e17055',ylabel='ATR')]
    elif itype == "money-flow":
        t=(df['High']+df['Low']+df['Close'])/3; mf=t*df['Volume']
        p=mf.where(t>t.shift(1),0).rolling(14).sum(); n=mf.where(t<t.shift(1),0).rolling(14).sum()
        df['m']=100-(100/(1+p/n))
        apds=[mpf.make_addplot(df['m'],panel=1,color='#7c4dff',ylabel='MFI')]
        mpf.plot(df,type='candle',style=style,addplot=apds,volume=True,
                hlines=dict(hlines=[80,20],colors=['#ef5350','#26a69a'],linestyle='--'),
                savefig=f"{OUTPUT_DIR}/{slug}.png",tight_layout=True,figsize=(12,7)); return
    else:
        raise ValueError(f"Unknown type: {itype}")

    mpf.plot(df,type='candle',style=style,addplot=apds,volume=True,
            savefig=f"{OUTPUT_DIR}/{slug}.png",tight_layout=True,figsize=(12,7))
    print(f"✅ {OUTPUT_DIR}/{slug}.png")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("slug"); p.add_argument("type", choices=list(TICKERS.keys()))
    p.add_argument("ticker", nargs="?")
    a = p.parse_args()
    gen(a.slug, a.type, a.ticker)
