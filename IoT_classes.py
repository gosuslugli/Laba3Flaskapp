import random
from datetime import datetime
from typing import List, Dict, Tuple


class Lighters:
    def __init__(self):
        self.lighers = list()
        self.total_status = False

    def add_lighter(self):
        self.lighers.append(Lighter(f'light{len(self.lighers)}'))

    def switch_all_on(self):
        for ligther in self.lighers:
            ligther.turn_on()
        self.total_status = True

        return self.total_status

    def switch_all_off(self):
        for ligther in self.lighers:
            ligther.turn_off()
        self.total_status = False

        return self.total_status


class Lighter:
    def __init__(self, light_name):
        self.status: int = False
        self.voltage: int = 220
        self.light_name = light_name

    def turn(self):
        self.status = not self.status
        return self.status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False


class Sensor:
    def __init__(self, sensor_name="undefiend", serial_number=0):
        self.sensor_name: str = sensor_name
        self.serial_number: int = serial_number
        self.connection = True
        self.value: float = None
        self.logging_data: List[Dict[str: float]] = list()
        self.base_len_logging: int = 1024

    def show_base_info(self) -> Tuple:
        return (self.sensor_name, self.serial_number, self.logging_data)

    def logging_data_f(self):
        self.check_len_logging_data()
        self.logging_data.append({str(datetime.now()).split(".")[0]: self.value})

    def check_len_logging_data(self):
        if len(self.logging_data) >= 1024:
            self.logging_data.pop(0)


class Temperature_Sencor(Sensor):
    def __init__(self, sensor_name, seirial_number):
        super().__init__(sensor_name, seirial_number)

    def check_data(self):
        if not self.value:
            self.value = random.gauss(20.0, 1)
        else:
            self.value = random.gauss(self.value, 2)
        return self.value

    def show_data(self):
        d = self.check_data()
        self.logging_data_f()
        return d


class Light_Sensor(Sensor):
    def __init__(self, sensor_name, seirial_number):
        super().__init__(sensor_name, seirial_number)

    def check_data(self):
        if not self.value:
            if datetime.now().hour > 18 and datetime.now().hour <= 24:
                self.value = random.gauss(100.0, 10)
            elif datetime.now().hour > 7 and datetime.now().hour <= 18:
                self.value = random.gauss(400.0, 50)
            else:
                self.value = random.gauss(200.0, 10)
        else:
            self.value = random.gauss(self.value, 5)
        return self.value

    def show_data(self):
        d = self.check_data()
        self.logging_data_f()
        return d


class Camera_Sensor(Sensor):
    def __init__(self, sensor_name, seirial_number):
        super().__init__(sensor_name, seirial_number)

    def check_data(self):
        if not self.value:
            self.value = random.randint(0, 15)
        else:
            self.value = int(round(abs(random.gauss(self.value, 10))))
        return self.value

    def show_data(self):
        d = self.check_data()
        self.logging_data_f()
        return d
