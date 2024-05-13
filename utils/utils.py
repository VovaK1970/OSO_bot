class Sender():
    def __init__(self, api):
        self.api = api

    def __call__(self, text, *args, **kwargs):
        return self.api.messages.send(message=text, random_id=0, **kwargs)

