from util.playerActions import *
from util.gameActions import *

if __name__ == "__main__":
    addPlayers(["JZT", "Arky"])
    jzt = getPlayerByName("JZT")
    assert jzt.name == "JZT"
    arky = getPlayerByName("Arky")
    assert arky.name == "Arky"
    message(jzt.name, arky.name, "its working!", 1)
    message(jzt.name, arky.name, "db is set up! btw i've poisoned someone", 1)
    messagesFromJZT = getMessagesFromPlayer("JZT")
    for m in messagesFromJZT:
        print(f'Content: {m.content}\nPublic Info: {m.publicInfo}')
        assert m.fromPlayerID == 1
    messagesToArky = getMessagesToPlayer("Arky")
    for m in messagesToArky:
        assert m.toPlayerName == "Arky"

    