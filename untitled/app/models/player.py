from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Boolean,
    TIMESTAMP,
    func
)

from app.core.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(BigInteger, primary_key=True)

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    is_active = Column(Boolean, default=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )