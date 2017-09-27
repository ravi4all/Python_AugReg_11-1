# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='demo', autocommit=True)

cursor = connection.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1060, 695)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 130, 291, 61))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 230, 291, 61))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(380, 140, 331, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 230, 331, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 320, 291, 61))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 320, 331, 61))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 470, 331, 51))
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.exec_query)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Name"))
        self.label_2.setText(_translate("Dialog", "Enter Mail"))
        self.label_3.setText(_translate("Dialog", "Enter Password"))
        self.pushButton.setText(_translate("Dialog", "Submit"))

    def exec_query(self):

        self.name = self.lineEdit.text()
        self.email = self.lineEdit_2.text()
        self.pwd = self.lineEdit_3.text()

        query = "INSERT INTO mytable (Name,Email,password) VALUES (%s,%s,%s)"

        cursor.execute(query, (self.name, self.email, self.pwd))

        print("Data Inserted...")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

