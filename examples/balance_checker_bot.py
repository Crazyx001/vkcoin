import vk_requests
import vkcoin

from vbio import VkBot
from vbio.servers import LongPollClient

api = vk_requests.create_api(service_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  # Токен ВКонтакте
merchant = vkcoin.VKCoin(user_id=123456789, key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  # Ваш ID и ключ
bot = VkBot(api=api)
server = LongPollClient(bot)  # Инициализируем LongPoll


@bot.message_handler()  # При любом сообщении
def on_message(message):
    user_balance = merchant.get_balance(message.from_id)  # Получаем баланс отправителя
    user_balance = float(user_balance[str(message.from_id)]) / 1000  # Переводим всё в читабельный вид
    message.answer(message='Ваш баланс: {balance}'.format(balance=user_balance))


if __name__ == '__main__':
    server.run()
