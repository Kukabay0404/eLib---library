from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import DateTime, func

class Book(Base):
    __tablename__ = 'books'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    title : Mapped[str] = mapped_column(nullable=False )
    author : Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    category_id : Mapped[int] = mapped_column(ForeignKey('categories.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                 onupdate=func.now())
    file_path : Mapped[str | None] = mapped_column(String(255), nullable=True)

    category = relationship('Category', back_populates='books')
