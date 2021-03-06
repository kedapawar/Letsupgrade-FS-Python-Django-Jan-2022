# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from typing_extensions import Self
from PyQt5 import QtCore, QtGui, QtWidgets
# importing libraries
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(232, 243)
        self.res = QtWidgets.QLineEdit(Dialog)
        self.res.setGeometry(QtCore.QRect(0, 0, 231, 51))
        self.res.setObjectName("res")
        self.clr = QtWidgets.QPushButton(Dialog)
        self.clr.setGeometry(QtCore.QRect(0, 50, 111, 31))
        self.clr.setObjectName("clr")
        self.dell = QtWidgets.QPushButton(Dialog)
        self.dell.setGeometry(QtCore.QRect(120, 50, 111, 31))
        self.dell.setObjectName("del")
        self.p1 = QtWidgets.QPushButton(Dialog)
        self.p1.setGeometry(QtCore.QRect(0, 90, 51, 31))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QPushButton(Dialog)
        self.p2.setGeometry(QtCore.QRect(60, 90, 51, 31))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QPushButton(Dialog)
        self.p3.setGeometry(QtCore.QRect(120, 90, 51, 31))
        self.p3.setObjectName("p3")
        self.mul = QtWidgets.QPushButton(Dialog)
        self.mul.setGeometry(QtCore.QRect(180, 90, 51, 31))
        self.mul.setObjectName("mul")
        self.p4 = QtWidgets.QPushButton(Dialog)
        self.p4.setGeometry(QtCore.QRect(0, 130, 51, 31))
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QPushButton(Dialog)
        self.p5.setGeometry(QtCore.QRect(60, 130, 51, 31))
        self.p5.setObjectName("p5")
        self.sub = QtWidgets.QPushButton(Dialog)
        self.sub.setGeometry(QtCore.QRect(180, 130, 51, 31))
        self.sub.setObjectName("sub")
        self.p6 = QtWidgets.QPushButton(Dialog)
        self.p6.setGeometry(QtCore.QRect(120, 130, 51, 31))
        self.p6.setObjectName("p6")
        self.p8 = QtWidgets.QPushButton(Dialog)
        self.p8.setGeometry(QtCore.QRect(60, 170, 51, 31))
        self.p8.setObjectName("p8")
        self.p7 = QtWidgets.QPushButton(Dialog)
        self.p7.setGeometry(QtCore.QRect(0, 170, 51, 31))
        self.p7.setObjectName("p7")
        self.p9 = QtWidgets.QPushButton(Dialog)
        self.p9.setGeometry(QtCore.QRect(120, 170, 51, 31))
        self.p9.setObjectName("p9")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(180, 170, 51, 31))
        self.add.setObjectName("add")
        self.dot = QtWidgets.QPushButton(Dialog)
        self.dot.setGeometry(QtCore.QRect(60, 210, 51, 31))
        self.dot.setObjectName("dot")
        self.p0 = QtWidgets.QPushButton(Dialog)
        self.p0.setGeometry(QtCore.QRect(0, 210, 51, 31))
        self.p0.setObjectName("p0")
        self.div = QtWidgets.QPushButton(Dialog)
        self.div.setGeometry(QtCore.QRect(120, 210, 51, 31))
        self.div.setObjectName("div")
        self.equal = QtWidgets.QPushButton(Dialog)
        self.equal.setGeometry(QtCore.QRect(180, 210, 51, 31))
        self.equal.setObjectName("equl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def Add(self):
            # appending label text
        text = self.res.text()
        self.res.setText(text + " + ")   

    def Sub(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + " - ") 

    def Mul(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + " * ")  

    def Div(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + " / ") 

    def Dot(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + " . ")  

    def Equal(self):
        # appending label text
        text1 = self.res.text()
        # get the label text
        # getting the ans
        try:
          ans = eval(text1)
        # setting text to the label
          self.res.setText(str(ans))
        except:
           self.res.setText("Wrong Input")
    
    
    def Clr(self):
        # appending label text
        #text = self.res.text()
        self.res.setText(" ")

    def Dell(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text[:len(text)-1])

    def one(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "1")   

    def two(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "2")     

    def three(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "3")  

    def four(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "4")  

    def five(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "5")      

    def six(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "6")  

    def seven(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "7")  

    def eight(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "8")      

    def nine(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "9") 

    def zero(self):
        # appending label text
        text = self.res.text()
        self.res.setText(text + "0")                             

    
                                      

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.clr.setText(_translate("Dialog", "CLEAR"))
            self.dell.setText(_translate("Dialog", "DELETE"))
            self.p1.setText(_translate("Dialog", "1"))
            self.p2.setText(_translate("Dialog", "2"))
            self.p3.setText(_translate("Dialog", "3"))
            self.mul.setText(_translate("Dialog", "*"))
            self.p4.setText(_translate("Dialog", "4"))
            self.p5.setText(_translate("Dialog", "5"))
            self.sub.setText(_translate("Dialog", "-"))
            self.p6.setText(_translate("Dialog", "6"))
            self.p8.setText(_translate("Dialog", "8"))
            self.p7.setText(_translate("Dialog", "7"))
            self.p9.setText(_translate("Dialog", "9"))
            self.add.setText(_translate("Dialog", "+"))
            self.dot.setText(_translate("Dialog", "."))
            self.p0.setText(_translate("Dialog", "0"))
            self.div.setText(_translate("Dialog", "/"))
            self.equal.setText(_translate("Dialog", "="))
            self.add.clicked.connect(self.Add)
            self.sub.clicked.connect(self.Sub)
            self.mul.clicked.connect(self.Mul)
            self.div.clicked.connect(self.Div)
            self.dot.clicked.connect(self.Dot)
            self.equal.clicked.connect(self.Equal)
            self.clr.clicked.connect(self.Clr)
            self.dell.clicked.connect(self.Dell)
            self.p1.clicked.connect(self.one)
            self.p2.clicked.connect(self.two)
            self.p3.clicked.connect(self.three)
            self.p4.clicked.connect(self.four)
            self.p5.clicked.connect(self.five)
            self.p6.clicked.connect(self.six)
            self.p7.clicked.connect(self.seven)
            self.p8.clicked.connect(self.eight)
            self.p9.clicked.connect(self.nine)
            self.p0.clicked.connect(self.zero)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())