from flask import Flask
from routes import bp_routes

app = Flask(__name__)
app.register_blueprint(bp_routes)

if __name__ == "__main__":
    app.run(debug=True)
