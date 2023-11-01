from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.Base import Base

class GameName(Base):
    __tablename__ = "game_names"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), unique=True)

    game: Mapped['Game'] = relationship(back_populates="name")
    guesses: Mapped['Guess'] = relationship(back_populates="guessed_game_name")

    def __repr__(self):
        return f"<GameName(id='{self.id}', name='{self.name}', game='{self.game}')>"
