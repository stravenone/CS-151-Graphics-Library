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
class snowflake(object):
    def __init__(self):
        self.side_length = None
        self.centerX = None
        self.centerY = None
        
    def length(self, side_length):
        self.side_length = side_length
    def centerXY(self, centerX, centerY):
        self.centerX = centerX
        self.centerY = centerY
    def create_snowflake(self):
        centerX = self.centerX
        centerY = self.centerY
        side_length = self.side_length
        
        dec_pos = side_length*(4/5)
        dec_length = side_length/4

        point1 = [centerX - (side_length)/2, centerY + (side_length)/2**.33]

        p1_dec1_p1 = [(centerX - (dec_pos)/2), (centerY + (side_length)/2**.33)]
        p1_dec1_p2 = [centerX - (dec_pos)/2, centerY + (dec_pos)/2**.33]
        p1_dec1_p3 = [(centerX - (dec_pos)/2) - dec_length/2, (centerY + (side_length)/2**.33) - ((dec_length)/2)]

        opp_point1 = [centerX + (side_length)/2, centerY - (side_length)/2**.33]

        p1_dec2_p1 = [(centerX + (dec_pos)/2), (centerY - (side_length)/2**.33)]
        p1_dec2_p2 = [centerX + (dec_pos)/2, centerY - (dec_pos)/2**.33]
        p1_dec2_p3 = [(centerX + (dec_pos)/2) + dec_length/2, (centerY - (side_length)/2**.33) + ((dec_length)/2)]

        point2 = [centerX - (side_length)/2, centerY - (side_length)/2**.33]

        p1_dec3_p1 = [(centerX - (dec_pos)/2), (centerY - (side_length)/2**.33)]
        p1_dec3_p2 = [centerX - (dec_pos)/2, centerY - (dec_pos)/2**.33]
        p1_dec3_p3 = [(centerX - (dec_pos)/2) - dec_length/2, (centerY - (side_length)/2**.33) + ((dec_length)/2)]

        opp_point2 = [centerX + (side_length)/2, centerY + (side_length)/2**.33]
    
        p1_dec4_p1 = [(centerX + (dec_pos)/2), (centerY + (side_length)/2**.33)]
        p1_dec4_p2 = [centerX + (dec_pos)/2, centerY + (dec_pos)/2**.33]
        p1_dec4_p3 = [(centerX + (dec_pos)/2) + dec_length/2, (centerY + (side_length)/2**.33) - ((dec_length)/2)]
        
        horizontal_p1 = [centerX - side_length, centerY]
        horizontal_p2 = [centerX + side_length, centerY]

        horizontal_dec_p1 = [centerX - dec_pos, centerY]
        horizontal_dec_p2 = [centerX - dec_pos - (dec_length/2), centerY - dec_length/2]

        horizontal_dec2_p1 = [centerX - dec_pos, centerY]
        horizontal_dec2_p2 = [centerX - dec_pos - (dec_length/2), centerY + dec_length/2]

        horizontal_dec3_p1 = [centerX + dec_pos, centerY]
        horizontal_dec3_p2 = [centerX + dec_pos + (dec_length/2), centerY - dec_length/2]

        horizontal_dec4_p1 = [centerX + dec_pos, centerY]
        horizontal_dec4_p2 = [centerX + dec_pos + (dec_length/2), centerY + dec_length/2]


        #snowflake
        canvas.create_line(point1, opp_point1,fill="light blue", width = 4)
        canvas.create_line(point2, opp_point2,fill="light blue", width = 4)
        canvas.create_line(horizontal_p1, horizontal_p2,fill="light blue", width = 4)
        #snowflake decorations
        canvas.create_line(horizontal_dec_p1, horizontal_dec_p2,fill="light blue", width = 4)
        canvas.create_line(horizontal_dec2_p1, horizontal_dec2_p2,fill="light blue", width = 4)
        canvas.create_line(horizontal_dec3_p1, horizontal_dec3_p2,fill="light blue", width = 4)
        canvas.create_line(horizontal_dec4_p1, horizontal_dec4_p2,fill="light blue", width = 4)

        canvas.create_line(p1_dec1_p1, p1_dec1_p2,fill="light blue", width = 4 )
        canvas.create_line(p1_dec1_p2,p1_dec1_p3,fill="light blue", width = 4 )

        canvas.create_line(p1_dec2_p1,p1_dec2_p2,fill="light blue", width = 4)
        canvas.create_line(p1_dec2_p2,p1_dec2_p3,fill="light blue", width = 4)

        canvas.create_line(p1_dec3_p1,p1_dec3_p2,fill="light blue", width = 4)
        canvas.create_line(p1_dec3_p2,p1_dec3_p3,fill="light blue", width = 4)
    
        canvas.create_line(p1_dec4_p1,p1_dec4_p2,fill="light blue", width = 4)
        canvas.create_line(p1_dec4_p2,p1_dec4_p3,fill="light blue", width = 4)
        
        
