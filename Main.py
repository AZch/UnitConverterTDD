import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Converter import Converter

import MainWnd

class MainRelease(QtWidgets.QMainWindow, MainWnd.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__converter = Converter()
        self.__arrAddQuant = [0] * (len(self.__converter.getQuantities()))
        self.addQuant.clicked.connect(self.addQuantity)
        self.addQuant_2.clicked.connect(self.addArrQuant)
        self.MakeConv.clicked.connect(self.makeConvert)

    def makeConvert(self):
        res = self.__converter.transferQuant(
            self.__converter.getIdByName(self.cmbAllQuantFrom.currentText()),
            self.__converter.getIdByName(self.cmbAllQuantTo.currentText()),
            self.SIConvFrom.value()
        )
        self.SIConvTo.setValue(res)

    def addArrQuant(self):
        self.__arrAddQuant[self.__converter.getIdByName(self.cmbAllQuantFrom_2.currentText())] = self.SIConvFrom_2.value()

    def addQuantity(self):
        self.__converter.addQuantities(self.nameQuant.text(), self.__arrAddQuant)
        self.cmbAllQuantFrom_2.clear()
        self.cmbAllQuantFrom_2.addItems(self.__converter.getNames())
        self.cmbAllQuantFrom.clear()
        self.cmbAllQuantFrom.addItems(self.__converter.getNames())
        self.cmbAllQuantTo.clear()
        self.cmbAllQuantTo.addItems(self.__converter.getNames())
        self.__arrAddQuant = [0] * (len(self.__converter.getQuantities()))
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainRelease()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()