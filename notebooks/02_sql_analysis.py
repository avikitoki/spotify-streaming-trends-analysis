# ══════════════════════════════════════════════════════════════════
# SPOTIFY STREAMING TRENDS ANALYSIS
# Notebook 2: SQL Analysis via SQLite
# ══════════════════════════════════════════════════════════════════

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid")
GREEN = "#1DB954"

# ── Load CSVs into SQLite in-memory database ───────────────────────
print("Loading data into SQLite...")
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("data/spotify.db")

tracks = pd.read_csv("data/processed/tracks_clean.csv")
charts = pd.read_csv("data/processed/charts_clean.csv")

tracks.to_sql("tracks", conn, index=False, if_exists="replace")
charts.to_sql("charts", conn, index=False, if_exists="replace")
print(" Data loaded into SQLite")
print(f"   tracks rows: {pd.read_sql('SELECT COUNT(*) as n FROM tracks', conn).iloc[0,0]:,}")
print(f"   charts rows: {pd.read_sql('SELECT COUNT(*) as n FROM charts', conn).iloc[0,0]:,}")


# ══════════════════════════════════════════════════════════════════
# Q1 — Top 10 genres by average popularity
# ══════════════════════════════════════════════════════════════════
q1 = pd.read_sql("""
    SELECT 
        track_genre,
        COUNT(*) AS track_count,
        ROUND(AVG(popularity), 2) AS avg_popularity,
        ROUND(AVG(danceability), 3) AS avg_danceability,
        ROUND(AVG(energy), 3) AS avg_energy
    FROM tracks
    GROUP BY track_genre
    ORDER BY avg_popularity DESC
    LIMIT 10
""", conn)

print("\n── Q1: Top 10 Genres by Avg Popularity ──")
print(q1.to_string(index=False))


# ══════════════════════════════════════════════════════════════════
# Q2 — Top 15 most charting artists globally
# ══════════════════════════════════════════════════════════════════
q2 = pd.read_sql("""
    SELECT 
        artists,
        COUNT(*) AS total_chart_appearances,
        ROUND(AVG(popularity), 1) AS avg_popularity,
        COUNT(DISTINCT country) AS countries_charted_in
    FROM charts
    GROUP BY artists
    ORDER BY total_chart_appearances DESC
    LIMIT 15
""", conn)

print("\n── Q2: Top 15 Most Charting Artists Globally ──")
print(q2.to_string(index=False))

fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(q2["artists"], q2["total_chart_appearances"], color=GREEN)
ax.set_xlabel("Total Chart Appearances")
ax.set_title("Top 15 Artists by Global Chart Appearances (SQL)")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("visuals/sql_01_top_artists.png")
print(" Saved: sql_01_top_artists.png")


# ══════════════════════════════════════════════════════════════════
# Q3 — Songs that hit #1 in the most countries
# ══════════════════════════════════════════════════════════════════
q3 = pd.read_sql("""
    SELECT 
        name,
        artists,
        COUNT(DISTINCT country) AS countries_reached_number_1,
        ROUND(AVG(popularity), 1) AS avg_popularity
    FROM charts
    WHERE daily_rank = 1
    GROUP BY name, artists
    ORDER BY countries_reached_number_1 DESC
    LIMIT 10
""", conn)

print("\n── Q3: Songs That Reached #1 in Most Countries ──")
print(q3.to_string(index=False))

fig, ax = plt.subplots(figsize=(12, 5))
labels = [f"{row['name'][:25]}\n({row['artists'][:20]})" for _, row in q3.iterrows()]
ax.barh(labels, q3["countries_reached_number_1"], color=GREEN)
ax.set_xlabel("Number of Countries Reached #1")
ax.set_title("Songs That Reached #1 in the Most Countries")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("visuals/sql_02_number1_countries.png")
print(" Saved: sql_02_number1_countries.png")


# ══════════════════════════════════════════════════════════════════
# Q4 — Audio profile: Rank 1 vs Rank 50
# ══════════════════════════════════════════════════════════════════
q4 = pd.read_sql("""
    SELECT
        CASE WHEN daily_rank = 1 THEN 'Rank 1' ELSE 'Rank 50' END AS rank_group,
        ROUND(AVG(danceability), 3) AS avg_danceability,
        ROUND(AVG(energy), 3) AS avg_energy,
        ROUND(AVG(valence), 3) AS avg_valence,
        ROUND(AVG(acousticness), 3) AS avg_acousticness,
        ROUND(AVG(tempo), 1) AS avg_tempo
    FROM charts
    WHERE daily_rank IN (1, 50)
    GROUP BY rank_group
""", conn)

print("\n── Q4: Audio Profile Rank 1 vs Rank 50 ──")
print(q4.to_string(index=False))


# ══════════════════════════════════════════════════════════════════
# Q5 — Countries that favour high-energy tracks
# ══════════════════════════════════════════════════════════════════
q5 = pd.read_sql("""
    SELECT
        country,
        ROUND(AVG(energy), 3) AS avg_energy,
        ROUND(AVG(danceability), 3) AS avg_danceability,
        ROUND(AVG(valence), 3) AS avg_valence,
        COUNT(*) AS entries
    FROM charts
    WHERE daily_rank <= 10
    GROUP BY country
    ORDER BY avg_energy DESC
    LIMIT 15
""", conn)

print("\n── Q5: Countries Favouring High-Energy Tracks ──")
print(q5.to_string(index=False))

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(q5["country"], q5["avg_energy"], color=GREEN)
ax.set_xlabel("Country")
ax.set_ylabel("Average Energy Score")
ax.set_title("Countries with Highest Average Energy in Top 10 Charts")
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig("visuals/sql_03_country_energy.png")
print(" Saved: sql_03_country_energy.png")


# ══════════════════════════════════════════════════════════════════
# Q6 — Explicit vs non-explicit chart performance
# ══════════════════════════════════════════════════════════════════
q6 = pd.read_sql("""
    SELECT
        is_explicit,
        COUNT(*) AS total_entries,
        ROUND(AVG(daily_rank), 1) AS avg_rank,
        ROUND(AVG(popularity), 1) AS avg_popularity,
        SUM(CASE WHEN daily_rank = 1 THEN 1 ELSE 0 END) AS number_1_appearances
    FROM charts
    GROUP BY is_explicit
""", conn)

print("\n── Q6: Explicit vs Non-Explicit Chart Performance ──")
print(q6.to_string(index=False))


# ══════════════════════════════════════════════════════════════════
# PRINT FINAL KEY FINDINGS
# ══════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("SQL ANALYSIS — KEY FINDINGS")
print("="*60)
print(f"\n Most charting artist: {q2.iloc[0]['artists']} "
      f"({int(q2.iloc[0]['total_chart_appearances']):,} appearances "
      f"across {int(q2.iloc[0]['countries_charted_in'])} countries)")
print(f"\n Song that hit #1 in most countries: {q3.iloc[0]['name']} "
      f"by {q3.iloc[0]['artists']} ({int(q3.iloc[0]['countries_reached_number_1'])} countries)")
print(f"\n Most high-energy market: {q5.iloc[0]['country']} "
      f"(avg energy: {q5.iloc[0]['avg_energy']})")
print(f"\n Top genre by popularity: {q1.iloc[0]['track_genre']} "
      f"(score: {q1.iloc[0]['avg_popularity']})")

conn.close()
print("\n All SQL queries complete. Visuals saved to visuals/")