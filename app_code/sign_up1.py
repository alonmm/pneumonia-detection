# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign_up(object):
    def setupUi(self, Dialog, client, main_win):
        Dialog.setObjectName("Dialog")
        Dialog.resize(376, 469)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 471, 461))
        self.frame_2.setStyleSheet("background-color: rgb(202,202,202);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 471, 491))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(54,54,54);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 410, 121, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 18pt\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 100, 281, 31))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 261, 71))
        self.label_3.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 160, 281, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 111, 21))
        self.label_5.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 111, 21))
        self.label_7.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 320, 181, 21))
        self.label_8.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 220, 281, 31))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.label_9.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 280, 281, 31))
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 340, 281, 31))
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(40, 380, 221, 21))
        self.label_11.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 380, 251, 21))
        self.label_12.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 380, 251, 21))
        self.label_13.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")

        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda: self.try_sign_up(Dialog, client, main_win))

    def try_sign_up(self, Dialog, client, main_win):
        full_name = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        username = self.lineEdit_3.text()
        password = self.lineEdit_6.text()
        confirm_pass = self.lineEdit_7.text()
        if full_name == '' or email == '' or username == '' or password == '' or confirm_pass == '':
            self.label_11.show()
            self.label_11.raise_()
            return
        if password != confirm_pass:
            self.label_12.show()
            self.label_12.raise_()
            return
        res = client.sign_up(full_name, email, username, password)
        print(res)
        res = client.handle_res(res, "sign_up")
        if res != None:
            main_win.turn_into_logged_in_mode(username, res)
            main_win.fill_table(client)
            Dialog.close()
        else:
            self.label_13.show()
            self.label_13.raise_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Sign_up", "Sign_up"))
        self.pushButton_2.setText(_translate("Dialog", "Sign up"))
        self.label_4.setText(_translate("Dialog", "First and last name:"))
        self.label_3.setText(_translate("Dialog", "Personal details"))
        self.label_5.setText(_translate("Dialog", "Username:"))
        self.label_7.setText(_translate("Dialog", "Password:"))
        self.label_8.setText(_translate("Dialog", "Confirm password:"))
        self.label_9.setText(_translate("Dialog", "e-mail:"))
        self.label_11.setText(_translate("Dialog", "please fill all the fields!"))
        self.label_12.setText(_translate("Dialog", "make sure you wrote the same password!"))
        self.label_13.setText(_translate("Dialog", "username already exists!"))
