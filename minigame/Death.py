from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from blabla import *
from choice import *


class Death_Game(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()#how window is looking like
        self.initUI()#create and changegraphical elements
        self.connects()#create connections btw elements
        self.show()#starting
    
    def set_appear(self):
        self.setWindowTitle(info_title)
        self.resize(inf_width, inf_height)
        self.move(inf_x, inf_y)
    
    def initUI(self):
        self.back = QPushButton(Back)
        self.info = QLabel(txtt)
        self.layout = QVBoxLayout()

        self.setFont(font3)
        
        self.layout.addWidget(self.back, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.info, alignment= Qt.AlignCenter)
        self.setLayout(self.layout)
    
    def to_choice(self):
        self.hide()
        
    
    def connects(self):
        self.back.clicked.connect(self.to_choice)
