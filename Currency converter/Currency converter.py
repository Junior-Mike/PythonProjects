import requests

# Getting the exchange rate
def exchange_rate(base_currency, target_currency):
    api_key = 'Your API key'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'

    response = requests.get(url) # Sending a GET request
    data = response.json() # Converts the JSON response to a dictionary

    if response.status_code != 200 or data['result'] != 'success':
        raise Exception('!Error when receiving currency exchange rate data!')
    return data['conversion_rate']

# Get the result 
def convert_currency(amount, rate):
    return round(amount * rate, 2)


def main():
    base_currency = input('Input base currency: ').upper()
    target_currency = input('Input target currency: ').upper()
    amount = float(input('Input amount to convert: '))

    try:
        rate = exchange_rate(base_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        print(f'{amount} {base_currency} = {converted_amount} {target_currency}')
    except Exception as ex:
        print('Error!')

if __name__ == '__main__':
    main()