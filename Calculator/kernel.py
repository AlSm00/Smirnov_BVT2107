class Evaluator():
    '''Класс, управляющий вычислением выражений'''
    #Расстановка приоритетов. Гарантируется, что операции из нулевого 
    #приоритета будут выполнены раньше, чем операции из первого,
    #из первого - раньше чем из второго, из второго - раньше чем из 
    #третьего
    zero_priority = ['!','SQRT']
    first_priority = ['*','/','MULT']
    second_priority = ['+','-','SUMM']
    third_priority = ['switch_mode','save','del','define','::']


    def __init__(self,comms,constants):
        '''Инициализация команд'''
        self.result = None
        self.expr = 0
        self.comms = comms
        self.macro = {}
        self.mem = constants


    def get_expr(self,expr):
        '''Получение строки, содержащей выражение для вычисления'''
        self.expr = '('+expr+')'


    def evaluate(self):
        '''Основной цикл работы ядра'''
        #Вычисления продолжаются, пока в строке остаются скобки.
        #Само выражение тоже берётся в скобки, поэтому результат всегда число - 
        #результат вычисления самого выражения.
        while '(' in self.expr:
            #сначала находим самую левую скобку - так не нарушиться порядок 
            #действий
            left, right = self.find_br()
            #вычисляем подвыражение в скобках
            val = self.eval_expr(left,right)
            #подставляем результат в основное выражение
            self.apply(left,right,val)
        #результат работы программы - то, что получилось после подстановки
        #результата в главную скобку
        if self.expr in self.mem.keys():
            self.expr = self.mem[self.expr]

        self.result = self.expr


    def find_br(self):
        '''Метод, ищущий скобки'''
        left = 0
        right = len(self.expr)-1
        #начало подвыражения - самая левая открывающаяся скобка 
        for i in range(len(self.expr)):
            if self.expr[i] == '(' and i > left:
                left = i
        
        #конец подвыражения - первая закрывающаяся собка,
        #идущая за началом выражения или иначе - последняя закрывающаяся
        #скобка между началом подвыражения и концом выражения, если идти с конца
        for i in range(len(self.expr)-1,left,-1):
            if self.expr[i] == ')' and i < right:
                right = i
        
        return left, right


    def eval_expr(self,left,right):
        '''Вычисление подвыражения'''
        #сами скобки из выражения исключаются
        cur_expr = self.expr[left+1:right]
        #Разделитель между оперндами - пробел
        ops = cur_expr.split(' ')
        while '' in ops:
            ops.remove('')
        counter = len(ops)
        
        #вычисление операторов нулевого приоритета
        for op in Evaluator.zero_priority:
            i = 0
            while op in ops:
                if ops[i] == op:
                    #сначала вычисляется оператор
                    lapply_dat,rapply_dat,val = self.eval_op(op,i,ops)
                    #затем результат вычислений подставляется в подвыражение
                    ops = self.apply_loc(i,lapply_dat,rapply_dat,ops,val)
                    #цикл начинается с начала
                    i = 0
                i+=1
                if i > counter-1:
                    break

        #Вычисление опреторов первого приоритета аналогично вычислению 
        #операторов нулевого приоритета
        for op in Evaluator.first_priority:
            i = 0
            while op in ops:
                if ops[i] == op:
                    lapply_dat,rapply_dat,val = self.eval_op(op,i,ops)
                    ops = self.apply_loc(i,lapply_dat,rapply_dat,ops,val)
                    i = 0
                i+=1
                if i > counter-1:
                    break

        #Вычисление опреторов второго приоритета аналогично вычислению 
        #операторов нулевого приоритета
        for op in Evaluator.second_priority:
            i = 0
            while op in ops:
                if ops[i] == op:
                    lapply_dat,rapply_dat,val = self.eval_op(op,i,ops)
                    ops = self.apply_loc(i,lapply_dat,rapply_dat,ops,val)
                    i = 0
                i+=1
                if i > counter-1:
                    break

        #Вычисление опреторов третьего приоритета аналогично вычислению 
        #операторов нулевого приоритета
        for op in Evaluator.third_priority:
            i = 0
            while op in ops:
                if ops[i] == op:
                    lapply_dat,rapply_dat,val = self.eval_op(op,i,ops)
                    ops = self.apply_loc(i,lapply_dat,rapply_dat,ops,val)
                    i = 0
                i+=1
                if i > counter-1:
                    break

        return ops


    def apply(self,left,right,value):
        '''Подстановка результатов вычисления подвыражения в выражение'''
        #подстановка происходит так: берётся часть выражения до (,
        #затем берётся часть выражения после ),
        #и, наконец, левая часть выражения конкатенируется с результатом
        #и правой частью выражения
        lhalf = self.expr[:left]
        rhalf = self.expr[right+1:]
        self.expr = lhalf+value[0]+rhalf


    def eval_op(self,op,i,cur_expr):
        ''' Вычисление оператора'''
        #Здесь i - позиция оператора в подвыражении
        #op - сам оператор(точнее, его имя)
        #cur_expr - само подвыражение

        if op != 'del':
            for k in range(len(cur_expr)):
                if cur_expr[k] in self.mem.keys():
                    cur_expr[k] = self.mem[cur_expr[k]]

        operator = None
        #Поиск опретора в comms
        for k in self.comms.keys():
            if k == op:
                operator = self.comms[k]
        
        #lapply_dat, rapply_dat - переменные, которые необходимы для постановки
        #результата вычисления оператора в подвыражение
        lapply_dat,rapply_dat = operator.capture_ops(pos = i,env = cur_expr)
        

        #Вычисление оператора с проверкой ошибок
        value = operator.error_catching()

        return lapply_dat,rapply_dat,value


    def apply_loc(self,i,lapply_dat,rapply_dat,cur_expr,value):
        '''Подстановка результатов вычисления оператора в подвыражение'''
        #Левая часть нового подввыражения - идёт от начала до позиции оператора - 
        #количество левых операндов оператора
        lexpr = cur_expr[:i-lapply_dat]
        rexpr = cur_expr[i+rapply_dat+1:]
        #Левая часть нового подввыражения - идёт от конца до позиции оператора + 
        #количество правых операндов оператора
        expr = lexpr + [value] + rexpr

        return expr


    def push_env(self,name,value):
        self.mem[name] = value
    

    def pop_env(self,name):
        del self.mem[name]


    def push_macro(self,macro,var):
        self.macro[macro] = var