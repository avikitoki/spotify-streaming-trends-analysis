-- ══════════════════════════════════════════════════════════════════
-- SPOTIFY STREAMING TRENDS — SQL ANALYSIS
-- Database: SQLite (spotify.db)
-- ══════════════════════════════════════════════════════════════════


-- ── Q1: Top 10 genres by average popularity ──────────────────────
SELECT 
    track_genre,
    COUNT(*) AS track_count,
    ROUND(AVG(popularity), 2) AS avg_popularity,
    ROUND(AVG(danceability), 3) AS avg_danceability,
    ROUND(AVG(energy), 3) AS avg_energy
FROM tracks
GROUP BY track_genre
ORDER BY avg_popularity DESC
LIMIT 10;


-- ── Q2: Top 15 most charting artists globally ────────────────────
SELECT 
    artists,
    COUNT(*) AS total_chart_appearances,
    ROUND(AVG(popularity), 1) AS avg_popularity,
    COUNT(DISTINCT country) AS countries_charted_in
FROM charts
GROUP BY artists
ORDER BY total_chart_appearances DESC
LIMIT 15;


-- ── Q3: Top 10 countries by chart activity ───────────────────────
SELECT 
    country,
    COUNT(*) AS total_entries,
    COUNT(DISTINCT name) AS unique_songs,
    ROUND(AVG(popularity), 1) AS avg_popularity
FROM charts
GROUP BY country
ORDER BY total_entries DESC
LIMIT 10;


-- ── Q4: Songs that reached #1 in the most countries ──────────────
SELECT 
    name,
    artists,
    COUNT(DISTINCT country) AS countries_reached_number_1,
    ROUND(AVG(popularity), 1) AS avg_popularity
FROM charts
WHERE daily_rank = 1
GROUP BY name, artists
ORDER BY countries_reached_number_1 DESC
LIMIT 10;


-- ── Q5: Audio profile of rank 1 songs vs rank 50 songs ───────────
SELECT
    CASE WHEN daily_rank = 1 THEN 'Rank 1' ELSE 'Rank 50' END AS rank_group,
    ROUND(AVG(danceability), 3) AS avg_danceability,
    ROUND(AVG(energy), 3) AS avg_energy,
    ROUND(AVG(valence), 3) AS avg_valence,
    ROUND(AVG(acousticness), 3) AS avg_acousticness,
    ROUND(AVG(tempo), 1) AS avg_tempo
FROM charts
WHERE daily_rank IN (1, 50)
GROUP BY rank_group;


-- ── Q6: Monthly average popularity trend ─────────────────────────
SELECT
    year,
    month,
    COUNT(*) AS chart_entries,
    ROUND(AVG(popularity), 2) AS avg_popularity,
    ROUND(AVG(danceability), 3) AS avg_danceability,
    ROUND(AVG(energy), 3) AS avg_energy
FROM charts
GROUP BY year, month
ORDER BY year, month;


-- ── Q7: Explicit vs non-explicit performance on charts ───────────
SELECT
    is_explicit,
    COUNT(*) AS total_entries,
    ROUND(AVG(daily_rank), 1) AS avg_rank,
    ROUND(AVG(popularity), 1) AS avg_popularity,
    SUM(CASE WHEN daily_rank = 1 THEN 1 ELSE 0 END) AS number_1_appearances
FROM charts
GROUP BY is_explicit;


-- ── Q8: Top 10 songs by number of consecutive days in top 10 ─────
SELECT
    name,
    artists,
    COUNT(*) AS days_in_top_10,
    COUNT(DISTINCT country) AS countries,
    ROUND(AVG(popularity), 1) AS avg_popularity
FROM charts
WHERE daily_rank <= 10
GROUP BY name, artists
ORDER BY days_in_top_10 DESC
LIMIT 10;


-- ── Q9: Which countries favour high-energy tracks? ───────────────
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
LIMIT 15;


-- ── Q10: Rising artists — most improved weekly movement ──────────
SELECT
    artists,
    ROUND(AVG(weekly_movement), 1) AS avg_weekly_climb,
    COUNT(*) AS chart_entries,
    ROUND(AVG(popularity), 1) AS avg_popularity
FROM charts
WHERE weekly_movement > 0
GROUP BY artists
HAVING chart_entries >= 50
ORDER BY avg_weekly_climb DESC
LIMIT 10;