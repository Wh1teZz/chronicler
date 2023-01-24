from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from schemas.base import Base

class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String) #this is the discord name
    messagesSent = Column(Integer)
    messagesRecv = Column(Integer)
    charSent = Column(Integer)
    charRecv = Column(Integer)
    messages = relationship("Message", back_populates="fromPlayer")

    def __init__(self, name, messagesSent, messagesRecv, charSent, charRecv):
        self.name = name
        self.messagesSent = messagesSent
        self.messagesRecv = messagesRecv
        self.charSent = charSent
        self.charRecv = charRecv