from schemas.player import Player
from schemas.channel import Channel
from schemas.townSquare import TownSquare
from schemas.base import session_factory

def addPlayers(names: list) -> bool:
    #check dupes
    if len(set(names)) != len(names): return False

    session = session_factory()
    for name in names:
        session.add(Player(name, 0, 0, 0, 0))
    session.commit()
    session.close()
    return True

def addChannels(channels: list) -> bool:
    #check dupes
    if len(set(channels)) != len(channels): return False

    session = session_factory()
    for channel in channels:
        session.add(Channel(channel))
    session.commit()
    session.close()
    return True

def initTownSquare(name: str, reportChannel: str) -> bool:
    session = session_factory()

    ts = session.query(TownSquare).all()
    if len(ts) != 0:
        session.close()
        return False

    session.add(TownSquare(name, reportChannel))
    session.commit()
    session.close()
    return True