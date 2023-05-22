from PyQt5 import QtCore, QtGui, QtWidgets
from idSetter import Ui_Set_IDs
import threading
from usbtiva import communication
import datetime
from message_decoder import decode


com = communication()


def getNameFromID(ID):
    try:
        flag = False
        with open('ids.txt', 'r') as f:
            lines = f.readlines()
            
        for i in range(len(lines)):
            if lines[i][:-1] == ID:
                flag = True
                break
        if flag: return lines[i+1]
    except:
        pass
    
    return "Not defined"
            
class Ui_MainWindow(object):        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 887)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop.setIcon(icon)
        self.Stop.setCheckable(False)
        self.Stop.setAutoDefault(False)
        self.Stop.setObjectName("Stop")
        self.gridLayout_2.addWidget(self.Stop, 0, 2, 1, 1)
        self.SearchBar = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPointSize(10)
        self.SearchBar.setFont(font)
        self.SearchBar.setObjectName("SearchBar")
        self.gridLayout_2.addWidget(self.SearchBar, 0, 3, 1, 1)
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start.setIcon(icon1)
        self.Start.setCheckable(False)
        self.Start.setAutoDefault(False)
        self.Start.setObjectName("Start")
        self.gridLayout_2.addWidget(self.Start, 0, 0, 1, 1)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setAutoFillBackground(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pause.setIcon(icon2)
        self.Pause.setCheckable(False)
        self.Pause.setAutoDefault(False)
        self.Pause.setObjectName("Pause")
        self.gridLayout_2.addWidget(self.Pause, 0, 1, 1, 1)
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setAutoFillBackground(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search.setIcon(icon3)
        self.Search.setCheckable(False)
        self.Search.setAutoDefault(False)
        self.Search.setObjectName("Search")
        self.gridLayout_2.addWidget(self.Search, 0, 5, 1, 1)
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dataTable.setFont(font)
        self.dataTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.gridLayout_2.addWidget(self.dataTable, 1, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 21))
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
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSet_ID_Names)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

###############################################################################
###############################################################################
        self.start = False
        com.store = False
        self.Start.clicked.connect(self.evt_start)
        self.Stop.clicked.connect(self.evt_stop)
        self.Pause.clicked.connect(self.evt_pause)
        self.actionSet_ID_Names.triggered.connect(self.openSetID_ui)

        self.time = datetime.datetime.now()
        self.time_run = datetime.timedelta()
        
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
                field = decode(msg[1])
                name = getNameFromID(field[0])
                time = str(msg[0]-self.time+self.time_run)[:-3]
                self.entry([time,
                            "CAN0",
                            field[0],
                            'RX',
                            name,
                            "[~|~|~]",
                            field[1]])
            else:
                break

        if self.start:
            threading.Timer(0.01, self.t_checkForMsgs).start()
    
    def openSetID_ui(self):
        self.setID_win = QtWidgets.QMainWindow()
        self.setID_ui = Ui_Set_IDs()
        self.setID_ui.setupUi(self.setID_win)
        self.setID_win.show()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Stop.setStatusTip(_translate("MainWindow", "Stop tracing"))
        self.Start.setStatusTip(_translate("MainWindow", "Start tracing"))
        self.Pause.setStatusTip(_translate("MainWindow", "Pause tracing"))
        self.Search.setStatusTip(_translate("MainWindow", "Search"))
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
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
