import sys
import pandas as pd
import matplotlib.pyplot as plt
from visualizer import make_four_monthly_plot

try:
    import yfinance as yf

    yf.set_tz_cache_location("./cache")

except ImportError:
    print("The 'yfinance' package is required. Install it with 'pip install yfinance'.")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize_stock.py SYMBOL")
        sys.exit(1)

    symbol = sys.argv[1].upper()

    # Fetch monthly data from the start of trading
    data = yf.download(
        symbol, period="max", interval="1mo", auto_adjust=True, multi_level_index=False
    )
    if data is None or data.empty:
        print(f"No data found for {symbol}.")
        sys.exit(1)

    data.reset_index(inplace=True)

    make_four_monthly_plot(data, symbol)


if __name__ == "__main__":
    main()
