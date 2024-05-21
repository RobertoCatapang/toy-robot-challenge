from pydantic import BaseModel, Field


class RobotPayload(BaseModel):
    x: int
    y: int
    facing: str = Field(pattern="^[A-Z]+$")  # Match all uppercase letters
