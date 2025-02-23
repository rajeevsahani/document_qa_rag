# from sqlalchemy import Column, String
# from sqlalchemy.dialects.postgresql import UUID
# from pgvector.sqlalchemy import Vector
# from sqlalchemy.ext.declarative import declarative_base
# import uuid

# Base = declarative_base()

# class Document(Base):
#     __tablename__ = "documents"

#     id = Column(UUID, primary_key=True, default=uuid.uuid4)
#     filename = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     embedding = Column(Vector(384))  # Ensure this matches your embedding model
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, String, Text, UUID
import uuid
import json
from database import Base

class Document(Base):
    __tablename__ = 'documents'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(768), nullable=False)  # Storing embedding as a vector of length 768

    def __init__(self, filename, content, embedding):
        self.filename = filename
        self.content = content
        self.embedding = embedding

    def get_embedding(self):
        return self.embedding
