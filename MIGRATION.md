# vkcoin
Миграция на версию 2.0

* VKCoinApi -> VKCoin
* VKCoinWS -> VKCoin
* callback_start -> run_callback
* longpoll_start -> run_longpoll
* run_ws -> run_websocket
* get_user_balance -> get_balance
* send_coins -> send_payment
* В get_balance необязательно передавать ID текущего аккаунта, что бы получить его баланс
* В ответе WebSocket `user_from` изменён на `from_id`
* При получении данных из функции (get_balance etc.) `['response']` писать не нужно.
