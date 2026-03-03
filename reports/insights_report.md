# Spotify Streaming Trends — Insights Report
**Analyst:** Victor Adeyemi  
**Dataset:** 89,740 tracks | 2,081,378 chart entries | 72 countries  
**Period:** October 2023 – June 2025  
**Tools:** Python (pandas, matplotlib, seaborn), SQL (SQLite)

---

## Executive Summary

This report analyses Spotify streaming trends across 72 countries using 
two datasets: a 90K-track audio features dataset and a 2M+ row daily 
charts dataset spanning nearly two years. The analysis surfaces insights 
across four areas: genre popularity, artist dominance, market 
characteristics, and audio feature patterns — the kind of intelligence 
a streaming platform would use to inform editorial, licensing, and 
product decisions.

---

## 1. Genre Landscape

K-pop leads all genres with an average popularity score of 59.4, followed 
closely by pop-film (59.1) and metal (56.4). This is notable because 
k-pop's dominance is not just a volume story — the dataset was sampled 
evenly across genres, meaning k-pop outperforms on quality of engagement 
rather than sheer catalogue size.

K-pop tracks also show strong audio characteristics that may explain their 
performance: above-average danceability (0.642) and energy (0.683), 
suggesting listeners are drawn to high-energy, rhythmically engaging 
content regardless of language barrier.

**Business implication:** Playlist curation and recommendation algorithms 
should weight k-pop tracks more heavily in markets where danceability and 
energy scores correlate with engagement — particularly in Asia-Pacific 
and Latin American markets where this analysis shows high energy 
preferences.

---

## 2. Artist Dominance

Billie Eilish is the most globally dominant artist in this dataset with 
31,457 chart appearances across 67 of 72 countries — the broadest 
geographic reach of any artist analysed. This near-universal presence 
suggests her appeal transcends regional music preferences, making her 
a reliable anchor for global playlist strategies.

The top 5 most charting artists are:

| Artist | Chart Appearances | Countries | Avg Popularity |
|--------|------------------|-----------|----------------|
| Billie Eilish | 31,457 | 67 | 94.1 |
| Bad Bunny | 30,997 | 50 | 90.4 |
| Sabrina Carpenter | 27,894 | 64 | 91.8 |
| KAROL G | 20,406 | 26 | 88.4 |
| Jimin | 18,401 | 51 | 84.5 |

A key contrast: Bad Bunny has nearly as many appearances as Billie Eilish 
but in only 50 countries, indicating concentrated dominance in Latin 
markets. KAROL G shows even sharper concentration — 20,406 appearances 
in just 26 countries — pointing to extremely deep penetration in a 
specific regional market rather than broad global reach.

**Business implication:** Artist-market fit matters as much as raw 
popularity. Regional editorial teams should leverage concentrated 
dominance (Bad Bunny, KAROL G) for targeted market campaigns rather 
than treating all top artists as globally interchangeable.

---

## 3. Global #1 Performance

The song that reached #1 in the most countries is Mariah Carey's 
*All I Want for Christmas Is You*, tied with Jimin's *Who* — both 
reaching the top spot in 26 countries. This is a striking finding: 
a 1994 Christmas song competing directly with a 2024 K-pop release 
for global #1 dominance demonstrates the enduring power of catalogue 
music and seasonal streaming spikes.

*Die With A Smile* by Lady Gaga and Bruno Mars achieved the highest 
average popularity score among #1 songs at 98.9 — the closest to a 
perfect score in this entire dataset — while reaching #1 in 18 
countries, suggesting that peak popularity does not always translate 
to the widest geographic reach.

**Business implication:** Seasonal catalogue reactivation (Christmas 
music, summer hits) represents a predictable, high-ROI opportunity. 
Spotify should build automated playlist and marketing triggers around 
known seasonal performers rather than relying solely on new releases 
to drive chart activity.

---

## 4. Audio Features & Chart Performance

Rank 1 songs versus Rank 50 songs show consistent audio differences 
across every measured dimension:

| Feature | Rank 1 | Rank 50 | Difference |
|---------|--------|---------|------------|
| Danceability | 0.688 | 0.670 | +0.018 |
| Energy | 0.665 | 0.648 | +0.017 |
| Valence | 0.583 | 0.542 | +0.041 |
| Acousticness | 0.255 | 0.281 | -0.026 |
| Tempo | 122.8 | 122.5 | +0.3 BPM |

The most significant differentiator is valence — the musical measure 
of positivity. Rank 1 songs score 7.6% higher on valence than Rank 50 
songs. Combined with lower acousticness, this paints a clear picture: 
the songs that reach #1 globally tend to be more positive, more 
danceable, more energetic, and less acoustic than their lower-ranked 
counterparts.

**Business implication:** These audio feature thresholds could serve 
as input signals in Spotify's recommendation and editorial promotion 
models — tracks meeting the high-valence, high-danceability, 
low-acousticness profile are statistically more likely to perform 
at the top of charts.

---

## 5. Market Characteristics

Bulgaria (BG) leads all 72 markets in average energy score (0.801) 
among top 10 charting tracks, followed by Japan (0.765) and Romania 
(0.744). This reveals meaningful cultural variation in listening 
preferences that has direct implications for market-specific playlist 
curation.

Notably, Japan's high energy preference (0.765) paired with moderate 
danceability (0.621) differs from Latin markets like Mexico (energy: 
0.698, danceability: 0.743) — suggesting Japan favours intensity over 
rhythm while Latin markets favour both equally.

**Business implication:** A single global playlist strategy is 
insufficient. Market-specific audio feature profiling should inform 
localised playlist curation, particularly in high-engagement markets 
like Bulgaria, Japan, and Romania where listener preferences diverge 
significantly from the global average.

---

## 6. Explicit Content Performance

Explicit tracks represent 32.6% of all chart entries but perform 
marginally better on average rank (25.0 vs 25.7) and significantly 
better on popularity (77.9 vs 74.7). This suggests that explicit 
content, while a smaller share of the catalogue, punches above its 
weight in engagement terms.

**Business implication:** Content filtering settings that default to 
hiding explicit tracks may be suppressing some of the platform's 
highest-performing content from discovery surfaces. A/B testing 
explicit content visibility settings against engagement metrics 
could surface meaningful uplift opportunities.

---

## Conclusions & Recommendations

Three strategic recommendations emerge from this analysis:

**1. Invest in K-pop and high-energy genres for global growth.** 
K-pop's top popularity ranking combined with strong audio feature 
scores suggests it is underrepresented relative to its engagement 
potential in non-Asian markets.

**2. Build market-specific audio profiles into recommendation systems.** 
The energy and danceability variance across 72 markets is too 
significant to ignore. Localised curation using market-level audio 
feature benchmarks would improve relevance and time-on-platform.

**3. Automate seasonal catalogue reactivation.** The sustained 
global dominance of *All I Want for Christmas Is You* after 30 years 
is a signal, not a coincidence. Building predictive seasonal triggers 
into editorial workflows would capture this value systematically 
rather than reactively.

---

*Analysis conducted by Victor Adeyemi as part of a data analytics 
portfolio project. Dataset sourced from Kaggle. Full code and 
methodology available at github.com/[avikitoki]/spotify-streaming-trends-analysis*