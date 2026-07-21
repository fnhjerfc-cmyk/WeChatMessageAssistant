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
            ORDER BY receive_time DESC, id DESC
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

    def get_message_by_id(self, message_id):
        row = self.database.get_message_by_id(message_id)

        if row is None:
            return None

        return Message(
            id=row[0],
            group_name=row[1],
            sender=row[2],
            content=row[3],
            receive_time=row[4]
        )

    def search_messages(self, keyword):
        cursor = self.database.conn.cursor()

        search_pattern = f"%{keyword}%"

        cursor.execute("""
            SELECT
                id,
                group_name,
                sender,
                content,
                receive_time
            FROM messages
            WHERE group_name LIKE ?
                OR sender LIKE ?
                OR content LIKE ?
            ORDER BY receive_time DESC, id DESC
        """, (search_pattern, search_pattern, search_pattern))

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