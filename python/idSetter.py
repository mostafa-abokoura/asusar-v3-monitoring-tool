#idSetter

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_IDs(object):
    def setupUi(self, Set_IDs):
        self.win = Set_IDs
        Set_IDs.setObjectName("Set_IDs")
        Set_IDs.setEnabled(True)
        Set_IDs.resize(332, 282)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Set_IDs.sizePolicy().hasHeightForWidth())
        Set_IDs.setSizePolicy(sizePolicy)
        Set_IDs.setMinimumSize(QtCore.QSize(332, 282))
        Set_IDs.setMaximumSize(QtCore.QSize(332, 282))
        Set_IDs.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Set_IDs.setAnimated(True)
        Set_IDs.setDocumentMode(False)
        Set_IDs.setTabShape(QtWidgets.QTabWidget.Rounded)
        Set_IDs.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        Set_IDs.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Set_IDs)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 10, 61, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 10, 151, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEdit_2.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 21, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 21, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 10, 21, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 311, 231))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        Set_IDs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Set_IDs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 21))
        self.menubar.setObjectName("menubar")
        Set_IDs.setMenuBar(self.menubar)

        self.retranslateUi(Set_IDs)
        QtCore.QMetaObject.connectSlotsByName(Set_IDs)

        ##############################################################

        self.readData()
        self.pushButton.clicked.connect(self.add_clicked)
        self.pushButton_2.clicked.connect(self.remove_clicked)

        self.lineEdit.textEdited.connect(self.editID)
        self.lineEdit_2.textEdited.connect(self.editName)
        self.tableWidget.cellChanged.connect(self.updateData)

    def retranslateUi(self, Set_IDs):
        _translate = QtCore.QCoreApplication.translate
        Set_IDs.setWindowTitle(_translate("Set_IDs", "Define ID Names"))
        self.lineEdit.setText(_translate("Set_IDs", "ID [HEX]"))
        self.lineEdit_2.setText(_translate("Set_IDs", "Name"))
        self.lineEdit_3.setText(_translate("Set_IDs", "0x"))
        self.pushButton.setText(_translate("Set_IDs", "+"))
        self.pushButton_2.setText(_translate("Set_IDs", "-"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Set_IDs", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Set_IDs", "Name"))
    
    def add_clicked(self):
        ID = self.lineEdit.displayText()
        Name = self.lineEdit_2.displayText()
        
        rowCount = self.tableWidget.rowCount()       
        self.tableWidget.insertRow(rowCount)
        
        self.tableWidget.setItem(rowCount, 0,
                                QtWidgets.QTableWidgetItem(str(ID)))
        
        self.tableWidget.setItem(rowCount, 1,
                                 QtWidgets.QTableWidgetItem(str(Name)))
        self.updateData()

    def remove_clicked(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())
        self.updateData()

    def editID(self):
        if (str(self.lineEdit.displayText())[:-1] == "ID [HEX]"):
            self.lineEdit.setText(str(self.lineEdit.displayText())[-1])
        elif (str(self.lineEdit.displayText()) == "ID [HEX"):
            self.lineEdit.clear()

    def editName(self):
        if (str(self.lineEdit_2.displayText())[:-1] == "Name"):
            self.lineEdit_2.setText(str(self.lineEdit_2.displayText())[-1])
        elif (str(self.lineEdit_2.displayText()) == "Nam"):
            self.lineEdit_2.clear()

    def updateData(self):
        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()

        try:
            with open('ids.txt', 'w') as f:
                for i in range(rowCount):
                    for j in range(columnCount):
                        rowData = self.tableWidget.item(i, j)
                        f.write(rowData.text())
                        f.write("\n")
        except:
            pass

    def readData(self):
           
        with open('ids.txt', 'r') as f:
            data = f.readlines()
            
        rows = int(len(data)/2)
        for i in range(rows):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0,
                                QtWidgets.QTableWidgetItem(data[2*i][:-1]))
            self.tableWidget.setItem(i, 1,
                                QtWidgets.QTableWidgetItem(data[(2*i)+1][:-1]))
        
