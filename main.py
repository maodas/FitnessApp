# Import
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QHeaderView, QCheckBox, QDateEdit, QLineEdit 
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
#
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#
import numpy as np
from sys import exit
#


#Main Class
class FitTrack(QWidget):
    def __init__(self):
                super().__init__()
    #init UI
    def initUI(self):
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())

        self.kal_box = QLineEdit()
        self.kal_box.setPlaceholderText("Number of Burned Calories")
        
        self.distance_box = QLineEdit()
        self.distance_box.setPlaceholderText("Enter distance ran")

        self.description = QLineEdit()
        self.description.setPlaceholderText("Enter a description")

        self.submit_btn = QPushButton("Submit")
        self.add_btn = QPushButton("Add")
        self.delete_btn = QPushButton("Delete")
        self.clear_btn = QPushButton("Clear")
        self.dark_mode = QCheckBox("Dark Mode")
             
    #Load Tables
    #Add Tables
    #Delete Tables
    #Calculate calories
    #Click
    #Dark Mode
    #Reset

#Initizaly my DB