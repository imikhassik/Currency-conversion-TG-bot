import requests
import json


from config import currencies


class APIException(Exception):
    pass


class Conversion:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            if base.lower() not in currencies.keys():
                raise APIException(f"Не нашёл такой валюты: {base}")
            elif quote.lower() not in currencies.keys():
                raise APIException(f"Не нашёл такой валюты: {quote}")
            elif not amount.isnumeric():
                raise APIException(f"{amount} не похоже на количество!")
        except APIException as e:
            return e
        else:
            base = currencies[base.lower()]
            quote = currencies[quote.lower()]
            amount = float(amount)
            response = requests.get(f'https://api.exchangerate.host/convert?from={base}&to={quote}')
            data = json.loads(response.content)
            return round(data['info']['rate'] * amount, 2)
