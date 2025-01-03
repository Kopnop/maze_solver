from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        pass

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line, color="black"):
        line.draw(self.__canvas, color)
        

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, color="black"):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=color, width = 2)