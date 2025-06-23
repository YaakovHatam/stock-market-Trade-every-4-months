import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load sample data
    df = pd.read_csv('nasdaq_sample.csv', parse_dates=['date'])
    df.set_index('date', inplace=True)

    # Resample to 4-month frequency, taking the last available close
    df_4m = df.resample('4M').last()

    # Plot original monthly data and 4-month resampled data
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['close'], label='Monthly Close', marker='o')
    plt.plot(df_4m.index, df_4m['close'], label='4-Month Close', marker='s')
    plt.title('NASDAQ Monthly vs. 4-Month Close')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # Save the figure instead of displaying it to avoid GUI requirements
    plt.savefig('nasdaq_plot.png')
    print('Plot saved to nasdaq_plot.png')

if __name__ == '__main__':
    main()
