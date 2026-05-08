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

    @staticmethod
    async def submit_score(db, player_id, score):
        new_entry = LeaderboardEntry(
            player_id=player_id,
            score=score
        )
        db.add(new_entry)
        await db.commit()
        await db.refresh(new_entry)
        return new_entry