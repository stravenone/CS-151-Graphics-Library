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
        
class Triangle():
    def _init_(self):
        self.color=''
        self.outline=''
        self.width=None
    
    def fill_color(self,color):
        self.color=color
    
    def shape_outline_color(self,outline):
        self.outline=outline
    
    def triangle_width(self,width):
        self.width=width
    
    def triangle_side_length(self,side_length):
        self.side_length=side_length
    
    def starting_point(self,x1,y1):
        self.x1=x1
        self.y1=y1
    
    def starting_point(self,x2,y2):
        self.x2=x2
        self.y2=y2
   
def starting_point(self,x3,y3):
        self.x1=x3
        self.y1=y3
    
    def triangle_points(self,x1,y1):
        x1=self.x1
        y1=self.y1
        x2=self.x2
        y2=self.y2
        x3=self.x3
        y3=self.y3
        side_length=self.side_length
        color = self.color
        outline = self.outline
        width = self.width
        
        point1=[x1,y1] 
        point2=[x2,y2]
        point3=[x3,y3]        
        my_canvas.create_polygon(point1,point2,point3, fill=color, outline=outline, width=width)
        master.mainloop()


        
class Messing_With_Shapes(Frame):  
    def mouse_enter(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
        self.draw.itemconfig(CURRENT, fill="red")

    def mouse_leave(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
        self.draw.itemconfig(CURRENT, fill="blue")

    def create_shape(self):
        self.draw = Canvas(self, width=500, height=500)
        self.draw.pack(side=LEFT)
        
        points = [0,0,200,200,0,200]
        triangle = self.draw.create_polygon(points, outline='green', fill='yellow', width=3)

        self.draw.tag_bind(triangle, "<Any-Enter>", self.mouseEnter)
        self.draw.tag_bind(triangle, "<Any-Leave>", self.mouseLeave)
    
    def move_shape(self):
        for x in range(50):
            y=x=5
            my_canvas.move(self,x,y)
            my_canvas.update()
            
    def paint(self):
        x1=(self.x-1)
        y1=(self.y-1)
        x2=(self.x+1)
        y2=(self.y+1)
        my_canvas.create_oval(x1,y1,x2,y2,fill='green')
    
    master = Tk()
    master.title("Painting using Ovals")
    my_canvas=Canvas(master, width=500, height=150)
    my_canvas.pack(expand = YES, fill = BOTH)
    my_canvas.bind( "<B1-Motion>", paint )
    message=Label(master,text="Use mouse to draw")
    message.pack( side = BOTTOM )
   
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        master.mainloop()

    def pentagon(x,y,z):
        masters = Tk()
        canvas=Canvas(masters, width=200, height=200)
        canvas.pack()
        point1=[x,y]
        point2=[x+30,y+60]
        point3=[x+90,y+60]
        point4=[x+120,y]
        point5=[x+60,y-30]
        point=[point1,point2,point3,point4,point5]
        canvas.create_polygon(point, outline='black', fill=z, width=3)
        masters.mainloop() 

