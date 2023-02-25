from PyQt5.QtWidgets import *
from random import shuffle
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,350)
        self.setWindowTitle("BigPuzz")
        self.setStyleSheet('background-color:green')
        # layout
        self.vMain = QVBoxLayout()
        self.grid = QGridLayout()
        self.resCLS = QHBoxLayout()
        # buttons
        self.btn1 = QPushButton()
        self.btn1.clicked.connect(self.btn_1)
        self.btn2 = QPushButton()
        self.btn2.clicked.connect(self.btn_2)
        self.btn3 = QPushButton()
        self.btn3.clicked.connect(self.btn_3)
        self.btn4 = QPushButton()
        self.btn4.clicked.connect(self.btn_4)
        self.btn5 = QPushButton()
        self.btn5.clicked.connect(self.btn_5)
        self.btn6 = QPushButton()
        self.btn6.clicked.connect(self.btn_6)
        self.btn7 = QPushButton()
        self.btn7.clicked.connect(self.btn_7)
        self.btn8 = QPushButton()
        self.btn8.clicked.connect(self.btn_8)
        self.btn9 = QPushButton()
        self.btn9.clicked.connect(self.btn_9)
        self.btn10 = QPushButton()
        self.btn10.clicked.connect(self.btn_10)
        self.btn11 = QPushButton()
        self.btn11.clicked.connect(self.btn_11)
        self.btn12 = QPushButton()
        self.btn12.clicked.connect(self.btn_12)
        self.btn13 = QPushButton()
        self.btn13.clicked.connect(self.btn_13)
        self.btn14 = QPushButton()
        self.btn14.clicked.connect(self.btn_14)
        self.btn15 = QPushButton()
        self.btn15.clicked.connect(self.btn_15)
        self.btn16 = QPushButton()
        self.btn16.clicked.connect(self.btn_16)
        self.close_btn = QPushButton('Close')
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setStyleSheet('background-color:yellow;height:40px;border-radius:20px')
        self.reset_btn = QPushButton('Reset')
        self.reset_btn.clicked.connect(self.reset)
        self.reset_btn.setStyleSheet('background-color:yellow;height:40px;border-radius:20px')
        # list
        self.lst_num = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','']
        self.lst_num_copy = self.lst_num.copy()
        self.lst_btn = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]
        # add grid
        index = 0
        for i in range(4):
            for j in range(4):
                self.grid.addWidget(self.lst_btn[index],i,j)
                self.lst_btn[index].setStyleSheet('background-color:orange;text-align: center;height:50px;border-radius:20px;font-size:20px')
                index+=1
        # add lay
        self.resCLS.addWidget(self.reset_btn)
        self.resCLS.addWidget(self.close_btn)
        self.vMain.addLayout(self.grid)
        self.vMain.addLayout(self.resCLS)
        self.setLayout(self.vMain)
        
    def check_win(self):
        count = 0
        for i in range(16):
            if self.lst_btn[i].text()==self.lst_num_copy[i]:
                count += 1
    
        if count == 16:
                self.msg = QMessageBox()
                self.msg.setWindowTitle('YouTop')
                self.msg.setStyleSheet('font-size:15px')
                self.msg.setIcon(self.msg.Information)
                self.msg.setText('Winner Winner')
                self.msg.buttonClicked.connect(self.reset)
                self.msg.show()
                self.msg.exec_()
        else:
                return False
            
    def reset(self):
        shuffle(self.lst_num)
        for i in range(16):
            self.lst_btn[i].setText(self.lst_num[i])
        self.check_win()
        
    def close(self) -> bool:
        return super().close()
    
    # methot button
     
    def btn_1(self):
        if self.btn2.text()=="":
            self.btn2.setText(self.btn1.text())
            self.btn1.setText('')
        elif self.btn5.text()=='':
            self.btn5.setText(self.btn1.text())
            self.btn1.setText('')
        self.check_win()
    def btn_2(self):
        if self.btn1.text()=="":
            self.btn1.setText(self.btn2.text())
            self.btn2.setText('')
        elif self.btn3.text()=='':
            self.btn3.setText(self.btn2.text())
            self.btn2.setText('')
        elif self.btn6.text()=='':
            self.btn6.setText(self.btn2.text())
            self.btn2.setText('')
        self.check_win()
    def btn_3(self):
        if self.btn2.text()=="":
            self.btn2.setText(self.btn3.text())
            self.btn3.setText('')
        elif self.btn4.text()=='':
            self.btn4.setText(self.btn3.text())
            self.btn3.setText('')
        elif self.btn7.text()=='':
            self.btn7.setText(self.btn3.text())
            self.btn3.setText('')
        self.check_win()
    def btn_4(self):
        if self.btn3.text()=="":
            self.btn3.setText(self.btn4.text())
            self.btn4.setText('')
        elif self.btn8.text()=='':
            self.btn8.setText(self.btn4.text())
            self.btn4.setText('')
        self.check_win()
    def btn_5(self):
        if self.btn1.text()=="":
            self.btn1.setText(self.btn5.text())
            self.btn5.setText('')
        elif self.btn6.text()=='':
            self.btn6.setText(self.btn5.text())
            self.btn5.setText('')
        elif self.btn9.text()=='':
            self.btn9.setText(self.btn5.text())
            self.btn5.setText('')
        self.check_win()
    def btn_6(self):
        if self.btn5.text()=="":
            self.btn5.setText(self.btn6.text())
            self.btn6.setText('')
        elif self.btn2.text()=='':
            self.btn2.setText(self.btn6.text())
            self.btn6.setText('')
        elif self.btn7.text()=='':
            self.btn7.setText(self.btn6.text())
            self.btn6.setText('')
        elif self.btn10.text()=='':
            self.btn10.setText(self.btn6.text())
            self.btn6.setText('')
        self.check_win()
    def btn_7(self):
        if self.btn3.text()=="":
            self.btn3.setText(self.btn7.text())
            self.btn7.setText('')
        elif self.btn6.text()=='':
            self.btn6.setText(self.btn7.text())
            self.btn7.setText('')
        elif self.btn8.text()=='':
            self.btn8.setText(self.btn7.text())
            self.btn7.setText('')
        elif self.btn11.text()=='':
            self.btn11.setText(self.btn7.text())
            self.btn7.setText('')
        self.check_win()
        
    def btn_8(self):
        if self.btn4.text()=="":
            self.btn4.setText(self.btn8.text())
            self.btn8.setText('')
        elif self.btn7.text()=='':
            self.btn7.setText(self.btn8.text())
            self.btn8.setText('')
        elif self.btn12.text()=='':
            self.btn12.setText(self.btn8.text())
            self.btn8.setText('')
        self.check_win()     
    def btn_9(self):
        if self.btn5.text()=="":
            self.btn5.setText(self.btn9.text())
            self.btn9.setText('')
        elif self.btn10.text()=='':
            self.btn10.setText(self.btn9.text())
            self.btn9.setText('')
        elif self.btn13.text()=='':
            self.btn13.setText(self.btn9.text())
            self.btn9.setText('')
        self.check_win()
    
    def btn_10(self):
        if self.btn6.text()=="":
            self.btn6.setText(self.btn10.text())
            self.btn10.setText('')
        elif self.btn9.text()=='':
            self.btn9.setText(self.btn10.text())
            self.btn10.setText('')
        elif self.btn11.text()=='':
            self.btn11.setText(self.btn10.text())
            self.btn10.setText('')
        elif self.btn14.text()=='':
            self.btn14.setText(self.btn10.text())
            self.btn10.setText('')
        self.check_win()

    def btn_11(self):
        if self.btn10.text()=="":
            self.btn10.setText(self.btn11.text())
            self.btn11.setText('')
        elif self.btn7.text()=='':
            self.btn7.setText(self.btn11.text())
            self.btn11.setText('')
        elif self.btn12.text()=='':
            self.btn12.setText(self.btn11.text())
            self.btn11.setText('')
        elif self.btn15.text()=='':
            self.btn15.setText(self.btn11.text())
            self.btn11.setText('')    
        self.check_win()
    
    def btn_12(self):
        if self.btn8.text()=="":
            self.btn8.setText(self.btn12.text())
            self.btn12.setText('')
        elif self.btn11.text()=='':
            self.btn11.setText(self.btn12.text())
            self.btn12.setText('')
        elif self.btn16.text()=='':
            self.btn16.setText(self.btn12.text())
            self.btn12.setText('')
        self.check_win()
        
    def btn_13(self):
        if self.btn9.text()=="":
            self.btn9.setText(self.btn13.text())
            self.btn13.setText('')
        elif self.btn14.text()=='':
            self.btn14.setText(self.btn13.text())
            self.btn13.setText('')
        self.check_win()
        
    def btn_14(self):
        if self.btn10.text()=="":
            self.btn10.setText(self.btn14.text())
            self.btn14.setText('')
        elif self.btn13.text()=='':
            self.btn13.setText(self.btn14.text())
            self.btn14.setText('')
        elif self.btn15.text()=='':
            self.btn15.setText(self.btn14.text())
            self.btn14.setText('')
        self.check_win()
        
    def btn_15(self):
        if self.btn11.text()=="":
            self.btn11.setText(self.btn15.text())
            self.btn15.setText('')
        elif self.btn14.text()=='':
            self.btn14.setText(self.btn15.text())
            self.btn15.setText('')
        elif self.btn16.text()=='':
            self.btn16.setText(self.btn15.text())
            self.btn15.setText('')
        self.check_win()
        
    def btn_16(self):
        if self.btn12.text()=="":
            self.btn12.setText(self.btn16.text())
            self.btn16.setText('')
        elif self.btn15.text()=='':
            self.btn15.setText(self.btn16.text())
            self.btn16.setText('')
        self.check_win()
    
    
app = QApplication([])
window = Window()
window.reset()
window.show()
app.exec_()