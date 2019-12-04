import tkinter
#creates window
window = tkinter.Tk()
window.title("GUI")

# creates canvas
canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()



class hexagon(object):
    def __init__(self):
        self.center_x = None
        self.center_y = None
        self.side_length = None
        self.color = ''
        self.outline = ''
        self.width = None
    def center_coordinates(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
    def hex_side_length(self, side_length):
        self.side_length = side_length
    def hex_color(self,color):
        self.color = color
    def hex_outline(self, outline):
        self.outline = outline
    def hex_width(self, width):
        self.width = width
    def create_hex(self):
        center_x = self.center_x
        center_y = self.center_y
        side_length = self.side_length
        color = self.color
        outline = self.outline
        width = self.width
        
        z = ((side_length**2) - ((side_length/2)**2))**.5
        point1 = [center_x + side_length, center_y]
        point2 = [center_x + side_length/2, center_y + z]
        point3 = [center_x - side_length/2,center_y + z]
        point4 = [center_x - side_length, center_y]
        point5 = [center_x - side_length/2, center_y - z]
        point6 = [center_x + side_length/2, center_y - z]
    
        canvas.create_polygon(point1, point2, point3, point4, point5, point6, fill=color, outline = outline, width = width)
