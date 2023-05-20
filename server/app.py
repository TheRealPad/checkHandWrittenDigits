import os
from flask import Flask
from flask_http_middleware import MiddlewareManager
from model.model import HandWrittenModel
from middleware.middleware import AccessMiddleware
from routes.routes import Routes

def initMiddelware(app):
    app.wsgi_app = MiddlewareManager(app)
    app.wsgi_app.add_middleware(AccessMiddleware)

def initRoutes(app, model):
    routes = Routes(model)
    app.add_url_rule('/analyseImage', methods=['POST'], view_func=routes.analyseImage)

def initServer(model):
    app = Flask(__name__)
    initMiddelware(app)
    initRoutes(app, model)
    return app

if __name__ == "__main__":
    try:
        handWrittenDigits = HandWrittenModel()
        handWrittenDigits.createModel()
    except Exception as error:
        print("Error with model: ", error)
    app = initServer(handWrittenDigits)
    api_port = 8080
    app.run(host='0.0.0.0', port=api_port, debug=True, use_reloader=False)
