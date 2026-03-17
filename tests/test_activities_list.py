def test_get_activities_returns_seeded_data(client):
    # Arrange
    expected_activity_count = 9

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == expected_activity_count
    assert "Chess Club" in payload
    assert "Science Club" in payload


def test_each_activity_contains_required_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for details in payload.values():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
