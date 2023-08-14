import requests


class SendMsg:

    email_service_token = '7X5l68iaYji64yMjDKE7p1ksROdFkJFhwzts'

    @staticmethod
    def send_msg(id: int, text: str):
        try:
            token = "6183526112:AAEeN5HurcqvW4jPpMlY1Oqpog0QY2lrwTo"
            chat_id = id
            url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
            results = requests.get(url_req)
            return results
        except Exception as e:
            return False

    @staticmethod
    def send_message_email_welcome(email: str, link: str):

        headers = {
            'authorization': SendMsg.email_service_token
        }

        data = {
            'subject': 'UpCard Авторизация',
            'html': f'<html><head></head><body><p>Для авторизации перейдите по ссылке {link}</p><br><p>Спасибо, что выбрали нас!</p></body></html>',
            'from': 'admin@upcard.online',
            'to': f'{email}'
        }

        request = requests.post('https://api.smtp.bz/v1/smtp/send', headers=headers, data=data)
        return request.json()['result']

    @staticmethod
    def send_message_email_subscribe(email: str):

        headers = {
            'authorization': SendMsg.email_service_token
        }

        data = {
            'subject': 'UpCard Подписка',
            'html': f'<html><head></head><body><p>Вы оформили базовую подписку.</p></body></html>',
            'from': 'admin@upcard.online',
            'to': f'{email}'
        }

        request = requests.post('https://api.smtp.bz/v1/smtp/send', headers=headers, data=data)
        return request.json()['result']
