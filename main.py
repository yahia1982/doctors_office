import os
from flask import Flask, jsonify
from flask_cors import CORS

from routes.medical_history import medical_history_bp
from routes.patient_bp import patient_bp
from routes.prescriptions_bp import prescriptions_bp
from routes.staff_bp import staff_bp
from routes.appointments_bp import appointments_bp
from routes.users_bp import users_bp

API_BASE_PATH = "/api"

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "url not found."}), 404


def register_extensions(app):
    cors_path = API_BASE_PATH + "/*"
    CORS(app, resources={
        cors_path: {"origins": "*"}
    })


def register_blueprints(app):
    app.register_blueprint(users_bp, url_prefix=API_BASE_PATH)
    app.register_blueprint(appointments_bp, url_prefix=API_BASE_PATH + '/appointments')
    app.register_blueprint(staff_bp, url_prefix=API_BASE_PATH + '/doctors')
    app.register_blueprint(patient_bp, url_prefix=API_BASE_PATH + '/patients')
    app.register_blueprint(prescriptions_bp, url_prefix=API_BASE_PATH + '/prescriptions')
    app.register_blueprint(medical_history_bp, url_prefix=API_BASE_PATH + '/history')


if __name__ == '__main__':
    register_blueprints(app)
    register_extensions(app)
    app.run()
