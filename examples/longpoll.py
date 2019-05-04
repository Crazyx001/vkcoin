import vkcoin

merchant = vkcoin.VKCoinApi(user_id=123456789, key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  # Ваш ID и ключ


@merchant.lp_handler
def payment_received(data):
    """
    При получении платежа будет запущена эта функция. Она может называться как угодно

    :param data['to_id']: Ваш ID ВКонтакте
    :param data['id']: ID платежа
    :param data['created_at']: Unix timestamp, время когда был совершён платёж
    :param data['from_id']: ID отправителя платежа
    :param data['amount']: Количество полученных VK Coin
    """

    user_id = data['from_id']
    amount = data['amount']

    print('Получен платёж на сумму {amount} от {user_id}'.format(amount=amount, user_id=user_id))
    # Вместо print вы можете выполнить ваши действия


merchant.longpoll_start(tx=[1])  # Запускаем LongPoll