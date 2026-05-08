from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.middleware.auth_dependency import get_current_user
from app.models.player import Player
from app.schemas.leaderboard import ScoreSubmitRequest
from app.services.leaderboard_service import LeaderboardService

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


@router.get("/")
async def get_leaderboard(
        limit: int = 10,
        db: AsyncSession = Depends(get_db)
):
    return await LeaderboardService.get_top_players(db, limit)


@router.post("/")
async def submit_score(
        data: ScoreSubmitRequest,
        db: AsyncSession = Depends(get_db),
        current_user: Player = Depends(get_current_user)
):
    return await LeaderboardService.submit_score(db, current_user.id, data.score)