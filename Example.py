import tkinter
import graphics
#creates window
window = tkinter.Tk()
window.title("GUI")

# creates canvas
canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()
#create hexagon
newHex = hexagon()
newHex.center_coordinates(250,250)
newHex.hex_side_length(50)
newHex.hex_color("green")
newHex.hex_outline("blue")
newHex.hex_width(20)
newHex.create_hex()
#create snowflake
mySnowflake = snowflake()
mySnowflake.centerXY(250,250)
mySnowflake.length(100)
mySnowflake.create_snowflake()



window.mainloop()
