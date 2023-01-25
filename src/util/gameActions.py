from schemas.player import Player
from schemas.channel import Channel
from schemas.townSquare import TownSquare
from schemas.message import Message
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

def getAllChannels() -> list[Channel]:
    session = session_factory()
    channels = session.query(Channel).all()
    session.close()
    return channels

def isChannel(channelName) -> bool:
    session = session_factory()
    channel = session.query(Channel).filter(Channel.channelName == channelName).first()
    session.close()
    return True if channel else False

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

def getTownSquare() -> TownSquare:
    session = session_factory()
    ts = session.query(TownSquare).first()
    session.close()
    return ts

def prevDay() -> int:
    session = session_factory()
    ts = session.query(TownSquare).first()
    ts.day -= 1
    day = ts.day
    session.add(ts)
    session.commit()
    session.close()
    return day

def nextDay() -> int:
    session = session_factory()
    ts = session.query(TownSquare).first()
    ts.day += 1
    day = ts.day
    session.add(ts)
    session.commit()
    session.close()
    return day

def resetGame() -> bool:
    session = session_factory()
    ts = session.query(TownSquare).all()
    for x in ts:
        session.delete(x)
    m = session.query(Message).all()
    for x in m:
        session.delete(x)
    p = session.query(Player).all()
    for x in p:
        session.delete(x)
    c = session.query(Channel).all()
    for x in c:
        session.delete(x)
    session.commit()
    session.close()
    return True