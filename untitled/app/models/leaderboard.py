from sqlalchemy import (
    Column,
    BigInteger,
    ForeignKey,
    Integer,
    TIMESTAMP,
    func
)

from app.core.database import Base


class LeaderboardEntry(Base):
    __tablename__ = "leaderboard_entries"

    id = Column(BigInteger, primary_key=True)

    player_id = Column(
        BigInteger,
        ForeignKey("players.id", ondelete="CASCADE")
    )

    score = Column(Integer, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )