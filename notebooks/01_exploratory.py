# ══════════════════════════════════════════════════════════════════
# SPOTIFY STREAMING TRENDS ANALYSIS
# Notebook 1: Exploratory Data Analysis
# ══════════════════════════════════════════════════════════════════

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Style ──────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "figure.dpi": 150,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "axes.titleweight": "bold",
    "figure.facecolor": "white"
})
GREEN = "#1DB954"   # Spotify green

# ── Load Data ──────────────────────────────────────────────────────
tracks = pd.read_csv("data/processed/tracks_clean.csv")
charts = pd.read_csv("data/processed/charts_clean.csv")
charts["snapshot_date"] = pd.to_datetime(charts["snapshot_date"])

print(f"Tracks: {tracks.shape}")
print(f"Charts: {charts.shape}")
print(f"Countries in charts: {charts['country'].nunique()}")
print(f"Date range: {charts['snapshot_date'].min()} → {charts['snapshot_date'].max()}")


# ══════════════════════════════════════════════════════════════════
# SECTION 1 — GENRE ANALYSIS (from tracks dataset)
# ══════════════════════════════════════════════════════════════════

# Q1: What are the top 15 genres by track count?
top_genres = (tracks.groupby("track_genre")
              .size()
              .reset_index(name="track_count")
              .sort_values("track_count", ascending=False)
              .head(15))

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(top_genres["track_genre"], top_genres["track_count"], color=GREEN)
ax.set_xlabel("Number of Tracks")
ax.set_title("Top 15 Genres by Track Count")
ax.invert_yaxis()
for bar in bars:
    ax.text(bar.get_width() + 30, bar.get_y() + bar.get_height()/2,
            f'{int(bar.get_width()):,}', va='center', fontsize=9)
plt.tight_layout()
plt.savefig("visuals/01_top_genres_by_count.png")
plt.show()
print("✅ Saved: 01_top_genres_by_count.png")


# Q2: Average popularity by genre (top 20)
genre_popularity = (tracks.groupby("track_genre")["popularity"]
                    .mean()
                    .reset_index()
                    .sort_values("popularity", ascending=False)
                    .head(20))

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(genre_popularity["track_genre"], genre_popularity["popularity"], color=GREEN)
ax.set_xlabel("Average Popularity Score (0–100)")
ax.set_title("Top 20 Genres by Average Popularity Score")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("visuals/02_top_genres_by_popularity.png")
plt.show()
print(" Saved: 02_top_genres_by_popularity.png")


# ══════════════════════════════════════════════════════════════════
# SECTION 2 — AUDIO FEATURES vs POPULARITY
# ══════════════════════════════════════════════════════════════════

audio_features = ["danceability", "energy", "valence",
                  "speechiness", "acousticness", "liveness"]

# Q3: Correlation of audio features with popularity
correlations = (tracks[audio_features + ["popularity"]]
                .corr()["popularity"]
                .drop("popularity")
                .sort_values())

fig, ax = plt.subplots(figsize=(9, 5))
colors = [GREEN if v > 0 else "#E74C3C" for v in correlations.values]
ax.barh(correlations.index, correlations.values, color=colors)
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("Audio Feature Correlation with Track Popularity")
ax.set_xlabel("Pearson Correlation Coefficient")
plt.tight_layout()
plt.savefig("visuals/03_audio_feature_correlation.png")
plt.show()
print("✅ Saved: 03_audio_feature_correlation.png")


# Q4: Popularity distribution — explicit vs non-explicit
fig, ax = plt.subplots(figsize=(9, 5))
for label, color in [(True, GREEN), (False, "#95A5A6")]:
    subset = tracks[tracks["explicit"] == label]["popularity"]
    ax.hist(subset, bins=30, alpha=0.6, color=color,
            label="Explicit" if label else "Non-Explicit")
ax.set_xlabel("Popularity Score")
ax.set_ylabel("Number of Tracks")
ax.set_title("Popularity Distribution: Explicit vs Non-Explicit Tracks")
ax.legend()
plt.tight_layout()
plt.savefig("visuals/04_explicit_vs_popularity.png")
plt.show()
print("✅ Saved: 04_explicit_vs_popularity.png")


# ══════════════════════════════════════════════════════════════════
# SECTION 3 — CHARTS: COUNTRY & RANKING ANALYSIS
# ══════════════════════════════════════════════════════════════════

# Q5: Top 15 countries by number of chart entries
top_countries = (charts.groupby("country")
                 .size()
                 .reset_index(name="entries")
                 .sort_values("entries", ascending=False)
                 .head(15))

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top_countries["country"], top_countries["entries"], color=GREEN)
ax.set_xlabel("Country")
ax.set_ylabel("Chart Entries")
ax.set_title("Top 15 Countries by Number of Chart Entries")
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig("visuals/05_top_countries_chart_entries.png")
plt.show()
print("✅ Saved: 05_top_countries_chart_entries.png")


# Q6: Average audio profile of Top 10 vs Bottom 10 ranked songs
top10 = charts[charts["daily_rank"] <= 10][audio_features].mean()
bottom10 = charts[charts["daily_rank"] >= 41][audio_features].mean()

comparison = pd.DataFrame({"Top 10": top10, "Rank 41–50": bottom10})

fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(audio_features))
width = 0.35
ax.bar([i - width/2 for i in x], comparison["Top 10"], width,
       label="Top 10", color=GREEN)
ax.bar([i + width/2 for i in x], comparison["Rank 41–50"], width,
       label="Rank 41–50", color="#95A5A6")
ax.set_xticks(list(x))
ax.set_xticklabels(audio_features, rotation=20)
ax.set_title("Audio Profile: Top 10 vs Rank 41–50 Songs")
ax.set_ylabel("Average Feature Score")
ax.legend()
plt.tight_layout()
plt.savefig("visuals/06_top10_vs_bottom_audio_profile.png")
plt.show()
print("✅ Saved: 06_top10_vs_bottom_audio_profile.png")


# Q7: Monthly chart trends — average popularity over time
monthly = (charts.groupby(["year", "month"])["popularity"]
           .mean()
           .reset_index())
monthly["period"] = pd.to_datetime(
    monthly["year"].astype(str) + "-" + monthly["month"].astype(str).str.zfill(2))
monthly = monthly.sort_values("period")

fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(monthly["period"], monthly["popularity"],
        color=GREEN, linewidth=2, marker="o", markersize=3)
ax.set_xlabel("Date")
ax.set_ylabel("Average Popularity Score")
ax.set_title("Average Track Popularity on Charts Over Time")
ax.tick_params(axis='x', rotation=30)
plt.tight_layout()
plt.savefig("visuals/07_popularity_over_time.png")
plt.show()
print("✅ Saved: 07_popularity_over_time.png")


# ══════════════════════════════════════════════════════════════════
# SECTION 4 — TOP ARTISTS
# ══════════════════════════════════════════════════════════════════

# Q8: Top 15 most charting artists globally
top_artists = (charts.groupby("artists")
               .size()
               .reset_index(name="chart_appearances")
               .sort_values("chart_appearances", ascending=False)
               .head(15))

fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(top_artists["artists"], top_artists["chart_appearances"], color=GREEN)
ax.set_xlabel("Total Chart Appearances")
ax.set_title("Top 15 Artists by Global Chart Appearances")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("visuals/08_top_artists_global.png")
plt.show()
print("✅ Saved: 08_top_artists_global.png")


# ══════════════════════════════════════════════════════════════════
# SUMMARY STATS — print key findings to console
# ══════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("KEY FINDINGS SUMMARY")
print("="*60)
print(f"\n Total tracks analysed: {len(tracks):,}")
print(f" Total chart entries analysed: {len(charts):,}")
print(f" Countries covered: {charts['country'].nunique()}")
print(f"\n Most popular genre: {genre_popularity.iloc[0]['track_genre']} "
      f"(avg popularity: {genre_popularity.iloc[0]['popularity']:.1f})")
print(f"\n Most charting artist: {top_artists.iloc[0]['artists']} "
      f"({top_artists.iloc[0]['chart_appearances']:,} appearances)")
print(f"\n Top charting country: {top_countries.iloc[0]['country']} "
      f"({top_countries.iloc[0]['entries']:,} entries)")

diff = top10 - bottom10
most_diff = diff.abs().idxmax()
print(f"\n Biggest audio difference between top 10 and lower ranked: {most_diff} "
      f"( {diff[most_diff]:.3f})")
print("\n All visuals saved to visuals/")