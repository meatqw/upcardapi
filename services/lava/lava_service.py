import json

import requests


class Lava:
    api_url = 'https://api.lava.ru'

    LAVA_TOKEN = ('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJjMjRjZ'
                  'DhhYy0zOTg4LTBmNWYtMjkyMy0yODE5NmU0M2JjYzEiLCJ0'
                  'aWQiOiJmNzFjYmNjNC0yMjAyLTIzZTgtNThjNS03NDIxM2RiZT'
                  'UyZTUifQ.TfaQcN34iBsO2fSyzH9bcJvXzwfUh5CxpzNaa2ydJXQ')

    headers = {
        "Authorization": LAVA_TOKEN,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def __get(self, method: str):
        return requests.get(url=self.api_url + method, headers=self.headers)

    def __post(self, method: str, data: dict):
        return requests.post(url=self.api_url + method, headers=self.headers, data=json.dumps(data))

    def ping(self):
        return self.__get("/test/ping")

    def invoice(self, cost: int, order_id: int, signature: str, shop_id: str, success_usl: str):
        data = {
            "sum": cost,
            "orderId": order_id,
            "signature": signature,
            "shopId": shop_id,
            "successUrl": success_usl
        }

        req = self.__post("/business/invoice/create", data)
        print(req.json())


lava = Lava()
lava.ping()
lava.invoice(4, 1, "2", "8eb468c2-3ac1-11ee-be56-0242ac120002", 'https://google.com')
