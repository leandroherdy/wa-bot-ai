import random
import time

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from app.schemas.waha_schema import WebhookRequestSchema
from app.services.waha_service import Waha


router = APIRouter()


@router.post("/webhook", status_code=status.HTTP_201_CREATED)
async def webhook(data: WebhookRequestSchema):
    print(data.event)
    print(data.payload["from"])

    waha = Waha()
    chat_id = data["payload"]["from"]

    waha.start_typing(chat_id=chat_id)
    time.sleep(random.randint(3, 5))

    waha.send_message(chat_id=chat_id, message="Resposta Automática ;)")

    waha.stop_typing(chat_id=chat_id)

    return (JSONResponse({"status": "success"}),)
