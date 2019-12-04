import tkinter
#creates window
window = tkinter.Tk()
window.title("GUI")

# creates canvas
canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()

newHex = hexagon()
newHex.center_coordinates(250,250)
newHex.hex_side_length(50)
newHex.hex_color("green")
newHex.hex_outline("blue")
newHex.hex_width(20)
newHex.create_hex()

window.mainloop()
