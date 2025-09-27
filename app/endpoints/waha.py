from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import logging
import random
import asyncio
from app.schemas.waha_schema import WebhookRequestSchema
from app.services.waha_service import Waha
from app.services.groq_API_client import GroqAPIClient
from app.services.groq_API_client import PostgresRetriever


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter()


@router.post("/webhook", status_code=status.HTTP_201_CREATED)
async def webhook(data: WebhookRequestSchema):
    """
    Handles incoming webhook events, processes instructions,
    and responds to the chat using Groq API and Waha service.

    Args:
        data (WebhookRequestSchema): The incoming webhook data.

    Returns:
        JSONResponse: Status of the processing.
    """
    try:
        logger.info(f"Received event: {data}")

        waha = Waha()

        chat_id = data.payload["from"]
        received_message = data.payload["body"]

        is_group = "@g.us" in chat_id
        is_status = "status@broadcast" in chat_id

        if is_group or is_status:
            return JSONResponse(
                {"status": "success", "message": "Group/status message ignored."}
            )

        logger.info(f"Starting typing simulation for chat_id: {chat_id}")
        waha.start_typing(chat_id=chat_id)
        history_messages = waha.get_history_messages(chat_id=chat_id, limit=10)

        logger.info("Searching for relevant context in PostgreSQL")
        retriever = PostgresRetriever()
        relevant_docs = retriever._PostgresRetriever__retriever.get_relevant_documents(
            received_message
        )
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        await asyncio.sleep(random.randint(3, 5))

        logger.info("Processing instruction with GroqAPIClient.")
        groq_api_client = GroqAPIClient()
        response = groq_api_client.process_instruction(
            history_messages=history_messages, text=received_message, context=context
        )

        logger.info(f"Sending message to chat_id: {chat_id}")
        waha.send_message(chat_id=chat_id, message=response)

        waha.stop_typing(chat_id=chat_id)

        logger.info(f"Message sent successfully to chat_id: {chat_id}")
        return JSONResponse(
            {"status": "success", "chat_id": chat_id, "response": response}
        )

    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return JSONResponse(
            {"status": "error", "detail": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
