from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800,600)

    # lineA = Line(Point(10,10), Point(100,100))
    # lineB = Line(Point(0,100), Point(100,100))
    # win.draw_line(lineA, "red")
    # win.draw_line(lineB, "blue")

    # cellA = Cell(win)
    # cellA.set_postion(200, 200, 300, 300)
    # cellB = Cell(win)
    # #cellB.set_postion(500, 400, 600, 500)
    # cellA.has_bottom_wall = False
    # cellA.draw()
    # cellB.draw(500, 400, 600, 500)

    # cellA.draw_move(cellB)

#__init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
    maze = Maze(50,50, 10, 10, 50, 50, win)

    win.wait_for_close()


main()