# Form implementation generated from reading ui file '.\dsa_project_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(1232, 779)
        Window.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        Window.setStyleSheet("background-color: #0B192C;")
        self.data_view = QtWidgets.QTableView(parent=Window)
        self.data_view.setGeometry(QtCore.QRect(30, 260, 1181, 381))
        self.data_view.setStyleSheet(
            "QTableView {\n"
            "    background-color: #33372C;\n"
            "    border-radius: 10px;\n"
            "    border: 1px solid #5A5A5A;\n"
            "    color: whitesmoke;\n"
            "    gridline-color: #5A5A5A;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    background-color: #5A5A5A;\n"
            "    color: whitesmoke;\n"
            "    padding: 4px;\n"
            "    border: 1px solid #3C3D37;\n"
            "}\n"
            "\n"
            "QTableView::item {\n"
            "    border: none;\n"
            "    padding: 4px;\n"
            "}\n"
            "\n"
            "QTableView::item:selected {\n"
            "    background-color: #6A6A6A;\n"
            "    color: white;\n"
            "}"
        )
        self.data_view.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.data_view.setObjectName("data_view")
        self.data_view.horizontalHeader().setCascadingSectionResizes(True)
        self.data_view.horizontalHeader().setDefaultSectionSize(140)
        self.data_view.horizontalHeader().setMinimumSectionSize(70)
        self.data_view.horizontalHeader().setStretchLastSection(True)
        self.data_view.verticalHeader().setCascadingSectionResizes(True)
        self.data_view.verticalHeader().setStretchLastSection(True)
        self.frame = QtWidgets.QFrame(parent=Window)
        self.frame.setGeometry(QtCore.QRect(430, 730, 361, 41))
        self.frame.setStyleSheet(
            "QFrame {\n"
            "    border: 2px solid #693DC3; /* Border color */\n"
            "    border-radius: 10px; /* Rounded corners */\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
            "                                stop:0 #E6E6FA, stop:1 #D9D9D9); /* Light gradient background */\n"
            "    padding: 20px; /* Padding inside the frame */\n"
            "}\n"
            "\n"
            ""
        )
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(
            "QLabel {\n" "    color: #FF6500;\n" "    text-align: center;\n" "}"
        )
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=Window)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:whitesmoke;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.txt_algorithm = QtWidgets.QComboBox(parent=Window)
        self.txt_algorithm.setGeometry(QtCore.QRect(30, 200, 221, 41))
        self.txt_algorithm.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.txt_algorithm.setStyleSheet("border:0.5px solid whitesmoke;\n"
"border-radius:5px;\n"
"color:whitesmoke;\n"
"padding:0px auto;\n"
"font-size:15px;\n"
"font-weight:500;\n"
"\n"
"")
        self.txt_algorithm.setMinimumContentsLength(0)
        self.txt_algorithm.setObjectName("txt_algorithm")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_algorithm.addItem("")
        self.txt_sorting_base = QtWidgets.QComboBox(parent=Window)
        self.txt_sorting_base.setGeometry(QtCore.QRect(270, 200, 221, 41))
        self.txt_sorting_base.setStyleSheet("border:0.5px solid whitesmoke;\n"
"border-radius:5px;\n"
"color:whitesmoke;\n"
"padding:0px auto;\n"
"font-size:15px;\n"
"font-weight:500;\n"
"\n"
"")
        self.txt_sorting_base.setObjectName("txt_sorting_base")
        self.txt_sorting_base.addItem("")
        self.txt_sorting_base.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=Window)
        self.pushButton.setGeometry(QtCore.QRect(510, 200, 171, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(parent=Window)
        self.progressBar.setGeometry(QtCore.QRect(180, 650, 761, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid whitesmoke;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: whitesmoke;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FF6500; /* Set the filling color here */\n"
"    width: 20px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.txt_url = QtWidgets.QLineEdit(parent=Window)
        self.txt_url.setGeometry(QtCore.QRect(30, 140, 461, 41))
        self.txt_url.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
"border-radius:5px;\n"
"border:0.5px solid white;\n"
"padding:4px auto;\n"
"color:whitesmoke;\n"
"")
        self.txt_url.setObjectName("txt_url")
        self.txt_search = QtWidgets.QLineEdit(parent=Window)
        self.txt_search.setGeometry(QtCore.QRect(710, 200, 211, 41))
        self.txt_search.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
"border-radius:5px;\n"
"border:0.5px solid white;\n"
"padding:4px auto;\n"
"color:whitesmoke;\n"
"")
        self.txt_search.setObjectName("txt_search")
        self.btn_scrap = QtWidgets.QPushButton(parent=Window)
        self.btn_scrap.setGeometry(QtCore.QRect(510, 140, 171, 41))
        self.btn_scrap.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.btn_scrap.setObjectName("btn_scrap")
        self.scarpping_bar = QtWidgets.QProgressBar(parent=Window)
        self.scarpping_bar.setGeometry(QtCore.QRect(180, 690, 761, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.scarpping_bar.setFont(font)
        self.scarpping_bar.setAutoFillBackground(False)
        self.scarpping_bar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid whitesmoke;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: whitesmoke;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FF6500; /* Set the filling color here */\n"
"    width: 20px;\n"
"}")
        self.scarpping_bar.setProperty("value", 0)
        self.scarpping_bar.setObjectName("scarpping_bar")
        self.label_4 = QtWidgets.QLabel(parent=Window)
        self.label_4.setGeometry(QtCore.QRect(70, 650, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color:whitesmoke;\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=Window)
        self.label_3.setGeometry(QtCore.QRect(70, 690, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color:whitesmoke;\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.btn_search = QtWidgets.QPushButton(parent=Window)
        self.btn_search.setGeometry(QtCore.QRect(1110, 200, 101, 41))
        self.btn_search.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.btn_search.setObjectName("btn_search")
        self.label_6 = QtWidgets.QLabel(parent=Window)
        self.label_6.setGeometry(QtCore.QRect(290, 10, 341, 111))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/logo.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(parent=Window)
        self.frame_2.setGeometry(QtCore.QRect(710, 60, 501, 121))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border: 2px solid whitesmoke;  /* Set the border color and width */\n"
"    border-radius: 10px;        /* Set the corner radius */\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border:none;\n" "color:whitesmoke;\n" "\n" "")
        self.label_7.setObjectName("label_7")
        self.btn_start = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_start.setGeometry(QtCore.QRect(20, 70, 91, 41))
        self.btn_start.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_stop.setGeometry(QtCore.QRect(140, 70, 91, 41))
        self.btn_stop.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.btn_stop.setObjectName("btn_stop")
        self.btn_pause = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_pause.setGeometry(QtCore.QRect(260, 70, 91, 41))
        self.btn_pause.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.btn_pause.setObjectName("btn_pause")
        self.btn_Resume = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_Resume.setGeometry(QtCore.QRect(370, 70, 111, 41))
        self.btn_Resume.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid whitesmoke;\n"
"    color: white; /* Change text color for better contrast */\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #693DC3, stop:1 black);\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #5728A1, stop:1 #1A1A1A); /* Darker gradient for deeper effect */\n"
"    color: #F1F1F1; /* Lightened text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 rgba(105, 61, 195, 0.9), stop:1 rgba(0, 0, 0, 0.8)); /* Slightly darker gradient */\n"
"    color: #E0E0E0; /* Even lighter text color when pressed */\n"
"}\n"
"")
        self.btn_Resume.setObjectName("btn_Resume")
        self.txt_searching_base = QtWidgets.QComboBox(parent=Window)
        self.txt_searching_base.setGeometry(QtCore.QRect(930, 200, 171, 41))
        self.txt_searching_base.setStyleSheet("border:0.5px solid whitesmoke;\n"
"border-radius:5px;\n"
"color:whitesmoke;\n"
"padding:0px auto;\n"
"font-size:15px;\n"
"font-weight:500;\n"
"\n"
"")
        self.txt_searching_base.setObjectName("txt_searching_base")
        self.txt_searching_base.addItem("")
        self.txt_searching_base.addItem("")
        self.txt_searching_base.addItem("")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Data Scrapper"))
        self.label_5.setText(_translate("Window", "0.0000"))
        self.label_2.setText(_translate("Window", "Web Minner"))
        self.txt_algorithm.setCurrentText(_translate("Window", "Bubble Sort"))
        self.txt_algorithm.setItemText(0, _translate("Window", "Bubble Sort"))
        self.txt_algorithm.setItemText(1, _translate("Window", "Insertion Sort"))
        self.txt_algorithm.setItemText(2, _translate("Window", "Merge Sort"))
        self.txt_algorithm.setItemText(3, _translate("Window", "Selection Sort"))
        self.txt_algorithm.setItemText(4, _translate("Window", "Quick Sort"))
        self.txt_algorithm.setItemText(5, _translate("Window", "Hybrid Merge Sort"))
        self.txt_algorithm.setItemText(6, _translate("Window", "Count Sort"))
        self.txt_algorithm.setItemText(7, _translate("Window", "Bucket Sort"))
        self.txt_algorithm.setItemText(8, _translate("Window", "Radix Sort"))
        self.txt_algorithm.setItemText(9, _translate("Window", "Heap Sort"))
        self.txt_algorithm.setItemText(10, _translate("Window", "Shell Sort"))
        self.txt_sorting_base.setItemText(0, _translate("Window", "Ascending"))
        self.txt_sorting_base.setItemText(1, _translate("Window", "Descending"))
        self.pushButton.setText(_translate("Window", "Start Sorting"))
        self.txt_url.setPlaceholderText(_translate("Window", "Paste url to scrap ...."))
        self.txt_search.setPlaceholderText(_translate("Window", "Search .."))
        self.btn_scrap.setText(_translate("Window", "Scrap"))
        self.label_4.setText(_translate("Window", "Sorting"))
        self.label_3.setText(_translate("Window", "Scrapping"))
        self.btn_search.setText(_translate("Window", "Search"))
        self.label_7.setText(
            _translate("Window", "For Url : https://catalog.data.gov/dataset/")
        )
        self.btn_start.setText(_translate("Window", "Start"))
        self.btn_stop.setText(_translate("Window", "Stop"))
        self.btn_pause.setText(_translate("Window", "Pause"))
        self.btn_Resume.setText(_translate("Window", "Resume"))
        self.txt_searching_base.setItemText(0, _translate("Window", "Contains"))
        self.txt_searching_base.setItemText(1, _translate("Window", "Start with"))
        self.txt_searching_base.setItemText(2, _translate("Window", "Ends with"))
