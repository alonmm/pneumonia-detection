# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_results_win(object):
    def setupUi(self, Dialog, is_pneu, is_patient):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 321)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        Dialog.setModal(True)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 441, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 491, 241))
        self.textEdit_2.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 16pt")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(490, 0, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo1.png"))
        self.label.setObjectName("label")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 70, 491, 241))
        self.textEdit_3.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgb(54, 54, 54);\n"
"font-size: 16pt")
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 270, 81, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 18pt\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label.raise_()
        self.pushButton_4.raise_()

        self.pushButton_4.clicked.connect(lambda: self.close_win(Dialog))


        if is_patient:
            self.label_3.raise_()
        if is_pneu:
            self.textEdit_2.raise_()
        else:
            self.textEdit_3.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def close_win(self, Dialog):
        Dialog.close()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Patient was added susccesfully."))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Our detection is that your patient <span style=\" font-weight:600;\">is suffering</span> from pneumania.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">In that case we reccomend you to make sure your diagnose is accurate and that you are giving the right treatment.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">We want to remind you that the results</span><span style=\" font-size:12pt; font-weight:600;\"> are not</span><span style=\" font-size:12pt;\"> accurate in 100%.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The tool is an </span><span style=\" font-size:12pt; font-weight:600;\">advisory tool only</span><span style=\" font-size:12pt;\"> and is not intended to replace the doctor\'s judgment.</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Our detection is that your patient <span style=\" font-weight:600;\">isn\'t suffering</span> from pneumania.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">In that case we reccomend you to make sure your diagnose is accurate. We reccomnd you to check if the patient is suffering from another disease</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">We want to remind you that the results</span><span style=\" font-size:12pt; font-weight:600;\"> are not</span><span style=\" font-size:12pt;\"> accurate in 100%.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The tool is an </span><span style=\" font-size:12pt; font-weight:600;\">advisory tool only</span><span style=\" font-size:12pt;\"> and is not intended to replace the doctor\'s judgment.</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "Ok"))
