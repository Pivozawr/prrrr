from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from blabla import *
from final import *
from inff import *

class XXX_Game(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()#how window is looking like
        self.initUI()#create and change graphical elements
        self.connects()#create connections btw elements
        self.show()#starting
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(500, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.board = [0] * 9
        self.turn = 1
        self.winner = 0
        self.buttonList = []
        

        grid = QGridLayout()
        for i in range(3):
            for j in range(3):
                button = QPushButton('')
                button.setMinimumSize(150,150)
                button.clicked.connect(self.Click)
                button.setFont(font5)
                self.buttonList.append(button)
                grid.addWidget(button, i, j)
        
        self.info = QPushButton('INFO')
        self.back = QPushButton('BACK')
        self.reset = QPushButton('RESET')
        
        self.info.setMinimumSize(150,50)
        self.info.setMinimumSize(100,50)
        self.back.setMinimumSize(100,50)
        self.reset.setFont(font5)
        self.info.setFont(font5)
        self.back.setFont(font5)
        
        self.layout = QVBoxLayout()
        self.Hlayout = QHBoxLayout()


        self.Hlayout.addWidget(self.back, alignment= Qt.AlignLeft)
        self.Hlayout.addWidget(self.reset, alignment= Qt.AlignCenter)
        self.Hlayout.addWidget(self.info, alignment= Qt.AlignRight)
        self.layout.addLayout(self.Hlayout)
        self.layout.addLayout(grid)
        self.setLayout(self.layout)
        

        

    def Click(self):
        button = self.sender()
        index = self.buttonList.index(button)

        

        if self.board[index] == 0 and self.winner == 0:
            button.setText('X' if self.turn == 1 else 'O')
            self.board[index] = self.turn
            self.turn = 3 - self.turn # 1 -> 2, 2 -> 1

            self.checkWinner()

            
    

    def checkWinner(self):
        win_options = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]]
        ]
        for option in win_options:
            if option == [1,1,1]:                
                self.winner = 'Выиграли Крестики'
                self.fin = Final1()
                

            elif option == [2,2,2]:
                self.winner = 'Выиграли Нолики'
                self.fin = Final2()
                self.fin.show()
                
            
            elif not 0 in self.board:
                self.winner = 'Ничья'
                self.fin = Final3()
                

    def to_choice(self):
        self.close()
       
    def to_info(self):
        self.I = Inff()    

    def resett(self):
        self.close()
        self.b = XXX_Game()
        self.b.show()
        

    def connects(self):
        self.back.clicked.connect(self.to_choice)
        self.info.clicked.connect(self.to_info)
        self.reset.clicked.connect(self.resett)
