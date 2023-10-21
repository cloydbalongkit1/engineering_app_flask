import os
from flask_bootstrap import Bootstrap5
from flask import Flask

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get('ENG_AP_SECRET_KEY')

from engineering_app import routes
