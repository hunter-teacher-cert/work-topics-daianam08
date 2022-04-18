# Import the Python Image Library
import PIL
from PIL import Image,ImageDraw

# Set the size of your canvas
width = 200
height = 200

# Create and draw your canvas using RGB colors
img = Image.new(mode="RGB",size=(width,height))
img.show()
imgd = ImageDraw.Draw(img)

# Visualize the graph in this way
# 0 1 2 3 4 5 
# 1
# 2
# 3
# 4
# 5

# Draw lines then fill line with color
# Uses coordinates to create the lines, like in this sample
# (Upper left x coordinate, upper left y coordinate, lower right x coordinate, lower right y coordinate)
imgd.line([(10,10),(10,50)],fill=(0,0,255), width = 1)
imgd.line([(10,10),(50, 10)],fill=(255,255,0), width = 1)
imgd.line([(50,10),(10,50)],fill=(255,0,255), width = 1)

#  How large the triangle will be using a as parameter
def draw_tri(a, b):
  imgd.line([(0,0),(0,a)],fill=(255,0,0), width = 1)
  imgd.line([(0,0),(a, 0)],fill=(255,0,0), width = 1)
  imgd.line([(a,0),(0,a)],fill=(255,0,0), width = 1)
  imgd.line([(0,0),(b,0)],fill=(255,0,0), width = 1)
  imgd.line([(0,0),(0, b)],fill=(255,0,0), width = 1)
  imgd.line([(0,b),(b,0)],fill=(255,0,0), width = 1)
  
  # imgd.line([(0,0),(10,10)],fill=(255,255,0), width = 1)
  # imgd.line([(10,10),(10,10+a)],fill=(255,255,0), width = 1)
  # imgd.line([(0,0),(10,10+a)],fill=(255,255,0), width = 1)
  # pass
#  Draws your triangle based on the inputed size, starting at (0,0) . keep it under canvas size!
draw_tri(100, 100)

#  saves image as a jpg, will rewrite every time you run
img.save("my_drawing.jpg")

