import arifm_exc
from basic_op import Operator


class Cadd(Operator):
    def __init__(self):
        super().__init__(name='+',left_op_c=1,right_op_c=1)
    
    def comput(self):
        return str(float(self.left_ops[0]) + float(self.right_ops[0]))
    
    def error_catching(self):
        return super().error_catching(ValueError,IndexError)


class Csub(Operator):
    def __init__(self):
        super().__init__(name='-',left_op_c=1,right_op_c=1)
    
    def comput(self):
        return str(float(self.left_ops[0]) - float(self.right_ops[0]))
    
    def error_catching(self):
        return super().error_catching(ValueError,IndexError)


class Cmul(Operator):
    def __init__(self):
        super().__init__(name='*',left_op_c=1,right_op_c=1)
    
    def comput(self):
        return str(float(self.left_ops[0]) * float(self.right_ops[0]))

    def error_catching(self):
        return super().error_catching(ValueError,IndexError)


class Cdiv(Operator):
    def __init__(self):
        super().__init__(name='/',left_op_c=1,right_op_c=1)
    
    def comput(self):
        return str(float(self.left_ops[0]) / float(self.right_ops[0]))

    def error_catching(self):
        return super().error_catching(ValueError,ZeroDivisionError,IndexError)


class Cfact(Operator):
    def __init__(self):
        super().__init__(name = '!',left_op_c=1,right_op_c=0)
    
    def comput(self):
        res = 1
        for n in range(1,int(self.left_ops[0])+1):
            res = res*n
        return str(res)
    def error_catching(self):
        return super().error_catching(ValueError,arifm_exc.FloatArgumentError,IndexError)


class Cnadd(Operator):
    def __init__(self):
        super().__init__(name = 'SUMM',left_op_c = 1,right_op_c = 1)
    
    def capture_ops(self,env,pos):
        super().capture_ops(pos = pos,env = env)
        self.right_op_c = int(self.left_ops[0])
        self.right_ops = env[pos+1:pos+self.right_op_c+1]

        return self.left_op_c,self.right_op_c

    def comput(self):
        summ = 0
        for i in range(len(self.right_ops)):
            summ += float(self.right_ops[i])
        return str(summ)

    def error_catching(self):
        return super().error_catching(ValueError,arifm_exc.FloatArgumentError,IndexError)


class Cnmul(Operator):
    def __init__(self):
        super().__init__(name = 'MULT',left_op_c = 1,right_op_c = 1)
    
    def capture_ops(self,env,pos):
        super().capture_ops(pos = pos,env = env)
        self.right_op_c = int(self.left_ops[0])
        self.right_ops = env[pos+1:pos+self.right_op_c+1]

        return self.left_op_c,self.right_op_c

    def comput(self):
        mul_res = 1
        for i in range(len(self.right_ops)):
            mul_res *= float(self.right_ops[i])
        return str(mul_res)

    def error_catching(self):
        return super().error_catching(ValueError,arifm_exc.FloatArgumentError,IndexError)


class Csqrt(Operator):
    def __init__(self):
        super().__init__(name = 'SQRT', left_op_c=0, right_op_c=1)
    def comput(self):
        if float(self.right_ops[0]) < 0:
            raise arifm_exc.ArgumentBelowZeroError
        i = 1
        sqrt = 0
        while i*i <= float(self.right_ops[0]):
            sqrt = i*i
            i+=1
        
        if sqrt == 0:
            sqrt = 1
        
        for _ in range(10):
            sqrt = 0.5*(sqrt + float(self.right_ops[0])/sqrt)
        
        return str(sqrt)

    def error_catching(self):
        return super().error_catching(ValueError,arifm_exc.ArgumentBelowZeroError,IndexError)

        

arifmetics = {
    '+':Cadd(),
    '-':Csub(),
    '*':Cmul(),
    '/':Cdiv(),
    '!':Cfact(),
    'SUMM':Cnadd(),
    'MULT':Cnmul(),
    'SQRT':Csqrt()
}

constants = {
    'pi':'3.1415926535',
    'e':'2.7182818284',
    'phi':'1.6180339887',
    'psi':'1.465571231'
}