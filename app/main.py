from fastapi import FastAPI
from app.api import rag, feedback
from app.core.logging import setup_logging
from app.core.metrics import metrics_router


setup_logging()

app = FastAPI(title = "Discord RAG FAQ Chatbot Backend")

# get other routers in other files
app.include_router(rag.router, prefix='/api')
app.include_router(feedback.router, prefix='/api')
app.include_router(metrics_router)

@ app.get("/health")
def health():
    return {"status": "ok"}