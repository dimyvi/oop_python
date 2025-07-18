class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        del cls.msgs[id(msg)]

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls ,num):
        all_messages = list(cls.msgs.values())
        last_messages = all_messages[-num:] if num <= len(all_messages) else all_messages
        return [msg.text for msg in last_messages]

    @classmethod
    def total_messages(cls ,msg):
        print(len(msg))

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
