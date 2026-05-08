from sqlalchemy import select, desc

from app.models.leaderboard import LeaderboardEntry
from app.models.player import Player


class LeaderboardService:

    @staticmethod
    async def get_top_players(db, limit=10):

        result = await db.execute(
            select(
                Player.username,
                LeaderboardEntry.score
            )
            .join(
                Player,
                Player.id == LeaderboardEntry.player_id
            )
            .order_by(desc(LeaderboardEntry.score))
            .limit(limit)
        )

        rows = result.all()

        return [
            {
                "username": row.username,
                "score": row.score
            }
            for row in rows
        ]