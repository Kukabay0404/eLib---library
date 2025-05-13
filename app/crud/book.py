from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_session
from app.models.book import Book
from app.schemas.book import BookCreate


async def create_book(data : BookCreate, db : AsyncSession):
    book = Book(**data.model_dump())
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book

async def get_all_books(db:AsyncSession):
    result = await db.execute(select(Book))
    return result.scalars().all()

async def get_book_by_id(book_id : int, db : AsyncSession):
    result = await db.execute(select(Book).where(Book.id == book_id))
    return result.scalar_one_or_none()

