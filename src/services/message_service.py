from models.message import Message
from services.database_service import DatabaseService


class MessageService:

    def __init__(self):
        self.database = DatabaseService()

    def add_message(self, group_name, sender, content, receive_time):
        cursor = self.database.conn.cursor()

        cursor.execute("""
            INSERT INTO messages(
                group_name,
                sender,
                content,
                receive_time
            )
            VALUES(?,?,?,?)
        """, (
            group_name,
            sender,
            content,
            receive_time
        ))

        self.database.conn.commit()

    def get_all_messages(self):

        cursor = self.database.conn.cursor()

        cursor.execute("""
            SELECT
                group_name,
                sender,
                content,
                receive_time
            FROM messages
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        messages = []

        for row in rows:
            message = Message(
                group_name=row[0],
                sender=row[1],
                content=row[2],
                receive_time=row[3]
            )

            messages.append(message)

        return messages