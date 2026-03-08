def test_update_user(api_client, base_url):
    payload = {"job": "QAEatRC"}
    response = api_client.put(f"{base_url}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "QAEatRC"
