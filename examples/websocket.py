import vkcoin

merchant = vkcoin.VKCoin(user_id=123456789, key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', token='xxxxxxxxxxxxxxxxxxx')  # Ваш ID, токен VK Coin и ВК


@merchant.payment_handler(handler_type='websocket')
def payment_received(data):
    """
    При получении платежа будет запущена эта функция. Она может называться как угодно

    :param data['to_id']: Ваш ID ВКонтакте
    :param data['balance']: Ваш текущий баланс
    :param data['from_id']: Отправитель платежа
    :param data['amount']: Количество полученных VK Coin
    """

    user_id = data['from_id']
    amount = data['amount']

    print('Получен платёж на сумму {amount} от {user_id}'.format(amount=amount, user_id=user_id))
    # Вместо print вы можете выполнить ваши действия


merchant.run_websocket(tx=[1])  # Запускаем  прослушивание
