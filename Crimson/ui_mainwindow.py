# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 750)
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_afe_data_channel = QLabel(self.centralwidget)
        self.label_afe_data_channel.setObjectName(u"label_afe_data_channel")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.label_afe_data_channel.setFont(font1)

        self.gridLayout_2.addWidget(self.label_afe_data_channel, 1, 0, 1, 2)

        self.combo_box_afe_data_channel = QComboBox(self.centralwidget)
        self.combo_box_afe_data_channel.setObjectName(u"combo_box_afe_data_channel")
        self.combo_box_afe_data_channel.setFont(font)

        self.gridLayout_2.addWidget(self.combo_box_afe_data_channel, 1, 2, 1, 3)

        self.combo_box_afe_sample_rate = QComboBox(self.centralwidget)
        self.combo_box_afe_sample_rate.setObjectName(u"combo_box_afe_sample_rate")
        self.combo_box_afe_sample_rate.setFont(font)

        self.gridLayout_2.addWidget(self.combo_box_afe_sample_rate, 2, 2, 1, 3)

        self.label_afe_sample_rate = QLabel(self.centralwidget)
        self.label_afe_sample_rate.setObjectName(u"label_afe_sample_rate")
        self.label_afe_sample_rate.setFont(font1)

        self.gridLayout_2.addWidget(self.label_afe_sample_rate, 2, 0, 1, 2)

        self.combo_box_afe_rld_channel = QComboBox(self.centralwidget)
        self.combo_box_afe_rld_channel.setObjectName(u"combo_box_afe_rld_channel")
        self.combo_box_afe_rld_channel.setFont(font)

        self.gridLayout_2.addWidget(self.combo_box_afe_rld_channel, 4, 2, 1, 3)

        self.label_afe_lead_off_option = QLabel(self.centralwidget)
        self.label_afe_lead_off_option.setObjectName(u"label_afe_lead_off_option")
        self.label_afe_lead_off_option.setFont(font1)

        self.gridLayout_2.addWidget(self.label_afe_lead_off_option, 3, 0, 1, 2)

        self.combo_box_afe_lead_off_option = QComboBox(self.centralwidget)
        self.combo_box_afe_lead_off_option.setObjectName(u"combo_box_afe_lead_off_option")
        self.combo_box_afe_lead_off_option.setFont(font)

        self.gridLayout_2.addWidget(self.combo_box_afe_lead_off_option, 3, 2, 1, 3)

        self.label_afe_rld_channel = QLabel(self.centralwidget)
        self.label_afe_rld_channel.setObjectName(u"label_afe_rld_channel")
        self.label_afe_rld_channel.setFont(font1)

        self.gridLayout_2.addWidget(self.label_afe_rld_channel, 4, 0, 1, 2)

        self.label_afe_lead_off_channel = QLabel(self.centralwidget)
        self.label_afe_lead_off_channel.setObjectName(u"label_afe_lead_off_channel")
        self.label_afe_lead_off_channel.setFont(font1)

        self.gridLayout_2.addWidget(self.label_afe_lead_off_channel, 5, 0, 1, 2)

        self.combo_box_afe_lead_off_channel = QComboBox(self.centralwidget)
        self.combo_box_afe_lead_off_channel.setObjectName(u"combo_box_afe_lead_off_channel")
        self.combo_box_afe_lead_off_channel.setFont(font)

        self.gridLayout_2.addWidget(self.combo_box_afe_lead_off_channel, 5, 2, 1, 3)

        self.button_send_afe = QPushButton(self.centralwidget)
        self.button_send_afe.setObjectName(u"button_send_afe")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(13)
        font2.setItalic(False)
        self.button_send_afe.setFont(font2)

        self.gridLayout_2.addWidget(self.button_send_afe, 6, 0, 1, 5)

        self.label_afe = QLabel(self.centralwidget)
        self.label_afe.setObjectName(u"label_afe")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_afe.setFont(font3)

        self.gridLayout_2.addWidget(self.label_afe, 0, 0, 1, 5)


        self.gridLayout_7.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_acc_option = QLabel(self.centralwidget)
        self.label_acc_option.setObjectName(u"label_acc_option")
        self.label_acc_option.setFont(font1)

        self.gridLayout_3.addWidget(self.label_acc_option, 1, 0, 1, 1)

        self.combo_box_acc_option = QComboBox(self.centralwidget)
        self.combo_box_acc_option.setObjectName(u"combo_box_acc_option")
        self.combo_box_acc_option.setFont(font)

        self.gridLayout_3.addWidget(self.combo_box_acc_option, 1, 1, 1, 2)

        self.label_acc_sample_rate = QLabel(self.centralwidget)
        self.label_acc_sample_rate.setObjectName(u"label_acc_sample_rate")
        self.label_acc_sample_rate.setFont(font1)

        self.gridLayout_3.addWidget(self.label_acc_sample_rate, 2, 0, 1, 1)

        self.combo_box_acc_sample_rate = QComboBox(self.centralwidget)
        self.combo_box_acc_sample_rate.setObjectName(u"combo_box_acc_sample_rate")
        self.combo_box_acc_sample_rate.setFont(font)

        self.gridLayout_3.addWidget(self.combo_box_acc_sample_rate, 2, 1, 1, 2)

        self.button_send_acc = QPushButton(self.centralwidget)
        self.button_send_acc.setObjectName(u"button_send_acc")
        self.button_send_acc.setFont(font2)

        self.gridLayout_3.addWidget(self.button_send_acc, 3, 0, 1, 3)

        self.label_acc = QLabel(self.centralwidget)
        self.label_acc.setObjectName(u"label_acc")
        self.label_acc.setFont(font3)

        self.gridLayout_3.addWidget(self.label_acc, 0, 0, 1, 3)


        self.gridLayout_7.addLayout(self.gridLayout_3, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_hardware_revision = QLabel(self.centralwidget)
        self.label_hardware_revision.setObjectName(u"label_hardware_revision")
        self.label_hardware_revision.setFont(font2)

        self.gridLayout.addWidget(self.label_hardware_revision, 1, 0, 1, 1)

        self.label_firmware_revision_value = QLabel(self.centralwidget)
        self.label_firmware_revision_value.setObjectName(u"label_firmware_revision_value")
        self.label_firmware_revision_value.setFont(font2)

        self.gridLayout.addWidget(self.label_firmware_revision_value, 1, 3, 1, 1)

        self.label_manufacturer_value = QLabel(self.centralwidget)
        self.label_manufacturer_value.setObjectName(u"label_manufacturer_value")
        self.label_manufacturer_value.setFont(font2)

        self.gridLayout.addWidget(self.label_manufacturer_value, 0, 1, 1, 1)

        self.label_serial_number_value = QLabel(self.centralwidget)
        self.label_serial_number_value.setObjectName(u"label_serial_number_value")
        self.label_serial_number_value.setFont(font2)

        self.gridLayout.addWidget(self.label_serial_number_value, 0, 5, 1, 1)

        self.label_serial_number = QLabel(self.centralwidget)
        self.label_serial_number.setObjectName(u"label_serial_number")
        self.label_serial_number.setFont(font2)

        self.gridLayout.addWidget(self.label_serial_number, 0, 4, 1, 1)

        self.label_model_number = QLabel(self.centralwidget)
        self.label_model_number.setObjectName(u"label_model_number")
        self.label_model_number.setFont(font2)

        self.gridLayout.addWidget(self.label_model_number, 0, 2, 1, 1)

        self.label_firmware_revision = QLabel(self.centralwidget)
        self.label_firmware_revision.setObjectName(u"label_firmware_revision")
        self.label_firmware_revision.setFont(font2)

        self.gridLayout.addWidget(self.label_firmware_revision, 1, 2, 1, 1)

        self.label_manufacturer = QLabel(self.centralwidget)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        self.label_manufacturer.setFont(font2)

        self.gridLayout.addWidget(self.label_manufacturer, 0, 0, 1, 1)

        self.label_model_number_value = QLabel(self.centralwidget)
        self.label_model_number_value.setObjectName(u"label_model_number_value")
        self.label_model_number_value.setFont(font2)

        self.gridLayout.addWidget(self.label_model_number_value, 0, 3, 1, 1)

        self.label_hardware_revision_value = QLabel(self.centralwidget)
        self.label_hardware_revision_value.setObjectName(u"label_hardware_revision_value")
        self.label_hardware_revision_value.setFont(font2)

        self.gridLayout.addWidget(self.label_hardware_revision_value, 1, 1, 1, 1)

        self.button_rename = QPushButton(self.centralwidget)
        self.button_rename.setObjectName(u"button_rename")
        self.button_rename.setFont(font2)

        self.gridLayout.addWidget(self.button_rename, 1, 4, 1, 2)


        self.gridLayout_7.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_meditation_level = QLabel(self.centralwidget)
        self.label_meditation_level.setObjectName(u"label_meditation_level")
        self.label_meditation_level.setFont(font1)

        self.gridLayout_5.addWidget(self.label_meditation_level, 3, 0, 1, 3)

        self.label_meditation_level_value = QLabel(self.centralwidget)
        self.label_meditation_level_value.setObjectName(u"label_meditation_level_value")
        self.label_meditation_level_value.setFont(font1)

        self.gridLayout_5.addWidget(self.label_meditation_level_value, 3, 3, 1, 2)

        self.label_attention_level_value = QLabel(self.centralwidget)
        self.label_attention_level_value.setObjectName(u"label_attention_level_value")
        self.label_attention_level_value.setFont(font1)

        self.gridLayout_5.addWidget(self.label_attention_level_value, 2, 3, 1, 2)

        self.label_contact_value = QLabel(self.centralwidget)
        self.label_contact_value.setObjectName(u"label_contact_value")
        self.label_contact_value.setFont(font1)

        self.gridLayout_5.addWidget(self.label_contact_value, 1, 3, 1, 2)

        self.label_connectivity_value = QLabel(self.centralwidget)
        self.label_connectivity_value.setObjectName(u"label_connectivity_value")
        self.label_connectivity_value.setFont(font1)

        self.gridLayout_5.addWidget(self.label_connectivity_value, 0, 3, 1, 2)

        self.label_connectivity = QLabel(self.centralwidget)
        self.label_connectivity.setObjectName(u"label_connectivity")
        self.label_connectivity.setFont(font1)

        self.gridLayout_5.addWidget(self.label_connectivity, 0, 0, 1, 3)

        self.label_contact = QLabel(self.centralwidget)
        self.label_contact.setObjectName(u"label_contact")
        self.label_contact.setFont(font1)

        self.gridLayout_5.addWidget(self.label_contact, 1, 0, 1, 3)

        self.label_attention_level = QLabel(self.centralwidget)
        self.label_attention_level.setObjectName(u"label_attention_level")
        self.label_attention_level.setFont(font1)

        self.gridLayout_5.addWidget(self.label_attention_level, 2, 0, 1, 3)


        self.gridLayout_7.addLayout(self.gridLayout_5, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_led_color = QLabel(self.centralwidget)
        self.label_led_color.setObjectName(u"label_led_color")
        self.label_led_color.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_led_color)

        self.button_red = QPushButton(self.centralwidget)
        self.button_red.setObjectName(u"button_red")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_red.sizePolicy().hasHeightForWidth())
        self.button_red.setSizePolicy(sizePolicy)
        self.button_red.setFont(font2)

        self.horizontalLayout_3.addWidget(self.button_red)

        self.button_green = QPushButton(self.centralwidget)
        self.button_green.setObjectName(u"button_green")
        sizePolicy.setHeightForWidth(self.button_green.sizePolicy().hasHeightForWidth())
        self.button_green.setSizePolicy(sizePolicy)
        self.button_green.setFont(font2)

        self.horizontalLayout_3.addWidget(self.button_green)

        self.button_blue = QPushButton(self.centralwidget)
        self.button_blue.setObjectName(u"button_blue")
        sizePolicy.setHeightForWidth(self.button_blue.sizePolicy().hasHeightForWidth())
        self.button_blue.setSizePolicy(sizePolicy)
        self.button_blue.setFont(font2)

        self.horizontalLayout_3.addWidget(self.button_blue)

        self.button_collect_data = QPushButton(self.centralwidget)
        self.button_collect_data.setObjectName(u"button_collect_data")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_collect_data.sizePolicy().hasHeightForWidth())
        self.button_collect_data.setSizePolicy(sizePolicy1)
        self.button_collect_data.setFont(font2)

        self.horizontalLayout_3.addWidget(self.button_collect_data)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 6, 0, 1, 3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_beta = QLabel(self.centralwidget)
        self.label_beta.setObjectName(u"label_beta")
        self.label_beta.setFont(font2)
        self.label_beta.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_beta, 0, 0, 1, 1)

        self.label_theta = QLabel(self.centralwidget)
        self.label_theta.setObjectName(u"label_theta")
        self.label_theta.setFont(font2)
        self.label_theta.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_theta, 0, 1, 1, 1)

        self.label_alpha = QLabel(self.centralwidget)
        self.label_alpha.setObjectName(u"label_alpha")
        self.label_alpha.setFont(font2)
        self.label_alpha.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_alpha, 0, 2, 1, 1)

        self.label_low_beta = QLabel(self.centralwidget)
        self.label_low_beta.setObjectName(u"label_low_beta")
        self.label_low_beta.setFont(font2)
        self.label_low_beta.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_low_beta, 0, 3, 1, 1)

        self.label_high_beta = QLabel(self.centralwidget)
        self.label_high_beta.setObjectName(u"label_high_beta")
        self.label_high_beta.setFont(font2)
        self.label_high_beta.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_high_beta, 0, 4, 1, 1)

        self.label_gamma = QLabel(self.centralwidget)
        self.label_gamma.setObjectName(u"label_gamma")
        self.label_gamma.setFont(font2)
        self.label_gamma.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_gamma, 0, 5, 1, 1)

        self.label_delta_value = QLabel(self.centralwidget)
        self.label_delta_value.setObjectName(u"label_delta_value")
        self.label_delta_value.setFont(font2)
        self.label_delta_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_delta_value, 1, 0, 1, 1)

        self.label_theta_value = QLabel(self.centralwidget)
        self.label_theta_value.setObjectName(u"label_theta_value")
        self.label_theta_value.setFont(font2)
        self.label_theta_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_theta_value, 1, 1, 1, 1)

        self.label_alpha_value = QLabel(self.centralwidget)
        self.label_alpha_value.setObjectName(u"label_alpha_value")
        self.label_alpha_value.setFont(font2)
        self.label_alpha_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_alpha_value, 1, 2, 1, 1)

        self.label_low_beta_value = QLabel(self.centralwidget)
        self.label_low_beta_value.setObjectName(u"label_low_beta_value")
        self.label_low_beta_value.setFont(font2)
        self.label_low_beta_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_low_beta_value, 1, 3, 1, 1)

        self.label_high_beta_value = QLabel(self.centralwidget)
        self.label_high_beta_value.setObjectName(u"label_high_beta_value")
        self.label_high_beta_value.setFont(font2)
        self.label_high_beta_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_high_beta_value, 1, 4, 1, 1)

        self.label_gamma_value = QLabel(self.centralwidget)
        self.label_gamma_value.setObjectName(u"label_gamma_value")
        self.label_gamma_value.setFont(font2)
        self.label_gamma_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_gamma_value, 1, 5, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 5, 0, 1, 3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_fft = QLabel(self.centralwidget)
        self.label_fft.setObjectName(u"label_fft")
        self.label_fft.setFont(font1)
        self.label_fft.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fft, 0, 1, 1, 1)

        self.label_raw_eeg = QLabel(self.centralwidget)
        self.label_raw_eeg.setObjectName(u"label_raw_eeg")
        self.label_raw_eeg.setFont(font2)
        self.label_raw_eeg.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_raw_eeg, 0, 0, 1, 1)

        self.plot_raw_data = PlotWidget(self.centralwidget)
        self.plot_raw_data.setObjectName(u"plot_raw_data")
        self.plot_raw_data.setFont(font)

        self.gridLayout_6.addWidget(self.plot_raw_data, 1, 0, 1, 1)

        self.plot_fft = PlotWidget(self.centralwidget)
        self.plot_fft.setObjectName(u"plot_fft")
        self.plot_fft.setFont(font)

        self.gridLayout_6.addWidget(self.plot_fft, 1, 1, 1, 1)

        self.plot_attention = PlotWidget(self.centralwidget)
        self.plot_attention.setObjectName(u"plot_attention")
        self.plot_attention.setFont(font)

        self.gridLayout_6.addWidget(self.plot_attention, 3, 0, 1, 1)

        self.label_meditation_curve = QLabel(self.centralwidget)
        self.label_meditation_curve.setObjectName(u"label_meditation_curve")
        self.label_meditation_curve.setFont(font1)
        self.label_meditation_curve.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_meditation_curve, 2, 1, 1, 1)

        self.label_attention_curve = QLabel(self.centralwidget)
        self.label_attention_curve.setObjectName(u"label_attention_curve")
        self.label_attention_curve.setFont(font1)
        self.label_attention_curve.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_attention_curve, 2, 0, 1, 1)

        self.plot_meditation = PlotWidget(self.centralwidget)
        self.plot_meditation.setObjectName(u"plot_meditation")
        self.plot_meditation.setFont(font)

        self.gridLayout_6.addWidget(self.plot_meditation, 3, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 2, 1, 3, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_scan = QPushButton(self.centralwidget)
        self.button_scan.setObjectName(u"button_scan")
        sizePolicy.setHeightForWidth(self.button_scan.sizePolicy().hasHeightForWidth())
        self.button_scan.setSizePolicy(sizePolicy)
        self.button_scan.setFont(font1)

        self.horizontalLayout.addWidget(self.button_scan)

        self.combo_box_device_list = QComboBox(self.centralwidget)
        self.combo_box_device_list.setObjectName(u"combo_box_device_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_box_device_list.sizePolicy().hasHeightForWidth())
        self.combo_box_device_list.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(13)
        self.combo_box_device_list.setFont(font4)

        self.horizontalLayout.addWidget(self.combo_box_device_list)

        self.button_connect = QPushButton(self.centralwidget)
        self.button_connect.setObjectName(u"button_connect")
        sizePolicy.setHeightForWidth(self.button_connect.sizePolicy().hasHeightForWidth())
        self.button_connect.setSizePolicy(sizePolicy)
        self.button_connect.setFont(font4)

        self.horizontalLayout.addWidget(self.button_connect)

        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        self.button_start.setFont(font4)

        self.horizontalLayout.addWidget(self.button_start)


        self.gridLayout_7.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_afe_data_channel.setText(QCoreApplication.translate("MainWindow", u"Data Channel", None))
        self.label_afe_sample_rate.setText(QCoreApplication.translate("MainWindow", u"Sample Rate", None))
        self.label_afe_lead_off_option.setText(QCoreApplication.translate("MainWindow", u"Lead Off Option", None))
        self.label_afe_rld_channel.setText(QCoreApplication.translate("MainWindow", u"Rld Channel", None))
        self.label_afe_lead_off_channel.setText(QCoreApplication.translate("MainWindow", u"Lead Off Channel", None))
        self.button_send_afe.setText(QCoreApplication.translate("MainWindow", u"Send AFE Configuration", None))
        self.label_afe.setText(QCoreApplication.translate("MainWindow", u"AFE", None))
        self.label_acc_option.setText(QCoreApplication.translate("MainWindow", u"ACC Option", None))
        self.label_acc_sample_rate.setText(QCoreApplication.translate("MainWindow", u"Sample Rate", None))
        self.button_send_acc.setText(QCoreApplication.translate("MainWindow", u"Send ACC Configuration", None))
        self.label_acc.setText(QCoreApplication.translate("MainWindow", u"ACC", None))
        self.label_hardware_revision.setText(QCoreApplication.translate("MainWindow", u"Hardware Revision:", None))
        self.label_firmware_revision_value.setText(QCoreApplication.translate("MainWindow", u"V0.0.0", None))
        self.label_manufacturer_value.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_serial_number_value.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_serial_number.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.label_model_number.setText(QCoreApplication.translate("MainWindow", u"Model Number:", None))
        self.label_firmware_revision.setText(QCoreApplication.translate("MainWindow", u"Firmware Revison:", None))
        self.label_manufacturer.setText(QCoreApplication.translate("MainWindow", u"Manufacturer:", None))
        self.label_model_number_value.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_hardware_revision_value.setText(QCoreApplication.translate("MainWindow", u"V0.0.0", None))
        self.button_rename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.label_meditation_level.setText(QCoreApplication.translate("MainWindow", u"Meditation Level:", None))
        self.label_meditation_level_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_attention_level_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_contact_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_connectivity_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_connectivity.setText(QCoreApplication.translate("MainWindow", u"Connectivity:", None))
        self.label_contact.setText(QCoreApplication.translate("MainWindow", u"Contact:", None))
        self.label_attention_level.setText(QCoreApplication.translate("MainWindow", u"Attention Level:", None))
        self.label_led_color.setText(QCoreApplication.translate("MainWindow", u"LED Color", None))
        self.button_red.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.button_green.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.button_blue.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.button_collect_data.setText(QCoreApplication.translate("MainWindow", u"Collect Data", None))
        self.label_beta.setText(QCoreApplication.translate("MainWindow", u"Delta", None))
        self.label_theta.setText(QCoreApplication.translate("MainWindow", u"Theta", None))
        self.label_alpha.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.label_low_beta.setText(QCoreApplication.translate("MainWindow", u"Low Beta", None))
        self.label_high_beta.setText(QCoreApplication.translate("MainWindow", u"High Beta", None))
        self.label_gamma.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.label_delta_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_theta_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_alpha_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_low_beta_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_high_beta_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_gamma_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_fft.setText(QCoreApplication.translate("MainWindow", u"FFT ", None))
        self.label_raw_eeg.setText(QCoreApplication.translate("MainWindow", u"Raw EEG", None))
        self.label_meditation_curve.setText(QCoreApplication.translate("MainWindow", u"Meditation", None))
        self.label_attention_curve.setText(QCoreApplication.translate("MainWindow", u"Attention", None))
        self.button_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.button_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

