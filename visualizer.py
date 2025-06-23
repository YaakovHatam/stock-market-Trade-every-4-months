import pandas as pd
import matplotlib.pyplot as plt


def make_four_monthly_plot(df: pd.DataFrame, symbol: str):

    df.set_index("Date", inplace=True)

    # Resample to 4-month frequency, taking the last available close
    df_4m = df.resample("4M").last()

    # Determine direction of price change compared to the previous checkpoint
    df_4m["change"] = df_4m["Close"].diff()
    colors = df_4m["change"].apply(lambda x: "red" if x < 0 else "green")

    # Plot only the 4-month data, indicating up/down movements
    plt.figure(figsize=(10, 6))
    plt.plot(
        df_4m.index, df_4m["Close"], label="4-Month Close", color="blue", marker="o"
    )
    plt.scatter(df_4m.index, df_4m["Close"], s=100, c=colors, zorder=5)
    for idx, row in df_4m.iterrows():
        direction = "down" if row["change"] < 0 else "up"
        plt.text(
            idx,
            row["Close"],
            direction,
            color=colors.loc[idx],
            ha="center",
            va="bottom",
        )
    plt.title(f"{symbol} 4-Month Close")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.grid(True)
    plt.tight_layout()
    # Save the figure instead of displaying it to avoid GUI requirements
    outfile = f"./output/{symbol}_monthly_plot.png"
    plt.savefig(outfile)
    print(f"Plot saved to {outfile}")
