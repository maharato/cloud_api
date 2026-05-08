from sqlalchemy import select
from app.models.progress import PlayerProgress


class ProgressService:

    @staticmethod
    async def get_progress(db, player_id):
        result = await db.execute(
            select(PlayerProgress).where(PlayerProgress.player_id == player_id)
        )
        progress = result.scalar_one_or_none()

        if not progress:
            # Create default progress if not exists
            progress = PlayerProgress(player_id=player_id)
            db.add(progress)
            await db.commit()
            await db.refresh(progress)

        return progress

    @staticmethod
    async def update_progress(db, player_id, data):
        result = await db.execute(
            select(PlayerProgress).where(PlayerProgress.player_id == player_id)
        )
        progress = result.scalar_one_or_none()

        if not progress:
            progress = PlayerProgress(player_id=player_id)
            db.add(progress)

        progress.current_loop = data.currentLoop
        progress.total_loops_completed = data.totalLoopsCompleted
        progress.clues_found = data.cluesFound

        await db.commit()
        await db.refresh(progress)
        return progress