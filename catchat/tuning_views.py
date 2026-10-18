from flask_admin.contrib.sqla import ModelView

from .roles import AccessMixin


class AccountView(AccessMixin, ModelView):
    can_delete = False
    page_size = 100
