from flask import Blueprint, render_template

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('/')
def index():
    return render_template('index.html')

@bp_routes.route('/about')
def about():
    return render_template('about.html')

