from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.get('/')
def index():
   items = get_items()
   return render_template('index.html',items=items)

@app.post('/')
def add_new_item():
   new_item = add_item(request.form["title"])
   return redirect("/", code=302)