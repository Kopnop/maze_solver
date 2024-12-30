from graphics import *

class Cell():
    def __init__(self, win=None, x1=None, y1=None, x2=None, y2=None):
        self.has_left_wall = True    
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win

    def set_postion(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, x1=None, y1=None, x2=None, y2=None):
        if self.win is None:
            return
        if x1 and y2 and x2 and y2:
            self.set_postion(x1, y1, x2, y2)
        print("Drawing cell at", self.x1, self.y1, self.x2, self.y2)
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")

    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
        color = "gray" if undo else "red"
        from_point = Point((self.x1+self.x2)/2, (self.y1+self.y2)/2)
        to_point = Point((to_cell.x1+to_cell.x2)/2, (to_cell.y1+to_cell.y2)/2)
        self.win.draw_line(Line(from_point, to_point), color)

    # def __str__(self):
    #     return "allo"
    
    def __repr__(self):
        return "Cell:({},{})({},{})".format(self.x1, self.y1, self.x2, self.y2)