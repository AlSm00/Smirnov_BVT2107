class ArgumentBelowZeroError(ArithmeticError):
    def __str__(self):
        return "Argument is below zero."
 
    
class FloatArgumentError(ArithmeticError):
    def __str__(self):
        return "Argument type is 'Float', 'Int' type expected."


class OperandError(ArithmeticError):
    def __str__(self):
        return "Not enough operands"