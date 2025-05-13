from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.category import CategoryCreate, CategoryRead
from app.crud import category as category_crud

router = APIRouter(
    prefix='/categories', tags=['Categories']
)

@router.post('/', response_model=CategoryRead)
async def create_category(data : CategoryCreate, db : AsyncSession = Depends(get_session)):
    return await category_crud.create_category(data, db)

@router.get('/', response_model=list[CategoryRead])
async def list_categories(db : AsyncSession = Depends(get_session)):
    return await category_crud.get_all_categories(db)