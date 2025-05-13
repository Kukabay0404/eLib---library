from fastapi import FastAPI
from app.routers import auth
from app.database import init_db
from app.routers import users
from app.routers import books, categories

app = FastAPI(title='Электронная библиотека elib')

app.include_router(categories.router)
app.include_router(books.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get('/')
async def root():
    return {'message' : 'Добро пожаловать в электронную библиотеку ELib'}

@app.on_event("startup")
async def on_startup():
    await init_db()
