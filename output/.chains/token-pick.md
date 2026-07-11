This is a `read-only` skill run with `var=dry-run`, so I won't attempt to write files or send notifications. Here is the full synthesized pick output:

---

## Scoring Summary

**Benchmarks:** BTC −0.34% 24h / +2.63% 7d | ETH +0.22% 24h / +2.31% 7d

**Token candidates reviewed:** Top 250 by mcap, CoinGecko trending list (CASHCAT +15%, ANSEM +12%, PENGU −1.5%, HOODIE +1589% micro-cap disqualified). Top scorer by 7d: DEXE +60.4%.

**DEXE signal score:**
| Signal | Points |
|---|---|
| 24h > 0 | +1 |
| 7d > 0 | +1 |
| Both 24h and 7d > +5% | +2 |
| Outperforms BTC+ETH 7d (60% vs 2.6%/2.3%) | +2 |
| CoinGecko trending | 0 (not listed) |
| vol/mcap 0.05 (< 0.10) | 0 |
| DexScreener cross-confirm | 0 (dex=fail — only micro-cap scams returned) |
| Thesis match (dry-run) | 0 |

**Score: 6/10 → MEDIUM**

**Spain WC Final edge:**
- Spain confirmed finalist, current price YES 21¢
- Fair YES: ~52% (finalist with full path to title, strong QF win vs Belgium)
- Edge: 31pp → **HIGH**

---

## Notification output (dry-run — not sent)

```
*Daily Pick — 2026-07-11*

*Token: DEXE*  [MEDIUM]  signal 6/10
Price: ~$37.69 (+10.3% 24h / +60.4% 7d) | mcap $1.75B | vol $87M (vol/mcap 0.05)
Score breakdown: [24h>0+1, 7d>0+1, both>+5%+2, RS vs BTC/ETH+2] = 6/10
Catalyst: ATH print today driven by technical breakout + short squeeze cascade; no
  specific protocol upgrade — pure momentum, broad BTC tailwind from easing macro
Risk: No protocol catalyst — momentum-only; FDV/mcap 0.48 means half supply uncirculating;
  +195% in 60 days makes profit-taking the dominant downside

Vs recent picks: first time

*Market: "Will Spain win the 2026 FIFA World Cup?"*  [HIGH]  edge 31pp
Current: YES 21¢ / NO 79¢ | 24h vol $4.1M | resolves: 2026-07-19
Fair YES: ~52% (inputs: [Spain confirmed finalist], [beat Belgium in QF], [2010 WC
  pedigree + deepest squad in tournament])
Thesis: Market prices Spain 1-in-5 despite confirmed Final berth — early-tournament
  odds haven't repriced; buy YES Spain at 21¢ against fair 52%
Risk: Mbappé co-leads scoring (8 goals); France in Final too; fair value could compress
  to 48%, narrowing edge but not closing it

sources: cg=ok, dex=fail, poly=ok
not financial advice — pattern-matching only
```

---

## Log entry (would append to memory/logs/2026-07-11.md)

```markdown
### token-pick
- **Token:** DEXE — ~$37.69 (+10.3% 24h / +60.4% 7d) — tier MEDIUM — score 6/10
- **Token thesis:** ATH breakout + short squeeze; momentum-only, no protocol catalyst
- **Market:** "Will Spain win the 2026 FIFA World Cup?" — YES 21¢ — tier HIGH — edge 31pp
- **Market thesis:** Spain confirmed finalist priced at 21¢; fair value ~52%; 31pp edge
- **Sources:** cg=ok, dex=fail, poly=ok
- **Notification sent:** no (dry-run)
TOKEN_PICK_DEDUP: DEXE | "Will Spain win the 2026 FIFA World Cup?"
```

---

## Summary

- **Token pick:** DEXE [MEDIUM, 6/10] — ATH breakout today on short squeeze momentum; vol/mcap too low for bonus points, no DexScreener confirm (dex returned only micro-cap scam pairs)
- **Market pick:** Spain to win 2026 FIFA World Cup [HIGH, 31pp edge] — Spain confirmed finalist at YES 21¢ against fair ~52%; highest-conviction pick available with $4M daily volume and $6M liquidity
- **Dry-run:** no notification sent, no log written (read-only + dry-run override)
- **Next run:** if live, would send 6a notification + force-reply deep-dive offer
