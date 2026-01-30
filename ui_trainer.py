# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(548, 408)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dataset_zip_path = QLineEdit(self.centralwidget)
        self.dataset_zip_path.setObjectName(u"dataset_zip_path")
        self.dataset_zip_path.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.dataset_zip_path)

        self.dataset_zip_path_select = QPushButton(self.centralwidget)
        self.dataset_zip_path_select.setObjectName(u"dataset_zip_path_select")

        self.horizontalLayout_2.addWidget(self.dataset_zip_path_select)

        self.dataset_zip_path_unzip = QPushButton(self.centralwidget)
        self.dataset_zip_path_unzip.setObjectName(u"dataset_zip_path_unzip")

        self.horizontalLayout_2.addWidget(self.dataset_zip_path_unzip)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dataset_data_yaml_path = QLineEdit(self.centralwidget)
        self.dataset_data_yaml_path.setObjectName(u"dataset_data_yaml_path")
        self.dataset_data_yaml_path.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.dataset_data_yaml_path)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.model_weight_dir = QLineEdit(self.centralwidget)
        self.model_weight_dir.setObjectName(u"model_weight_dir")
        self.model_weight_dir.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.model_weight_dir)

        self.model_weight_dir_select = QPushButton(self.centralwidget)
        self.model_weight_dir_select.setObjectName(u"model_weight_dir_select")

        self.horizontalLayout_4.addWidget(self.model_weight_dir_select)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.model_prefix = QLineEdit(self.centralwidget)
        self.model_prefix.setObjectName(u"model_prefix")

        self.horizontalLayout.addWidget(self.model_prefix)

        self.model_gen = QComboBox(self.centralwidget)
        self.model_gen.addItem("")
        self.model_gen.addItem("")
        self.model_gen.setObjectName(u"model_gen")

        self.horizontalLayout.addWidget(self.model_gen)

        self.model_size = QComboBox(self.centralwidget)
        self.model_size.addItem("")
        self.model_size.addItem("")
        self.model_size.addItem("")
        self.model_size.addItem("")
        self.model_size.addItem("")
        self.model_size.setObjectName(u"model_size")

        self.horizontalLayout.addWidget(self.model_size)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.model_suffix = QLineEdit(self.centralwidget)
        self.model_suffix.setObjectName(u"model_suffix")
        self.model_suffix.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.model_suffix)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.batch_size = QLineEdit(self.centralwidget)
        self.batch_size.setObjectName(u"batch_size")

        self.gridLayout.addWidget(self.batch_size, 1, 1, 1, 1)

        self.img_size = QLineEdit(self.centralwidget)
        self.img_size.setObjectName(u"img_size")

        self.gridLayout.addWidget(self.img_size, 1, 2, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.epochs = QLineEdit(self.centralwidget)
        self.epochs.setObjectName(u"epochs")

        self.gridLayout.addWidget(self.epochs, 1, 0, 1, 1)

        self.project = QLineEdit(self.centralwidget)
        self.project.setObjectName(u"project")

        self.gridLayout.addWidget(self.project, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_train = QCommandLinkButton(self.centralwidget)
        self.btn_train.setObjectName(u"btn_train")

        self.horizontalLayout_5.addWidget(self.btn_train)

        self.btn_pause = QCommandLinkButton(self.centralwidget)
        self.btn_pause.setObjectName(u"btn_pause")

        self.horizontalLayout_5.addWidget(self.btn_pause)

        self.btn_stop = QCommandLinkButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout_5.addWidget(self.btn_stop)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 548, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u538b\u7f29\u5305", None))
        self.dataset_zip_path.setText(QCoreApplication.translate("MainWindow", u"D:/wk/Codehub/0/phimate/.cache/chair_det.v5i.yolov11.zip", None))
        self.dataset_zip_path_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.dataset_zip_path_unzip.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u538b\u5e76\u5904\u7406", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u914d\u7f6e\u6587\u4ef6", None))
        self.dataset_data_yaml_path.setText(QCoreApplication.translate("MainWindow", u"D:/wk/Codehub/0/phimate/.cache/chair_det.v5i.yolov11/data.yaml", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u6587\u4ef6\u76ee\u5f55", None))
        self.model_weight_dir.setText(QCoreApplication.translate("MainWindow", u"data/weights", None))
        self.model_weight_dir_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u5c3a\u5bf8", None))
        self.model_prefix.setText(QCoreApplication.translate("MainWindow", u"yolo", None))
        self.model_gen.setItemText(0, QCoreApplication.translate("MainWindow", u"11", None))
        self.model_gen.setItemText(1, QCoreApplication.translate("MainWindow", u"12", None))

        self.model_size.setItemText(0, QCoreApplication.translate("MainWindow", u"n", None))
        self.model_size.setItemText(1, QCoreApplication.translate("MainWindow", u"s", None))
        self.model_size.setItemText(2, QCoreApplication.translate("MainWindow", u"m", None))
        self.model_size.setItemText(3, QCoreApplication.translate("MainWindow", u"l", None))
        self.model_size.setItemText(4, QCoreApplication.translate("MainWindow", u"x", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.model_suffix.setText(QCoreApplication.translate("MainWindow", u"seg", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"batch_size", None))
        self.batch_size.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.img_size.setText(QCoreApplication.translate("MainWindow", u"640", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"project", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"img_size", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"epochs", None))
        self.epochs.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.project.setText(QCoreApplication.translate("MainWindow", u"chair_det", None))
        self.btn_train.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bad\u7ec3", None))
        self.btn_pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u4efb\u52a1", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5f03\u4efb\u52a1", None))
    # retranslateUi

