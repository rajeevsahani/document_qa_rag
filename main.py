from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from services import DocumentService
from repository import DocumentRepository
from schemas import QueryRequest

app = FastAPI()

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    """
    Uploads a document, extracts content, generates embeddings, and saves it to the database.
    """
    service = DocumentService(DocumentRepository(db))
    return await service.process_file(file)

@app.get("/documents/")
async def list_documents(db: AsyncSession = Depends(get_db)):
    """
    Retrieves a list of document filenames.
    """
    service = DocumentService(DocumentRepository(db))
    return await service.list_documents()

@app.post("/query/")
async def query_documents(request: QueryRequest, db: AsyncSession = Depends(get_db)):
    """
    Retrieves the top 5 most relevant documents based on semantic similarity.
    """
    service = DocumentService(DocumentRepository(db))
    return await service.search_documents(request.query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

