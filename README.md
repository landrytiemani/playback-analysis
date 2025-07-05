# Playback Pattern Analysis

This project analyzes streaming playback behavior using simulated data to replicate a Netflix-style analytics pipeline. It demonstrates proficiency in SQL, Python, data modeling, and A/B testing.

## Key Objectives
- Analyze playback session data (buffering start time, device type, completion rate)
- Simulate A/B testing to estimate the impact of buffering delay on viewer engagement
- Transform and enrich raw data using ETL techniques
- Generate structured summary reports and visualizations to support experimentation insights

## Stack
- Python (pandas, matplotlib, seaborn)
- Jupyter Notebooks
- SQL-style logic using `groupby`
- JSON reporting
- Mock ETL flow (standalone script simulating Airflow DAG behavior)


## Project Structure

- `data/`: contains example session logs and annotations
- `notebooks/`: contains A/B testing analysis
- `scripts/`: includes mock ETL pipeline scripts
- `dashboard/`: includes visualizations and demo images
- `requirements.txt`: Python dependencies

##  Dataset

The dataset is **synthetic**, generated using Python. It simulates 100 streaming sessions with the following attributes:

- `device`: TV, Mobile, Laptop, Tablet
- `buffering_start_time`: Simulated delay in seconds before playback begins
- `completion_rate`: Portion of video completed (0.0 to 1.0)
- `variant`: A or B (for simulated A/B testing)

These values allow for controlled experimentation and realistic feature engineering without accessing proprietary data.


## Getting Started

```bash
pip install -r requirements.txt
```
---