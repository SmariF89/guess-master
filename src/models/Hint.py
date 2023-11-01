from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.Base import Base

class Hint(Base):
    __tablename__ = "hints"

    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), primary_key=True)

    publish_year: Mapped[int]
    publish_year_reqs: Mapped[int]

    genre: Mapped[str]
    genre_reqs: Mapped[int]

    sound_type: Mapped[str]
    sound_type_reqs: Mapped[int]

    creator: Mapped[str]
    creator_reqs: Mapped[int]

    platform: Mapped[str]
    platform_reqs: Mapped[int]

    game: Mapped['Game'] = relationship(back_populates="hint")
