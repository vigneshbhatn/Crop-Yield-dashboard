# 🌾 Crop Yield Prediction & Visualization Dashboard

An end-to-end system for predicting and visualizing crop yields across Indian states, built for a hackathon. Combines machine learning predictions with real data and delivers insights through an interactive Power BI dashboard.

---

## 🚀 Tech Stack

- **Python** – Data processing and pipeline scripting
- **MySQL** – Backend database to store real + predicted data
- **Power BI** – For data visualization and dashboarding
- **Pandas** – For data wrangling
- **Scikit-learn / XGBoost** – ML model for yield prediction (handled by teammate)

---

## 📊 What It Does

- Predicts crop yield based on:
  - Crop type
  - Season
  - State
  - Area, rainfall, fertilizer, pesticide usage
- Merges predicted data with historical yield data
- Stores both in a MySQL database
- Displays:
  - Yield trends per crop/state/season
  - Comparison of real vs predicted yield
  - Insights on factors affecting yield (rainfall, fertilizer, etc.)

---
💡 Highlights
Easy data updates: Just drop new predicted CSVs

Scalable DB backend for future data additions

Rich visualization layer for non-technical users (e.g., farmers, agri-policy makers)

👨‍💻 Team Contributions
You: Data engineering, backend pipeline, Power BI integration

Teammate: ML model training, generating predictions

🏁 Future Scope
Web UI to upload new prediction files

Scheduled DB refresh for Power BI

Geo-mapped visuals for district-level insights



