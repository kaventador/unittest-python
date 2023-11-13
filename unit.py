

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y == 0:
        return ZeroDivisionError("can't devide zero")
    return x,y

add(5,4)
subtract(5,4)
multiply(5,4)
division(5,4)