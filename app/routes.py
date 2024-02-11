from flask import render_template, jsonify

from app import app, sensors, lighter


@app.route('/')
@app.route('/index')
def main():
    return render_template("index.html")


@app.route('/get_data')
def get_data():
    # Здесь ваш код для получения данных, которые нужно обновлять
    data = {}
    # await asyncio.sleep(1)
    for el in sensors:
        if el.connection == False:
            data[el.sensor_name] = "{}".format("Not Connected")
        else:
            data[el.sensor_name] = "{}".format(int(el.check_data()))
    return jsonify(data)


@app.route('/switch_light')
def switch_light():
    status = lighter.total_status
    if status:
        lighter.switch_all_off()
    else:
        lighter.switch_all_on()
    return jsonify({"status": lighter.total_status})
