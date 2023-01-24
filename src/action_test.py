from utils.actions import *

if __name__ == "__main__":
    addPlayers(["JZT", "Arky"])
    jzt = getPlayerByName("JZT")
    arky = getPlayerByName("Arky")
    message(jzt, arky, "its working!", 1)
    message(jzt, arky, "db is set up!", 1)
    messages = getMessagesFromPlayer("JZT")
    for m in messages:
        print(m.content)