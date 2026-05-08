from sqlalchemy import (
    Column,
    BigInteger,
    ForeignKey,
    Integer
)

from app.core.database import Base


class PlayerProgress(Base):
    __tablename__ = "player_progress"

    id = Column(BigInteger, primary_key=True)

    player_id = Column(
        BigInteger,
        ForeignKey("players.id", ondelete="CASCADE")
    )

    current_loop = Column(Integer, default=0)

    total_loops_completed = Column(Integer, default=0)

    clues_found = Column(Integer, default=0)