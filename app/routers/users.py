from fastapi import APIRouter, Depends
from app.schemas.user import UserRead
from app.auth.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/me', response_model=UserRead)
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user
