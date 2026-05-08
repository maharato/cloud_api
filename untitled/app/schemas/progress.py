from pydantic import BaseModel


class ProgressUpdateRequest(BaseModel):
    currentLoop: int
    totalLoopsCompleted: int
    cluesFound: int