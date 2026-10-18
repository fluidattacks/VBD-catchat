from flask_login import current_user


class AccessMixin:
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
