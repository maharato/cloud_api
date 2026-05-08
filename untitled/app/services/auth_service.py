from sqlalchemy import select

from app.models.player import Player

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    async def register(db, data):

        player = Player(
            username=data.username,
            email=data.email,
            password_hash=hash_password(data.password)
        )

        db.add(player)

        await db.commit()

        await db.refresh(player)

        token = create_access_token(
            {"sub": str(player.id)}
        )

        return {
            "accessToken": token,
            "playerId": player.id
        }

    @staticmethod
    async def login(db, data):

        result = await db.execute(
            select(Player).where(
                Player.username == data.username
            )
        )

        player = result.scalar_one_or_none()

        if not player:
            return None

        if not verify_password(
                data.password,
                player.password_hash
        ):
            return None

        token = create_access_token(
            {"sub": str(player.id)}
        )

        return {
            "accessToken": token,
            "playerId": player.id
        }