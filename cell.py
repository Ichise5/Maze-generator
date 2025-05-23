from graphics import *

class Cell():
    def __init__(self,
                 win:Window,
                 left_wall:bool = True,
                 right_wall:bool = True,
                 top_wall:bool = True,
                 bottom_wall:bool = True,
                 x1:int = -1,
                 x2:int = -1,
                 y1:int = -1,
                 y2:int = -1,
                 visited:bool = False):
        
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self.set_points(x1, y1, x2, y2)
        self.__win = win
        self._fill_color = "black"
        self.visited = visited
    
    def __repr__(self):
        string =  f"""These are the individual points:
x1: {self.__x1}, y1: {self.__y1}
x2: {self.__x2}, y2: {self.__y2}
has left: {self.has_left_wall}, has right: {self.has_right_wall}
has top: {self.has_top_wall}, has bottom: {self.has_bottom_wall}
"""
        return string
    
    def set_points(self, x1, y1, x2, y2):
        if x1<x2:
            self.__x1 = x1
            self.__x2 = x2
        else:
            self.__x1 = x2
            self.__x2 = x1
        
        if y1<y2:
            self.__y1 = y1
            self.__y2 = y2
        else:
            self.__y1 = y2
            self.__y2 = y1

    def draw(self,
             x1 = None,
             x2 = None,
             y1 = None ,
             y2 = None):
        
        if x1 is None:
            x1 = self.__x1
        if x2 is None:
            x2 = self.__x2
        if y1 is None:
            y1 = self.__y1
        if y2 is None:
            y2 = self.__y2

        self.set_points(x1, y1, x2, y2)

        self.left_wall = Line.from_4points(self.__x1, self.__y1, self.__x1, self.__y2)
        self.right_wall = Line.from_4points(self.__x2, self.__y1, self.__x2, self.__y2)
        self.top_wall = Line.from_4points(self.__x1, self.__y1, self.__x2, self.__y1)
        self.bottom_wall = Line.from_4points(self.__x1, self.__y2, self.__x2, self.__y2)
        
        if self.has_left_wall:
            self.__win.draw_line(self.left_wall, self._fill_color)
        else:
            self.__win.draw_line(self.left_wall, "white")
        
        if self.has_right_wall:
            self.__win.draw_line(self.right_wall, self._fill_color)
        else:
            self.__win.draw_line(self.right_wall, "white")
        
        if self.has_top_wall:
            self.__win.draw_line(self.top_wall, self._fill_color)
        else:
            self.__win.draw_line(self.top_wall, "white")
        
        if self.has_bottom_wall:
            self.__win.draw_line(self.bottom_wall, self._fill_color)
        else:
            self.__win.draw_line(self.bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        center1 = Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2)
        center2 = Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)
        
        if undo:
            self.__win.draw_line(Line(center1, center2), "gray")
        else:
            self.__win.draw_line(Line(center1, center2), "red")
