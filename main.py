# - Have a defined ratio for wanted stocks and cash reserve
# - Get the current account
# - Determine the wanted state
# - Determine the single buy action to get closer to the wanted state
from os import path

import polars as pl
import sys

def load_ratios(ratios_file_name: str) -> pl.DataFrame:
    return pl.read_csv(ratios_file_name)

def load_portfolio(portfolio_file_name: str) -> pl.DataFrame:
    return pl.read_csv(portfolio_file_name,decimal_comma=True).select(isin="Symbool/ISIN",name="Product",value="Waarde in EUR")

def calculate_desired_state_with_diff(df_ratios: pl.DataFrame, df_portfolio: pl.DataFrame) -> pl.DataFrame:
    df_joined = df_portfolio.join(df_ratios, on="isin",nulls_equal=True)
    return df_joined.with_columns(desired_value=pl.col("ratio") * pl.sum("value")).with_columns(diff=pl.col("desired_value")- pl.col("value"))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {path.basename(sys.argv[0])} <ratios_file> <portfolio_file>")
        sys.exit(1)

    df_ratios = load_ratios(sys.argv[1])
    df_portfolio = load_portfolio(sys.argv[2])
    df_desired = calculate_desired_state_with_diff(df_ratios, df_portfolio)

    print("Resulting calculation:")
    print(df_desired)
    print()

    # Advice to invest everything into the stock with the highest possible diff, so only do one buy action each month
    # to avoid paying too much transaction fees
    (isin, name) = df_desired.sort("diff", descending=True).select("isin", "name").row(0)
    print(f"Advice: invest funds into '{name}' ({isin}).")
    print(f"Total account value: {df_desired.select("value").sum().item()} EUR")
