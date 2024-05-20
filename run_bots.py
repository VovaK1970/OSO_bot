import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

from env import OSO_APP_VK_TOKEN as token

from utils import Bots, utils

if __name__ == '__main__':
    basic_bot = Bots.BasicBot(token=token)

    basic_bot.start()
