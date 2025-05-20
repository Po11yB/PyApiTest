import requests

class User:
    def __init__(self, id, email, first_name, last_name, avatar ):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    @classmethod
    def from_api (cls, user_id):
        response = requests.get (f"https://reqres.in/api/users/{user_id}")
        if response.status_code == 200:
            data = response.json().get("data")
            return cls(
                id=data["id"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                avatar=data["avatar"]
            )
        else:
            print(f"ID {user_id} is not found")
            return None

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def is_valid_email(self) -> bool:
        return "@" in self.email and "." in self.email
