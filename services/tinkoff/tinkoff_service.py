import json
import requests
import hashlib


class Tinkoff:
    api_url = 'https://securepay.tinkoff.ru/v2/'

    # TERMINAL_TEST = '1688986064848DEMO'
    # PASSWORD_TEST = 'zf0lsbwur8h0dxcx'

    TERMINAL = '1688986064848'
    PASSWORD = 'xtep9xb8e2veaa7t'

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def __get(self, method: str):
        return requests.get(url=self.api_url + method, headers=self.headers)

    def __post(self, method: str, data: dict):
        return requests.post(url=self.api_url + method, headers=self.headers, data=json.dumps(data))

    def get_token(self, payment_id: str):
        token_string = self.PASSWORD + payment_id + self.TERMINAL
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

    def get_state(self, payment_id: str):
        """Проверка платежр"""
        req_data = {
            "TerminalKey": self.TERMINAL,
            "PaymentId": payment_id,
            "Token": self.get_token(payment_id)
        }

        req = self.__post("GetState", req_data)
        return req.json()
