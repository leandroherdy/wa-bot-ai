import random
import time
import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from app.schemas.waha_schema import WebhookRequestSchema
from app.services.waha_service import Waha


router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post("/webhook", status_code=status.HTTP_201_CREATED)
async def webhook(data: WebhookRequestSchema):
    try:
        logger.info(f"Received event: {data}")

        waha = Waha()
        chat_id = data.payload["from"]

        logger.info(f"Starting typing simulation for chat_id: {chat_id}")
        waha.start_typing(chat_id=chat_id)
        time.sleep(random.randint(3, 5))

        logger.info(f"Sending message to chat_id: {chat_id}")
        waha.send_message(chat_id=chat_id, message="Automated Response ;)")

        waha.stop_typing(chat_id=chat_id)

        return JSONResponse({"status": "success"})
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return JSONResponse(
            {"status": "error", "detail": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
