from Drawmen import *
from time import sleep

def f(x):
    return x*x

pen_down()
for x in range(0, 7):
    to_point(x,f(x))

sleep(10)
