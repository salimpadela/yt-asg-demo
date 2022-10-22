from flask import Blueprint, jsonify


healthstatus_blueprint = Blueprint('healthstatus_blueprint', __name__)

@healthstatus_blueprint.route('/')
def healthstatus():
    return jsonify(status="up")

