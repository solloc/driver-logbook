from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/users')

from driver_logbook.app.users import routes  # noqa: E402, F401
