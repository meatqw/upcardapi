import requests



def send_message_email(email, link):
    
    headers = {
        'authorization': '7X5l68iaYji64yMjDKE7p1ksROdFkJFhwzts'
    }

    data = {
        'subject': 'UpCard Авторизация',
        'html': f'<html><head></head><body><p>Для авторизации перейдите по ссылке {link}</p><br><p>Спасибо, что выбрали нас!</p></body></html>',
        'from': 'admin@upcard.online',
        'to': f'{email}'
    }
    
    request = requests.post('https://api.smtp.bz/v1/smtp/send', headers=headers, data=data)
    return request.json()['result']
