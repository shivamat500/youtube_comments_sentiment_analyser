This project provides a production‑ready pipeline for analyzing sentiment in YouTube comments. It automates the process of:

Collecting and merging raw comment data from multiple Excel files.

Running sentiment classification using HuggingFace Transformers (nlptown/bert-base-multilingual-uncased-sentiment).

Mapping star ratings into business‑friendly categories (Negative, Neutral, Positive).

Exporting clean, structured results for downstream analysis or reporting.

✨ Features
Config‑driven workflow: All paths, model names, and mappings are defined in config.yaml.

Data ingestion: Reads multiple .xlsx files from a raw data folder and combines them into a single dataset.

Sentiment analysis: Uses HuggingFace pipeline with PyTorch backend.

Custom mapping: Converts star ratings (1–5) into simplified sentiment categories.

Logging: Tracks progress and errors in logs/.

Modular scripts:

read_data.py → merges raw Excel files into processed_data/comments_data.xlsx

sentiment_analysis.py → runs classification and saves results to output/comments_with_sentiment.xlsx

🛠️ Tech Stack
Python 3.10+

Pandas for data handling

Transformers (HuggingFace) for NLP

PyTorch as ML backend

YAML for configuration

OpenPyXL for Excel I/O
