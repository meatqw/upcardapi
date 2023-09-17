import json
import requests
import hashlib


class Tinkoff:
    api_url = 'https://securepay.tinkoff.ru/v2/'

    TERMINAL = '1688986064848DEMO'
    PASSWORD = 'zf0lsbwur8h0dxcx'

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def __get(self, method: str):
        return requests.get(url=self.api_url + method, headers=self.headers)

    def __post(self, method: str, data: dict):
        return requests.post(url=self.api_url + method, headers=self.headers, data=json.dumps(data))

    def get_token(self, data):
        token_string = self.PASSWORD + data['PaymentId'] + self.TERMINAL
        sha256 = hashlib.sha256()
        sha256.update(token_string.encode('utf-8'))
        return sha256.hexdigest()

    def init(self, data: dict):
        """Инициализация платежа"""
        req_data = {
            "TerminalKey": self.TERMINAL,
            "Amount": float(data['Amount']) * 100,
            "OrderId": data['OrderId'],
        }

        req = self.__post("Init", req_data)
        return req.json()

    def get_state(self, data: dict):

        req_data = {
            "TerminalKey": self.TERMINAL,
            "PaymentId": data['PaymentId'],
            "Token": self.get_token(data)
        }

        req = self.__post("GetState", req_data)
        return req.json()
