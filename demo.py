#!/usr/bin/env python

#------------------------------------------------------------------
# Demonstration for PyQt Lightning Talk
#
# Created by:   Steven Ortega
#               Aaron Kim
#               Ivan Luna
# 
# Created on:   21 October, 2024
# 
# Link to presentation:
# https://tinyurl.com/pyqt-demo
#------------------------------------------------------------------

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QSlider
from PyQt5.QtCore import Qt

# Function to update the label with text from the edit field
def update_label():
    text = text_field.text()
    label.setText(text)

# Helper function to create a slider
def create_slider(y_position, default_value, on_change_callback):
    slider = QSlider(Qt.Horizontal, window)
    slider.setGeometry(100, y_position, 200, 30)
    slider.setMinimum(0)
    slider.setMaximum(255)
    slider.setValue(default_value)
    slider.valueChanged.connect(on_change_callback)
    return slider

# Function to change the background color based on RGB slider values
def change_background_color():
    r = slider_r.value()
    g = slider_g.value()
    b = slider_b.value()
    color_value = f'rgb({r}, {g}, {b})'
    window.setStyleSheet(f"background-color: {color_value};")

# Create the application
app = QApplication([])
app.setStyle('Fusion')  # You can also try 'Windows', 'Fusion', etc.

# Create a window
window = QWidget()
window.setWindowTitle('PyQt Interactive Demo')
window.setGeometry(200, 200, 400, 450)


#------------------------------------------------------------------
# Create a Label
#------------------------------------------------------------------
#
# label = QLabel('This is a Label', window)
# label.setGeometry(150, 50, 150, 30)
#
#------------------------------------------------------------------


#------------------------------------------------------------------
# Create a Text Input Field
#------------------------------------------------------------------
#
# text_field = QLineEdit('Edit me', window)
# text_field.setGeometry(100, 100, 200, 30)
#
#------------------------------------------------------------------


#------------------------------------------------------------------
# Create a Button that updates the label with text from the edit field
#------------------------------------------------------------------
#
# button = QPushButton('Update Label', window)
# button.setGeometry(150, 150, 100, 30)
# button.clicked.connect(update_label)
#
#------------------------------------------------------------------


#------------------------------------------------------------------
# Create sliders to change background color
#------------------------------------------------------------------
#
# # Create RGB labels
# label_r = QLabel('R', window)
# label_r.setGeometry(70, 200, 20, 30)
#
# label_g = QLabel('G', window)
# label_g.setGeometry(70, 250, 20, 30)
#
# label_b = QLabel('B', window)
# label_b.setGeometry(70, 300, 20, 30)
#
# # Create sliders for Red, Green, and Blue (RGB) values using the helper function
# slider_r = create_slider(200, 255, change_background_color)  # Red slider
# slider_g = create_slider(250, 255, change_background_color)  # Green slider
# slider_b = create_slider(300, 255, change_background_color)  # Blue slider
#
#------------------------------------------------------------------


#------------------------------------------------------------------
# Code to execute the gui
#------------------------------------------------------------------
# Set initial background color to gray
window.setStyleSheet("background-color: rgb(150, 150, 150);")
window.show()

# Run the application event loop
app.exec_()
