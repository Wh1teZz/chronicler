from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship
from schemas.base import Base

class TownSquare(Base):
    __tablename__ = 'TownSquare'
    
    id = Column(Integer, primary_key=True)
    players = relationship("Player", back_populates="TownSquare")
    day = Column(Integer)

    def __init__(self, day=1):
        self.day = day
