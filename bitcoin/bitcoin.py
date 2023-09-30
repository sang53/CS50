import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    num = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

while True:
    try:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        break
    except requests.RequestException:
        continue

price = bitcoin.json()["bpi"]["USD"]["rate_float"] * num
print(f"${price:,.4f}")

