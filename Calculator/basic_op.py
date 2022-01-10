class Operator():
    def __init__(self,name,left_op_c,right_op_c,error_catch = True):
        self.name = name
        self.left_op_c = left_op_c
        self.right_op_c = right_op_c
        self.error_catch = error_catch
        self.env = None
        self.pos = None


    def capture_ops(self,pos,env):
        self.left_ops = env[pos-self.left_op_c:pos]
        self.right_ops = env[pos+1:pos+self.right_op_c+1]

        return self.left_op_c,self.right_op_c
 
    
    def error_catching(self,*exceptions):
        '''Метод, обрабатывающий ошибки. Максимальное число ошибок - 3.'''
#Возможно отключение обработки ошибок при инициализации оператора.
        if self.error_catch:
            k = len(exceptions)
            self.exceptions = exceptions
#Возможна настройка того, какие исключения будут обрабатываться.
#(Параметр *exceptions)

            if k == 1:
                def catch_error(self):
                    try:
                        result = self.comput()
                    except self.exceptions[0]:
                        result = str(self.exceptions[0])
                    return result

            elif k == 2:
                def catch_error(self):
                    try:
                        result = self.comput()
                    except self.exceptions[0]:
                        result = str(self.exceptions[0])
                    except self.exceptions[1]:
                        result = str(self.exceptions[1])
                    return result

            elif k == 3:
                def catch_error(self):
                    try:
                        result = self.comput()
                    except self.exceptions[0]:
                        result = str(self.exceptions[0])
                    except self.exceptions[1]:
                        result = str(self.exceptions[1])
                    except self.exceptions[2]:
                        result = str(self.exceptions[2])
                    return result

        else:
            def catch_error(self):
                return self.comput()
        
        result = catch_error(self)
        return result

            
    def comput(self):
        pass