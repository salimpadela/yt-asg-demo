from flask import Blueprint, render_template
import requests
homepage_blueprint = Blueprint('homepage_blueprint', __name__)

@homepage_blueprint.route('/')
def homepage():
    resp = {"instanceId":"N/A","availabilityZone":"N/A"}
    instance_identity_url = "http://169.254.169.254/latest/dynamic/instance-identity/document/"
    try:
        r = requests.get(instance_identity_url, timeout=3)
        resp = r.json()
        instance_id = resp.get("instanceId")
        az = resp.get("availabilityZone")
        resp = {"instanceId":f"{instance_id}","availabilityZone":f"{az}"}

    except:
        pass


    return render_template('homepage.html',data=resp)
