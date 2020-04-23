from graphics import *

win_size = 920
win = GraphWin("Alyssa Drawing Game", win_size, win_size)
win.setBackground('white')

start_point = 10
sq_size = 300

p1 = Point(start_point, start_point)
p2 = Point(start_point + sq_size * 3, start_point + sq_size * 3)

r_frame = Rectangle(p1, p2)
r_frame.setWidth(5)
r_frame.draw(win)

l1 = Line(Point(start_point, start_point + sq_size), Point(start_point + sq_size*3, start_point + sq_size))
l1.draw(win)
l1.setWidth(5)

l2 = Line(Point(start_point, start_point + sq_size*2), Point(start_point + sq_size*3, start_point + sq_size * 2))
l2.draw(win)
l2.setWidth(5)

l3 = Line(Point(start_point+sq_size, start_point),Point(start_point+sq_size,start_point+sq_size*3))
l3.draw(win)
l3.setWidth(5)

l4 = Line(Point(start_point+sq_size*2, start_point),Point(start_point+sq_size*2,start_point+sq_size*3))
l4.draw(win)
l4.setWidth(5)


#pt = Point(100, 100)
#pt.draw(win)

#cir = Circle(pt, 30)
#cir.draw(win)

while True:
    click_point = win.getMouse()
    
    sq_x = 2
    sq_y = 2
    if click_point.x > (start_point + sq_size*2):
        sq_x = 3
    elif click_point.x < (start_point + sq_size):
        sq_x = 1

    if click_point.y > (start_point + sq_size*2):
        sq_y = 3
    elif click_point.y < (start_point + sq_size):
        sq_y = 1

    print("Square column = {}, row = {}".format(sq_x, sq_y))

    rx = Point(start_point + (sq_x - 1)*sq_size, start_point + (sq_y - 1) * sq_size)
    ry = Point(start_point + (sq_x)*sq_size, start_point + (sq_y) * sq_size)
    sq = Rectangle(rx, ry)
    sq.setFill("green")
    sq.draw(win)

    new_circle = Circle(click_point, 50)
    new_circle.setWidth(5)
    new_circle.draw(win)


win.getMouse()

win.close()

