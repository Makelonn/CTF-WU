from PIL import Image, ImageDraw
import os

def create_grid_image(canvas_size=(1000, 1000), grid_size=16):
    # Create a blank image with white background
    img = Image.new("RGB", canvas_size, "white")
    draw = ImageDraw.Draw(img)
    
    # Define grid properties
    cell_size = img.width // grid_size
    
    # Draw vertical grid lines
    for i in range(1, grid_size):
        x = i * cell_size
        draw.line([(x, 0), (x, img.height)], fill="pink", width=1)
    
    # Draw horizontal grid lines
    for i in range(1, grid_size):
        y = i * cell_size
        draw.line([(0, y), (img.width, y)], fill="pink", width=1)
    
    return img

def grid_to_pixel_coordinate(coord, cell_size, offset=4):
    # x+offset so the 0,0 is centered, and *cell_size to convert to pixel coordinates
    return (((coord[0]+offset) * cell_size), ((coord[1]+offset) * cell_size))

def draw_lines_on_grid(image, coordinates, cell_size):
    draw = ImageDraw.Draw(image)
    
    very_beginning = coordinates.pop(0)
    last_endpoint =  very_beginning
    # Re insert the first at the end
    coordinates.append(very_beginning)
    #print(coordinates)
    while len(coordinates) >=2:
        start = last_endpoint
        objective = coordinates.pop(0)
        objective = (start[0] + objective[0], start[1] + objective[1])
        #print(f"Drawing line from {start} to {objective}")
        draw.line([grid_to_pixel_coordinate(start, cell_size), grid_to_pixel_coordinate(objective, cell_size)], fill="blue", width=4)
        #image.show()
        last_endpoint = objective

"""# Now, we can draw lines on the grid
coordinates = [(2, 0), (-1, 2), (-1, -2), (0,0)]
draw_lines_on_grid(grid_image, coordinates, Canvas_size_px // Nb_cells_per_side)
grid_image.show()  # Display the image
# Save the image to file
grid_image.save("grid_with_lines.png")"""

def draw_images_and_save(coordinates_list, output_folder="output"):
    result_images = []

    # Definition of canvas parameters
    canvas_size_px = 1500
    Nb_cells_per_side = 8

    index = 0
    for coordinates in coordinates_list :
        # First, creating the image
        grid_image = create_grid_image(canvas_size=(canvas_size_px, canvas_size_px) , grid_size=Nb_cells_per_side)
        
        draw_lines_on_grid(grid_image, coordinates, canvas_size_px // Nb_cells_per_side)
        grid_image.save(f"output/result_{index}.jpg")
        index += 1
        result_images.append(grid_image)

    # Concatenate images horizontally
    total_width = len(result_images) * canvas_size_px

    result_image = Image.new("RGB", (total_width, canvas_size_px))
    x_offset = 0
    for img in result_images:
        result_image.paste(img, (x_offset, 0))
        x_offset += canvas_size_px

    result_image.save(f"{output_folder}/combined_result.jpg")

# Example usage:
#coordinates_list = [[(2, 0), (-1, 2), (-1, -2),(0, 0), (3, 0),(-1, 2), (2, 0), (-1, -2),(0, 0), (1, 0)] *6]
# Actual list
coordinates_list = [[(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]]

# Now cleaning the list so each form is in a different list
debug = True
cleaned = []
for i in coordinates_list:
    if debug: print("LIST n°", i)
    if (0,0) not in i :
        cleaned.append(i)
        if debug: print("No (0,0) in the list")
    else:
        # Count the number of (0,0) in the list
        count = i.count((0,0))
        if debug : print(count, "in the list")
        for j in range(count):
            if debug : print("--- Doing n°", j)
            first = i.index((0,0))
            
            if i[:first] != []:
                cleaned.append(i[:first])
            if debug : print("Append ", i[:first])

            i = i[first+1:]
            if debug : print("New list ", i)
        if len(i) > 0: 
            cleaned.append(i)
if debug:
    for i in cleaned:
        print(i)

if not os.path.exists("output"):
    os.makedirs("output")

draw_images_and_save(cleaned)

print("Main is done")

# Redo some stuff that i'm not sure about
# 3, 1 ? , 3&1 together, 7, 

a = [# Should be a 3
[(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0)],
# Should be a 1
[(3,-1),(0,2),(0,0)],
# 1 and 3 together to check that i did not miss anything
[(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0)],
# Should be a 7
[(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0)]]

draw_images_and_save(a, output_folder="check")

print("Check done")