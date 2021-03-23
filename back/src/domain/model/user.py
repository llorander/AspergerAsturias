import hashlib


def hash_password(password):
    hash_obj = hashlib.sha256(password.encode())
    return hash_obj.hexdigest()


class User:
    def __init__(self, id_user, name_user, mail_user, password_user, points_user, state_user, id_admin):
        self.id_user = id_user
        self.name_user = name_user
        self.mail_user = mail_user
        self.password_user = password_user
        self.points_user = points_user
        self.state_user = bool(state_user)
        self.id_admin = id_admin

    def check_password(self, password):
        return hash_password(password) == self.password_user

    def __getstate__(self):

        # not sending "password" when instance is "jsonified"

        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "is_admin": self.is_admin,
        }
