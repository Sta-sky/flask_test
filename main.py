
from flask import Flask
from flask_test.login.views import login
from flask_test.login.views import check_login


app = Flask(
    __name__,
    template_folder='static/templates',
    static_folder='static')
app.register_blueprint(login, url_prefix='/user')
app.register_blueprint(check_login, url_prefix='/user')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
