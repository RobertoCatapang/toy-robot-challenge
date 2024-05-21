from fastapi import APIRouter
from loguru import logger

from api.schema import RobotPayload

router = APIRouter()


@router.post("/place", name="place")
def place(payload: RobotPayload) -> RobotPayload:
    """Places the robot at the x and y are integers that relate to a location on the
    grid. Values that are outside the boundary of the grid should not be allowed.
    `facing` is a string referencing the direction the robot is facing. Values NORTH,
    SOUTH, EAST or WEST are allowed."""
    logger.info("Placing Robot...")

    # Check if given inputs are valid
    if payload.facing not in ("EAST", "WEST", "NORTH", "SOUTH"):
        raise ValueError("Input not valid")

    if payload.x > 4 or payload.y > 4:
        raise ValueError("Input moves robot out of bounds")

    if payload.x < 0 or payload.y < 0:
        raise ValueError("Input moves robot out of bounds")

    return RobotPayload(x=payload.x, y=payload.y, facing=payload.facing)


@router.post("/move")
def move(payload: RobotPayload) -> RobotPayload:
    """Moves the robot 1 grid unit in the direction it is facing unless that movement will
    cause the robot to fall off the grid."""
    logger.debug("Moving robot...")

    match payload.facing:
        case "EAST":
            payload.x += 1
        case "WEST":
            payload.x -= 1
        case "NORTH":
            payload.y += 1
        case "SOUTH":
            payload.y -= 1
        case _:
            raise ValueError("Input not valid")

    if payload.x > 4 or payload.y > 4:
        raise ValueError("Input moves robot out of bounds")

    if payload.x < 0 or payload.y < 0:
        raise ValueError("Input moves robot out of bounds")

    return payload


@router.post("/left")
def left(payload: RobotPayload) -> RobotPayload:
    """Rotate the robot 90° anticlockwise/counterclockwise."""
    logger.debug("Turning left...")

    match payload.facing:
        case "EAST":
            payload.facing = "NORTH"
        case "WEST":
            payload.facing = "SOUTH"
        case "NORTH":
            payload.facing = "WEST"
        case "SOUTH":
            payload.facing = "EAST"
        case _:
            raise ValueError("Input not valid")

    return payload


@router.post("/right")
def right(payload: RobotPayload) -> RobotPayload:
    """Rotate the robot 90° clockwise."""
    logger.debug("Turning right...")

    match payload.facing:
        case "EAST":
            payload.facing = "SOUTH"
        case "WEST":
            payload.facing = "NORTH"
        case "NORTH":
            payload.facing = "EAST"
        case "SOUTH":
            payload.facing = "WEST"
        case _:
            raise ValueError("Input not valid")

    return payload


@router.post("/report")
def report(payload: RobotPayload) -> RobotPayload:
    """Outputs the robot's current grid location and facing direction."""
    logger.info(f"Robot is located at {payload.x}, {payload.y} facing {payload.facing}")

    return payload
