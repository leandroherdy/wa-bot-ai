from pydantic import BaseModel


class MessageSchema(BaseModel):
    session: str
    chatId: str
    text: str

    class Config:
        from_attributes = True


class WebhookRequestSchema(BaseModel):
    payload: MessageSchema
