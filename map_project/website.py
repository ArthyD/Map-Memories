from flask import Blueprint, render_template, request, flash, jsonify, send_file,redirect
from . import db, ALLOWED_EXTENSIONS,UPLOAD_FOLDER,script_directory
from sqlalchemy import func
from werkzeug.utils import secure_filename
import os
import subprocess
from .models import ImageServer
from flask_cors import cross_origin, CORS

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    if request.method == 'POST':
        if 'upload' in request.form:
            name = request.form.get('name')
            lat = request.form.get('lat')
            long = request.form.get("long")
            photo = request.form.get("img")
            file = request.files['img']
            file_path = os.path.join(script_directory, UPLOAD_FOLDER)
            print(f"{name} : {photo}")
            if file.filename == '':
                flash('No selected file', 'error')
                return render_template("home.html")
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(file_path, filename)
                file.save(file_path)
            new_image = ImageServer(name=name, lat=lat, long=long, path=filename)
            db.session.add(new_image)
            db.session.commit()
            photo_list = ImageServer.query.all()
            return render_template("home.html", photo_list=photo_list)
        elif 'suppr' in request.form:
            id = request.form.get("suppr")
            photo_to_delete = ImageServer.query.filter_by(id=id).first()
            file_path = os.path.join(script_directory, UPLOAD_FOLDER)
            os.remove(os.path.join(file_path, photo_to_delete.path))
            db.session.delete(photo_to_delete)
            db.session.commit()
            
            photo_list = ImageServer.query.all()
            return render_template("home.html", photo_list=photo_list)
    photo_list = ImageServer.query.all()     
    return render_template("home.html", photo_list=photo_list)

@views.route('/get_locations')
@cross_origin()
def get_locations():
    locations = []
    result = ImageServer.query.all() 
    for row in result:
        image = dict(name=row.name, lat=row.lat, long=row.long, comment=row.comment, path=row.path)
        print(image)
        locations.append(image)
    return locations

@views.route('/get_image/<name>')
@cross_origin()
def get_iamge(name):
    
    return send_file(UPLOAD_FOLDER+"/"+name)


@views.route('/connect', methods=['GET', 'POST'])
@cross_origin()
def connect():
    if request.method == 'POST':
        ssid = request.form.get('ssid')
        password = request.form.get('pass')
        runAndWait("ifconfig wlan1 up")
        runAndWait("raspi-config nonint do_wifi_country FR")
        runAndWait(f"raspi-config nonint do_wifi_ssid_passphrase '{ssid}' '{password}'")
        runAndWait("ifconfig wlan1 up")
        # os.system(f"wpa_passphrase '{ssid}' '{password}' >> /etc/wpa_supplicant/wpa_supplicant.conf'")
        # os.system("pkill wpa_supplicant")
        # os.system("wpa_supplicant -d -i wlan1 -c /etc/wpa_supplicant/wpa_supplicant.conf")
        return redirect("/")

    return render_template("connect.html")

def runAndWait(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    var = process.returncode
    print(var)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS