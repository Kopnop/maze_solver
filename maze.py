import time
from cell import *
from graphics import *

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            current_x = self.x1 + i*self.cell_size_x
            col = []
            for j in range(self.num_cols):
                current_y = self.y1 + j*self.cell_size_y
                cell = Cell(self.win, current_x, current_y, current_x+self.cell_size_x, current_y+self.cell_size_y)
                col.append(cell)
                #cell.draw() 
            self._cells.append(col)

        #print("Created cells:",self._cells)
        
        #could draw while creating cells in the loop above, but kept it like that to seperate data and graphics
        self._draw_cells()

        self._animate()

    def _draw_cells(self):
        if self.win is None:
            return
        for col in self._cells:
            for cell in col:
                cell.draw()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)        