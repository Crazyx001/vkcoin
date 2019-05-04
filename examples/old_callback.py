import vkcoin

callback = vkcoin.VKCoinWS(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  # Ваш токен или ссылка на Iframe


@callback.handler
def payment_received(data):
    """
    При получении платежа будет запущена эта функция. Она может называться как угодно

    :param data['to_id']: Ваш ID ВКонтакте
    :param data['balance']: Ваш текущий баланс
    :param data['user_from']: Отправитель платежа
    :param data['amount']: Количество полученных VK Coin
    """

    user_id = data['user_from']
    amount = data['amount']

    print('Получен платёж на сумму {amount} от {user_id}'.format(amount=amount, user_id=user_id))
    # Вместо print вы можете выполнить ваши действия


callback.run_ws()  # Запускаем  прослушивание
