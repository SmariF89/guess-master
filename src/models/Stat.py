from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.Base import Base

class Stat(Base):
    __tablename__ = "stats"

    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), primary_key=True)

    times_won: Mapped[int]
    times_lost: Mapped[int]
    times_started: Mapped[int]

    average_guess_count: Mapped[float]

    game: Mapped['Game'] = relationship(back_populates="stats")

    def __repr__(self):
        return f"<Audio(game_id='{self.game_id}', link='{self.link}')>"
