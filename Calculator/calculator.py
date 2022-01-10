import sys
import main
from PyQt5.QtWidgets import *

ev = main.init()

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QGridLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_back = QPushButton("Back", self)
        self.hbox_first.addWidget(self.b_back,0,0)

        self.b_clr = QPushButton("Clear", self)
        self.hbox_first.addWidget(self.b_clr,0,3)
        
        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0,1,0)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1,1,1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2,1,2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3,1,3)

        self.b_4 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_4,2,0)

        self.b_5 = QPushButton("5", self)
        self.hbox_first.addWidget(self.b_5,2,1)

        self.b_6 = QPushButton("6", self)
        self.hbox_first.addWidget(self.b_6,2,2)

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7,2,3)

        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8,3,1)

        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9,3,2)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus,4,0)

        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus,4,1)

        self.b_mul = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_mul,4,2)

        self.b_div = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_div,4,3)

        self.b_lbr = QPushButton("(", self)
        self.hbox_first.addWidget(self.b_lbr,5,0)

        self.b_rbr = QPushButton(")", self)
        self.hbox_first.addWidget(self.b_rbr,5,1)

        self.b_dot = QPushButton('.', self)
        self.hbox_first.addWidget(self.b_dot,5,2)

        self.b_pi = QPushButton('pi',self)
        self.hbox_first.addWidget(self.b_pi,6,0)

        self.b_e = QPushButton('e',self)
        self.hbox_first.addWidget(self.b_e,6,1)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_back.clicked.connect(lambda: self._button("Back"))
        self.b_plus.clicked.connect(lambda: self._button("+"))
        self.b_clr.clicked.connect(lambda: self._button("clr"))
        self.b_mul.clicked.connect(lambda: self._button("*"))
        self.b_div.clicked.connect(lambda: self._button("/"))
        self.b_pi.clicked.connect(lambda: self._button("pi"))
        self.b_dot.clicked.connect(lambda: self._button("."))
        self.b_e.clicked.connect(lambda: self._button("e"))
        self.b_minus.clicked.connect(lambda: self._button("-"))
        self.b_result.clicked.connect(self._result)

        self.b_lbr.clicked.connect(lambda: self._button("("))
        self.b_rbr.clicked.connect(lambda: self._button(")"))

        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))


    def _button(self, param):
        line = self.input.text()
        if param == '+' or param == '-' or param == '*' or param == '/' or param == 'e' or param == 'pi' :
            self.input.setText(line + ' ' + param + ' ')
        elif param == '(':
            self.input.setText(line + ' (')
        elif param == ')':
            self.input.setText(line + ') ')
        elif param == 'Back':
            self.input.setText(line[:-1])
        elif param == 'clr':
            self.input.setText('')
        else:
            self.input.setText(line + param)


    def _result(self):
        res = main.comput(ev = ev,line = self.input.text())
        self.input.setText(res)

app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
