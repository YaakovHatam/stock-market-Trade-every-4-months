import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load sample data
    df = pd.read_csv('nasdaq_sample.csv', parse_dates=['date'])
    df.set_index('date', inplace=True)

    # Resample to 4-month frequency, taking the last available close
    df_4m = df.resample('4M').last()

    # Determine direction of price change compared to the previous checkpoint
    df_4m['change'] = df_4m['close'].diff()
    colors = df_4m['change'].apply(lambda x: 'red' if x < 0 else 'green')

    # Plot only the 4-month data, indicating up/down movements
    plt.figure(figsize=(10, 6))
    plt.plot(df_4m.index, df_4m['close'], label='4-Month Close', color='blue', marker='o')
    plt.scatter(df_4m.index, df_4m['close'], s=100, c=colors, zorder=5)
    for idx, row in df_4m.iterrows():
        direction = 'down' if row['change'] < 0 else 'up'
        plt.text(idx, row['close'], direction, color=colors.loc[idx],
                 ha='center', va='bottom')
    plt.title('NASDAQ 4-Month Close')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.tight_layout()
    # Save the figure instead of displaying it to avoid GUI requirements
    plt.savefig('nasdaq_4m_plot.png')
    print('Plot saved to nasdaq_4m_plot.png')

if __name__ == '__main__':
    main()
