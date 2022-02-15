# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'adminUI.ui'
##
# Created by: Qt User Interface Compiler version 6.2.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QRadioButton, QScrollArea, QSizePolicy, QWidget, QVBoxLayout)


class AccountUI(object):
    def setupUi(self, account_settings_form):
        if not account_settings_form.objectName():
            account_settings_form.setObjectName(u"account_settings_form")
        account_settings_form.resize(1520, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            account_settings_form.sizePolicy().hasHeightForWidth())
        account_settings_form.setSizePolicy(sizePolicy)
        account_settings_form.setAutoFillBackground(False)
        account_settings_form.setStyleSheet(u"background-color:#F8F8FF;")
        self.account_settings_label = QLabel(account_settings_form)
        self.account_settings_label.setObjectName(u"account_settings_label")
        self.account_settings_label.setGeometry(QRect(100, 60, 701, 91))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(72)
        font.setBold(True)
        self.account_settings_label.setFont(font)
        self.account_settings_label.setStyleSheet(u"color:#1A374D;")
        self.account_settings_label.setMargin(-2)
        self.employee_acc_list_widget = QWidget(account_settings_form)
        self.employee_acc_list_widget.setObjectName(
            u"employee_acc_list_widget")
        self.employee_acc_list_widget.setGeometry(QRect(100, 222, 380, 765))
        self.employee_acc_list_widget.setStyleSheet(u"background-color:#ffffff;\n"
                                                    "border-radius: 10px;")
        self.employee_acc_list_label = QLabel(self.employee_acc_list_widget)
        self.employee_acc_list_label.setObjectName(u"employee_acc_list_label")
        self.employee_acc_list_label.setGeometry(QRect(0, 0, 380, 80))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.employee_acc_list_label.setFont(font1)
        self.employee_acc_list_label.setStyleSheet(u"color:#1A374D;")
        self.employee_acc_list_label.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.employee_acc_list_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 80, 380, 685))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("padding:0px; margin:0px;")
        self.scrollArea_widget = QWidget()
        self.scrollArea_widget.setObjectName(u"scrollArea_widget")
        self.scrollArea_widget.setGeometry(QRect(0, 0, 380, 685))
        self.scrollArea_widget.setStyleSheet(
            "padding:0px; margin:0px; background-color:#006700")
        self.scrollArea.setWidget(self.scrollArea_widget)
        self.create_new_acc_widget = QWidget(account_settings_form)
        self.create_new_acc_widget.setObjectName(u"create_new_acc_widget")
        self.create_new_acc_widget.setGeometry(QRect(560, 220, 850, 350))
        self.create_new_acc_widget.setStyleSheet(u"background-color:#ffffff;\n"
                                                 "border-radius: 10px;")
        self.create_new_acc_label = QLabel(self.create_new_acc_widget)
        self.create_new_acc_label.setObjectName(u"create_new_acc_label")
        self.create_new_acc_label.setGeometry(QRect(40, 30, 271, 41))
        self.create_new_acc_label.setFont(font1)
        self.create_new_acc_label.setStyleSheet(u"color:#1A374D;")
        self.create_first_name_label = QLabel(self.create_new_acc_widget)
        self.create_first_name_label.setObjectName(u"create_first_name_label")
        self.create_first_name_label.setGeometry(QRect(40, 90, 100, 30))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(18)
        self.create_first_name_label.setFont(font2)
        self.create_first_name_label.setStyleSheet(u"color:#1A374D;")
        self.create_last_name_label = QLabel(self.create_new_acc_widget)
        self.create_last_name_label.setObjectName(u"create_last_name_label")
        self.create_last_name_label.setGeometry(QRect(40, 140, 100, 30))
        self.create_last_name_label.setFont(font2)
        self.create_last_name_label.setStyleSheet(u"color:#1A374D;")
        self.create_username_label = QLabel(self.create_new_acc_widget)
        self.create_username_label.setObjectName(u"create_username_label")
        self.create_username_label.setGeometry(QRect(40, 190, 100, 30))
        self.create_username_label.setFont(font2)
        self.create_username_label.setStyleSheet(u"color:#1A374D;")
        self.password_label = QLabel(self.create_new_acc_widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(40, 240, 100, 30))
        self.password_label.setFont(font2)
        self.password_label.setStyleSheet(u"color:#1A374D;")
        self.usin_create_first_name = QLineEdit(self.create_new_acc_widget)
        self.usin_create_first_name.setObjectName(u"usin_create_first_name")
        self.usin_create_first_name.setGeometry(QRect(160, 90, 620, 30))
        self.usin_create_first_name.setStyleSheet(u"background-color: #DDDDDD;\n"
                                                  "border-radius: 0px;")
        self.btn_create_admin = QRadioButton(self.create_new_acc_widget)
        self.btn_create_admin.setObjectName(u"btn_create_admin")
        self.btn_create_admin.setEnabled(True)
        self.btn_create_admin.setGeometry(QRect(40, 290, 211, 20))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.btn_create_admin.setFont(font3)
        self.btn_create_admin.setLayoutDirection(Qt.RightToLeft)
        self.btn_create_admin.setStyleSheet(u"color:#1A374D;")
        self.usin_create_last_name = QLineEdit(self.create_new_acc_widget)
        self.usin_create_last_name.setObjectName(u"usin_create_last_name")
        self.usin_create_last_name.setGeometry(QRect(160, 140, 620, 30))
        self.usin_create_last_name.setStyleSheet(u"background-color: #DDDDDD;\n"
                                                 "border-radius: 0px;")
        self.usin_create_password = QLineEdit(self.create_new_acc_widget)
        self.usin_create_password.setObjectName(u"usin_create_password")
        self.usin_create_password.setGeometry(QRect(160, 240, 280, 30))
        self.usin_create_password.setStyleSheet(u"background-color: #DDDDDD;\n"
                                                "border-radius: 0px;")
        self.usin_create_confirm = QLineEdit(self.create_new_acc_widget)
        self.usin_create_confirm.setObjectName(u"usin_create_confirm")
        self.usin_create_confirm.setGeometry(QRect(570, 240, 210, 30))
        self.usin_create_confirm.setStyleSheet(u"background-color: #DDDDDD;\n"
                                               "border-radius: 0px;")
        self.create_confirm_label = QLabel(self.create_new_acc_widget)
        self.create_confirm_label.setObjectName(u"create_confirm_label")
        self.create_confirm_label.setGeometry(QRect(470, 240, 81, 30))
        self.create_confirm_label.setFont(font2)
        self.create_confirm_label.setStyleSheet(u"color:#1A374D;")
        self.btn_create_account = QPushButton(self.create_new_acc_widget)
        self.btn_create_account.setObjectName(u"btn_create_account")
        self.btn_create_account.setGeometry(QRect(580, 290, 200, 30))
        self.btn_create_account.setFont(font2)
        self.btn_create_account.setStyleSheet(u"background: #FDCB6E;\n"
                                              "border-radius: 10px;")
        self.create_username = QLabel(self.create_new_acc_widget)
        self.create_username.setObjectName(u"create_username")
        self.create_username.setGeometry(QRect(160, 190, 281, 30))
        self.create_username.setFont(font2)
        self.create_username.setStyleSheet(u"color:#1A374D;")
        self.edit_employee_acc_widget = QWidget(account_settings_form)
        self.edit_employee_acc_widget.setObjectName(
            u"edit_employee_acc_widget")
        self.edit_employee_acc_widget.setGeometry(QRect(560, 638, 850, 350))
        self.edit_employee_acc_widget.setStyleSheet(u"background-color:#ffffff;\n"
                                                    "border-radius: 10px;")
        self.edit_employee_acc_label = QLabel(self.edit_employee_acc_widget)
        self.edit_employee_acc_label.setObjectName(u"edit_employee_acc_label")
        self.edit_employee_acc_label.setGeometry(QRect(40, 30, 301, 41))
        self.edit_employee_acc_label.setFont(font1)
        self.edit_employee_acc_label.setStyleSheet(u"color:#1A374D;")
        self.edit_first_name_label = QLabel(self.edit_employee_acc_widget)
        self.edit_first_name_label.setObjectName(u"edit_first_name_label")
        self.edit_first_name_label.setGeometry(QRect(40, 100, 100, 30))
        self.edit_first_name_label.setFont(font2)
        self.edit_first_name_label.setStyleSheet(u"color:#1A374D;")
        self.edit_last_name_label = QLabel(self.edit_employee_acc_widget)
        self.edit_last_name_label.setObjectName(u"edit_last_name_label")
        self.edit_last_name_label.setGeometry(QRect(40, 150, 100, 30))
        self.edit_last_name_label.setFont(font2)
        self.edit_last_name_label.setStyleSheet(u"color:#1A374D;")
        self.edit_username_label = QLabel(self.edit_employee_acc_widget)
        self.edit_username_label.setObjectName(u"edit_username_label")
        self.edit_username_label.setGeometry(QRect(40, 200, 100, 30))
        self.edit_username_label.setFont(font2)
        self.edit_username_label.setStyleSheet(u"color:#1A374D;")
        self.edit_change_password_label = QLabel(self.edit_employee_acc_widget)
        self.edit_change_password_label.setObjectName(
            u"edit_change_password_label")
        self.edit_change_password_label.setGeometry(QRect(320, 200, 181, 30))
        self.edit_change_password_label.setFont(font2)
        self.edit_change_password_label.setStyleSheet(u"color:#1A374D;")
        self.usin_edit_first_name = QLineEdit(self.edit_employee_acc_widget)
        self.usin_edit_first_name.setObjectName(u"usin_edit_first_name")
        self.usin_edit_first_name.setGeometry(QRect(160, 100, 620, 30))
        self.usin_edit_first_name.setStyleSheet(u"background-color: #DDDDDD;\n"
                                                "border-radius: 0px;")
        self.usin_edit_last_name = QLineEdit(self.edit_employee_acc_widget)
        self.usin_edit_last_name.setObjectName(u"usin_edit_last_name")
        self.usin_edit_last_name.setGeometry(QRect(160, 150, 620, 30))
        self.usin_edit_last_name.setStyleSheet(u"background-color: #DDDDDD;\n"
                                               "border-radius: 0px;")
        self.usin_edit_change_password = QLineEdit(
            self.edit_employee_acc_widget)
        self.usin_edit_change_password.setObjectName(
            u"usin_edit_change_password")
        self.usin_edit_change_password.setGeometry(QRect(515, 200, 265, 30))
        self.usin_edit_change_password.setStyleSheet(u"background-color: #DDDDDD;\n"
                                                     "border-radius: 0px;")
        self.usin_edit_password = QLineEdit(self.edit_employee_acc_widget)
        self.usin_edit_password.setObjectName(u"usin_edit_password")
        self.usin_edit_password.setGeometry(QRect(160, 280, 265, 30))
        self.usin_edit_password.setStyleSheet(u"background-color: #DDDDDD;\n"
                                              "border-radius: 0px;")
        self.edit_password_label = QLabel(self.edit_employee_acc_widget)
        self.edit_password_label.setObjectName(u"edit_password_label")
        self.edit_password_label.setGeometry(QRect(40, 280, 101, 30))
        self.edit_password_label.setFont(font2)
        self.edit_password_label.setStyleSheet(u"color:#1A374D;")
        self.btn_save_changes = QPushButton(self.edit_employee_acc_widget)
        self.btn_save_changes.setObjectName(u"btn_save_changes")
        self.btn_save_changes.setGeometry(QRect(610, 280, 170, 30))
        self.btn_save_changes.setFont(font2)
        self.btn_save_changes.setStyleSheet(u"background: #FDCB6E;\n"
                                            "border-radius: 10px;")
        self.edit_description_label = QLabel(self.edit_employee_acc_widget)
        self.edit_description_label.setObjectName(u"edit_description_label")
        self.edit_description_label.setGeometry(QRect(40, 70, 501, 16))
        self.edit_description_label.setStyleSheet(u"color:#1A374D;")
        self.edit_username = QLabel(self.edit_employee_acc_widget)
        self.edit_username.setObjectName(u"edit_username")
        self.edit_username.setGeometry(QRect(160, 200, 141, 30))
        self.edit_username.setFont(font2)
        self.edit_username.setStyleSheet(u"color:#1A374D;")
        self.edit_admin_confirm_label = QLabel(self.edit_employee_acc_widget)
        self.edit_admin_confirm_label.setObjectName(
            u"edit_admin_confirm_label")
        self.edit_admin_confirm_label.setGeometry(QRect(40, 255, 501, 16))
        self.edit_admin_confirm_label.setStyleSheet(u"color:#1A374D;")
        self.btn_delete = QPushButton(self.edit_employee_acc_widget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(460, 280, 140, 30))
        self.btn_delete.setFont(font2)
        self.btn_delete.setStyleSheet(u"background: #FDCB6E;\n"
                                      "border-radius: 10px;")
        QWidget.setTabOrder(self.usin_create_first_name,
                            self.usin_create_last_name)
        QWidget.setTabOrder(self.usin_create_last_name,
                            self.usin_create_password)
        QWidget.setTabOrder(self.usin_create_password, self.btn_create_admin)
        QWidget.setTabOrder(self.btn_create_admin, self.usin_create_confirm)
        QWidget.setTabOrder(self.usin_create_confirm, self.btn_create_account)
        QWidget.setTabOrder(self.btn_create_account, self.usin_edit_first_name)
        QWidget.setTabOrder(self.usin_edit_first_name,
                            self.usin_edit_last_name)
        QWidget.setTabOrder(self.usin_edit_last_name,
                            self.usin_edit_change_password)
        QWidget.setTabOrder(self.usin_edit_change_password,
                            self.usin_edit_password)
        QWidget.setTabOrder(self.usin_edit_password, self.btn_save_changes)

        self.retranslateUi(account_settings_form)

        QMetaObject.connectSlotsByName(account_settings_form)
    # setupUi

    def retranslateUi(self, account_settings_form):
        account_settings_form.setWindowTitle(
            QCoreApplication.translate("account_settings_form", u"Form", None))
        self.account_settings_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Account Settings ", None))
        self.employee_acc_list_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Employee Account List", None))
        self.create_new_acc_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Create New Account", None))
        self.create_first_name_label.setText(QCoreApplication.translate(
            "account_settings_form", u"First Name:", None))
        self.create_last_name_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Last Name:", None))
        self.create_username_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Username:", None))
        self.password_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Password:", None))
        self.btn_create_admin.setText(QCoreApplication.translate(
            "account_settings_form", u"Create as admin account ", None))
        self.create_confirm_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Confirm:", None))
        self.btn_create_account.setText(QCoreApplication.translate(
            "account_settings_form", u"Create Account", None))
        self.create_username.setText("")
        self.edit_employee_acc_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Edit Employee Account", None))
        self.edit_first_name_label.setText(QCoreApplication.translate(
            "account_settings_form", u"First Name:", None))
        self.edit_last_name_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Last Name:", None))
        self.edit_username_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Username:", None))
        self.edit_change_password_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Change Password:", None))
        self.usin_edit_change_password.setText("")
        self.usin_edit_password.setText("")
        self.edit_password_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Password:", None))
        self.btn_save_changes.setText(QCoreApplication.translate(
            "account_settings_form", u"Save Changes", None))
        self.edit_description_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Click on an employee card on the left to select an employee account", None))
        self.edit_username.setText("")
        self.edit_admin_confirm_label.setText(QCoreApplication.translate(
            "account_settings_form", u"Admin Confirmation:", None))
        self.btn_delete.setText(QCoreApplication.translate(
            "account_settings_form", u"Delete", None))
    # retranslateUi
