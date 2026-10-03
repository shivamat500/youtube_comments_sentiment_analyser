import logging
import pandas as pd
import yaml
from transformers import pipeline

# ---------------- Logging Setup ----------------
logging.basicConfig(
    filename="logs/sentiment.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Config Loader ----------------
def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

# ---------------- Data Loader ----------------
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(path)
        logging.info(f"Loaded {len(df)} rows from {path}")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

# ---------------- Sentiment Classifier ----------------
def classify_text(text: str, classifier, mapping: dict) -> str:
    if pd.isna(text) or str(text).strip() == "":
        return "Empty"
    try:
        output = classifier(str(text))
        label = output[0]['label']
        return mapping.get(label, label)
    except Exception as e:
        logging.error(f"Error classifying text '{text}': {e}")
        return "Error"

# ---------------- Main Pipeline ----------------
def main():
    config = load_config()
    df = load_data(config["input_file"])

    classifier = pipeline("sentiment-analysis", model=config["model_name"])
    mapping = config["mapping"]

    df["sentiment"] = df["Comment"].apply(lambda x: classify_text(x, classifier, mapping))

    df.to_excel(config["output_file"], index=False)
    logging.info(f"Analysis complete. File created: {config['output_file']}")
    print(f"Analysis complete. File created: {config['output_file']}")
# ---------------- Entry Point ----------------
if __name__ == "__main__":
    main()
