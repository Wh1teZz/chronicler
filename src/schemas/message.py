from sqlalchemy import Column, String, Integer, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from schemas.base import Base
from schemas.player import Player


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    publicInfo = Column(String)
    day = Column(Integer)
    nomination = Column(Boolean)
    toPlayerName = Column(String)
    fromPlayerID = Column(Integer, ForeignKey('player.id'))
    fromPlayer = relationship("Player", back_populates="messages")

    def __init__(self, fromPlayer: Player, toPlayerName, content: str, 
    publicInfo: str, day: int, nomination=False):
        self.content = content
        self.publicInfo = publicInfo
        self.day = day
        self.fromPlayer = fromPlayer
        self.toPlayerName = toPlayerName
        self.nomination = nomination
        
