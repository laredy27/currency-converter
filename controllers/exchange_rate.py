import json
import requests
import time

EXCHANGE_RATE_FEEDS_URL = "http://www.floatrates.com/daily/"

def get_currency_rates(currency):
    res = requests.get(EXCHANGE_RATE_FEEDS_URL + currency + ".json")
    return json.loads(res.text)

def convert(input):
    data = json.loads(input)
    res = dict()

    xrates = get_currency_rates(data['sourceCurrency'])
    if data['targetCurrency'] in xrates:
        target = data['targetCurrency']
        targetCurrency = xrates[target]
        rate = targetCurrency['rate']

        newAmount = data['amount'] * rate

        res['currency'] = target
        res['amount'] = round(newAmount, 2)
        res['date'] = time.asctime()
        res['updatedAt'] = targetCurrency['date']

        return json.dumps(res)

    else:
        data['message'] = "Cannot convert currency"
        return json.dumps(data)
    