from user_class import User
from privileges_class import Privileges


class Admin(User):
    """add an attribute that stores a list of things an admin can do."""

    def __init__(self, first_name, last_name, age, hobby, height):
        super().__init__(first_name, last_name, age, hobby, height)
        privileges_list = [
            "can add post",
            "can delete post",
            "can ban user",
        ]
        self.privileges = Privileges(privileges_list)
