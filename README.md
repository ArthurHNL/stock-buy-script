# Stock Buy Calculator

**DISCLAIMER: Nothing in this repository should be remotely considered financial advice. This is merely a tool I use for my own investment strategy and I'm not even proud of the code. If you use this and lose money, do _not_ blame me.**

If you are looking for an investment strategy, please close this page and do your own research since I as a software developer am not qualified to give financial advice. If you think this strategy is stupid and are qualified to give financial advice, please contact me.

Personally I use a form of dollar-cost-averaging on ETFs. Basically, I have compiled a list of ETFs that I want to buy and hold according to a given ratio of ETFs and every month I move whatever I have left from my checking account to my investment account. Then you could invest in all of the assets depending on the ratios, but this has the downside of introducing a lot of transaction costs. Therefore, I instead invest all of the money I had left over that month into the asset that currently "needs" the most investment according to the ratios.

For months I did this using an Excel sheet to calculate everything by copy-pasting by hand. Then I found out that DEGIRO has a button in their interface to export your portfolio as CSV file so I decided to write this script. It takes two CSV files as input, one with the desired ratios and one with the desired portfolio. Then it spits out a dataframe like this:

```txt
Resulting calculation:
shape: (4, 6)
┌──────┬─────────────────────────────────┬────────┬────────┬───────────────┬─────────┐
│ isin ┆ name                            ┆ value  ┆ ratio  ┆ desired_value ┆ diff    │
│ ---  ┆ ---                             ┆ ---    ┆ ---    ┆ ---           ┆ ---     │
│ str  ┆ str                             ┆ f64    ┆ f64    ┆ f64           ┆ f64     │
╞══════╪═════════════════════════════════╪════════╪════════╪═══════════════╪═════════╡
│ null ┆ CASH & CASH FUND & FTX CASH (E… ┆ 1000.0 ┆ 0.0    ┆ 0.0           ┆ -1000.0 │
│ AAAA ┆ INDEX A                         ┆ 1000.0 ┆ 0.3333 ┆ 2333.1        ┆ 1333.1  │
│ BBBB ┆ INDEX B                         ┆ 2000.0 ┆ 0.3333 ┆ 2333.1        ┆ 333.1   │
│ CCCC ┆ INDEX C                         ┆ 3000.0 ┆ 0.3333 ┆ 2333.1        ┆ -666.9  │
└──────┴─────────────────────────────────┴────────┴────────┴───────────────┴─────────┘

Advice: invest funds into 'INDEX A' (AAAA).
Total account value: 7000.0 EUR
```

How to use it:

1. Ensure you have [uv](https://docs.astral.sh/uv/) installed.
2. Install dependencies: `uv sync`
3. Run the script: `uv run python main.py <ratios_file> <portfolio_file>`
4. Observe the output.

There are some `_dummy` files in the repo to illustrate how the CSVs should look.

Whilst I use it only for ETFs, it should work for any asset on DEGIRO that has an ISIN. It does however assume that there will only be one entry in the portfolio that does not have an ISIN, which is your cash account.

This script works when your portfolio on DEGIRO matches the file that has the desired ratios on how you want to invest and are using it monthly to see in which ETF you have to invest that month. I only wrote this after I bought my initial portfolio, so I do not know what this script will do when your portfolio does not match your selection of assets you want to invest in. Note that the `desired_ratios.csv` file has a line without an ISIN, this represents your cash account. Furthermore, the columns in the CSV file are Dutch for me and that is what this script interprets. If you have an English (or other language) DEGIRO interface, the column names may change and you may have to update the script to accommodate this.

Again: if you want to use this, use at your own risk.
