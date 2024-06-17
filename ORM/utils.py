from user import User

def new_user(user_id: int, name: str, age: int):
    new_user = User.create(
        id=user_id,
        name=name,
        age=age,
    )
    return new_user