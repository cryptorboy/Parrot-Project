# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Started.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_StartedForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 50, 161, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/GD/work/retro.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_StartedForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
