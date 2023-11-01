from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.Base import Base

class Audio(Base):
    __tablename__ = "audio"

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    link: Mapped[str] = mapped_column(String(), unique=True)

    game: Mapped['Game'] = relationship(back_populates="audio")

    def __repr__(self):
        return f"<Audio(game_id='{self.game_id}', link='{self.link}')>"
