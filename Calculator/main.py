import kernel, arifmetics

def init():
    ev = kernel.Evaluator(arifmetics.arifmetics,arifmetics.constants)
    return ev

def comput(ev,line):
    ev.get_expr(line)
    ev.evaluate()
    return ev.result