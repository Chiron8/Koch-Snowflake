from PIL import Image, ImageDraw
import math

resolution = 100000
quality = 9
angle = 0
points = [0, resolution-resolution/8]
currentx = points[0]
currenty = points[1]

img = Image.new('1', (resolution, resolution))
draw = ImageDraw.Draw(img)

def pointcalc(x1, y1, distance, deg):
    global currentx, currenty
    rad = math.radians(deg)
    
    x2 = x1 + distance * math.cos(rad)
    y2 = y1 + distance * math.sin(rad)
    currentx, currenty = x2, y2
    
    points.append(x2)
    points.append(y2)
    
def koch(resolution, quality):
    global currentx, currenty, angle
    if quality > 0:
        for i in [0, -60, 120, -60]:
            if i == 0:
                pointcalc(currentx, currenty, 
                (resolution/4**quality)/2, angle)
            else:
                angle = angle + i
                pointcalc(currentx, currenty, 
                resolution/4**quality, angle)
                
            koch(resolution/3, quality-1)
            
print("Calculating...")
koch(resolution, quality)
points.append(resolution)
points.append(resolution-resolution/8)

print("Drawing...")
draw.line(points, fill=1, width=1)
img.save("test.jpg")
print("Done! :)")
#img.show("test.jpg")
