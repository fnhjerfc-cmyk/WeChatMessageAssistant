from dataclasses import dataclass


@dataclass
class Message:
    """微信消息模型"""

    id: int
    group_name: str
    sender: str
    content: str
    receive_time: str

    is_at_me: int = 0
    reminder_time: str = ""
    reminder_status: int = 0