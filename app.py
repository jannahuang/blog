from flask import Flask

import config


# web framework
# web application
# __main__
app = Flask(__name__)

app.secret_key = config.secret_key


from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
from routes.board import main as board_routes

app.register_blueprint(topic_routes)
app.register_blueprint(index_routes, url_prefix='/login')
app.register_blueprint(reply_routes, url_prefix='/reply')
app.register_blueprint(board_routes, url_prefix='/board')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
