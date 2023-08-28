from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
import MySQLdb

import random
import json




from Windows.NewLoginUi import Ui_login_Form
from Windows.new_CreateAUi import Ui_Form
from Windows.New_forgot_passUi import Ui_forgotPass
from Windows.New_new_passUi import Ui_new_pass
from lib.send_otp import recive_otp



from lib.Ckeck_Pass import is_valid_password

from lib.Ckeck_Pass import is_valid_password


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.logui = Ui_login_Form()
        self.logui.setupUi(self)
        self.logui.Username_text.returnPressed.connect(self.moveFocus)
        self.logui.Password_text.returnPressed.connect(self.moveFocus)
        self.logui.Login_Button.clicked.connect(lambda: self.login())
        self.logui.Password_text.returnPressed.connect(self.logui.Login_Button.click)
        self.logui.Create_Acc.clicked.connect(lambda: self.createAcc())
        self.logui.Forgot_Password.clicked.connect(lambda: self.forgotPassword())

    """Create Account Function"""
    def createAcc(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.ui.pushButton.clicked.connect(lambda: created())
        def show_error(message):
            self.ui.error_lable.show()
            self.ui.error_lable.setText(message)

        def created():
            email_id = self.ui.Email_id.text()
            username = self.ui.Username.text()
            password = self.ui.CreatePass_2.text()
            cfpassword = self.ui.ConfirmPass.text()
            db = MySQLdb.connect(host="localhost", user="pratik", password="pratik[21]",database='parotdata')
            cur = db.cursor()
            sql = f"select * from users where username='{username}' or email='{email_id}'"
            cur.execute(sql)
            Checking_Exist_Acc = cur.fetchone()
            db.commit()
            db.close()

            if len(email_id)==0:
                show_error("please enter your email id")
            elif len(username)==0:
                show_error("please enter your username")
            elif len(password)==0:
                show_error("please enter your password")
            elif len(cfpassword)==0:
                show_error("please reenter your password")
            elif password != cfpassword:
                show_error("please reenter your password")
# <<<<<<< HEAD:lib/login.py
            elif is_valid_password(password) == False:
                show_error("Password: Min 8, Uppercase, Lowercase & special charectors")

            elif Checking_Exist_Acc:
                show_error("Already you have an account.")
            
            else:    
                try:
                    db = MySQLdb.connect(host="localhost", user="pratik", password="pratik[21]",database='parotdata')
                    cur = db.cursor()
                    sql = f"insert into users(username,password,email) values ('{username}','{password}','{email_id}')"
                    a=cur.execute(sql)
                    db.commit()
                    db.close()
                    if a == 1:
                        self.Form.close()

                except Exception as e:
                    error = e
                    f = str(error)
                    print(f)
                        
    """Create movement Function"""
    def moveFocus(self):
        cur_wid = QApplication.focusWidget()

        if cur_wid == self.logui.Username_text:
            self.logui.Password_text.setFocus()
        elif cur_wid == self.logui.Password_text:
            self.logui.Login_Button.setFocus()

        elif cur_wid == self.logui.Login_Button:
            self.logui.Username_text.setFocus()

    """loginFunction"""
    def login(self):
        username = self.logui.Username_text.text()
        password = self.logui.Password_text.text()

        print(len(username), password)

    

        """Database connection"""
        if len(username)>0 and len(password)>0:
            try:
                db = MySQLdb.connect(host="localhost",user='pratik',password='pratik[21]',database='parotdata')
                cur = db.cursor()
                sql = f"SELECT * FROM users WHERE username='{username}' or email='{username}' AND password='{password}'"   
                cur.execute(sql)
                row = cur.fetchone()

                print(row[1])
                if username == row[0] or username == row[2]:
                    if password == row[1]:
                        self.logui.label.setText("Successfully Logged in")
                        name = {
                            "name":username,
                        }
                        self.path = "lib/load.json"
                        with open(self.path,"w") as file:
                            json.dump(name,file)
                        self.close()
                    else:
                        self.logui.label.setText("Invalid Password")
                else:
                    self.logui.label.setText("Invalid username")

                db.commit()
                db.close()
            
   
            except Exception as e:
                self.logui.label.setText("Invalid username")
                print(e)

        else:
                self.logui.label.setText(f'Incurrect Username or Password')
                self.logui.label.adjustSize()

    def forgotPassword(self):
        self.otp_Form = QtWidgets.QWidget()
        self.ui = Ui_forgotPass()
        self.ui.setupUi(self.otp_Form)
        self.ui.send.clicked.connect(lambda: send_otp())
        self.ui.submit_button.clicked.connect(lambda: return_otp())
        self.otp_Form.show()
        def show_error(message):
            self.ui.error_lable.show()
            self.ui.error_lable.setText(message)

        def send_otp():
            self.otp = random.randint(10000,99999)
            print(self.otp)
            self.mob_num = self.ui.mobile_num_text_2.text()
            print(self.mob_num.isdigit())
            if self.mob_num.isdigit() and len(self.mob_num)==10:
                self.ui.send.setText("Resend")
                recive_otp(self.mob_num, self.otp)
            else:
                show_error("Please enter 10 digit mob number")

        def return_otp():
            try:
                self.entered_otp = int(self.ui.otp_text.text())
                print(type(self.entered_otp))
                if self.otp == self.entered_otp:
                    show_error("otp is currected") 
                    self.new_passForm = QtWidgets.QWidget()
                    self.ui = Ui_new_pass()
                    self.ui.setupUi(self.new_passForm)
                    self.ui.submit_button.clicked.connect(lambda: create_new_pass())
                    self.otp_Form.close()
                    self.new_passForm.show()

                    def create_new_pass():
                        self.email = self.ui.email_text.text()
                        self.new_password = self.ui.new_password.text()
                        self.confirm_password = self.ui.conferm_new_password.text()
                        if len(self.email)==0:
                            show_error('Please enter your email id')
                        elif len(self.new_password)==0:
                            show_error('Please enter your new password')
                        elif len(self.confirm_password)==0:
                            show_error('Please renter your password')
                        elif self.confirm_password != self.new_password:
                            show_error("Reenter your same password")
                        elif is_valid_password(self.new_password) == False:
                            show_error("Password: combination of uppercase and lowercase letters,numbers and special characters")
                        else:
                            try:   
                                db = MySQLdb.connect(host="localhost", user="pratik", password="pratik[21]",database='parotdata')
                                cur = db.cursor()
                                sql = f"Update users SET password = '{self.new_password}' WHERE email ='{self.email}'"
                                a=cur.execute(sql)
                                print(a)
                                if a==1:
                                    self.new_passForm.close()
                                if a==0:
                                    show_error("Provided emailid is incorrect")
                                db.commit()
                                db.close()
                            except Exception as e:
                                print(e)
                else:
                    show_error("please enter valid otp")
            except Exception as e:
                print(e)   
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = QtWidgets.QWidget()
    window = MainWindow()
    window.show()
    app.exec_()