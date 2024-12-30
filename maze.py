import random
import time
from cell import *
from graphics import *

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            current_y = self.y1 + i*self.cell_size_y
            col = []
            for j in range(self.num_rows):
                current_x = self.x1 + j*self.cell_size_x
                
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
        
    # def draw_cell(self, i, j):
    #     if self.win is None:
    #         return
    #     self._cells[i][j].draw()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.1)   

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._cells[0][0].draw()
        self._cells[self.num_cols-1][self.num_rows-1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_be_visited = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_be_visited.append((i-1, j))
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                to_be_visited.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_be_visited.append((i, j-1))
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                to_be_visited.append((i, j+1))
            if not to_be_visited:
                self._cells[i][j].draw()
                return
            random_direction = random.choice(to_be_visited)
            if i > random_direction[0]:
                self._cells[i][j].has_top_wall = False
                self._cells[random_direction[0]][random_direction[1]].has_bottom_wall = False
            elif i < random_direction[0]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[random_direction[0]][random_direction[1]].has_top_wall = False
            elif j > random_direction[1]:
                self._cells[i][j].has_left_wall = False
                self._cells[random_direction[0]][random_direction[1]].has_right_wall = False
            else: #j < random_direction[1]:
                self._cells[i][j].has_right_wall = False
                self._cells[random_direction[0]][random_direction[1]].has_left_wall = False
            self._break_walls_r(random_direction[0], random_direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        to_be_visited = []
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self.solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
            
        if i < self.num_cols-1 and not self._cells[i+1][j].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self.solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
            
        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self.solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
            
        if j < self.num_rows-1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self.solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False
