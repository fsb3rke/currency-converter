from datetime import date
from tabulate import tabulate
import requests


TODAY = date.today()
ROOT = f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{TODAY}"

def print_currency_table() -> None:
    API_LINK = f"{ROOT}/currencies.json"
    data = requests.get(API_LINK).json()
    stack = []
    for i in data:
        stack.append([i, data[i]])
    
    print(tabulate(stack, tablefmt="github"))

def convert(c_from: str, c_to: str, value: float) -> float:
    API_LINK = f"{ROOT}/currencies/{c_from}/{c_to}.json"
    data = requests.get(API_LINK).json()
    new_value = float(data[c_to]) * value
    return new_value

def user_handle() -> None:
    print('\n')
    currency_from = str(input("from: "))
    currency_to = str(input("to: "))
    value = float(input("value: "))
    new_value = convert(currency_from, currency_to, value)

    print(f"{value}( {currency_from.upper()} ) => {new_value}( {currency_to.upper()} )")

def main():
    print_currency_table()
    user_handle()

if __name__ == "__main__":
    main()
