# 📚 eLib - Electronic Library API (FastAPI)

This is a backend application for an electronic library, built with FastAPI. Users can register, log in, view a list of books, and upload or download books in PDF format.

## 🚀 Features

* 🔐 User registration and login (OAuth2 with JWT)
* 📖 Book management (create, list, view)
* 📁 Upload and download PDF files
* 🏷️ Book categories
* ⚡ Asynchronous database operations (SQLAlchemy + SQLite)
* 🔄 Database migrations with Alembic

## 🛠️ Tech Stack

* **FastAPI** — high-performance modern Python web framework
* **Pydantic v2** — data validation and serialization
* **SQLAlchemy 2.0** — modern ORM with async support
* **SQLite** — lightweight relational database
* **Alembic** — database migrations
* **JWT + OAuth2PasswordBearer** — user authentication
* **Uvicorn** — ASGI server

## 📂 Project Structure

```
app/
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── crud/           # Business logic
├── routers/        # FastAPI routers (endpoints)
├── database.py     # DB connection setup
├── main.py         # Entry point
uploads/            # Directory to store uploaded PDF files
```

## 🧪 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/electronic-library-api.git
cd electronic-library-api
```

2. **Create virtual environment and install dependencies:**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Run database migrations:**

```bash
alembic upgrade head
```

4. **Start the server:**

```bash
uvicorn app.main:app --reload
```

5. **Access docs:**
   Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to explore the interactive Swagger UI.

## 📁 Environment Configuration

You can create a `.env` file for environment variables (optional):

```env
DATABASE_URL=sqlite+aiosqlite:///./library.db
SECRET_KEY=your-secret-key
```

## 📬 Contact

If you have any questions or ideas, feel free to reach out.
✉️ [kuanyshperdebekov@gmail.com]

