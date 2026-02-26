import pandas as pd
import os

# ── Paths ──────────────────────────────────────────────
RAW = "data/raw"
PROCESSED = "data/processed"

# ══════════════════════════════════════════════════════
# 1. TRACKS DATASET
# ══════════════════════════════════════════════════════
print("Loading tracks...")
tracks = pd.read_csv(f"{RAW}/tracks.csv")

print(f"Raw tracks shape: {tracks.shape}")
print(tracks.dtypes)
print(tracks.isnull().sum())

# Drop duplicates
tracks.drop_duplicates(subset="track_id", inplace=True)

# Drop rows with missing critical fields
tracks.dropna(subset=["track_name", "artists", "popularity", "track_genre"], inplace=True)

# Clean column names
tracks.columns = tracks.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert duration from ms to seconds
tracks["duration_s"] = tracks["duration_ms"] / 1000
tracks.drop(columns=["duration_ms"], inplace=True)

# Ensure correct types
tracks["popularity"] = pd.to_numeric(tracks["popularity"], errors="coerce")
tracks["explicit"] = tracks["explicit"].astype(bool)

print(f"Clean tracks shape: {tracks.shape}")
tracks.to_csv(f"{PROCESSED}/tracks_clean.csv", index=False)
print(" tracks_clean.csv saved")

# ══════════════════════════════════════════════════════
# 2. CHARTS DATASET (Top Spotify Songs in 73 Countries)
# ══════════════════════════════════════════════════════
print("\nLoading charts...")
charts = pd.read_csv(f"{RAW}/charts.csv")

print(f"Raw charts shape: {charts.shape}")
print(charts.dtypes)
print(charts.isnull().sum())

# Drop duplicates
charts.drop_duplicates(inplace=True)

# Clean column names
charts.columns = charts.columns.str.strip().str.lower().str.replace(" ", "_")

# Drop nulls in critical columns
charts.dropna(subset=["name", "artists", "country", "daily_rank", "snapshot_date"], inplace=True)

# Parse dates
charts["snapshot_date"] = pd.to_datetime(charts["snapshot_date"], errors="coerce")
charts["album_release_date"] = pd.to_datetime(charts["album_release_date"], errors="coerce")
charts.dropna(subset=["snapshot_date"], inplace=True)

# Extract time features
charts["year"] = charts["snapshot_date"].dt.year
charts["month"] = charts["snapshot_date"].dt.month
charts["month_name"] = charts["snapshot_date"].dt.strftime("%B")

# Convert duration to seconds
charts["duration_s"] = charts["duration_ms"] / 1000
charts.drop(columns=["duration_ms"], inplace=True)

# Ensure correct types
charts["popularity"] = pd.to_numeric(charts["popularity"], errors="coerce")
charts["daily_rank"] = pd.to_numeric(charts["daily_rank"], errors="coerce")
charts["daily_movement"] = pd.to_numeric(charts["daily_movement"], errors="coerce")
charts["weekly_movement"] = pd.to_numeric(charts["weekly_movement"], errors="coerce")
charts["is_explicit"] = charts["is_explicit"].astype(bool)

# Audio feature columns — ensure all numeric
audio_features = [
    "danceability", "energy", "loudness", "speechiness",
    "acousticness", "instrumentalness", "liveness", "valence", "tempo"
]
for col in audio_features:
    charts[col] = pd.to_numeric(charts[col], errors="coerce")

# Drop rows where all audio features are null
charts.dropna(subset=audio_features, how="all", inplace=True)

# Keep only rank 1-50 for cleaner analysis
charts = charts[charts["daily_rank"] <= 50]

print(f"Clean charts shape: {charts.shape}")
print(charts.head(3))
charts.to_csv(f"{PROCESSED}/charts_clean.csv", index=False)
print(" charts_clean.csv saved")