from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from infa import *
from blabla import *
from choice import *



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
        self.Hello = QLabel(hello_txt)
        self.Info = QPushButton(Info)
        self.Start = QPushButton(butt_start_txt)
        
        self.Info.setStyleSheet("color: rgb(0,0,255)")
        self.Start.setStyleSheet("color: rgb(0,255,0)")

        self.Hlayout = QHBoxLayout()
        self.Vlayout = QVBoxLayout()
        self.Hlayout.addWidget(self.Info, alignment = Qt.AlignLeft)
        self.Vlayout.addWidget(self.Hello, alignment = Qt.AlignCenter)
        self.Vlayout.addWidget(self.Start, alignment = Qt.AlignCenter)
        self.Vlayout.addLayout(self.Hlayout)
        self.setLayout(self.Vlayout)

        self.Info.setFont(font4)
        self.Hello.setFont(QFont('Comic Sans Ms', 40))
        self.Start.setFont(font5)

    def nxt_page(self):
        self.ch = ChoiceWin()
        self.close()

    def info_page(self):
        self.ip = InfoWin()

    def connects(self):
        self.Start.clicked.connect(self.nxt_page)
        self.Info.clicked.connect(self.info_page)







app = QApplication([])
mw = MainWin()
app.exec_()