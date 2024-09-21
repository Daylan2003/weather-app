import sys #system variables
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout) 
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):  #class of weather app which inherits from the parent that is QWidget
    def __innit__(self):
        super().__innit__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("get Weather", self)
        self.temperature_label = QLabel("20°C", self)
        self.emoji_label = QLabel("sunsunsun", self)
        self.description_label = QLabel("Sunny", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()  #constructed a weather app object
    weather_app.show()          #shows weather app object
    sys.exit(app.exec_())        