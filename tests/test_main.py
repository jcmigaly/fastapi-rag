def test_hello_world(client):
    """Test the root endpoint returns Hello World"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World!" 