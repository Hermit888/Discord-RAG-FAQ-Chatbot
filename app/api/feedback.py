from fastapi import APIRouter
from app.models.schemas import FeedbackRequest
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@ router.post('/feedback')
def feedback(req:FeedbackRequest):
    # Log the feedback
    logger.info(
        'User feedback',
        extra = {
            'user_id': req.user_id,
            'query': req.query,
            'rating': req.rating
        }
    )

    return {'status': 'received'}
    