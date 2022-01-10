from types import DynamicClassAttribute
import psycopg2, week_count

class DB():
    def __init__(self):
        self.conn = psycopg2.connect(database = 'timetable',
                                     user = 'postgres',
                                     password = 'pstg54YuiOp890',
                                     host = 'localhost',
                                     port = '5432')
        self.cursor = self.conn.cursor()
        self.days = ['mon','tue','wed','thu','fri','sat']
    
    def _get_day_timetable(self,day,week):
        self.cursor.execute("SELECT subject,room_numb,start_time FROM timetable.timetable WHERE day=\'" + day + '\' AND week=' + str(week) + ';')
        res = self.cursor.fetchall()
        timetab = []
        for i in range(len(res)):
            output = []
            subj = res[i][0]
            output.append(subj)
            room_numb = res[i][1]
            output.append(room_numb)
            start_time = res[i][2]
            output.append(start_time)
            self.cursor.execute("SELECT full_name FROM timetable.teacher WHERE subject=" + '\'' + subj + '\'' +';')
            temp = self.cursor.fetchall()
            teacher = temp[0][0]
            output.append(teacher)
            timetab.append(output)
        return timetab
    
    def get_timetable(self,day):
        if day != 'current_week' and day != 'next_week':
            week = week_count.get_week()
            data = self._get_day_timetable(day,week)
            output = ''
            for i in range(len(data)):
                if data[i][0] != ' ':
                    output += 'Предмет: ' + data[i][0] + '\n'
                    output += 'Аудитория: ' + data[i][1] + '\n'
                    output += 'Начало: ' + data[i][2] + '\n'
                    output += 'Преподаватель: ' + data[i][3] + '\n'
                    output += '\n'
        elif day == 'current_week':
            week = week_count.get_week()
            output = ''
            for day in self.days:
                data = self._get_day_timetable(day,week)
                output += day 
                output += '\n'
                for i in range(len(data)):
                    if data[i][0] != ' ':
                        output += 'Предмет: ' + data[i][0] + '\n'
                        output += 'Аудитория: ' + data[i][1] + '\n'
                        output += 'Начало: ' + data[i][2] + '\n'
                        output += 'Преподаватель: ' + data[i][3] + '\n'
                        output += '\n'
        elif day == 'next_week':
            week = week_count.get_week()
            if week:
                week = 0
            else:
                week = 1
            output = ''
            for day in self.days:
                data = self._get_day_timetable(day,week)
                output += day 
                output += '\n'
                for i in range(len(data)):
                    if data[i][0] != ' ':
                        output += 'Предмет: ' + data[i][0] + '\n'
                        output += 'Аудитория: ' + data[i][1] + '\n'
                        output += 'Начало: ' + data[i][2] + '\n'
                        output += 'Преподаватель: ' + data[i][3] + '\n'
                        output += '\n'
        return output