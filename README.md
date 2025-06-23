# Stock Market Visualization (Trade Every 4 Months)

This repository contains a simple example application that demonstrates how Nasdaq index data might look if trading occurred once every four months instead of monthly. The dataset included here is a small sample of monthly closing prices for the Nasdaq index.

## Files

- `nasdaq_sample.csv` &ndash; Sample dataset with monthly closing prices (2023&ndash;2024).
- `visualize_nasdaq.py` &ndash; Python script that loads the sample data, resamples it to 4‑month intervals, and plots the result. Points are colored green if the price is higher than the previous 4‑month checkpoint and red if it is lower.
- `visualize_stock.py` &ndash; Fetches real historical data for any ticker symbol using `yfinance` and plots the monthly closing price from the start of trading.

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
   The generated plot shows the four‑month closing price series only. Each point is colored green if the price increased from the previous checkpoint or red if it decreased. The image is saved as `nasdaq_4m_plot.png` in the repository directory.
3. To download real monthly data for a stock and plot it, install `yfinance` and run:
   ```bash
   pip install yfinance
   python visualize_stock.py AAPL  # replace AAPL with the symbol you want
   ```
   The script saves the figure as `<SYMBOL>_monthly_plot.png`.

This is a minimal example to illustrate the concept. Fetching real data requires internet access.
