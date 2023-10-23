import os
from flask_bootstrap import Bootstrap5
from flask import Flask

app = Flask(__name__)
bootstrap = Bootstrap5(app)
# app.config['SECRET_KEY'] = os.environ.get('ENG_AP_SECRET_KEY')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from engineering_app import routes
