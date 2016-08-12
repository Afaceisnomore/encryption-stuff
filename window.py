#!-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSlot
from encryption.crypters import *
from encryption.analyzers import *


(Ui_MainWindow, QMainWindow) = uic.loadUiType('window.ui')
class SquareDialog(QDialog):
    def __init__(self, parent=None):
        from PyQt5.QtGui import QFont
        QDialog.__init__(self, parent)
        self.square = QTextEdit()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.square)
        self.setLayout(main_layout)
        self.setFixedSize(650, 660)
        self.square.setFont(QFont("Times", 14))


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    cc = CaesarCrypter()
    vc = VigenereCrypter()
    ca = CaesarAnalyzer()
    va = VigenereAnalyzer()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.square_dialog = SquareDialog(self)

    def __del__(self):
        self.ui = None

    @pyqtSlot(name='on_toolButtonInput_clicked')
    def showFileDialogInput(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        if len(file_path) > 0:
            self.ui.lineEditInput.setText(file_path)
            self.ui.lineEditOutput.setText(file_path[:(len(file_path) - 4)] + "_.txt")

    @pyqtSlot(name='on_toolButtonOutput_clicked')
    def showFileDialogOutput(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        if len(file_path) > 0:
            self.ui.lineEditOutput.setText(file_path)

    @pyqtSlot(name='on_pushButtonRun_clicked')
    def run(self):
        input_file = open(self.ui.lineEditInput.text(), 'r')
        output_file = open(self.ui.lineEditOutput.text(), 'w')

        if self.ui.radioButtonMode1.isChecked():
            offset, ok = QInputDialog.getInt(self, 'Input Dialog', 'Enter offset:')
            if ok:
                for line in input_file:
                    output_file.write(self.cc.encrypt(line, offset))

        if self.ui.radioButtonMode2.isChecked():
            key, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter keyword:')
            if ok:
                for line in input_file:
                    output_file.write(self.vc.encrypt(line, key))
                self.square_dialog.square.setText(str(self.vc.square))
                self.square_dialog.show()

        if self.ui.radioButtonMode3.isChecked():
            for line in input_file:
                self.ca << line
            self.ca.analyze()
            key = self.ca.find_key()
            QMessageBox.information(self, "Key is...", str(key))
            input_file.seek(0)
            for line in input_file:
                output_file.write(self.cc.encrypt(line, -1 * key))

        if self.ui.radioButtonMode4.isChecked():
            pass

        input_file.close()
        output_file.close()


if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('Chipers')
    # create widget
    w = MainWindow()
    w.setWindowTitle('Chipers')
    w.show()

    # execute application
    sys.exit(app.exec_())