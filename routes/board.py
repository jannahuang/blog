from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)

import uuid
csrf_tokens = dict()


@main.route("/admin")
def index():
    token = str(uuid.uuid4())
    u = current_user()
    csrf_tokens['token'] = u.id
    return render_template('board/admin_index.html', token=token)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Board.new(form)
    return redirect(url_for('topic.index'))

