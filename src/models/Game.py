from typing import List
from src.models.Base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Integer, func

from datetime import datetime

class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_id: Mapped[int] = mapped_column(ForeignKey('game_names.id'), unique=True)
    num: Mapped[int] = mapped_column(Integer, unique=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    name: Mapped['GameName'] = relationship(back_populates="game")
    audio: Mapped[List['Audio']] = relationship(back_populates="game")
    stats: Mapped['Stat'] = relationship(back_populates="game")
    guesses: Mapped[List['Guess']] = relationship(back_populates="game")
    hint: Mapped['Hint'] = relationship(back_populates="game")

    def __repr__(self):
        return f"<Game(name_id='{self.name_id}', num={self.num}, date_created='{self.date_created}')>"
