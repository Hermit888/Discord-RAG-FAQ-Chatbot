from pydantic import BaseModel

"""
Schemas for request and response models.
"""

class RagRequest(BaseModel):
    user_id: str
    query: str

class RagResponse(BaseModel):
    answer: str

class FeedbackRequest(BaseModel):
    user_id: str
    query: str
    rating: int