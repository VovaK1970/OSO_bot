import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

from env import OSO_APP_VK_TOKEN as token

HELLO_WORDS = ('start', 'begin', 'начать', 'привет', 'добрый день', 'здравствуйте')

class Sender():
    def __init__(self, api):
        self.api = api

    def __call__(self, text, *args, **kwargs):
        return self.api.messages.send(message=text, random_id=0, **kwargs)


def run_bot(token):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    sender = Sender(vk)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text.lower()
            user_id = event.user_id

            if text in HELLO_WORDS:
                sender('Добро пожаловать в ОСО!', user_id=user_id)
            else:
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('Привет', color=VkKeyboardColor.SECONDARY)
                keyboard.add_button('Здравствуйте', color=VkKeyboardColor.NEGATIVE)
                sender('Привет!',
                       user_id=user_id,
                       keyboard=keyboard.get_keyboard())









if __name__ == '__main__':
    run_bot(token)