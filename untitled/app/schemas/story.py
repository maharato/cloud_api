from pydantic import BaseModel


class StoryUpdateRequest(BaseModel):
    storyState: str
    ending: str
    isFinished: bool
    choices: dict