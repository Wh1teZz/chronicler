from schemas.message import Message
from schemas.player import Player
from schemas.base import session_factory

def addPlayers(names: list) -> None:
    session = session_factory()
    for name in names:
        session.add(Player(name, 0, 0, 0, 0))
    session.commit()
    session.close()

def getPlayerByName(name: str) -> Player:
    session = session_factory()
    player = session.query(Player).filter(Player.name == name).first()
    session.close()
    return player

def getMessagesFromPlayer(name: str) -> list[Message]:
    session = session_factory()
    player = session.query(Player).filter(Player.name == name).first()
    messages = session.query(Message).filter(Message.fromPlayer == player).all()
    session.close()
    return messages

def message(fromPlayer: Player, toPlayer: Player, content, day, nomination=False) -> None:
    session = session_factory()
    session.add(Message(fromPlayer, toPlayer, content, day, nomination))
    session.commit()
    session.close()

