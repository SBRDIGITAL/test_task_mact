from pydantic import BaseModel


class SomeMessage(BaseModel):
    message: str = 'ok'