# Spotify-streaming-trends-analysis
Analyze listening patterns — what genres dominate, which artists are trending, how streams vary by time/country, and what makes a song hit the top charts

---

## 📌 Overview
Why does it matter to a company like Spotify?]

This project analyzes 600K+ Spotify tracks and multi-country chart data 
to uncover streaming trends, genre dominance patterns, and artist growth signals. 
---

## 🎯 Business Questions Answered
-   Which genres dominate streaming across different markets?
-  What audio features correlate most with high popularity?
-  Which artists showed the highest growth in chart appearances?

---

## 🛠️ Tools & Technologies
- **Python** (pandas, numpy, matplotlib, seaborn)
- **SQL** (SQLite / PostgreSQL)
- **Tableau / Power BI** (for dashboard)
- **Jupyter Notebook**

---

## 📂 Dataset
| Dataset | Source | Size |
|--------|--------|------|
| Spotify Tracks | [Kaggle Link] | 600K+ rows |
| Spotify Charts | [Kaggle Link] | X rows |

---

## 🔍 Key Findings
1. **Finding 1** — e.g. Pop and Latin genres account for 47% of top 200 chart 
   appearances globally, with Latin showing 23% YoY growth.
2. **Finding 2** — e.g. Tracks with high energy (>0.8) and low acousticness 
   are 3x more likely to appear in the top 50.
3. **Finding 3** — e.g. Markets in Southeast Asia showed the fastest streaming 
   growth, led by Indonesia and Philippines.

*(Fill these in after your actual analysis)*

---

## 📊 Dashboard Preview
![Dashboard](dashboard/spotify_dashboard.png)

---

## 🚀 How to Run This Project
```bash
# Clone the repo
git clone https://github.com/yourusername/[repo-name].git

# Install dependencies
pip install -r requirements.txt

# Run the cleaning script
python src/clean_data.py

# Open the notebooks
jupyter notebook
```

---

## 📁 Project Structure
```
spotify-streaming-trends-analysis/
│
├── data/
│   ├── raw/                  # original downloaded CSV files go here
│   └── processed/            # cleaned data after your Python script
│
├── notebooks/
│   └── 01_exploration.ipynb  # EDA and analysis
│   └── 02_sql_queries.ipynb  # your SQL work via SQLite or pandas
│
├── sql/
│   └── queries.sql           # all your SQL queries as standalone file
│
├── dashboard/
│   └── spotify_dashboard.png # screenshot of your Tableau/PowerBI dashboard
│   └── spotify_dashboard.pbix # actual dashboard file if Power BI
│
├── reports/
│   └── insights_report.md    # your written business insight report
│
├── src/
│   └── clean_data.py         # reusable cleaning script
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 💡 Business Recommendation
[2-3 sentences written like you're talking to a product or 
business team. What should Spotify do based on your findings? 
This section is what separates analysts from data processors.]

---

## 👤 Author
**Victor Adeyemi**  
[https://www.linkedin.com/in/victor-adeyemi-29a54b334/] | [adeyemivicotr912@gmail.com]
```

---

## Your `.gitignore` file (same for all 3 repos)
```
# Data files (too large for GitHub)
data/raw/
*.csv
*.xlsx

# Python
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
venv/

# OS
.DS_Store
Thumbs.db
