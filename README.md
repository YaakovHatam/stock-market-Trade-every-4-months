# Stock Market Visualization (Trade Every 4 Months)

This repository contains a simple example application that demonstrates how Nasdaq index data might look if trading occurred once every four months instead of monthly. The dataset included here is a small sample of monthly closing prices for the Nasdaq index.

## Files

- `nasdaq_sample.csv` &ndash; Sample dataset with monthly closing prices (2023&ndash;2024).
- `visualize_nasdaq.py` &ndash; Python script that loads the sample data, resamples it to 4‑month intervals, and plots the result.

## Usage

1. Install dependencies (requires Python 3 and `pandas`/`matplotlib`).
   If you have network access, you can install them via `pip`:
   ```bash
   pip install pandas matplotlib
   ```
2. Run the script:
   ```bash
   python visualize_nasdaq.py
   ```
   A plot window will appear showing the monthly closing prices and the prices if trading were done only once every four months.

This is a minimal example to illustrate the concept without fetching real data from the internet.
