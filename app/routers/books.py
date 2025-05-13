from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.book import BookCreate, BookRead
from app.crud import book as book_crud
from typing import List
from fastapi import UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
import os.path
import shutil

UPLOAD_DIR = 'uploads'

router = APIRouter(
    prefix='/books',
    tags=['Books']
)

@router.post('/', response_model=BookRead, status_code=201)
async def create_book(data : BookCreate, db : AsyncSession = Depends(get_session)):
    return await book_crud.create_book(data, db)

@router.get('/', response_model=List[BookRead])
async def list_books(db : AsyncSession = Depends(get_session)):
    return await book_crud.get_all_books(db)

@router.post('/{book_id}/upload')
async def upload_book_file(book_id : int, file : UploadFile = File(...), db : AsyncSession = Depends(get_session)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail='Only PDF files are allowed')

    file_location = os.path.join(UPLOAD_DIR, f'book_{book_id}.pdf')

    with open(file_location, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    book = await book_crud.get_book_by_id(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.file_path = file_location
    await db.commit()

    return {"message": "File uploaded successfully"}


@router.get("/{book_id}/download")
async def download_book_file(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await book_crud.get_book_by_id(book_id, db)
    if not book or not book.file_path:
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(book.file_path, media_type="application/pdf", filename=f"{book.title}.pdf")


