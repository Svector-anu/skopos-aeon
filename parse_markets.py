import json, math, sys

with open('cg_markets.json') as f:
    data = json.load(f)

with open('cg_trending.json') as f:
    trending_data = json.load(f)

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usds','frax','usdp','nusd','mim','tether-gold','bridged-tether-solana'}
WRAPPED = {'wbtc','weth','steth','weeth','wsteth','cbeth','reth','lseth','ezeth','wbeth','rseth','meth','seth2','solvbtc','solvbtc-bbn','lombard-staked-btc','tbtc','wbtc-2'}

def is_stable(c):
    sym = c['symbol'].upper()
    name = (c['name'] or '').lower()
    cid = c['id']
    if cid in STABLE_IDS:
        return True
    if sym.startswith(('USD','EUR','GBP')) and len(sym) <= 6:
        return True
    if 'stablecoin' in name:
        return True
    return False

def is_wrapped(c):
    return c['id'] in WRAPPED

def fmt_price(p):
    if p is None:
        return 'n/a'
    if p >= 1000:
        return f"${p:,.0f}"
    if p >= 1:
        return f"${p:.4g}"
    if p >= 0.01:
        return f"${p:.4f}"
    return f"${p:.6f}"

def fmt_vol(v):
    if v is None:
        return 'n/a'
    if v >= 1e9:
        return f"${v/1e9:.2f}B"
    if v >= 1e6:
        return f"${v/1e6:.1f}M"
    if v >= 1e3:
        return f"${v/1e3:.0f}K"
    return f"${v:.0f}"

def fmt_mcap(v):
    if v is None:
        return 'n/a'
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    if v >= 1e6:
        return f"${v/1e6:.0f}M"
    return f"${v:.0f}"

def fmt_pct(p):
    if p is None:
        return 'n/a'
    s = '+' if p > 0 else ''
    return f"{s}{p:.1f}%"

filtered = [c for c in data if not is_stable(c) and not is_wrapped(c) and (c.get('total_volume') or 0) >= 1_000_000]
print(f"Filtered: {len(filtered)} coins (from {len(data)})")

# Market pulse
top100 = sorted(filtered, key=lambda c: c.get('market_cap_rank') or 9999)[:100]
green_count = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
chg_top50 = sorted([c.get('price_change_percentage_24h') or 0 for c in top100[:50]])
median_50 = chg_top50[len(chg_top50)//2]
print(f"Top-100 green: {green_count}/100, median top-50 24h: {median_50:.2f}%")

# Winners/losers
by_24h = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0)
losers = by_24h[:10]
winners = list(reversed(by_24h[-10:]))

# Trending
trending_coins = trending_data.get('coins', [])[:7]
trending_ids = set(t['item']['id'] for t in trending_coins)
trending_syms = set(t['item']['symbol'].upper() for t in trending_coins)

# Tag computation
def compute_tags(c, in_trending):
    tags = []
    chg24 = c.get('price_change_percentage_24h') or 0
    chg7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 9999
    sym = c['symbol'].upper()

    is_winner = chg24 > 0
    is_loser = chg24 < 0

    if in_trending and is_winner:
        tags.append('[TRENDING+UP]')
    elif in_trending and is_loser:
        tags.append('[TRENDING+DOWN]')

    if chg24 > 15 and chg7d > 25:
        tags.append('[BREAKOUT]')

    if chg24 > 20 and chg7d < 0:
        tags.append('[FADE]')

    if chg24 < -10:
        vol_to_mcap = vol / mcap if mcap > 0 else 0
        if vol_to_mcap > 0.25:
            tags.append('[CAPITULATION]')

    if rank > 150 and chg24 > 30:
        tags.append('[PUMP-RISK]')

    if mcap > 0 and mcap < 50_000_000:
        tags.append('[MICROCAP]')
    elif rank <= 20:
        tags.append('[MAJOR]')

    return tags[:2]

print("\n=== WINNERS (with tags) ===")
results_winners = []
for c in winners:
    in_t = c['id'] in trending_ids or c['symbol'].upper() in trending_syms
    tags = compute_tags(c, in_t)
    results_winners.append((c, tags))
    print(f"{c['symbol']} ({c['name']}) rank#{c.get('market_cap_rank','?')} price={fmt_price(c['current_price'])} 24h={fmt_pct(c.get('price_change_percentage_24h'))} 7d={fmt_pct(c.get('price_change_percentage_7d_in_currency'))} 1h={fmt_pct(c.get('price_change_percentage_1h_in_currency'))} vol={fmt_vol(c['total_volume'])} mcap={fmt_mcap(c.get('market_cap'))} tags={tags}")

print("\n=== LOSERS (with tags) ===")
results_losers = []
for c in losers:
    in_t = c['id'] in trending_ids or c['symbol'].upper() in trending_syms
    tags = compute_tags(c, in_t)
    results_losers.append((c, tags))
    print(f"{c['symbol']} ({c['name']}) rank#{c.get('market_cap_rank','?')} price={fmt_price(c['current_price'])} 24h={fmt_pct(c.get('price_change_percentage_24h'))} 7d={fmt_pct(c.get('price_change_percentage_7d_in_currency'))} 1h={fmt_pct(c.get('price_change_percentage_1h_in_currency'))} vol={fmt_vol(c['total_volume'])} mcap={fmt_mcap(c.get('market_cap'))} tags={tags}")

print("\n=== TRENDING ===")
# Build a lookup by id for trending
coin_lookup = {c['id']: c for c in data}
for t in trending_coins:
    item = t['item']
    cid = item['id']
    sym = item['symbol']
    name = item['name']
    rank = item.get('market_cap_rank', 'n/a')
    price = item.get('data', {}).get('price', None)
    chg24_str = item.get('data', {}).get('price_change_percentage_24h', {})
    chg24 = chg24_str.get('usd', None) if isinstance(chg24_str, dict) else None
    if price is None:
        # try lookup
        lc = coin_lookup.get(cid)
        if lc:
            price = lc['current_price']
            chg24 = lc.get('price_change_percentage_24h')
    # tags
    in_winners = any(c['id'] == cid for c,_ in results_winners)
    in_losers = any(c['id'] == cid for c,_ in results_losers)
    tag = '[TRENDING+UP]' if in_winners else ('[TRENDING+DOWN]' if in_losers else '')
    print(f"{name} ({sym}) rank#{rank} price={fmt_price(price)} 24h={fmt_pct(chg24)} {tag}")

print(f"\nPulse: {green_count}/100 green, median top-50 = {fmt_pct(median_50)}")
