from pydantic import BaseModel

class FaqQuery(BaseModel):
    is_query_valid: bool
    reason: str