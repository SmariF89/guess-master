from src.models.Base import Base

from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Guess(Base):
    __tablename__ = 'guesses'

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey('games.id'))
    guessed_game_name_id: Mapped[int] = mapped_column(ForeignKey('game_names.id'))

    correct: Mapped[bool] = mapped_column(Boolean())
    try_num: Mapped[int] = mapped_column(Integer())

    game: Mapped['Game'] = relationship(back_populates="guesses")
    guessed_game_name: Mapped['GameName'] = relationship(back_populates="guesses")
