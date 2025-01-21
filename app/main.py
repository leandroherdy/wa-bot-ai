from fastapi import APIRouter, FastAPI
from app.endpoints import waha

app = FastAPI(title="API Documentation - Chatbot Integration with Groq API")


router = APIRouter()


app.include_router(waha.router, prefix="/api/chatbot", tags=["chatbot"])
