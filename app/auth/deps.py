from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.auth.jwt_handler import decode_access_token
from app.crud.user import get_user_by_email, get_user_by_id
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
        token : str = Depends(oauth2_scheme),
        db : AsyncSession = Depends(get_session)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Не удалось проверить учетные данные',
        headers={"WWW-Authenticate": "Bearer"}
    )
    user_id = decode_access_token(token)
    if user_id is None:
        raise credentials_exception

    user = await get_user_by_id(int(user_id), db)
    if user is None:
        raise credentials_exception
    return user