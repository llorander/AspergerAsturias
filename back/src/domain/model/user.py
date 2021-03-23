import hashlib


def hash_password(user_password):
    hash_obj = hashlib.sha256(user_password.encode())
    return hash_obj.hexdigest()


class User:
    def __init__(
        self,
        id_user,
        name_user,
        mail_user,
        password_user,
        points_user,
        status_user,
        is_admin,
        id_admin,
    ):
        self.id_user = id_user
        self.name_user = name_user
        self.mail_user = mail_user
        self.password_user = password_user
        self.points_user = points_user
        self.state_user = state_user
        self.is_admin = is_admin
        self.id_admin = id_admin

    def check_password(self, user_password):
        return hash_password(user_password) == self.user_password

    def __getstate__(self):

        return {
            "id_user": self.id_user,
            "name_user": self.name_user,
            "mail_user": self.mail_admin,
            "is_admin": self.is_admin,
            "state_user": self.state_user,
        }


def create_user_from_dict(data):
    return User(
        data["id_user"],
        data["name_user"],
        data["password_user"],
        data["mail_user"],
        data["points_user"],
        data["state_user"],
        data["is_admin"],
        data["id_admin"],
    )