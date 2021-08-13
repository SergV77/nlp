from flask import Flask
from flask_bootstrap import Bootstrap
from flaskext.markdown import Markdown

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object("config")
Markdown(app)

from views import *

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


