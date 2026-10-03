# 📊 YouTube Comments Sentiment Analyser

## Overview
The **YouTube Comments Sentiment Analyser** is a production‑ready pipeline for processing and classifying sentiment in YouTube comments. It automates the workflow from raw data ingestion to structured sentiment output, making it easier to understand audience reactions and engagement.

## Features
- Merge multiple raw Excel files into one dataset
- Add metadata (source file, processed date)
- Run sentiment analysis using HuggingFace Transformers (`nlptown/bert-base-multilingual-uncased-sentiment`)
- Map star ratings into business‑friendly categories: Negative, Neutral, Positive
- Export results to Excel for reporting
- Configurable via `config.yaml`
- Logging for transparency and debugging

## Project Structure
youtube_comments_sentiment_analyser/
│── config.yaml
│── read_data.py
│── sentiment_analysis.py
│── requirements.txt
│── logs/
│    └── pipeline.log
│── raw_data/
│    └── *.xlsx
│── processed_data/
│    └── comments_data.xlsx
│── output/
│    └── comments_with_sentiment.xlsx

## Configuration
Edit `config.yaml` to set paths and model:
```yaml
raw_data_path: "raw_data"
input_file: "processed_data/comments_data.xlsx"
output_file: "output/comments_with_sentiment.xlsx"
model_name: "nlptown/bert-base-multilingual-uncased-sentiment"

mapping:
  "1 star": "Negative"
  "2 stars": "Negative"
  "3 stars": "Neutral"
  "4 stars": "Positive"
  "5 stars": "Positive"

Installation:

	conda create -n sentiment python=3.10
	conda activate sentiment
	pip install -r requirements.txt

Usage:
python sentiment_analysis.py




























