import psycopg2


class DB():
    def __init__(self):
        self.conn = psycopg2.connect(database = 'timetable',
                                     user = 'postgres',
                                     password = 'pstg54YuiOp890',
                                     host = 'localhost',
                                     port = '5432')
        self.cursor = self.conn.cursor()
        self.days = ['mon','tue','wed','thu','fri','sat']
        self.pairs_id = {'mon':[0,1,2,29,30],
            'tue':[6,7,8,31,32],
            'wed':[33,34,35,36,37],
            'thu':[14,15,16,38,39],
            'fri':[18,20,22,40,41],
            'sat':[24,26,42,43,44]}
        self.subjects = ['CT','CG','English','Ecology','PE','Philosophy','IiIT','LA','HM']
        self.teacher_id = 10
    
    def get_day_timetable(self,day,week):
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
            self.cursor.execute("SELECT full_name FROM timetable.teacher WHERE subject=" + '\'' + subj + '\'' +'\nORDER BY id;')
            temp = self.cursor.fetchall()
            teacher = temp[0][0]
            output.append(teacher)
            timetab.append(output)
        return timetab
    
    def update_row(self,pair_id,subject,room_numb,start_time):
        if subject not in self.subjects:
            subject = ' '
            room_numb = ''
            start_time = ''
        req = 'UPDATE timetable.timetable\nSET subject=\''+subject
        req += '\',\nroom_numb=\''+room_numb
        req += '\',\nstart_time=\''+start_time
        req += '\'\nWHERE id= '+str(pair_id) + ';'
        self.cursor.execute(req)
        self.conn.commit()
