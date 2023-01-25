from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from schemas.base import Base

class Channel(Base):
    __tablename__ = 'channel'
    
    id = Column(Integer, primary_key=True)
    channelName = Column(String)

    def __init__(self, channelName: str):
        self.channelName = channelName
