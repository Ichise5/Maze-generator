from tkinter import Tk, BOTH, Canvas

class Point():
    x: int
    y: int
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line():
    p1: Point
    p2: Point

    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2
    
    @classmethod
    def from_4points(cls, x1:int, y1:int, x2:int, y2:int):
        return cls(Point(x1,y1), Point(x2,y2))

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y,
                           fill=fill_color, width=2)
        
class Window():
    def __init__(self, width: int , height:int):
        self.__root = Tk()   
        self.__root.title("Maze Generator")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canvas, fill_color)

