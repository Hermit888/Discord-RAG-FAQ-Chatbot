from fastapi import APIRouter
from app.models.schemas import RagRequest, RagResponse
from app. services.rag_service import query_rag
from app. core. metrics import REQUEST_COUNT, REQUEST_LATENCY
import time
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@ router.post('/rag-query', response_model=RagResponse)
def rag_query(req: RagRequest):
    start = time.time()
    REQUEST_COUNT.labels(endpoint = '/api/rag-query').inc()

    # Log the request
    logger.info('RAG request', extra = {'user_id': req.user_id})

    # Call the RAG service to get the answer
    answer = query_rag(req.query)

    # Record latency
    REQUEST_LATENCY.labels(endpoint = '/api/rag-query').observe(time.time() - start)

    return RagResponse(answer = answer)