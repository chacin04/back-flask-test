from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<int:id>")
def hello_world(id):
    return f"<p>Hello,{id} muchachos!</p>"