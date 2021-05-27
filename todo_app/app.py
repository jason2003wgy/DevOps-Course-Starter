from flask import Flask, render_template
from todo_app.flask_config import Config
from todo_app.data.session_items import add_item, get_items

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    lst_item = get_items()
    return render_template('index.html', lst_item=lst_item)


if __name__ == '__main__':
    app.run()
