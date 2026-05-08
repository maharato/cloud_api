from sqlalchemy import (
    Column,
    BigInteger,
    ForeignKey,
    String,
    Boolean,
    JSON
)

from app.core.database import Base


class StoryProgress(Base):
    __tablename__ = "story_progress"

    id = Column(BigInteger, primary_key=True)

    player_id = Column(
        BigInteger,
        ForeignKey("players.id", ondelete="CASCADE")
    )

    current_story_state = Column(String(255))

    current_ending = Column(String(255))

    is_finished = Column(Boolean, default=False)

    choices_json = Column(JSON)