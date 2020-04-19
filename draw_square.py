from graphics import *

win = GraphWin("Alyssa Drawing Game", 500, 500)
win.setBackground('white')

start_point = 10
sq_size = 100

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

win.getMouse()
win.close()

