from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox
import functools

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tax-Toe")
        self.setFixedSize(300,350)

        self.gal = 1

        self.msg = QMessageBox()

        self.gridLay = QGridLayout()
        self.hLblLay = QHBoxLayout()
        self.hBtnLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.btn1 = QPushButton("")
        self.btn1.clicked.connect(lambda: self.clicker(self.btn1))

        self.btn2 = QPushButton("")
        self.btn2.clicked.connect(lambda: self.clicker(self.btn2))

        self.btn3 = QPushButton("")
        self.btn3.clicked.connect(lambda: self.clicker(self.btn3))

        self.btn4 = QPushButton("")
        self.btn4.clicked.connect(lambda: self.clicker(self.btn4))

        self.btn5 = QPushButton("")
        self.btn5.clicked.connect(lambda: self.clicker(self.btn5))

        self.btn6 = QPushButton("")
        self.btn6.clicked.connect(lambda: self.clicker(self.btn6))

        self.btn7 = QPushButton("")
        self.btn7.clicked.connect(lambda: self.clicker(self.btn7))

        self.btn8 = QPushButton("")
        self.btn8.clicked.connect(lambda: self.clicker(self.btn8))

        self.btn9 = QPushButton("")
        self.btn9.clicked.connect(lambda: self.clicker(self.btn9))

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        index = 0

        self.str_style = """QPushButton {
            color:red;
            background-color:white;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;
            height:70px;
            width:100px;
        }"""

        for i in range(3):
            for j in range(3):
                self.gridLay.addWidget(self.lst[index], i, j)
                self.lst[index].setStyleSheet(self.str_style)
                index+=1
        

        self.navbatLbl = QLabel("<<<X>>>")
        self.navbatLbl.setStyleSheet("font: bold 16pt Arial")

        self.resetBtn = QPushButton("RESET")
        self.resetBtn.clicked.connect(self.reset)

        self.closeBtn = QPushButton("CLOSE")
        self.closeBtn.clicked.connect(self.close)

        self.hLblLay.addStretch()
        self.hLblLay.addWidget(self.navbatLbl)
        self.hLblLay.addStretch()

        self.hBtnLay.addWidget(self.resetBtn)
        self.hBtnLay.addWidget(self.closeBtn)

        self.vMainLay.addLayout(self.gridLay)
        self.vMainLay.addLayout(self.hLblLay)
        self.vMainLay.addLayout(self.hBtnLay)

        self.setLayout(self.vMainLay)


    def reset(self):
        for i in self.lst:
            i.setEnabled(True)
            i.setText("")
            i.setStyleSheet(self.str_style)
        self.gal=1
        self.navbatLbl.setText("<<<X>>>")

    def disable(self):
        for i in self.lst:
            i.setEnabled(False)

    def win(self, tugma1: QPushButton, tugma2: QPushButton, tugma3: QPushButton):
        str_style = """QPushButton {
            color:floralwhite;
            background-color:dark-green;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;
            height:70px;
            width:100px;
        }"""
        tugma1.setStyleSheet(str_style)
        tugma2.setStyleSheet(str_style)
        tugma3.setStyleSheet(str_style)

        self.disable()

        self.msg.setIcon(self.msg.Information)
        self.msg.setText(tugma1.text()+" is Winner")
        self.msg.buttonClicked.connect(self.reset)
        self.msg.exec_()


    def checkWin(self):
        # horizontal
        if(self.btn1.text() != "" and self.btn1.text() == self.btn2.text() and self.btn1.text() == self.btn3.text()):
            self.win(self.btn1, self.btn2, self.btn3)
        
        if(self.btn4.text() != "" and self.btn4.text() == self.btn5.text() and self.btn4.text() == self.btn6.text()):
            self.win(self.btn4, self.btn5, self.btn6)

        if(self.btn7.text() != "" and self.btn7.text() == self.btn8.text() and self.btn7.text() == self.btn9.text()):
            self.win(self.btn7, self.btn8, self.btn9)

        # vertical
        if(self.btn1.text() != "" and self.btn1.text() == self.btn4.text() and self.btn1.text() == self.btn7.text()):
            self.win(self.btn1, self.btn4, self.btn7)
        
        if(self.btn2.text() != "" and self.btn2.text() == self.btn5.text() and self.btn2.text() == self.btn8.text()):
            self.win(self.btn2, self.btn5, self.btn8)

        if(self.btn3.text() != "" and self.btn3.text() == self.btn6.text() and self.btn3.text() == self.btn9.text()):
            self.win(self.btn3, self.btn6, self.btn9)

        # diogonal
        if(self.btn1.text() != "" and self.btn1.text() == self.btn5.text() and self.btn1.text() == self.btn9.text()):
            self.win(self.btn1, self.btn5, self.btn9)
        
        if(self.btn3.text() != "" and self.btn3.text() == self.btn5.text() and self.btn3.text() == self.btn7.text()):
            self.win(self.btn3, self.btn5, self.btn7)

        #durrang
        if(self.gal == 10):
            self.reset()

    def clicker(self, btn: QPushButton):
        if self.gal % 2 == 0:
            btn.setText("O")
            self.navbatLbl.setText("<<<X>>>")
        else:
            btn.setText("X")
            self.navbatLbl.setText("<<<O>>>")

        btn.setEnabled(False)
        self.gal+=1

        self.checkWin()

if __name__ == "__main__":
    app = QApplication([])
    oyna = Window()
    oyna.show()
    app.exec_()