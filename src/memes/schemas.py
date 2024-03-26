from pydantic import BaseModel

class SaveMemeRequest(BaseModel):
    id: str
    title: str
    score: int
    url: str
    created_utc: int
    author_name: str
    author_id: str