# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\New_forgot_passUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forgotPass(object):
    def setupUi(self, forgotPass):
        forgotPass.setObjectName("forgotPass")
        forgotPass.resize(1440, 799)
        forgotPass.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        forgotPass.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_background = QtWidgets.QLabel(forgotPass)
        self.main_background.setGeometry(QtCore.QRect(0, 0, 1440, 800))
        self.main_background.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0003s_0001_Vector-Smart-Object.png);")
        self.main_background.setText("")
        self.main_background.setObjectName("main_background")
        self.create_acc_background = QtWidgets.QLabel(forgotPass)
        self.create_acc_background.setGeometry(QtCore.QRect(480, 194, 505, 412))
        self.create_acc_background.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0003s_0000__Path_.png);")
        self.create_acc_background.setText("")
        self.create_acc_background.setObjectName("create_acc_background")
        self.Parrot = QtWidgets.QLabel(forgotPass)
        self.Parrot.setGeometry(QtCore.QRect(645, 260, 169, 15))
        self.Parrot.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0000_Parrot.png);")
        self.Parrot.setText("")
        self.Parrot.setObjectName("Parrot")
        self.mobile_num_text_2 = QtWidgets.QLineEdit(forgotPass)
        self.mobile_num_text_2.setGeometry(QtCore.QRect(610, 323, 235, 21))
        font = QtGui.QFont()
        font.setFamily("Hurme Geometric Sans 1")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(0)
        self.mobile_num_text_2.setFont(font)
        self.mobile_num_text_2.setAutoFillBackground(False)
        self.mobile_num_text_2.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/Line 1.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 14pt \"Hurme Geometric Sans 1\";")
        self.mobile_num_text_2.setMaxLength(32767)
        self.mobile_num_text_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mobile_num_text_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.mobile_num_text_2.setClearButtonEnabled(True)
        self.mobile_num_text_2.setObjectName("mobile_num_text_2")
        self.error_lable = QtWidgets.QLabel(forgotPass)
        self.error_lable.setGeometry(QtCore.QRect(600, 400, 261, 41))
        font = QtGui.QFont()
        font.setFamily("OCR-B 10 BT")
        font.setPointSize(10)
        font.setItalic(False)
        self.error_lable.setFont(font)
        self.error_lable.setStyleSheet("color: rgb(250, 85, 85);")
        self.error_lable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.error_lable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.error_lable.setWordWrap(True)
        self.error_lable.setObjectName("error_lable")
        self.cancel_button = QtWidgets.QPushButton(forgotPass)
        self.cancel_button.setEnabled(True)
        self.cancel_button.setGeometry(QtCore.QRect(960, 190, 21, 21))
        self.cancel_button.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/cancel button.png);")
        self.cancel_button.setText("")
        self.cancel_button.setObjectName("cancel_button")
        self.label = QtWidgets.QLabel(forgotPass)
        self.label.setGeometry(QtCore.QRect(609, 348, 247, 1))
        self.label.setStyleSheet("border-image: url(:/forgotpass/Project-Parot-assets/Create-acc-assets/Asset 2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(forgotPass)
        self.label_2.setGeometry(QtCore.QRect(648, 470, 178, 1))
        self.label_2.setStyleSheet("border-image: url(:/forgotpass/Project-Parot-assets/Create-acc-assets/Asset 2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.otp_text = QtWidgets.QLineEdit(forgotPass)
        self.otp_text.setGeometry(QtCore.QRect(660, 444, 149, 21))
        font = QtGui.QFont()
        font.setFamily("Hurme Geometric Sans 1")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(0)
        self.otp_text.setFont(font)
        self.otp_text.setAutoFillBackground(False)
        self.otp_text.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/Line 1.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 14pt \"Hurme Geometric Sans 1\";")
        self.otp_text.setMaxLength(32767)
        self.otp_text.setAlignment(QtCore.Qt.AlignCenter)
        self.otp_text.setClearButtonEnabled(True)
        self.otp_text.setObjectName("otp_text")
        self.send = QtWidgets.QPushButton(forgotPass)
        self.send.setGeometry(QtCore.QRect(680, 360, 106, 22))
        self.send.setStyleSheet("border-image: url(:/forgotpass/Project-Parot-assets/forgot-pass-assets/send_button.png);\n"
"font: 12pt \"Tourner\";\n"
"color: rgb(255, 255, 255);")
        self.send.setObjectName("send")
        self.submit_button = QtWidgets.QPushButton(forgotPass)
        self.submit_button.setGeometry(QtCore.QRect(571, 411, 321, 197))
        self.submit_button.setStyleSheet("border-image: url(:/createAcc/Project-Parot-assets/Create-acc-assets/create_account_ui_0000s_0002s_0000__Image_.png);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Tourner\";")
        self.submit_button.setObjectName("submit_button")




        
        self.main_background.raise_()
        self.create_acc_background.raise_()
        self.Parrot.raise_()
        self.mobile_num_text_2.raise_()
        self.error_lable.raise_()
        self.cancel_button.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.send.raise_()
        self.submit_button.raise_()
        self.otp_text.raise_()

        self.retranslateUi(forgotPass)
        QtCore.QMetaObject.connectSlotsByName(forgotPass)
        
        self.error_lable.hide()
        self.cancel_button.clicked.connect(forgotPass.close)

    def retranslateUi(self, forgotPass):
        _translate = QtCore.QCoreApplication.translate
        forgotPass.setWindowTitle(_translate("forgotPass", "Form"))
        self.mobile_num_text_2.setPlaceholderText(_translate("forgotPass", "Enter your mobile num."))
        self.error_lable.setText(_translate("forgotPass", "Password: Min 8, Uppercase, Lowercase & special charectors"))
        self.otp_text.setPlaceholderText(_translate("forgotPass", "Enter OTP here."))
        self.send.setText(_translate("forgotPass", "Send"))
        self.submit_button.setText(_translate("forgotPass", "Submit"))
# import resource_rc
from Windows import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    forgotPass = QtWidgets.QWidget()
    ui = Ui_forgotPass()
    ui.setupUi(forgotPass)
    forgotPass.show()
    sys.exit(app.exec_())
