import sys
import pandas as pd
import matplotlib.pyplot as plt

try:
    import yfinance as yf
except ImportError:
    print("The 'yfinance' package is required. Install it with 'pip install yfinance'.")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize_stock.py SYMBOL")
        sys.exit(1)

    symbol = sys.argv[1].upper()

    # Fetch monthly data from the start of trading
    data = yf.download(symbol, period="max", interval="1mo", auto_adjust=True)
    if data.empty:
        print(f"No data found for {symbol}.")
        sys.exit(1)

    close = data['Close'].dropna()

    plt.figure(figsize=(10, 6))
    plt.plot(close.index, close.values, marker='o')
    plt.title(f"{symbol} Monthly Close")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.grid(True)
    plt.tight_layout()
    outfile = f"{symbol}_monthly_plot.png"
    plt.savefig(outfile)
    print(f"Plot saved to {outfile}")


if __name__ == "__main__":
    main()
