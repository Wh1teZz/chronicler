from schemas.message import Message
from schemas.player import Player
from schemas.base import session_factory
from config import *
from random import randint, choices

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
    player = getPlayerByName(name)
    messages = session.query(Message).filter(Message.fromPlayer == player).all()
    session.close()
    return messages

def getMessagesToPlayer(name: str) -> list[Message]:
    session = session_factory()
    messages = session.query(Message).filter(Message.toPlayerName == name).all()
    session.close()
    return messages

def generatePublicInfo(content, volume, fromPlayerName, toPlayerName, day) -> str:
    # generate a random num for variety of public info
    r = randint(0,3)

    # adjust volume based on message length
    messageVolume = len(content) // 2
    if messageVolume > LOUD:
        volume += 20
    elif messageVolume > MODERATE:
        volume += 10
    elif messageVolume > QUIET:
        volume += 5
        
    # check content for keywords
    messageKeywords = BASE_KEYWORDS
    for k in KEYWORDS:
        if k in content:
            messageKeywords.append(k)

    # get some keywords
    k0, k1, k2 = choices(messageKeywords, k=3)

    # get messages from player to target
    messagesFromPlayer = getMessagesFromPlayer(fromPlayerName)
    nMessagesToPlayer = 0
    for m in messagesFromPlayer:
        if m.toPlayerName == toPlayerName:
            nMessagesToPlayer += 1
    
    # adjust for volume
    if volume < QUIET:
        if r == 0:
            return f'{fromPlayerName} has conversed with someone on day {day}.'
        elif r == 1:
            return f'{fromPlayerName} has conversed with someone. The day is uncertain.'
        elif r == 2:
            return f'{fromPlayerName} has conversed with {toPlayerName}. The day is uncertain.'
        elif r == 3:
            return f'{fromPlayerName} has conversed with someone. The day is uncertain. However, they conversed about "{k0}"'
    elif volume < MODERATE:
        if r == 0:
            return f'{fromPlayerName} has conversed with {toPlayerName} on day {day}.'
        elif r == 1:
            return f'{fromPlayerName} has conversed with {toPlayerName}. The day is {day}. They talked about "{k0}"'
        elif r == 2:
            return f'{fromPlayerName} has conversed with someone. The day is {day}. {fromPlayerName} has sent up to {volume} messages this game.'
        elif r == 3:
            return f'{fromPlayerName} has conversed with someone. The day is uncertain. However, they conversed about "{k0}" and "{k1}"'
    elif volume < LOUD:
        if r == 0:
            return f'{fromPlayerName} has conversed with {toPlayerName} on day {day}. They talked about "{k0}" and "{k1}".'
        elif r == 1:
            return f'{fromPlayerName} has conversed with {toPlayerName}. The day is {day}. {fromPlayerName} has sent {nMessagesToPlayer} messages to {toPlayerName} this game.'
        elif r >= 2:
            return f'{fromPlayerName} has conversed with {toPlayerName} on day {day}. They talked about "{k0}", "{k1}" and "{k2}.'
    else:
        return f'{fromPlayerName} has conversed with {toPlayerName} on day {day}. They talked about "{k0}", "{k1}" and "{k2}. {fromPlayerName} has sent {nMessagesToPlayer} messages to {toPlayerName} this game.'


def calculateVolume(player: Player) -> int:
    return player.messagesSent + (player.charSent // 100)

def message(fromPlayer: Player, toPlayerName: str, content: str, day: int, nomination=False) -> None:
    session = session_factory()
    volume = calculateVolume(fromPlayer)
    publicInfo = generatePublicInfo(content, volume, fromPlayer.name, toPlayerName, day)
    session.add(Message(fromPlayer, toPlayerName, content, publicInfo, day, nomination))
    session.commit()
    session.close()

