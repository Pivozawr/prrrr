from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from blabla import *



class Final1(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()#how window is looking like
        self.initUI()#create and changegraphical elements
        self.connects()#create connections btw elements
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(500, 500)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt = QLabel(winner1)
        self.back = QPushButton(back_txt)

        self.txt.setFont(font5)
        self.back.setFont(font5)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.txt, alignment= Qt.AlignCenter)
        self.layout.addWidget(self.back, alignment= Qt.AlignBottom)
        self.setLayout(self.layout)

    def to_choice(self):
        self.close()
    
    def connects(self):
        self.back.clicked.connect(self.to_choice)

class Final2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()#how window is looking like
        self.initUI()#create and changegraphical elements
        self.connects()#create connections btw elements
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(500, 500)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt = QLabel(winner2)
        self.back = QPushButton(back_txt)

        self.txt.setFont(font5)
        self.back.setFont(font5)
        
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.txt, alignment= Qt.AlignCenter)
        self.layout.addWidget(self.back, alignment= Qt.AlignBottom)
        self.setLayout(self.layout)

    def to_choice(self):
        self.close()
    
    def connects(self):
        self.back.clicked.connect(self.to_choice)

class Final3(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()#how window is looking like
        self.initUI()#create and changegraphical elements
        self.connects()#create connections btw elements
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(500, 500)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt = QLabel(tie)
        self.back = QPushButton(back_txt)

        self.txt.setFont(font5)
        self.back.setFont(font5)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.txt, alignment= Qt.AlignCenter)
        self.layout.addWidget(self.back, alignment= Qt.AlignBottom)
        self.setLayout(self.layout)

    def to_choice(self):
        self.close()
    
    def connects(self):
        self.back.clicked.connect(self.to_choice)