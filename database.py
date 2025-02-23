from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Database URL for PostgreSQL
DATABASE_URL = "postgresql+asyncpg://postgres:Innefu%40123@192.168.2.227:5432/embedding_db"

# Create an asynchronous engine for PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# SessionLocal for AsyncSession management
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency to get the DB session
async def get_db():
    async with SessionLocal() as db:
        yield db