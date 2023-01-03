# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1504, 900)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("backgound-color: rgb(179, 200, 181)")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -30, 1501, 931))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color:rgb(172, 255, 211)")
        self.widget.setObjectName("widget")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(20, 50, 351, 861))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color:rgb(85, 255, 127)")
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtSoDinh = QtWidgets.QLineEdit(self.frame_2)
        self.txtSoDinh.setGeometry(QtCore.QRect(210, 70, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtSoDinh.setFont(font)
        self.txtSoDinh.setStyleSheet("background:rgb(255, 255, 255)")
        self.txtSoDinh.setObjectName("txtSoDinh")
        self.txtMaTran = QtWidgets.QTextEdit(self.frame_2)
        self.txtMaTran.setGeometry(QtCore.QRect(10, 160, 331, 321))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtMaTran.setFont(font)
        self.txtMaTran.setStyleSheet("background: rgb(255, 255, 255)")
        self.txtMaTran.setObjectName("txtMaTran")
        self.btnKruscal = QtWidgets.QPushButton(self.frame_2)
        self.btnKruscal.setGeometry(QtCore.QRect(40, 520, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnKruscal.setFont(font)
        self.btnKruscal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnKruscal.setStyleSheet("background:rgb(255, 85, 0)")
        self.btnKruscal.setObjectName("btnKruscal")
        self.btnPrim = QtWidgets.QPushButton(self.frame_2)
        self.btnPrim.setGeometry(QtCore.QRect(210, 520, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnPrim.setFont(font)
        self.btnPrim.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPrim.setStyleSheet("background:rgb(255, 85, 0)")
        self.btnPrim.setObjectName("btnPrim")
        self.btnInfo = QtWidgets.QPushButton(self.frame_2)
        self.btnInfo.setGeometry(QtCore.QRect(90, 740, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnInfo.setFont(font)
        self.btnInfo.setStyleSheet("background:rgb(255, 85, 0)")
        self.btnInfo.setObjectName("btnInfo")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(390, 50, 1091, 861))
        self.frame_3.setStyleSheet("background-color: rgb(85, 255, 127)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tblMaTran = QtWidgets.QTableWidget(self.frame_3)
        self.tblMaTran.setGeometry(QtCore.QRect(10, 10, 331, 311))
        self.tblMaTran.setMinimumSize(QtCore.QSize(301, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tblMaTran.setFont(font)
        self.tblMaTran.setStyleSheet("background:rgb(255, 255, 255)")
        self.tblMaTran.setObjectName("tblMaTran")
        self.tblMaTran.setColumnCount(0)
        self.tblMaTran.setRowCount(0)
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setGeometry(QtCore.QRect(350, 10, 731, 311))
        self.widget_4.setStyleSheet("background:rgb(255, 255, 255)")
        self.widget_4.setObjectName("widget_4")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(210, 360, 871, 481))
        self.frame.setStyleSheet("background: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnNext = QtWidgets.QPushButton(self.frame)
        self.btnNext.setGeometry(QtCore.QRect(770, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnNext.setFont(font)
        self.btnNext.setStyleSheet("background:rgb(255, 85, 0)")
        self.btnNext.setObjectName("btnNext")
        self.btnPrev = QtWidgets.QPushButton(self.frame)
        self.btnPrev.setGeometry(QtCore.QRect(660, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnPrev.setFont(font)
        self.btnPrev.setStyleSheet("background:rgb(255, 85, 0)")
        self.btnPrev.setObjectName("btnPrev")
        self.txtResult = QtWidgets.QPlainTextEdit(self.frame_3)
        self.txtResult.setGeometry(QtCore.QRect(10, 360, 191, 481))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtResult.setFont(font)
        self.txtResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtResult.setStyleSheet("background: rgb(255, 255, 255)")
        self.txtResult.setReadOnly(True)
        self.txtResult.setObjectName("txtResult")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(60, 320, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: rgb(85, 255, 127)")
        self.label_2.setObjectName("label_2")
        self.frame_3.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Số đỉnh của đồ thị:"))
        self.btnKruscal.setText(_translate("MainWindow", "Kruscal"))
        self.btnPrim.setText(_translate("MainWindow", "Prim"))
        self.btnInfo.setText(_translate("MainWindow", "Hướng dẫn"))
        self.btnNext.setText(_translate("MainWindow", "Tiếp"))
        self.btnPrev.setText(_translate("MainWindow", "Trước"))
        self.label_2.setText(_translate("MainWindow", "Kết quả:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
