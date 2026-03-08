def test_create_user(api_client, base_url):
    payload = {"name": "MKHLK", "job": "QAE"}
    response = api_client.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "MKHLK"
