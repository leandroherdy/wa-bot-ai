from pydantic import BaseModel
from typing import Dict
from typing import Any


class WebhookRequestSchema(BaseModel):
    event: str
    payload: Dict[str, Any]
