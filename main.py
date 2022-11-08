# This is a PyQT Script
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT Test : Folder Directory")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    # method for widgets
    def UiComponents(self):
        # creating a push button
        button = QPushButton("CLICK", self)

        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)

        # adding action to a button
        button.clicked.connect(self.pick_new)

    def pick_new(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        return folder_path


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
