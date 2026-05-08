from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.middleware.auth_dependency import get_current_user
from app.models.player import Player
from app.schemas.progress import ProgressUpdateRequest
from app.services.progress_service import ProgressService

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/")
async def get_progress(
        db: AsyncSession = Depends(get_db),
        current_user: Player = Depends(get_current_user)
):
    return await ProgressService.get_progress(db, current_user.id)


@router.put("/")
async def update_progress(
        data: ProgressUpdateRequest,
        db: AsyncSession = Depends(get_db),
        current_user: Player = Depends(get_current_user)
):
    return await ProgressService.update_progress(db, current_user.id, data)