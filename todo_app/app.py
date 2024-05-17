from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import add_item, get_items, update_status_to_done

from todo_app.data.view_model import ViewModel
from todo_app.flask_config import Config

def create_app():
   app = Flask(__name__)
   app.config.from_object(Config())


   @app.get('/')
   def index():
      items = get_items()
      view_model = ViewModel(items)
      return render_template('index.html', view_model = view_model)

   @app.post('/add-item')
   def add_new_item():
      new_item = add_item(request.form["title"])
      return redirect("/", code=302)

   @app.post('/complete/<item_id>')
   def complete_item(item_id):
      update_status_to_done(item_id)
      return redirect("/", code=302)
   return app
