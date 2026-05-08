from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.middleware.auth_dependency import get_current_user
from app.models.player import Player
from app.schemas.story import StoryUpdateRequest
from app.services.story_service import StoryService

router = APIRouter(prefix="/story", tags=["story"])


@router.get("/")
async def get_story(
        db: AsyncSession = Depends(get_db),
        current_user: Player = Depends(get_current_user)
):
    return await StoryService.get_story(db, current_user.id)


@router.put("/")
async def update_story(
        data: StoryUpdateRequest,
        db: AsyncSession = Depends(get_db),
        current_user: Player = Depends(get_current_user)
):
    return await StoryService.update_story(db, current_user.id, data)