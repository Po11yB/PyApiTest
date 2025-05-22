import requests
from user import User

HEADERS = {"x-api-key": "reqres-free-v1"}

def test_get_user_id ():
    response = requests.get ("https://reqres.in/api/users/2", headers=HEADERS)
    assert response.status_code == 200

    data = response.json().get("data")
    user = User (
        id=data["id"],
        email=data["email"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        avatar=data["avatar"]
    )

    assert user.id == 2
    assert user.full_name() == "Janet Weaver"
    assert user.is_valid_email()

# Test: Manually created object

def test_user_object():
    u = User(1, "test@email.com", "Polly", "Test", "https://reqres.in/img.jpg")
    assert u.id == 1
    assert u.first_name == "Polly"
    assert u.last_name == "Test"

try:
    user_id = int(input("Put user ID:"))
    user = User.from_api(user_id)
    if user:
        print (user.full_name())
    else:
        print("User no found")
except ValueError:
    print("Invalid user ID")
