# YouTube Data Pipeline Project

---

## 🔧 Tech Stack

- **Python** – API extraction (YouTube Data API v3)
- **Snowflake** – Cloud data warehouse
- **dbt** – Data modeling and transformations (RAW → STAGING → MART)
- **Metabase** – Dashboard visualization (run locally using Docker)

---

## Pipeline Overview

1. **Extraction (Python)**  
   - Collected public YouTube channel statistics using the YouTube Data API v3  
   - Saved results as a local CSV file  

2. **Data Loading (Snowflake UI)**  
   - Uploaded the CSV to Snowflake's `RAW` schema using the web interface  

3. **Transformation (dbt)**  
   - Created staging models with type casting and column cleanup  
   - Built a final mart table `mart_youtube_videos` with per-video metrics and engagement rate  

4. **Visualization (Metabase)**  
   - Connected to Snowflake using Metabase (via Docker)  
   - Created charts using the final mart table:  
     - 📈 Monthly Video Upload Trend  
     - 📊 Top Videos by Engagement Rate  

---

## Folder Structure

```plaintext

youtube_data_pipeline_project/
│
├── extract/                          # 1. Data extraction logic
│   └── youtube_data_extraction.py    # Python script to call YouTube API and export CSV
│
├── data/                             # 2. Load raw data to Snowflake
│   └── youtube_video_data.csv
│
├── transform/                        # 3. dbt transformation project
│   ├── dbt_project.yml               # dbt project config
│   ├── profiles.yml                  # dbt profile (Snowflake connection)
│   └── models/
│       ├── sources/                  # dbt source definitions
│       ├── staging/                  # Cleaned, typed tables from raw schema
│       └── marts/                    # Final aggregated metrics
│
├── visualize/                        # 4. Dashboard visualizations (Metabase)
│   ├── metabase_dashboard.png        # Full dashboard screenshot
│   └── charts/                       # individual chart exports
│
├── README.md                         # Project documentation

```
---

## Dashboards

- **Chart 1:** *Total Videos Published per Channe*  
  A bar chart showing the number of videos published by each YouTube channel.

- **Chart 2:** *Average Engagement Rate – techTFQ Channel*  
  A line chart tracking the average engagement rate over time for the techTFQ channel. Engagement rate is calculated as `(likes + comments) / views`.

---

## ▶How to Reproduce

1. Set up a Snowflake account and create schemas: `RAW`, `DBT_STAGING`, `DBT_ANALYTICS`
2. Clone this repo and set up a dbt profile for Snowflake connection
3. Upload the provided CSV to `RAW.YOUTUBE_VIDEO_DATA`
4. Run the dbt models to build the final data marts in Snowflake.
5. Launch Metabase using Docker and connect to Snowflake project
6. Sync the schema and explore dashboards

---

## Acknowledgements

The initial Python extraction logic was adapted from this YouTube tutorial:  
📹 [Python Project to Scrape YouTube using YouTube Data API | Analyze and Visualize YouTube data](https://youtu.be/SwSbnmqk3zY?si=MCuMuyiloGqE8Y32)

All Snowflake loading, dbt transformations, and Metabase dashboarding were independently designed and implemented.

