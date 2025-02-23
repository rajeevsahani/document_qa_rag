from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Document
from schemas import QueryRequest

class DocumentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_document(self, filename: str, content: str, embedding: list):
        new_doc = Document(filename=filename, content=content, embedding=embedding)
        self.db.add(new_doc)
        await self.db.commit()
        return new_doc.id

    async def get_documents(self):
        result = await self.db.execute(select(Document.id, Document.filename))
        return [{"id": str(row[0]), "filename": row[1]} for row in result.fetchall()]

    async def search_similar_documents(self,query_text: str, query_embedding: list):

        # Perform similarity search using cosine distance (<=> operator in pgvector)
        stmt = select(Document.filename, Document.content).order_by(Document.embedding.cosine_distance(query_embedding)).limit(1)  # Fetch top 5 similar documents

        result = await self.db.execute(stmt)
        rows = result.all()

        # return {"query": query_text, "results": [{"filename": row[0], "content": row[1]} for row in rows]}
        return { "query": query_text, "results": [{"filename": row[0], "content": row[1], "similarity_score": row[2]} for row in rows]}

