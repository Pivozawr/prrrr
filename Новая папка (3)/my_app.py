from instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()#how window is looking like
        self.initUI()#create and changegraphical elements
        self.connects()#create connections btw elements
        self.show()#starting

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setFont(QFont('Comic Sans MS', 25))
        self.instruction = QLabel(txt_instruction)
        self.instruction.setFont(QFont('Comic Sans MS', 12))
        self.button = QPushButton(txt_next)
        self.button.setFont(QFont('Comic Sans MS', 12))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        


    def connects(self):
        self.button.clicked.connect(self.next_click)
    
    def next_click(self):
        self.tw = TestWin()
        self.hide()
        



    

app = QApplication([])
mw = MainWin()
app.exec_()