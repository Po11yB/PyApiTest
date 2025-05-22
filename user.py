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
        try:
            response = requests.get (f"https://reqres.in/api/users/{user_id}")
            response.raise_for_status()
            data = response.json().get("data")
            if not data:
                raise ValueError ("No data response")
            return cls(
                id=data["id"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                avatar=data["avatar"]
            )
        except ValueError as e:
            print(f"Invalid response {e}")
        except KeyError as k:
            print(f"Invalid key data {k}")
        return None



    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def is_valid_email(self) -> bool:
        return "@" in self.email and "." in self.email
