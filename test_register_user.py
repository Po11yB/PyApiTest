import requests

HEADERS = {"x-api-key": "reqres-free-v1"}

def test_successful_user_registration ():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post ("https://reqres.in/api/register", json=payload, headers=HEADERS)
    assert response.status_code == 200

    data = response.json ()
    assert "id" in data
    assert "token" in data
    print("Successful registration", data)

def test_unsuccessful_registration ():
    payload = {
        "email": "sydney@fife"
    }

    response = requests.post ("https://reqres.in/api/register", json=payload, headers=HEADERS)
    assert response.status_code == 400

    data = response.json ()
    assert data["error"] == "Missing password"
    print("Unsuccessful registration", data)






