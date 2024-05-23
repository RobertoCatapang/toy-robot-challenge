from pydantic import BaseModel, Field


# Create a class to validate the payload sent and recived by the API
class RobotPayload(BaseModel):
    x: int
    y: int
    facing: str = Field(pattern="^[A-Z]+$")  # Match all uppercase letters
