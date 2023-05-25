from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from blabla import *
from Death import *
from xox import *


class ChoiceWin(QWidget):
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
        self.xxx = QPushButton(xxx_txt)
        self.death = QPushButton(death_txt)
        self.Choice = QLabel(choice_txt)

        self.setFont(font5)
        self.Choice.setFont(QFont('Comic Sans Ms', 40))

        self.HLayout1 = QHBoxLayout()
        self.VLayout = QVBoxLayout()
        self.HLayout1.addWidget(self.xxx, alignment= Qt.AlignTop)
        self.HLayout1.addWidget(self.death, alignment= Qt.AlignTop)
        self.VLayout.addWidget(self.Choice, alignment= Qt.AlignVCenter)
        self.VLayout.addLayout(self.HLayout1)
        self.setLayout(self.VLayout)

    def xxx_game(self):
        self.game = XXX_Game()


    def death_game(self):
        self.game = Death_Game()
    
    def connects(self):
        self.xxx.clicked.connect(self.xxx_game)
        self.death.clicked.connect(self.death_game)

