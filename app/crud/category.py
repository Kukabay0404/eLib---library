from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.category import Category
from app.schemas.category import CategoryCreate

async def create_category(data : CategoryCreate, db : AsyncSession):
    category = Category(**data.dict())
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category

async def get_all_categories(db : AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()

async def get_category_by_id(category_id : int, db: AsyncSession):
    result = await db.execute(select(Category).where(Category.id == category_id))
    return result.scalar_one_or_none()
