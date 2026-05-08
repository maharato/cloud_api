from pydantic import BaseModel


class ScoreSubmitRequest(BaseModel):
    score: int
