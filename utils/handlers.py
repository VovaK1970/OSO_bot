from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class BasicHandler:
    def __init__(self, trigger_phrases=None):
        assert isinstance(trigger_phrases, list | str | None), 'trigger_phrases must be provided'

        self.trigger_phrases = trigger_phrases

    def react(self, text: '', *args, **kwargs):
        return {}


class HelloHandler(BasicHandler):
    def react(self, text: '', *args, **kwargs):
        return {'text': 'Добро пожаловать в ОСО!'}


class MenuHandler(BasicHandler):

    def react(self, text: '', kb: VkKeyboard = None, *args, **kwargs):
        return {'text': 'Привет!', 'keyboard': kb.get_keyboard()}


class CommandHandler:
    commands = {}

    def __init__(self):
        for command in self.commands.keys():
            assert command.startswith('/'), 'command must start with /'
            assert ' ' not in command, 'command must not contain spaces'

    def react(self, command: '', *args, **kwargs):
        assert command in self.commands.keys(), 'unknown command'
        return self.commands.get(command, None)(*args, **kwargs)


class ModeChangeHandler(CommandHandler):

    def __init__(self):
        commands = {
            '/Зарегисрироваться': self.register_user,
            '/Зарегистрировать мероприятие': self.register_event,
            '/Завершить': self.finish,
            '/Отмена': self.exit,
        }

        super().__init__()

    def register_user(self):
        return {'mode': 'REGISTER_USER', 'result': None}

    def register_event(self):
        if 'name' not in user_input:
            user_input['name'] = message
            return {'mode': 'REGISTER_EVENT', 'input': 'description', 'prompt': 'Введите название мероприятия:'}

        if 'name' in user_input:
            name = user_input['name']

            event = add_event(db, name)

            user_input.clear()

            return {'mode': 'DEFAULT', 'result': 'Событие "{event.name}" успешно зарегистрировано!'}

        return {'mode': 'REGISTER_EVENT', 'input': 'name', 'prompt': 'Введите название мероприятия:'}


    def finish(self):
        return {'mode': 'DEFAULT', 'result': True}

    def exit(self):
        return {'mode': 'DEFAULT', 'result': True}

class EventHandler(CommandHandler):

    def __init__(self):
        self.commands = {
            '/Создать': self.add_event,
            '/Зарегистрироваться': self.apply,
            '/О событии':self.get_event_info
        }

    def add_event(self, event_data:dict, user_data:dict):
        pass

    def apply(self, event_id:int, user_data:dict):
        pass

    def get_event_info(self, event_id:int):
        pass
