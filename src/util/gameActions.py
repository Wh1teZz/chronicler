from schemas.message import Message
from schemas.player import Player
from schemas.base import session_factory

def addPlayers(names: list) -> None:
    session = session_factory()
    for name in names:
        session.add(Player(name, 0, 0, 0, 0))
    session.commit()
    session.close()