from db import get_last_chats


def build_memory():

    chats=get_last_chats()

    memory=""

    for user,bot in chats:
        memory += f"User: {user}\nAI: {bot}\n"

    return memory