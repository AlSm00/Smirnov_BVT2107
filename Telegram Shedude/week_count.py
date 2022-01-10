import time

def get_week():
    w = time.strftime('%W')
    w = int(w) -34
    w = int(w)%2
    return w