from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth")


@router.post("/register")
async def register(
        data: RegisterRequest,
        db: AsyncSession = Depends(get_db)
):
    return await AuthService.register(db, data)


@router.post("/login")
async def login(
        data: LoginRequest,
        db: AsyncSession = Depends(get_db)
):

    result = await AuthService.login(db, data)

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return result
