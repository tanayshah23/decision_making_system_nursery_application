# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 539)
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(230, 360, 131, 51))
        self.b1.setObjectName("b1")
        self.p1 = QtWidgets.QRadioButton(Dialog)
        self.p1.setGeometry(QtCore.QRect(220, 80, 49, 17))
        self.p1.setObjectName("p1")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.p1)
        self.p2 = QtWidgets.QRadioButton(Dialog)
        self.p2.setGeometry(QtCore.QRect(274, 80, 78, 17))
        self.p2.setObjectName("p2")
        self.buttonGroup_2.addButton(self.p2)
        self.p3 = QtWidgets.QRadioButton(Dialog)
        self.p3.setGeometry(QtCore.QRect(357, 80, 121, 17))
        self.p3.setObjectName("p3")
        self.buttonGroup_2.addButton(self.p3)
        self.n3 = QtWidgets.QRadioButton(Dialog)
        self.n3.setGeometry(QtCore.QRect(360, 110, 67, 17))
        self.n3.setObjectName("n3")
        self.n1 = QtWidgets.QRadioButton(Dialog)
        self.n1.setGeometry(QtCore.QRect(220, 110, 55, 17))
        self.n1.setObjectName("n1")
        self.n2 = QtWidgets.QRadioButton(Dialog)
        self.n2.setGeometry(QtCore.QRect(280, 110, 81, 17))
        self.n2.setObjectName("n2")
        self.n4 = QtWidgets.QRadioButton(Dialog)
        self.n4.setGeometry(QtCore.QRect(430, 110, 55, 17))
        self.n4.setObjectName("n4")
        self.n5 = QtWidgets.QRadioButton(Dialog)
        self.n5.setGeometry(QtCore.QRect(490, 110, 91, 17))
        self.n5.setObjectName("n5")
        self.f1 = QtWidgets.QRadioButton(Dialog)
        self.f1.setGeometry(QtCore.QRect(220, 140, 71, 17))
        self.f1.setObjectName("f1")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.f1)
        self.f2 = QtWidgets.QRadioButton(Dialog)
        self.f2.setGeometry(QtCore.QRect(290, 140, 71, 17))
        self.f2.setObjectName("f2")
        self.buttonGroup.addButton(self.f2)
        self.f3 = QtWidgets.QRadioButton(Dialog)
        self.f3.setGeometry(QtCore.QRect(370, 140, 91, 17))
        self.f3.setObjectName("f3")
        self.buttonGroup.addButton(self.f3)
        self.f4 = QtWidgets.QRadioButton(Dialog)
        self.f4.setGeometry(QtCore.QRect(450, 140, 81, 17))
        self.f4.setObjectName("f4")
        self.buttonGroup.addButton(self.f4)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(90, 70, 126, 261))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.splitter_4 = QtWidgets.QSplitter(Dialog)
        self.splitter_4.setGeometry(QtCore.QRect(220, 240, 241, 17))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.fi1 = QtWidgets.QRadioButton(self.splitter_4)
        self.fi1.setObjectName("fi1")
        self.fi2 = QtWidgets.QRadioButton(self.splitter_4)
        self.fi2.setObjectName("fi2")
        self.lab = QtWidgets.QLabel(Dialog)
        self.lab.setGeometry(QtCore.QRect(100, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lab.setFont(font)
        self.lab.setObjectName("lab")
        self.splitter_3 = QtWidgets.QSplitter(Dialog)
        self.splitter_3.setGeometry(QtCore.QRect(220, 170, 191, 17))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.c1 = QtWidgets.QRadioButton(self.splitter_3)
        self.c1.setObjectName("c1")
        self.c2 = QtWidgets.QRadioButton(self.splitter_3)
        self.c2.setObjectName("c2")
        self.c3 = QtWidgets.QRadioButton(self.splitter_3)
        self.c3.setObjectName("c3")
        self.c4 = QtWidgets.QRadioButton(self.splitter_3)
        self.c4.setObjectName("c4")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(220, 210, 241, 17))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.h1 = QtWidgets.QRadioButton(self.splitter_2)
        self.h1.setObjectName("h1")
        self.h2 = QtWidgets.QRadioButton(self.splitter_2)
        self.h2.setObjectName("h2")
        self.h3 = QtWidgets.QRadioButton(self.splitter_2)
        self.h3.setObjectName("h3")
        self.splitter_5 = QtWidgets.QSplitter(Dialog)
        self.splitter_5.setGeometry(QtCore.QRect(220, 270, 311, 17))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.s1 = QtWidgets.QRadioButton(self.splitter_5)
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QRadioButton(self.splitter_5)
        self.s2.setObjectName("s2")
        self.s3 = QtWidgets.QRadioButton(self.splitter_5)
        self.s3.setObjectName("s3")
        self.splitter_6 = QtWidgets.QSplitter(Dialog)
        self.splitter_6.setGeometry(QtCore.QRect(220, 300, 301, 17))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.he1 = QtWidgets.QRadioButton(self.splitter_6)
        self.he1.setObjectName("he1")
        self.he2 = QtWidgets.QRadioButton(self.splitter_6)
        self.he2.setObjectName("he2")
        self.he3 = QtWidgets.QRadioButton(self.splitter_6)
        self.he3.setObjectName("he3")
        self.res = QtWidgets.QLabel(Dialog)
        self.res.setGeometry(QtCore.QRect(190, 450, 341, 31))
        self.res.setText("")
        self.res.setObjectName("res")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(140, 30, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.b1.setText(_translate("Dialog", "Check"))
        self.p1.setText(_translate("Dialog", "Usual"))
        self.p2.setText(_translate("Dialog", "Pretentious"))
        self.p3.setText(_translate("Dialog", "Greatly Pretentious"))
        self.n3.setText(_translate("Dialog", "Improper"))
        self.n1.setText(_translate("Dialog", "Proper"))
        self.n2.setText(_translate("Dialog", "Less Proper"))
        self.n4.setText(_translate("Dialog", "Critical"))
        self.n5.setText(_translate("Dialog", "Very Critical"))
        self.f1.setText(_translate("Dialog", "Complete"))
        self.f2.setText(_translate("Dialog", "Completed"))
        self.f3.setText(_translate("Dialog", "Incomplete"))
        self.f4.setText(_translate("Dialog", "Foster"))
        self.label.setText(_translate("Dialog", "Parents"))
        self.label_2.setText(_translate("Dialog", "Has Nurs"))
        self.label_3.setText(_translate("Dialog", "Form"))
        self.label_4.setText(_translate("Dialog", "No. Of Children"))
        self.label_5.setText(_translate("Dialog", "Housing"))
        self.label_6.setText(_translate("Dialog", "Finance"))
        self.label_7.setText(_translate("Dialog", "Social"))
        self.label_8.setText(_translate("Dialog", "Health"))
        self.fi1.setText(_translate("Dialog", "Convinient"))
        self.fi2.setText(_translate("Dialog", "Inconvinient"))
        self.lab.setText(_translate("Dialog", "Results: "))
        self.c1.setText(_translate("Dialog", "1"))
        self.c2.setText(_translate("Dialog", "2"))
        self.c3.setText(_translate("Dialog", "3"))
        self.c4.setText(_translate("Dialog", "More"))
        self.h1.setText(_translate("Dialog", "Convinient"))
        self.h2.setText(_translate("Dialog", "Less Convinient"))
        self.h3.setText(_translate("Dialog", "Critical"))
        self.s1.setText(_translate("Dialog", "Non Problematic"))
        self.s2.setText(_translate("Dialog", "Slightly Problematic"))
        self.s3.setText(_translate("Dialog", "Problematic"))
        self.he1.setText(_translate("Dialog", "Recommended"))
        self.he2.setText(_translate("Dialog", "Priority"))
        self.he3.setText(_translate("Dialog", "Not Recommended"))
        self.label_9.setText(_translate("Dialog", "Decision Making System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())