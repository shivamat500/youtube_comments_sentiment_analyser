import pandas as pd
import glob
import os
import yaml
from datetime import datetime
import logging

# Ensure directories exist
os.makedirs("processed_data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/read_data.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    data_path = config.get("raw_data_path")
    output_file = config.get("input_file")  # processed_data/comments_data.xlsx

    if not data_path or not os.path.exists(data_path):
        logging.error(f"Data path not found: {data_path}")
        raise ValueError("Invalid raw_data_path in config.yaml")

    excel_files = glob.glob(os.path.join(data_path, "*.xlsx"))
    if not excel_files:
        logging.error("No Excel files found in raw_data")
        raise ValueError("No Excel files to process")

    today = datetime.today().strftime("%Y-%m-%d")
    dfs = []

    for file in excel_files:
        df = pd.read_excel(file)
        df["source_file"] = os.path.basename(file)
        df["processed_date"] = today
        dfs.append(df)

    final_df = pd.concat(dfs, ignore_index=True)
    final_df.to_excel(output_file, index=False)

    logging.info(f"Combined {len(excel_files)} files into {output_file}")
    print(f"Completed: Total Combined {len(excel_files)} files into {output_file}")

if __name__ == "__main__":
    main()
