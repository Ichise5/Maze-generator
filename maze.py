from graphics import *
from cell import *
from time import sleep
import random

class Maze():
    __cells: list

    def __init__(
        self,
        x1:int,
        y1:int,
        num_rows:int,
        num_cols:int,
        cell_size_x: int,
        cell_size_y:int,
        win:Window|None = None,
        seed: int|None = None,
        create_cell_speed:float = 0.05,
        break_walls_speed:float = 0.05,
        solve_speed:float = 0.1
    ):
        
        self.__x = x1
        self.__y = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.__seed = seed
        self.__create_speed = create_cell_speed
        self.__break_walls_speed = break_walls_speed
        self.__solve_speed = solve_speed

        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            local_cells =[]
            for j in range(self.__num_rows):
                local_cells.append(Cell(self.__win,
                                            left_wall=True,
                                            right_wall=True,
                                            top_wall=True,
                                            bottom_wall=True,
                                            x1=self.__x+i*self.__cell_size_x,
                                            x2=self.__x+(i+1)*self.__cell_size_x,
                                            y1=self.__y+j*self.__cell_size_y,
                                            y2=self.__y+(j+1)*self.__cell_size_y))
            self.__cells.append(local_cells)
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j, self.__create_speed)

        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()
     


    def __draw_cell(self, i:int, j:int, draw_speed:float):
        if self.__win is None:
            return
        self.__cells[i][j].draw()
        self._animate(draw_speed)
        pass

    def _animate(self, time:float):
        self.__win.redraw()
        sleep(time)
        pass

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0, self.__break_walls_speed)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1,self.__num_rows-1, self.__break_walls_speed)

    def __break_walls_r(self, i:int, j:int):
        self.__cells[i][j].visited = True

        while 1:
            to_visit = [] 
            #print(f"Current cell: {[i,j]}")
            for cell_pos in [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]: #left, right, top, bottom
                    try:
                        if not self.__cells[cell_pos[0]][cell_pos[1]].visited:
                            if cell_pos[0] >= 0 and cell_pos[1] >= 0:
                                to_visit.append(cell_pos)
                    except IndexError:
                        continue
            #print(f"Cells to visit: {to_visit}")

            if not to_visit:
                self.__draw_cell(i,j, self.__break_walls_speed)
                return
            
            pos = random.randrange(len(to_visit))
            to_go = to_visit[pos]

            #print(f"Going to cell: {to_go}")
            if to_go[0] < i: #go left
                self.__cells[i][j].has_left_wall = False
                self.__cells[to_go[0]][to_go[1]].has_right_wall = False
            elif to_go[0] > i: #go right
                self.__cells[i][j].has_right_wall = False
                self.__cells[to_go[0]][to_go[1]].has_left_wall = False
            elif to_go[1] < j: #go top
                self.__cells[i][j].has_top_wall = False
                self.__cells[to_go[0]][to_go[1]].has_bottom_wall = False
            elif to_go[1] > j: #go bottom
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[to_go[0]][to_go[1]].has_top_wall = False
            
            self.__break_walls_r(to_go[0], to_go[1])
    
    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def solve(self)-> bool:
        return self.__solve_r(0,0) 
    
    def __solve_r(self,i: int, j:int) -> bool:
        self._animate(self.__solve_speed)
        self.__cells[i][j].visited= True

        if i == self.__num_cols-1 and j == self.__num_rows-1:
            return True
        
        for cell_pos in ["left", "right","top", "bottom"]: #for position
            match cell_pos:
                case "left":
                    if i-1>=0:
                        if not self.__cells[i][j].has_left_wall:
                            if not self.__cells[i-1][j].visited:
                                self.__cells[i][j].draw_move(self.__cells[i-1][j])
                                correct_path = self.__solve_r(i-1, j)
                                if correct_path:
                                    return True
                                else:
                                    self.__cells[i][j].draw_move(self.__cells[i-1][j], True)
                case "right":
                    if i+1<self.__num_cols:
                        if not self.__cells[i][j].has_right_wall:
                            if not self.__cells[i+1][j].visited:
                                self.__cells[i][j].draw_move(self.__cells[i+1][j])
                                correct_path = self.__solve_r(i+ 1, j)
                                if correct_path:
                                    return True
                                else:
                                    self.__cells[i][j].draw_move(self.__cells[i+1][j], True)
                case "top":
                    if j-1>=0:
                        if not self.__cells[i][j].has_top_wall:
                            if not self.__cells[i][j-1].visited:
                                self.__cells[i][j].draw_move(self.__cells[i][j-1])
                                correct_path = self.__solve_r(i, j-1)
                                if correct_path:
                                    return True
                                else:
                                    self.__cells[i][j].draw_move(self.__cells[i][j-1], True)
                case "bottom":
                    if j+1<self.__num_rows:
                        if not self.__cells[i][j].has_bottom_wall:
                            if not self.__cells[i][j+1].visited:
                                self.__cells[i][j].draw_move(self.__cells[i][j+1])
                                correct_path = self.__solve_r(i, j+1)
                                if correct_path:
                                    return True
                                else:
                                    self.__cells[i][j].draw_move(self.__cells[i][j+1], True)

        return False