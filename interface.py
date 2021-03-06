# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setObjectName("centralwidget")
        self.Uzli = QtWidgets.QLabel(self.centralwidget)
        self.Uzli.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Uzli.setFont(font)
        self.Uzli.setObjectName("Uzli")
        self.Sterjni = QtWidgets.QLabel(self.centralwidget)
        self.Sterjni.setGeometry(QtCore.QRect(230, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sterjni.setFont(font)
        self.Sterjni.setObjectName("Sterjni")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(660, 460, 101, 61))
        self.refresh.setObjectName("refresh")
        self.paint_widget = QtWidgets.QGraphicsView(self.centralwidget)
        self.paint_widget.setGeometry(QtCore.QRect(10, 270, 618, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paint_widget.sizePolicy().hasHeightForWidth())
        self.paint_widget.setSizePolicy(sizePolicy)
        self.paint_widget.setMouseTracking(True)
        self.paint_widget.setAutoFillBackground(True)
        self.paint_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.paint_widget.setObjectName("paint_widget")
        self.Sili = QtWidgets.QLabel(self.centralwidget)
        self.Sili.setGeometry(QtCore.QRect(540, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sili.setFont(font)
        self.Sili.setObjectName("Sili")
        self.left_zadel = QtWidgets.QPushButton(self.centralwidget)
        self.left_zadel.setGeometry(QtCore.QRect(660, 290, 101, 31))
        self.left_zadel.setAutoRepeat(False)
        self.left_zadel.setObjectName("left_zadel")
        self.right_zadel = QtWidgets.QPushButton(self.centralwidget)
        self.right_zadel.setGeometry(QtCore.QRect(660, 340, 101, 31))
        self.right_zadel.setAutoRepeat(False)
        self.right_zadel.setObjectName("right_zadel")
        self.dual_zadel = QtWidgets.QPushButton(self.centralwidget)
        self.dual_zadel.setGeometry(QtCore.QRect(660, 390, 101, 31))
        self.dual_zadel.setAutoRepeat(False)
        self.dual_zadel.setObjectName("dual_zadel")
        self.Uzli_table = QtWidgets.QTextEdit(self.centralwidget)
        self.Uzli_table.setGeometry(QtCore.QRect(10, 50, 201, 191))
        self.Uzli_table.setObjectName("Uzli_table")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 50, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 110, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 170, 81, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 180, 71, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 10, 211, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 20, 191, 16))
        self.label_10.setObjectName("label_10")
        self.Ster_table_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Ster_table_3.setGeometry(QtCore.QRect(310, 50, 201, 31))
        self.Ster_table_3.setObjectName("Ster_table_3")
        self.Ster_table_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.Ster_table_4.setGeometry(QtCore.QRect(310, 110, 201, 31))
        self.Ster_table_4.setObjectName("Ster_table_4")
        self.Ster_table_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.Ster_table_5.setGeometry(QtCore.QRect(310, 170, 201, 31))
        self.Ster_table_5.setObjectName("Ster_table_5")
        self.Sili_table_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Sili_table_1.setGeometry(QtCore.QRect(590, 50, 201, 31))
        self.Sili_table_1.setObjectName("Sili_table_1")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 50, 61, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(530, 60, 41, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(540, 100, 31, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(520, 110, 61, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(530, 170, 61, 20))
        self.label_15.setObjectName("label_15")
        self.Sili_table_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Sili_table_2.setGeometry(QtCore.QRect(590, 110, 201, 31))
        self.Sili_table_2.setObjectName("Sili_table_2")
        self.Sili_table_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Sili_table_3.setGeometry(QtCore.QRect(590, 170, 201, 31))
        self.Sili_table_3.setObjectName("Sili_table_3")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(600, 10, 161, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(630, 30, 91, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(520, 120, 61, 20))
        self.label_18.setObjectName("label_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_rasschet_2 = QtWidgets.QMenu(self.menubar)
        self.menu_rasschet_2.setObjectName("menu_rasschet_2")
        self.menu_info = QtWidgets.QMenu(self.menubar)
        self.menu_info.setObjectName("menu_info")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu_rasschet = QtWidgets.QAction(MainWindow)
        self.menu_rasschet.setObjectName("menu_rasschet")
        self.menu_help = QtWidgets.QAction(MainWindow)
        self.menu_help.setObjectName("menu_help")
        self.menu_about = QtWidgets.QAction(MainWindow)
        self.menu_about.setObjectName("menu_about")
        self.menu_save = QtWidgets.QAction(MainWindow)
        self.menu_save.setWhatsThis("")
        self.menu_save.setObjectName("menu_save")
        self.menu_open = QtWidgets.QAction(MainWindow)
        self.menu_open.setObjectName("menu_open")
        self.menu_rasschet_2.addAction(self.menu_rasschet)
        self.menu_info.addAction(self.menu_help)
        self.menu_info.addSeparator()
        self.menu_info.addAction(self.menu_about)
        self.menu_file.addAction(self.menu_save)
        self.menu_file.addAction(self.menu_open)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_rasschet_2.menuAction())
        self.menubar.addAction(self.menu_info.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sapr_P"))
        self.Uzli.setText(_translate("MainWindow", "Узлы:"))
        self.Sterjni.setText(_translate("MainWindow", "Стержни:"))
        self.refresh.setText(_translate("MainWindow", "Отрисовка"))
        self.Sili.setText(_translate("MainWindow", "Силы:"))
        self.left_zadel.setText(_translate("MainWindow", "Левая заделка"))
        self.right_zadel.setText(_translate("MainWindow", "Правая заделка"))
        self.dual_zadel.setText(_translate("MainWindow", "Обе заделки"))
        self.label.setText(_translate("MainWindow", "введите координаты Х"))
        self.label_2.setText(_translate("MainWindow", " узлов через пробел"))
        self.label_5.setText(_translate("MainWindow", "Площадь:"))
        self.label_6.setText(_translate("MainWindow", "Упругость:"))
        self.label_7.setText(_translate("MainWindow", "Максимальное"))
        self.label_8.setText(_translate("MainWindow", "напряжение:"))
        self.label_9.setText(_translate("MainWindow", "(ввод для каждого узла соотв значения"))
        self.label_10.setText(_translate("MainWindow", "в соотв строку, разделяя пробелом)"))
        self.label_11.setText(_translate("MainWindow", "Стержень/"))
        self.label_12.setText(_translate("MainWindow", "узел:"))
        self.label_13.setText(_translate("MainWindow", "Тип:"))
        self.label_14.setText(_translate("MainWindow", "Сосред (1)"))
        self.label_15.setText(_translate("MainWindow", "Значение:"))
        self.label_16.setText(_translate("MainWindow", "ввод указанных параметров"))
        self.label_17.setText(_translate("MainWindow", " через пробел"))
        self.label_18.setText(_translate("MainWindow", "Распред (2)"))
        self.menu_rasschet_2.setTitle(_translate("MainWindow", "Рассчет"))
        self.menu_info.setTitle(_translate("MainWindow", "Информация"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Сохранить"))
        self.action_2.setText(_translate("MainWindow", "Открыть"))
        self.menu_rasschet.setText(_translate("MainWindow", "Рассчет"))
        self.menu_rasschet.setStatusTip(_translate("MainWindow", "Рассчитать нагрузки"))
        self.menu_rasschet.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.menu_help.setText(_translate("MainWindow", "Помощь"))
        self.menu_about.setText(_translate("MainWindow", "О разработчике"))
        self.menu_save.setText(_translate("MainWindow", "Сохранить"))
        self.menu_save.setIconText(_translate("MainWindow", "Сохранить"))
        self.menu_save.setToolTip(_translate("MainWindow", "Сохранить"))
        self.menu_save.setStatusTip(_translate("MainWindow", "Сохранить файл"))
        self.menu_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menu_open.setText(_translate("MainWindow", "Открыть"))
        self.menu_open.setStatusTip(_translate("MainWindow", "Открыть файл"))
        self.menu_open.setShortcut(_translate("MainWindow", "Ctrl+O"))

