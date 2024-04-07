from PIL import Image, ImageDraw
import os

def create_grid_image(canvas_size=(1000, 1000), cell_size=16):
    # Create a blank image with white background
    img = Image.new("RGB", canvas_size, "white")
    draw = ImageDraw.Draw(img)
    
    # Define grid properties
    grid_size = cell_size * canvas_size[1]
    
    # Draw vertical grid lines
    for i in range(1, grid_size):
        x = i * cell_size
        draw.line([(x, 0), (x, img.height)], fill="pink", width=1)
    
    # Draw horizontal grid lines
    for i in range(1, grid_size):
        y = i * cell_size
        draw.line([(0, y), (img.width, y)], fill="pink", width=1)
    
    return img

def grid_to_pixel_coordinate(coord, cell_size, offset=0):
    # x+offset so the 0,0 is centered, and *cell_size to convert to pixel coordinates
    return (((coord[0]+offset) * cell_size), ((coord[1]+offset) * cell_size))

def draw_lines_on_grid(image, coordinates, cell_size):
    draw = ImageDraw.Draw(image)
    
    P = (1,1)
    drawing = True
    for i in coordinates:
        if i != (0,0):
            target = (P[0] + i[0], P[1] + i[1])
            if drawing:
                draw.line([grid_to_pixel_coordinate(P, cell_size), grid_to_pixel_coordinate(target, cell_size)], fill="blue", width=4)
            else:
                drawing = True
            P = target
        else:
            drawing = False


# Example usage:
#coordinates_list = [(2, 0), (-1, 2), (-1, -2),(0, 0), (3, 0),(-1, 2), (2, 0), (-1, -2),(0, 0), (1, 0)] *6
# Actual list
coordinates_list = [(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]

cell_px = 32
img = create_grid_image(cell_size=cell_px, canvas_size=(3000, 150))
draw_lines_on_grid(img, coordinates_list, cell_px)
img.save("tortugaaaaaas.jpg")