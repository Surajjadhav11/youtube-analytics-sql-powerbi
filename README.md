# 🎬 Advanced YouTube Content Performance Analytics  
## SQL + Power BI | Canada Market Analysis

---

## 📌 Project Overview

This project delivers an end-to-end analytics solution analyzing YouTube trending videos in Canada.  
The objective was to uncover performance patterns, engagement behavior, content acceleration dynamics, and market concentration insights using advanced SQL modeling and interactive Power BI dashboards.

The project simulates a real-world business intelligence workflow:
1. Data Engineering in SQL
2. KPI Modeling & Advanced Analysis
3. Executive Dashboard Visualization

---

## 🎯 Business Objectives

- Identify high-performing content categories
- Measure engagement effectiveness
- Analyze publish-to-trend speed
- Detect trending acceleration patterns
- Evaluate market dominance of top channels
- Translate data into strategic insights

---

## 🛠 Tech Stack

- **Database:** MySQL  
- **Visualization:** Power BI  
- **Dataset:** YouTube Trending Dataset (Canada)  
- **Techniques Used:**  
  - Window Functions (LAG, RANK, ROW_NUMBER)
  - Rolling Aggregations
  - Market Share Modeling
  - Feature Engineering
  - Data Transformation

---

## 🧠 Data Engineering Workflow

### 1️⃣ Data Cleaning
- Resolved encoding issues
- Converted trending_date to proper DATE format
- Extracted publish day & hour
- Removed problematic text fields

### 2️⃣ Feature Engineering
Created key business metrics:

- **Engagement Rate**
  (likes + comment_count) / views

- **Days to Trend**
  DATEDIFF(trending_date, publish_time)

- **Rolling 7-Day Momentum**
  SUM(views) OVER (7-day window)

- **Market Concentration Ratio**
  Top 5 channels' share of total views

---

## 📊 Advanced SQL Analysis

- Category Performance Ranking
- Engagement vs Views Analysis
- Fastest vs Slowest Trending Videos
- Rolling Trend Acceleration
- Channel Dominance Modeling
- Market Share Percentage Calculation

---

## 📈 Dashboard Features

### Page 1 – Market Overview
- KPI Cards (Total Views, Likes, Engagement, Videos)
- Category Performance Bar Chart
- Category Share Donut Chart
- Trending Views Over Time
- Top Channels by Engagement

### Page 2 – Momentum & Engagement
- Rolling 7-Day Trend Line
- Engagement vs Views Scatter Analysis
- Fastest Trending Videos
- Market Concentration Ratio (Top 5 Share)

### Page 3 – Trend Speed Analysis
- Average Days to Trend by Category
- Fastest & Slowest Trending Comparisons
- Interactive Filters (Category, Channel, Publish Day)

---

## 📷 Dashboard Preview

### 🟦 Market Overview Dashboard
![Market Overview](Screenshots/Image%1.png)

---

### 📈 Rolling 7-Day Trending Momentum & Engagement Analysis
![Momentum & Engagement](Screenshots/Image%2.png)

---

### ⚡ Fastest Trending Videos & Market Concentration
![Trending Speed](Screenshots/Image%3.png)

---

### 📊 Advanced Category & Trend Speed Analysis
![Category Analysis](Screenshots/Image%1.png)
---

## 🔎 Key Insights

- Entertainment & Music dominate total views
- Top 5 channels account for ~32% of total market views
- High views do not always imply high engagement
- Certain categories trend significantly faster
- Rolling momentum reveals accelerating growth behavior

---

## 💼 Business Applications

This analysis framework can support:

- Content strategy optimization
- Influencer campaign planning
- Audience engagement benchmarking
- Competitive channel analysis
- Platform performance evaluation

---

## 🚀 Future Improvements

- Predictive model for trending probability
- Automated ETL pipeline
- Real-time API integration
- Deployment to Power BI Service
- Dashboard performance optimization

---

## 👤 Author

Suraj Jadhav  
Aspiring Data Analyst  
SQL | Power BI | Business Intelligence | Data Visualization
