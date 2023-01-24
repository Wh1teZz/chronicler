from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from schemas.base import Base

class TownSquare(Base):
    __tablename__ = 'townsquare'
    
    id = Column(Integer, primary_key=True)
    players = relationship("Player", back_populates="townsquare")
    day = Column(Integer)

    def __init__(self, day=1):
        self.day = day
