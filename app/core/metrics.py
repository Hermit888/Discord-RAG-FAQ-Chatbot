from fastapi import APIRouter, Response
# Python client for the systems monitoring and alerting toolkit Prometheus
from prometheus_client import Counter, Histogram, generate_latest

"""Metrics for monitoring the FastAPI application using Prometheus."""

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total HTTP requests",
    ['endpoint']
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "Request latency",
    ['endpoint']
)

# Decorator to track request metrics
metrics_router = APIRouter()

@ metrics_router.get('/metrics')
def metrics():
    return Response(generate_latest(), media_type="text/plain")