import sys, database
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("timetable.ui",self)
        self.setWindowTitle("Timetable")
        self.db = database.DB()
        self.days = ['mon','tue','wed','thu','fri','sat']
        self.buttons = [self.pushButton,self.pushButton_2,self.pushButton_3,
            self.pushButton_4,self.pushButton_5,self.pushButton_6]
        self.tables = [self.tableWidget,self.tableWidget_2,self.tableWidget_3,
            self.tableWidget_4,self.tableWidget_5,self.tableWidget_6]
        for i in range(len(self.tables)):
            self.init_table(self.tables[i],self.days[i])
            self.buttons[i].clicked.connect(self.update_table)
        self.pairs_ids = self.db.pairs_id
        

    def init_table(self,table,day):
        data = self.db.get_day_timetable(day,0)
        table.setRowCount(5)
        for i in range(len(data)):
            table.setItem(i,0, QtWidgets.QTableWidgetItem(data[i][1]))
            table.setItem(i,1, QtWidgets.QTableWidgetItem(data[i][0]))
            table.setItem(i,2, QtWidgets.QTableWidgetItem(data[i][3]))
            table.setItem(i,3, QtWidgets.QTableWidgetItem(data[i][2]))
  
    
    def update_table(self):
        num = self.tabWidget.currentIndex()
        day = self.days[num]
        subjects = []
        start_times = []
        room_numbs = []
        for i in range(5):
            try:
                subject = self.tables[num].item(i,1).text()
                subjects.append(subject)
            except AttributeError:
                subjects.append(' ')
            
            try:
                room_numb = self.tables[num].item(i,0).text()
                room_numbs.append(room_numb)
            except AttributeError:
                room_numbs.append('')

            try:
                start_time = self.tables[num].item(i,3).text()
                start_times.append(start_time)
            except AttributeError:
                start_times.append('')
        

        for i in range(5):
            pair_id = self.pairs_ids[day][i]
            self.db.update_row(pair_id,subjects[i],room_numbs[i],start_times[i])


        for i in range(6):
            self.init_table(self.tables[i],self.days[i])


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(386)
widget.setFixedWidth(628)
widget.show()
sys.exit(app.exec_())
