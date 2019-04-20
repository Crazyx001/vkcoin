from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import vk_api
import vkcoin

vk_session = vk_api.VkApi(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  # Токен ВКонтакте
merchant = vkcoin.VKCoinApi(user_id=123456789, key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  # Ваш ID и ключ

longpoll = VkBotLongPoll(vk_session, group_id=123456789)  # Инициализируем LongPoll
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:  # Если пользователь отправил нам любое сообщение
        user_balance = merchant.get_user_balance(event.obj.from_id)  # Получаем его баланс
        user_balance = float(user_balance['response'][str(event.obj.from_id)]) / 1000  # Переводим всё в читабельный вид
        vk.messages.send(user_id=event.obj.from_id, message='Ваш баланс: {balance}'.format(balance=user_balance), random_id=get_random_id())  # Отправляем ответ
        # Вместо этого вы можете выполнить ваши действия
