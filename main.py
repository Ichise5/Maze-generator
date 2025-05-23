from graphics import *
from maze import *
import sys


def main():
    sys.setrecursionlimit(int(1e5))
    win = Window(800, 600)


    custom_maze = Maze(x1=10, y1=10,
                       num_rows=5, num_cols=5,
                       cell_size_x=40, cell_size_y=40, 
                       win=win,seed= 10)
    
    #custom_maze._Maze__break_walls_r(0,0)
    #custom_maze._Maze__reset_cells_visited()

    custom_maze.solve()
    win.wait_for_close()

main()