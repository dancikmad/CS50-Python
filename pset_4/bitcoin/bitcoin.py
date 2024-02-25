import requests
import sys

coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    print(f"${coindesk(input_request_value()):,.4f}")

def input_request_value():
    try:

        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            return float(sys.argv[1])

    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


def coindesk(amount):
    """Send a get requests to the Coindesk API and return the value for the requested amount
    of Bitcoin"""
    try:
        response = requests.get(coindesk_api)
        data = response.json()
        value = data["bpi"]["USD"]["rate_float"]
        amount_value = amount * value

    except requests.RequestException:
        print("Coinbase not available. Please try again in a few minutes.")
        sys.exit()

    return amount_value


if __name__ == '__main__':
    main()

