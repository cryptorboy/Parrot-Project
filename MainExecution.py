#All Windows Are In File

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
import sys
import os

from lib.login import MainWindow
from lib.startexec import Run_Class
# from Windows import Message


class ExecWindow(QMainWindow):
    def run(self):
        self.startexec_function()

    def Parrot_Function(self):
        self.Parrot_ui = Run_Class()
        self.Parrot_ui.run()

    def Login_Function(self):
        self.login_ui = MainWindow()
        self.login_ui.show()
        app.exec_()

    def startexec_function(self):
        path = "lib/load.json"
        if os.path.exists(path):
            self.Parrot_Function()
        else:
            self.Login_Function()
            if os.path.exists(path):
                self.show_popup()
                self.Parrot_Function()

    def show_popup(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Loging Status.')
        msg_box.setText('Successfully loggedin. Say Parrot!')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton('OK', QMessageBox.AcceptRole)
        result = msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExecWindow()
    window.run()
    