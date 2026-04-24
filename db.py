import sqlite3

conn = sqlite3.connect(
    "chat.db",
    check_same_thread=False
)

cursor=conn.cursor()


def init_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_reply TEXT
    )
    """)

    conn.commit()



def save_chat(user_msg,bot_reply):

    cursor.execute(
        """
        INSERT INTO chats
        (user_message,bot_reply)
        VALUES (?,?)
        """,
        (user_msg,bot_reply)
    )

    conn.commit()



def get_last_chats(limit=2):

    cursor.execute(
        """
        SELECT user_message,bot_reply
        FROM chats
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows=cursor.fetchall()

    return rows[::-1]