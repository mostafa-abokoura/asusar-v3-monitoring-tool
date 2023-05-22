from PyQt5 import QtCore, QtGui, QtWidgets
from idSetter import Ui_Set_IDs
import threading
from usbtiva import communication
import datetime
from message_decoder import decode
import cantools
from transmission_gui import Ui_TransmissionWindow

com = communication()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 800))
        self.tableWidget.setMaximumSize(QtCore.QSize(200, 800))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 7, 1, 1)
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setMinimumSize(QtCore.QSize(30, 0))
        self.Stop.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Stop.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop.setIcon(icon)
        self.Stop.setCheckable(False)
        self.Stop.setAutoDefault(False)
        self.Stop.setObjectName("Stop")
        self.gridLayout.addWidget(self.Stop, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start.sizePolicy().hasHeightForWidth())
        self.Start.setSizePolicy(sizePolicy)
        self.Start.setMinimumSize(QtCore.QSize(30, 0))
        self.Start.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Start.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start.setIcon(icon1)
        self.Start.setCheckable(False)
        self.Start.setAutoDefault(False)
        self.Start.setObjectName("Start")
        self.gridLayout.addWidget(self.Start, 0, 0, 1, 1)
        self.SearchBar = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy)
        self.SearchBar.setMinimumSize(QtCore.QSize(500, 0))
        self.SearchBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.SearchBar.setFont(font)
        self.SearchBar.setObjectName("SearchBar")
        self.gridLayout.addWidget(self.SearchBar, 0, 4, 1, 1)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setMinimumSize(QtCore.QSize(30, 0))
        self.Pause.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Pause.setAutoFillBackground(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pause.setIcon(icon2)
        self.Pause.setCheckable(False)
        self.Pause.setAutoDefault(False)
        self.Pause.setObjectName("Pause")
        self.gridLayout.addWidget(self.Pause, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(105, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(105, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 5, 1, 1)
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTable.sizePolicy().hasHeightForWidth())
        self.dataTable.setSizePolicy(sizePolicy)
        self.dataTable.setMinimumSize(QtCore.QSize(800, 800))
        self.dataTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(False)
        font.setWeight(50)
        self.dataTable.setFont(font)
        self.dataTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dataTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.dataTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.dataTable.setRowCount(0)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(6, item)
        self.dataTable.horizontalHeader().setVisible(True)
        self.dataTable.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTable.horizontalHeader().setMinimumSectionSize(39)
        self.dataTable.horizontalHeader().setSortIndicatorShown(True)
        self.dataTable.horizontalHeader().setStretchLastSection(True)
        self.dataTable.verticalHeader().setCascadingSectionResizes(True)
        self.dataTable.verticalHeader().setDefaultSectionSize(20)
        self.dataTable.verticalHeader().setMinimumSectionSize(23)
        self.dataTable.verticalHeader().setSortIndicatorShown(True)
        self.dataTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.dataTable, 1, 0, 1, 7)
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search.sizePolicy().hasHeightForWidth())
        self.Search.setSizePolicy(sizePolicy)
        self.Search.setMinimumSize(QtCore.QSize(30, 0))
        self.Search.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Search.setAutoFillBackground(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search.setIcon(icon3)
        self.Search.setCheckable(False)
        self.Search.setAutoDefault(False)
        self.Search.setObjectName("Search")
        self.gridLayout.addWidget(self.Search, 0, 6, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(184, 195, 255);\n"
"    border: 1px solid #888888;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 155, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 207, 139);\n"
"}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 7, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionFilters = QtWidgets.QAction(MainWindow)
        self.actionFilters.setObjectName("actionFilters")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSet_ID_Names = QtWidgets.QAction(MainWindow)
        self.actionSet_ID_Names.setObjectName("actionSet_ID_Names")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionStart)
        self.menuEdit.addAction(self.actionStop)
        self.menuEdit.addAction(self.actionFilters)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
###############################################################################################
        self.dbc = cantools.db.load_file('dbc.dbc')
        self.start = False
        com.store = True
        com.verbose = False
        self.pushButton.clicked.connect(self.openTransmissionWindow)
        self.Start.clicked.connect(self.evt_start)
        self.Stop.clicked.connect(self.evt_stop)
        self.Pause.clicked.connect(self.evt_pause)
        self.SearchBar.editingFinished.connect(self.search)
        self.Search.clicked.connect(self.search)
        self.dataTable.itemSelectionChanged.connect(self.show_signals)

        self.time = datetime.datetime.now()
        self.time_run = datetime.timedelta()

    def openTransmissionWindow(self):
        self.pushButton.setEnabled(False)
        dbc_file = 'dbc.dbc'
        self.ui_tw = Ui_TransmissionWindow(self, dbc_file, com)
        self.ui_tw.closeEvent = self.returnedFromTransmissionWindow

    def returnedFromTransmissionWindow(self, event):
        self.pushButton.setEnabled(True)
        
    def show_signals(self):
        curr_id = self.dataTable.item(self.dataTable.currentRow(), 2)
        msg_name = self.dataTable.item(self.dataTable.currentRow(), 4).text()
        msg_data = self.dataTable.item(self.dataTable.currentRow(), 6).text()
        
        if msg_name != 'UNDEFINED':
            data = int(msg_data.replace(' ', ''), 16)
            ID = curr_id.text()
            signals = self.dbc.get_message_by_frame_id(int(ID.replace(' ', ''), 16)).signals
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(['Name', 'Data'])
            self.tableWidget.setRowCount(len(signals))
            for i, sig in enumerate(signals):
                name = str(sig.name.replace('_', ' '))
                sig_name = QtWidgets.QTableWidgetItem(name)
                self.tableWidget.setItem(i, 0, sig_name)

                if 'l' == sig.byte_order[0]:
                    mask = (1 << sig.length) - 1
                    value = (data >> sig.start) & mask
                    sig_data = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, 1, sig_data)

        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            

    def evt_start(self):
        if not self.start:
            self.time = datetime.datetime.now()
            self.start = True
            com.store = True
            threading.Timer(0.01, self.t_checkForMsgs).start()

    def evt_stop(self):
        self.time_run = datetime.timedelta()
        self.dataTable.setRowCount(0)
        self.start = False
        com.store = False

    def evt_pause(self):
        if self.start is True:
            self.time_run += datetime.datetime.now() - self.time
            self.start = False
            com.store = False

    def t_checkForMsgs(self):
        while True:
            msg = com.Dequeue()
            if msg:
                rec_time, rec_msg = msg
                msg_ts, msg_dir, msg_ch, msg_id, msg_data = decode(rec_msg)
                try:
                    name = self.dbc.get_message_by_frame_id(int(msg_id.replace(' ', ''), 16)).name
                except KeyError:
                    name = "UNDEFINED"
                time = str(rec_time-self.time+self.time_run)[:-3]
                time = f'{int(msg_ts)//60:02d}:{msg_ts%60:06.3f}'
                msg_data = '00 ' * ((12 - len(msg_data)) // 3) + msg_data
                self.entry([time,
                            msg_ch,
                            msg_id,
                            msg_dir,
                            name,
                            "- - - - - -",
                            msg_data])
            else:
                break

        if self.start:
            threading.Timer(0.01, self.t_checkForMsgs).start()
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start.setStatusTip(_translate("MainWindow", "Start tracing"))
        self.Pause.setStatusTip(_translate("MainWindow", "Pause tracing"))
        self.Stop.setStatusTip(_translate("MainWindow", "Stop tracing"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Channel"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ID"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Name"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Data"))
        self.Search.setStatusTip(_translate("MainWindow", "Start tracing"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Channel"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Direction"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Name"))
        item = self.dataTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Event Type"))
        item = self.dataTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.pushButton.setText(_translate("MainWindow", "Open Transmission Window"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create New File"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open existing file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionFilters.setText(_translate("MainWindow", "Filters"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Close the tool"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSet_ID_Names.setText(_translate("MainWindow", "Define IDs"))

    def entry(self, data):
        rowCount = self.dataTable.rowCount()
        columnCount = self.dataTable.columnCount()        
        self.dataTable.insertRow(rowCount)
        
        for i in range(columnCount):
            self.insert(rowCount, i, data[i])
        self.dataTable.scrollToBottom()

    def insert(self, rowCount, index, data):
        self.dataTable.setItem(rowCount, index,
                               QtWidgets.QTableWidgetItem(str(data)))

    def select_labels(self, col):
        items = self.dataTable.findItems(self.SearchBar.text(),
                                           QtCore.Qt.MatchFixedString)
        try:
            print(items[0].row())
        except:
            pass
        if items:
            for i in range(0, len(items)):
                item = items[i]
                self.dataTable.item(item.row(), col).setSelected(True)

    def search(self):
        text = self.comboBox.currentText()
        if text == "Channel":
            self.select_labels(1)
        elif text == "ID":
            self.select_labels(2)
        elif text == "Name":
            self.select_labels(4)
        elif text == "Data":
            self.select_labels(6)
        else:
            pass


if __name__ == "__main__":
    import sys
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
