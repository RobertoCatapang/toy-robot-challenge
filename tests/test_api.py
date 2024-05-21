import pytest


# test functionality
def test_robot_gets_placed_correctly(test_client) -> None:
    payload = {"x": 3, "y": 1, "facing": "EAST"}
    response = test_client.post("/place", json=payload)

    assert response.json() == payload  # location should be at the given payload
    assert response.status_code == 200

def test_bot_moves_correctly(test_client) -> None:
    payload = {"x": 3, "y": 1, "facing": "EAST"}
    response = test_client.post("/move", json=payload)
    expected_result = {"x": 4, "y": 1, "facing": "EAST"}

    assert response.json() == expected_result  # moves one space to the east
    assert response.status_code == 200

def test_bot_turns_left_correctly(test_client) -> None:
    payload = {"x": 3, "y": 1, "facing": "EAST"}
    response = test_client.post("/left", json=payload)
    expected_result = {"x": 3, "y": 1, "facing": "NORTH"}

    assert response.json() == expected_result  # moves facing north
    assert response.status_code == 200

def test_bot_turns_right_correctly(test_client) -> None:
    payload = {"x": 3, "y": 1, "facing": "EAST"}
    response = test_client.post("/right", json=payload)
    expected_result = {"x": 3, "y": 1, "facing": "SOUTH"}

    assert response.json() == expected_result  # moves facing south
    assert response.status_code == 200

def test_bot_reports_correctly(test_client) -> None:
    payload = {"x": 0, "y": 0, "facing": "NORTH"}
    response = test_client.post("/report", json=payload)

    assert response.json() == payload
    assert response.status_code == 200


# test invalid cases
# out of bounds
def test_bot_moves_out_of_bounds(test_client) -> None:
    payload = {"x": 4, "y": 1, "facing": "EAST"}

    # Use pytest.raises to assert a ValueError is raised
    with pytest.raises(ValueError):
        test_client.post("/move", json=payload)

# invalid inputs
def test_invalid_x_input(test_client) -> None:
    payload = {"x": 41, "y": 1, "facing": "NORTH"}

    # Use pytest.raises to assert a ValueError is raised
    with pytest.raises(ValueError):
        test_client.post("/place", json=payload)

def test_invalid_y_input(test_client) -> None:
    payload = {"x": 4, "y": 11, "facing": "NORTH"}

    # Use pytest.raises to assert a ValueError is raised
    with pytest.raises(ValueError):
        test_client.post("/place", json=payload)

def test_invalid_facing_input(test_client) -> None:
    payload = {"x": 4, "y": 1, "facing": "NORTHEAST"}

    # Use pytest.raises to assert a ValueError is raised
    with pytest.raises(ValueError):
        test_client.post("/place", json=payload)

# orientation not capitalized
def test_invalid_facing_input_lowercased(test_client) -> None:
    payload = {"x": 4, "y": 1, "facing": "north"}
    response = test_client.post("/place", json=payload)

    # Expecting 422 since pydantic will not process any lowercase facing
    assert response.status_code == 422 