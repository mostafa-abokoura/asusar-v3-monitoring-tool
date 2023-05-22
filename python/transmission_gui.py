from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import cantools

CHANNELS = ('CAN0', 'CAN1')

class Ui_TransmissionWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, dbc_file=None, comm=None):
        super().__init__()
        self.parent = parent
        self.dbc_file = dbc_file
        self.setupUi()
        self.show()
        self.comm = comm

    def setupUi(self):
        self.setObjectName("TransmissionWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 0, 1, 1, 1)
        self.channel_select = QtWidgets.QComboBox(self.centralwidget)
        self.channel_select.setMaximumSize(QtCore.QSize(100, 16777215))
        self.channel_select.setObjectName("channel_select")
        self.channel_select.addItem("")
        self.channel_select.addItem("")
        self.channel_select.addItem("")
        self.gridLayout.addWidget(self.channel_select, 0, 2, 1, 1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        self.table.setEnabled(False)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 3)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        ###########################################################################################3
        self.channel_select.currentIndexChanged.connect(self.channel_select_change)
        self.label_file.setText(self.dbc_file)
        self.checkBoxGroup = QtWidgets.QButtonGroup(self)
        self.checkBoxGroup.setExclusive(False)
        self.checkBoxGroup.buttonToggled.connect(self.send_msg)
        self.load_data()
        self.table.cellChanged.connect(self.send_msg)
        
        
    def channel_select_change(self):
        text = self.channel_select.currentText()
        if text[0] == 'C' and self.channel_select.count() > 2:
            qm = QtWidgets.QMessageBox
            ret = qm.question(self,
                              'Select Confirmation',
                              f"<p>Are you sure to select <b>{text}</b>?</p>"
                              "<p>NOTE: Cannot be undone.</p>",
                              qm.Yes | qm.No)
            if ret == qm.Yes:
                self.table.setEnabled(True)
                self.channel_select.removeItem(0)
                self.channel_select.setEnabled(False)
            else:
                self.channel_select.setCurrentIndex(0)

    def reorder_data(self, data):
        result = data.replace(' ', '')
        result = data.replace(' ', '')[:8]
        result = '0' * (8 - len(result)) + result
        result = ' '.join(result[i:i+2] for i in range(0, len(result), 2))
        return result.upper()

    def send_msg(self):
        row = self.table.currentRow()
        send = self.table.cellWidget(row, 4)
        
        self.table.cellChanged.disconnect()
        msg_data = self.table.item(row, 3)
        new_msg = self.reorder_data(msg_data.text())
        msg_data.setText(new_msg)
        self.table.cellChanged.connect(self.send_msg)
        
        if send.checkState() == 2:
            ID = self.table.item(row, 0)
            period = self.table.item(row, 2)
            if self.comm != None and self.parent.start:
                Id = int(ID.text().replace(' ', ''), 16)
                Id2 = Id % 256
                Id1 = Id // 256
                pr = int(period.text())
                pr2 = pr % 256
                pr1 = pr // 256
                ch = self.channel_select.currentIndex() + 1
                dat = self.decode_msg(new_msg)
                msg = [0, row, ch, pr1, pr2, Id1, Id2]
                msg = msg + dat
                msg[0] = len(msg) - 1
                print(f"Enabling Message: Row({row}), ID({ID.text()}), Period({period.text()}), data({msg_data.text()})")
                self.comm.Transmit(msg)
        else:
            msg = [0, row, 0xFF]
            msg[0] = len(msg) - 1
            print(f"Disabling Message: Row({row})")
            self.comm.Transmit(msg)

    def decode_msg(self, msg):
        result = []
        msg = msg.replace(' ', '')
        data = int(msg, 16)
        while data != 0:
            result.append(data%256)
            data //= 256
        if len(result) == 0:
            result.append(0)
        return result[::-1]

    def load_data(self):
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 250)
        self.table.setColumnWidth(4, 60)
        self.table.setColumnWidth(1, 200)
        self.dbc = cantools.db.load_file(self.dbc_file)
        db = self.dbc

        self.table.setRowCount(len(db.messages))
        for i in range(len(db.messages)):
            msg = db.messages[i]
            Id = [msg.frame_id//256, msg.frame_id%256]
            ID = QtWidgets.QTableWidgetItem("%02x %02x"%(Id[0], Id[1]))
            ID.setFlags(ID.flags() & ~2)
            self.table.setItem(i, 0, ID)
            msg_name = QtWidgets.QTableWidgetItem(msg.name)
            msg_name.setFlags(msg_name.flags() & ~2)
            self.table.setItem(i, 1, msg_name)
            period = QtWidgets.QTableWidgetItem(str(msg._cycle_time))
            period.setFlags(period.flags() & ~2)
            self.table.setItem(i, 2, period)
            msg_data = QtWidgets.QTableWidgetItem("00 00 00 00")
            self.table.setItem(i, 3, msg_data)

            check_box = QtWidgets.QCheckBox('Send')
            self.checkBoxGroup.addButton(check_box)
            self.table.setCellWidget(i, 4, check_box)
            
    def retranslateUi(self, TransmissionWindow):
        _translate = QtCore.QCoreApplication.translate
        TransmissionWindow.setWindowTitle(_translate("TransmissionWindow", "Transmission"))
        self.label.setText(_translate("TransmissionWindow", "DBC File:"))
        self.label_file.setText(_translate("TransmissionWindow", "- - - - - -"))
        self.channel_select.setItemText(0, _translate("TransmissionWindow", "Select ..."))
        self.channel_select.setItemText(1, _translate("TransmissionWindow", "CAN0"))
        self.channel_select.setItemText(2, _translate("TransmissionWindow", "CAN1"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("TransmissionWindow", "ID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("TransmissionWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("TransmissionWindow", "Period"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("TransmissionWindow", "Data"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("TransmissionWindow", "State"))


if __name__ == "__main__":
    import sys
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_TransmissionWindow(None, 'dbc.dbc')
    sys.exit(app.exec_())
