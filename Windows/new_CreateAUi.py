# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\new_CreateAUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1440, 800)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_background = QtWidgets.QLabel(Form)
        self.main_background.setGeometry(QtCore.QRect(0, 0, 1440, 800))
        self.main_background.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0003s_0001_Vector-Smart-Object.png);")
        self.main_background.setText("")
        self.main_background.setObjectName("main_background")
        self.create_acc_background = QtWidgets.QLabel(Form)
        self.create_acc_background.setGeometry(QtCore.QRect(523, 110, 395, 582))
        self.create_acc_background.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0003s_0000__Path_.png);")
        self.create_acc_background.setText("")
        self.create_acc_background.setObjectName("create_acc_background")
        self.lines = QtWidgets.QLabel(Form)
        self.lines.setGeometry(QtCore.QRect(578, 248, 284, 196))
        self.lines.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0008_Lines.png);")
        self.lines.setText("")
        self.lines.setObjectName("lines")
        self.email_icon = QtWidgets.QLabel(Form)
        self.email_icon.setGeometry(QtCore.QRect(583, 224, 22, 19))
        self.email_icon.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0003__Group_.png);")
        self.email_icon.setText("")
        self.email_icon.setObjectName("email_icon")
        self.user_icon = QtWidgets.QLabel(Form)
        self.user_icon.setGeometry(QtCore.QRect(583, 290, 22, 25))
        self.user_icon.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0002__Group_.png);")
        self.user_icon.setText("")
        self.user_icon.setObjectName("user_icon")
        self.show_pass_button = QtWidgets.QPushButton(Form)
        self.show_pass_button.setGeometry(QtCore.QRect(820, 352, 34, 26))
        self.show_pass_button.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/show_pass_icon.png);")
        self.show_pass_button.setText("")
        self.show_pass_button.setObjectName("show_pass_button")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(838, 365, 16, 14))
        self.label_2.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0000s_0000__Group_.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Button_background = QtWidgets.QPushButton(Form)
        self.Button_background.setGeometry(QtCore.QRect(580, 460, 287, 177))
        self.Button_background.setAutoFillBackground(False)
        self.Button_background.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0002s_0000__Image_.png);")
        self.Button_background.setText("")
        self.Button_background.setAutoDefault(False)
        self.Button_background.setDefault(False)
        self.Button_background.setFlat(False)
        self.Button_background.setObjectName("Button_background")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(667, 536, 125, 36))
        self.pushButton.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0001s_0000__Group_.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton_2")
        self.Parrot = QtWidgets.QLabel(Form)
        self.Parrot.setGeometry(QtCore.QRect(643, 154, 152, 14))
        self.Parrot.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0000_Parrot.png);")
        self.Parrot.setText("")
        self.Parrot.setObjectName("Parrot")
        self.show_pass_2 = QtWidgets.QPushButton(Form)
        self.show_pass_2.setGeometry(QtCore.QRect(820, 417, 34, 24))
        self.show_pass_2.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/show_pass_icon.png);")
        self.show_pass_2.setText("")
        self.show_pass_2.setObjectName("show_pass_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(838, 428, 16, 14))
        self.label_4.setStyleSheet("image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0000s_0000__Group_.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Email_id = QtWidgets.QLineEdit(Form)
        self.Email_id.setGeometry(QtCore.QRect(608, 218, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Hurme Geometric Sans 1")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(0)
        self.Email_id.setFont(font)
        self.Email_id.setAutoFillBackground(False)
        self.Email_id.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/Line 1.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 14pt \"Hurme Geometric Sans 1\";")
        self.Email_id.setMaxLength(32767)
        self.Email_id.setClearButtonEnabled(True)
        self.Email_id.setObjectName("Email_id")
        self.Username = QtWidgets.QLineEdit(Form)
        self.Username.setGeometry(QtCore.QRect(608, 290, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Hurme Geometric Sans 1")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(0)
        self.Username.setFont(font)
        self.Username.setAutoFillBackground(False)
        self.Username.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/Line 1.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 14pt \"Hurme Geometric Sans 1\";")
        self.Username.setMaxLength(32767)
        self.Username.setClearButtonEnabled(True)
        self.Username.setObjectName("Username")
        self.CreatePass_2 = QtWidgets.QLineEdit(Form)
        self.CreatePass_2.setGeometry(QtCore.QRect(580, 349, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Hurme Geometric Sans 1")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(0)
        self.CreatePass_2.setFont(font)
        self.CreatePass_2.setAutoFillBackground(False)
        self.CreatePass_2.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/Line 1.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 14pt \"Hurme Geometric Sans 1\";")
        self.CreatePass_2.setMaxLength(32767)
        self.CreatePass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CreatePass_2.setClearButtonEnabled(False)
        self.CreatePass_2.setObjectName("CreatePass_2")
        self.ConfirmPass = QtWidgets.QLineEdit(Form)
        self.ConfirmPass.setGeometry(QtCore.QRect(580, 411, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Hurme Geometric Sans 1")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(0)
        self.ConfirmPass.setFont(font)
        self.ConfirmPass.setAutoFillBackground(False)
        self.ConfirmPass.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/Line 1.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 14pt \"Hurme Geometric Sans 1\";")
        self.ConfirmPass.setMaxLength(32767)
        self.ConfirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPass.setClearButtonEnabled(False)
        self.ConfirmPass.setObjectName("ConfirmPass")
        self.error_lable = QtWidgets.QLabel(Form)
        self.error_lable.setGeometry(QtCore.QRect(580, 450, 200, 50
                                                  ))
        font = QtGui.QFont()
        font.setFamily("OCR-B 10 BT")
        font.setPointSize(12)
        font.setItalic(False)
        self.error_lable.setFont(font)
        self.error_lable.setStyleSheet("color: rgb(250, 85, 85);")
        self.error_lable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.error_lable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_lable.setWordWrap(True)
        self.error_lable.setObjectName("error_lable")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(902, 115, 21, 21))
        self.cancel_button.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/cancel button.png);")
        self.cancel_button.setText("")
        self.cancel_button.setObjectName("cancel_button")
        self.hide_button = QtWidgets.QPushButton(Form)
        self.hide_button.setGeometry(QtCore.QRect(820, 352, 34, 26))
        self.hide_button.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/show_pass_icon.png);")
        self.hide_button.setText("")
        self.hide_button.setObjectName("hide_button")
        self.hide_button_2 = QtWidgets.QPushButton(Form)
        self.hide_button_2.setGeometry(QtCore.QRect(820, 417, 34, 24))
        self.hide_button_2.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/show_pass_icon.png);")
        self.hide_button_2.setText("")
        self.hide_button_2.setObjectName("hide_button_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.cancel_button.clicked.connect(Form.close)
        self.hide_button.hide()
        self.hide_button_2.hide()
        self.error_lable.hide()

        self.show_pass_button.clicked.connect(self.show_password_1)
        self.show_pass_2.clicked.connect(self.show_password_2)
        self.hide_button.clicked.connect(self.hide_password_1)
        self.hide_button_2.clicked.connect(self.hide_password_2)

    def show_password_1(self):
        self.show_pass_button.hide()
        self.label_2.hide()
        self.hide_button.show()
        self.CreatePass_2.setEchoMode(QtWidgets.QLineEdit.Normal)
    def hide_password_1(self):
        self.show_pass_button.show()
        self.label_2.show()
        self.hide_button.hide()
        self.CreatePass_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def show_password_2(self):
        self.show_pass_2.hide()
        self.label_4.hide()
        self.hide_button_2.show()
        self.ConfirmPass.setEchoMode(QtWidgets.QLineEdit.Normal)
    def hide_password_2(self):
        self.show_pass_2.show()
        self.label_4.show()
        self.hide_button_2.hide()
        self.ConfirmPass.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Email_id.setPlaceholderText(_translate("Form", "Enter Your Valid Email Id."))
        self.Username.setPlaceholderText(_translate("Form", "Create Username."))
        self.CreatePass_2.setPlaceholderText(_translate("Form", "Create Password."))
        self.ConfirmPass.setPlaceholderText(_translate("Form", "Confirm Password."))
        self.error_lable.setText(_translate("Form", "Password: Min 8, Uppercase, Lowercase & special charectors"))
from Windows import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
