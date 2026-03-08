def test_get_user(api_client, base_url):
    response = api_client.get(f"{base_url}/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
