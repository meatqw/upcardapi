from api.models import *
from services.tinkoff.tinkoff_service import Tinkoff
from services.send_message_service import SendMsg


def check_payment():
    """Проверка статуса плаьежей по крону"""
    for subscribe in UserSubscribe.objects.all():
        tinkoff = Tinkoff()
        try:
            if subscribe.status is False:
                payment_status = tinkoff.get_state(str(subscribe.payment_id.payment_id))

                subscribe.payment_id.status = payment_status['Status']
                subscribe.payment_id.save()

                if payment_status['Status'] == 'CONFIRMED':
                    SendMsg.send_msg(1655138958, f'NEW SUBSCRIBE {payment_status["Amount"]}')
                    subscribe.status = True
                    subscribe.save()
        except Exception as e:
            SendMsg.send_msg(1655138958, str(e))

