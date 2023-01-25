from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship
from schemas.base import Base

class TownSquare(Base):
    __tablename__ = 'townsquare'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reportChannel = Column(String)
    day = Column(Integer)
    isNomination = Column(Boolean)

    def __init__(self, name: str, reportChannel: str, day: int=1, isNomination: bool=False):
        self.name = name
        self.reportChannel = reportChannel
        self.day = day
        self.isNomination = isNomination
