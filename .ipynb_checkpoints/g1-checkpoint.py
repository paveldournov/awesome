#
# Draw Random Circles with colors
#
# Copyright Dasha Dournova, 2018
#

from graphics import *
import random
import time

def main():
    win = GraphWin("Investment Growth", 640, 480)
    win.setBackground("blue")
    #win = GraphWin("Circle", 100, 100)


#    while True:
#        p = win.getMouse()
#        c = Circle(p, 5)
#        c.setFill("yellow")
#        c.draw(win)

    colors = ["yellow", "purple", "green", "white", "orange", "red", "black", "pink"]
    print(colors[0])
    print(colors[6])


    for i in range(1,100):
        x = random.randint(1, 640)
        y = random.randint(1, 480)
        r = random.randint(1,40)
        ci = random.randint(0, 6)
        cs = colors[ci]
        c = Circle(Point(x,y), r)
        c.setFill(cs)
        c.draw(win)
        time.sleep(0.03)

    win.getMouse()
    win.close()

main()
