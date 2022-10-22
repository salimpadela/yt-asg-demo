from flask import Flask
from flask_cors import CORS


from homepage.homepage_blueprint import homepage_blueprint
from healthstatus.healthstatus_blueprint import healthstatus_blueprint

app = Flask(__name__)

CORS(app)

app.url_map.strict_slashes = False


app.register_blueprint(homepage_blueprint, url_prefix='/')
app.register_blueprint(healthstatus_blueprint, url_prefix='/healthstatus/')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)
