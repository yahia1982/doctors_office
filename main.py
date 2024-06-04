import os
from flask import Flask, jsonify
from flask_cors import CORS

from routes.staff_bp import staff_bp
from routes.appointments_bp import appointments_bp
from routes.users_bp import users_bp

from db.db import DBService

API_BASE_PATH = "/api"

def create_app():
    app = Flask(__name__)

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    cors_path = API_BASE_PATH + "/*"
    CORS(app, resources={
        cors_path: {"origins": "*"}
    })

def register_blueprints(app):
    app.register_blueprint(users_bp, url_prefix = API_BASE_PATH)
    app.register_blueprint(appointments_bp, url_prefix = API_BASE_PATH+'/appointments')
    app.register_blueprint(staff_bp, url_prefix =API_BASE_PATH + '/doctors')


if __name__ == '__main__':
    app = create_app()


    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error":"url not found."}), 404

    app.run()
