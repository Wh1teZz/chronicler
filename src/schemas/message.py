from sqlalchemy import Column, String, Integer, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from schemas.base import Base
from schemas.player import Player


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    day = Column(Integer)
    nomination = Column(Boolean)
    toPlayer = Column(Integer, ForeignKey('player.id'))
    fromPlayer = relationship("Player", back_populates="messages")

    def __init__(self, fromPlayer: Player, toPlayer: Player, content: str, day: int, nomination=False):
        self.content = content
        self.day = day
        self.fromPlayer = fromPlayer
        self.toPlayer = toPlayer
        self.nomination = nomination
        
