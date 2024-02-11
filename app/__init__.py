from flask import Flask

from IoT_classes import Temperature_Sencor, Light_Sensor, Camera_Sensor, Lighters

app = Flask(__name__, static_url_path="/static", static_folder="static")
sensors = [Temperature_Sencor("tp1", 1), Light_Sensor("lg1", 11), Camera_Sensor("cam1", 4313)]
lighter = Lighters()
for i in range(5):
    lighter.add_lighter()

from app import routes
