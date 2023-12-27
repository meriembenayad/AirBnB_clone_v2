#!/usr/bin/python3
""" Cities by States """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display cities """
    states = storage.all('States').values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_down(exception=None):
    """ close DB """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
