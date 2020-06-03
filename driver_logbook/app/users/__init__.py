from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/users')

from app.users import routes  # noqa: F401