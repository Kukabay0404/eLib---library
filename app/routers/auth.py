from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead, UserLogin
from app.database import get_session
from app.crud import user as user_crud
from app.auth.hash import verify_password
from app.auth.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register', response_model=UserRead)
async def register(user_data : UserCreate, db : AsyncSession = Depends(get_session)):
    existing = await user_crud.get_user_by_email(user_data.email, db)
    if existing:
        raise HTTPException(status_code=400, detail='Email уже зарегистрирован')
    user = await user_crud.create_user(user_data, db)
    return user

@router.post('/login')
async def login(
        form_data : OAuth2PasswordRequestForm = Depends(),
        db : AsyncSession = Depends(get_session)
):
    user = await user_crud.get_user_by_email(form_data.username, db)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Неверные email или пароль')
    token = create_access_token({'sub' : str(user.id)})
    return {'access_token' : token, 'token_type' : 'bearer'}