
from PyQt5.QtWidgets import QWidget
from m import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
# python -m PyQt5.uic.pyuic -x untitled.ui -o main.py  


class main_gui(QtWidgets.QMainWindow):
    def __init__(self,) -> None:
        super(main_gui,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # работа с портом 
        self.serial =  QSerialPort()
        self.serial.setBaudRate(9600)
        ports_arduino = QSerialPortInfo.availablePorts()
        lits_ports = []
        list_ports_name = []
        for port in ports_arduino:
            lits_ports.append(port.portName())
            list_ports_name.append(port.description())
        
        data_info_ports = dict(zip(lits_ports,list_ports_name))

        for key,value in data_info_ports.items():
            if value == 'USB-SERIAL CH340':
                self.serial.setPortName(key)
                self.serial.open(QIODevice.ReadWrite)
                self.serial.setDataTerminalReady(True)
                self.ui.stackedWidget.setCurrentIndex(0)
                self.ui.pushButton.clicked.connect(self.page_1)
                self.ui.pushButton_2.clicked.connect(self.page_2)
            else:
                pass




    def pors_reaf(self):
        rx = self.serial.readLine()
        self.data_ports = []
        self.data_ports.append(str(rx, 'utf-8'))
        self.unique_data = set(self.data_ports)
        if self.unique_data == {'\r\n'}:
            pass
        else:
            print(self.unique_data)
            self.model = QtCore.QStringListModel(self.unique_data)
            self.model.setStringList(self.data_ports)
            self.ui.listView.setModel(self.model)

    def page_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton_3.clicked.connect(self.page_0)


    def page_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.pushButton_4.clicked.connect(self.page_0)
        # self.model = QtCore.QStringListModel(self)
        self.serial.readyRead.connect(self.pors_reaf)
        # self.model.setStringList('gfg')
        # self.ui.listView.setModel(self.model)
        

    def page_0(self):
        self.ui.stackedWidget.setCurrentIndex(0)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = main_gui()
    application.show()
    sys.exit(app.exec())











