# This is a PyQT Script
import os.path

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

path = ""
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT Test : Folder Directory")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    # method for widgets
    def UiComponents(self):
        # BUTTON 1 : FILE DIRECTORY
        # creating a push button
        button = QPushButton("Select Directory", self)
        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)
        # adding action to a button
        button.clicked.connect(self.pick_new)

        # BUTTON 2 : Create files
        # creating a push button
        button2 = QPushButton("Select Directory", self)
        # setting geometry of button
        button2.setGeometry(400, 150, 100, 30)
        # adding action to a button
        button2.clicked.connect(self.create_files)


    def pick_new(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        path = folder_path
        return folder_path

    def create_files(self):
        self.projectname = "test"
        self.newpath = os.path.join(path,self.projectname)
        print(self.newpath)
        self.file = open("myfile.txt", "x")
        print("Hello World")
        return self.file


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
