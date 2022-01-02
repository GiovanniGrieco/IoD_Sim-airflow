# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'script.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtWidgets import *


class Ui_script_widget(object):
    def setupUi(self, script_widget):
        if not script_widget.objectName():
            script_widget.setObjectName(u"script_widget")
        script_widget.resize(1223, 876)
        self.gridLayout_4 = QGridLayout(script_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter_3 = QSplitter(script_widget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)

        self.splitter_3.addWidget(self.splitter)
        self.contents_widget = QWidget(self.splitter_3)
        self.contents_widget.setObjectName(u"contents_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contents_widget.sizePolicy().hasHeightForWidth())
        self.contents_widget.setSizePolicy(sizePolicy)
        self.contents_widget.setMinimumSize(QSize(200, 0))

        self.verticalLayout = QVBoxLayout(self.contents_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Settings Box Layout
        self.settings_groupBox = QGroupBox(self.contents_widget)
        self.settings_groupBox.setObjectName(u"settings_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.settings_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_IoDSimLocation = QHBoxLayout()

        # IoD Sim Location Label
        self.horizontalLayout_IoDSimLocation.setObjectName(u"horizontalLayout")
        self.label_IoDSimLocation = QLabel(self.settings_groupBox)
        self.label_IoDSimLocation.setObjectName(u"label_IoDSimLocation")
        self.horizontalLayout_IoDSimLocation.addWidget(self.label_IoDSimLocation)

        # IoD Sim Location Button
        self.pushButton_IoDSimLocation = QPushButton(self.settings_groupBox)
        self.pushButton_IoDSimLocation.setObjectName(u"pushButton_IoDSimLocation")

        self.horizontalLayout_IoDSimLocation.addWidget(self.pushButton_IoDSimLocation)

        self.verticalLayout_4.addLayout(self.horizontalLayout_IoDSimLocation)
        # / IoD Sim Location

        self.verticalLayout.addWidget(self.settings_groupBox)

        # IoD Sim Toolbox
        self.groupBox_IoDSimTools = QGroupBox(self.contents_widget)
        self.groupBox_IoDSimTools.setObjectName(u"groupBox_IoDSimTools")

        self.gridLayout_IoDSimTools = QGridLayout(self.groupBox_IoDSimTools)
        self.gridLayout_IoDSimTools.setObjectName(u"gridLayout_IoDSimTools")

        # Build Button
        self.button_Build_IoDSimTools = QPushButton(self.groupBox_IoDSimTools)
        self.button_Build_IoDSimTools.setObjectName(u"button_Build_IoDSimTools")
        self.gridLayout_IoDSimTools.addWidget(self.button_Build_IoDSimTools, 0, 0, 1, 1)

        # Run Button
        self.button_Run_IoDSimTools = QPushButton(self.groupBox_IoDSimTools)
        self.button_Run_IoDSimTools.setObjectName(u"button_Run_IoDSimTools")
        self.gridLayout_IoDSimTools.addWidget(self.button_Run_IoDSimTools, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.groupBox_IoDSimTools)
        # / IoD Sim Toolbox

        self.variables_group_box = QGroupBox(self.contents_widget)
        self.variables_group_box.setObjectName(u"variables_group_box")
        self.gridLayout_3 = QGridLayout(self.variables_group_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.variables_scrollArea = QScrollArea(self.variables_group_box)
        self.variables_scrollArea.setObjectName(u"variables_scrollArea")
        self.variables_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 628, 593))
        self.variables_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.variables_scrollArea, 0, 0, 1, 1)

        self.add_variable_push_button = QPushButton(self.variables_group_box)
        self.add_variable_push_button.setObjectName(u"add_variable_push_button")

        self.gridLayout_3.addWidget(self.add_variable_push_button, 2, 0, 1, 1)

        self.new_var_name_lineEdit = QLineEdit(self.variables_group_box)
        self.new_var_name_lineEdit.setObjectName(u"new_var_name_lineEdit")

        self.gridLayout_3.addWidget(self.new_var_name_lineEdit, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.variables_group_box)

        self.splitter_3.addWidget(self.contents_widget)

        self.gridLayout_4.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.retranslateUi(script_widget)

        QMetaObject.connectSlotsByName(script_widget)
    # setupUi

    def retranslateUi(self, script_widget):
        script_widget.setWindowTitle(QCoreApplication.translate("script_widget", u"Form", None))
        self.settings_groupBox.setTitle(QCoreApplication.translate("script_widget", u"Settings", None))
        self.label_IoDSimLocation.setText(QCoreApplication.translate("script_widget", u"IoD Sim Location", None))
        self.pushButton_IoDSimLocation.setText(QCoreApplication.translate("script_widget", u"Select Dir", None))
        self.variables_group_box.setTitle(QCoreApplication.translate("script_widget", u"Variables", None))
        self.add_variable_push_button.setText(QCoreApplication.translate("script_widget", u"add", None))
        self.new_var_name_lineEdit.setPlaceholderText(QCoreApplication.translate("script_widget", u"new var name", None))
        self.groupBox_IoDSimTools.setTitle(QCoreApplication.translate("script_widget", u"IoD Sim Tools", None))
        self.button_Build_IoDSimTools.setText(QCoreApplication.translate("script_widget", u"Build", None))
        self.button_Run_IoDSimTools.setText(QCoreApplication.translate("script_widget", u"Run", None))
    # retranslateUi

