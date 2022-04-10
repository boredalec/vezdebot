import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton

session = vk_api.VkApi(token = "7ae0793b35f3288b769bd6e4a540ff995984ce91d444d2338462536361be86fd2d21fd288e7cb2953d6fc")

def send_message(user_id, message, keyboard = None):
    post = {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    }

    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    session.method("messages.send", post)


for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id


        if text == "привет":
            send_message(user_id, "Привет вездекодерам!")

        if text == "начать":
            keyboard = VkKeyboard(one_time=True)

            keyboard.add_button('Мемы', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Анекдоты', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Видео приколы', VkKeyboardColor.PRIMARY)
            keyboard.add_line()

            keyboard.add_button('Поддержка 💬‍', VkKeyboardColor.SECONDARY)
            keyboard.add_button('Профиль ⚡', VkKeyboardColor.SECONDARY)
            keyboard.add_line()

            keyboard.add_button('Пожертвования 🤑', VkKeyboardColor.POSITIVE)
            keyboard.add_button('О боте 💿', VkKeyboardColor.NEGATIVE)


            send_message(user_id, 'Нажми на одну из кнопок, чтобы продолжить', keyboard)

        if text == "главная 🔥":
            keyboard = VkKeyboard(one_time=True)

            keyboard.add_button('Мемы', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Анекдоты', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Видео приколы', VkKeyboardColor.PRIMARY)
            keyboard.add_line()

            keyboard.add_button('Поддержка 💬‍', VkKeyboardColor.SECONDARY)
            keyboard.add_button('Профиль ⚡', VkKeyboardColor.SECONDARY)
            keyboard.add_line()

            keyboard.add_button('Пожертвования 🤑', VkKeyboardColor.POSITIVE)
            keyboard.add_button('О боте 💿', VkKeyboardColor.NEGATIVE)


            send_message(user_id, 'Главная 🔥', keyboard)

        if text == "поддержка 💬‍":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, 'Поддержка - @boredalec или @danyaser', keyboard)

        if text == "профиль ⚡":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, 'Просмотрено мемов: 0 \n Ваши пожертвования: 0р', keyboard)

        if text == "пожертвования 🤑":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, 'В разработке...', keyboard)

        if text == "о боте 💿":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, 'Бот был написан командой "Critical Damage 3.0" \n @boredalec \n @danyaser \n @rodriguezgp \n @id633353262', keyboard)

        if text == "мемы":
            keyboard = VkKeyboard(one_time=True)

            keyboard.add_button('Интернет-мемы 🌐', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Музыкальные мемы 🎵', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Мемы с котами', VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('18+ мемы 🔞', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Чёрный юмор', VkKeyboardColor.PRIMARY)
            keyboard.add_line()

            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "Выбери категорию", keyboard)

        if text == "анекдоты":
            keyboard = VkKeyboard(one_time=True)

            keyboard.add_button('Интернет-мемы 🌐', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Музыкальные мемы 🎵', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Мемы с котами', VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('18+ мемы 🔞', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Чёрный юмор', VkKeyboardColor.PRIMARY)
            keyboard.add_line()

            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "Выбери категорию", keyboard)

        if text == "видео приколы":
            keyboard = VkKeyboard(one_time=True)

            keyboard.add_button('Интернет-мемы 🌐', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Музыкальные мемы 🎵', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Мемы с котами', VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('18+ мемы 🔞', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Чёрный юмор', VkKeyboardColor.PRIMARY)
            keyboard.add_line()

            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "Выбери категорию", keyboard)

        if text == "интернет-мемы 🌐":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "В разработке...", keyboard)

        if text == "музыкальные мемы 🎵":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "В разработке...", keyboard)

        if text == "мемы с котами":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "В разработке...", keyboard)

        if text == "18+ мемы 🔞":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "В разработке...", keyboard)

        if text == "чёрный юмор":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Главная 🔥', VkKeyboardColor.SECONDARY)

            send_message(user_id, "В разработке...", keyboard)