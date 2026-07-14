from models.message import Message


class MessageManager:
    """消息管理器"""

    def __init__(self):
        self.messages = []

    def add_message(self, message: Message):
        """添加一条消息"""
        self.messages.append(message)

    def get_messages(self):
        """返回所有消息"""
        return self.messages

    def get_today_count(self):
        """今日消息数量"""
        return len(self.messages)

    def get_at_me_count(self):
        """@我的数量"""
        return sum(msg.is_at_me for msg in self.messages)