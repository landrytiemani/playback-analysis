"""
ETL pipeline simulating Airflow DAG behavior for Playback Analysis
"""

import pandas as pd
import os

def extract(path="data/sample_playback_data.csv"):
    print("Extracting data...")
    return pd.read_csv(path)

def transform(df):
    print("Transforming data...")

    # Flag mobile users
    df['is_mobile'] = df['device'].apply(lambda x: 1 if x.lower() == 'mobile' else 0)

    # Classify completion quality
    df['completion_flag'] = df['completion_rate'].apply(lambda x: 'High' if x > 0.85 else 'Low')

    # Bin buffering start time
    df['buffering_bin'] = pd.cut(df['buffering_start_time'],
                                 bins=[0, 1, 2, 3, 4, float("inf")],
                                 labels=["<1s", "1-2s", "2-3s", "3-4s", ">4s"],
                                 right=False)

    return df

def generate_summary(df):
    print("Generating summary report...")

    summary = {
        "variant_completion": df.groupby("variant")["completion_rate"].mean().round(3).to_dict(),
        "device_distribution": df["device"].value_counts().to_dict(),
        "completion_flag_counts": df["completion_flag"].value_counts().to_dict(),
        "buffering_distribution": df["buffering_bin"].value_counts().sort_index().to_dict()
    }

    return summary

def load(df, output_path="data/processed_playback_data.csv", summary_path="data/summary_report.json"):
    print("Loading data...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    summary = generate_summary(df)

    with open(summary_path, "w") as f:
        import json
        json.dump(summary, f, indent=4)

    print(f"Saved processed data to {output_path}")
    print(f"Saved summary report to {summary_path}")

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
    print("ETL pipeline completed successfully.")