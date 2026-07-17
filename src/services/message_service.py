from src.models.message import Message
from src.services.database_service import DatabaseService


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
                id,
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
                id=row[0],
                group_name=row[1],
                sender=row[2],
                content=row[3],
                receive_time=row[4]
            )

            messages.append(message)

        return messages