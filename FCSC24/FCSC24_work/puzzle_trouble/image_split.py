from PIL import Image

def split_image(image_path, output_folder):
    image = Image.open(image_path)
    nb_tiles = 16
    # Calculate dimensions for each mini-image
    width, height = image.size
    mini_width = width // nb_tiles
    mini_height = height // nb_tiles
    
    # Create output folder if it doesn't exist
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Split the image and save mini-images
    for i in range(nb_tiles):
        for j in range(nb_tiles):
            box = (j * mini_width, i * mini_height, (j + 1) * mini_width, (i + 1) * mini_height)
            mini_image = image.crop(box)
            # Save the image in format mini_image_00_00.jpg
            name = "mini_image"
            if len(str(i)) == 1: name += "_0" + str(i)
            else: name += "_" + str(i)
            if len(str(j)) == 1: name += "_0" + str(j)
            else: name += "_" + str(j)

            mini_image.save(f"{output_folder}/{name}.jpg")
            
if __name__ == "__main__":
    image_path = "./solve_output/grid_image_grey_100.jpg"  # Path to your input image
    output_folder = "tmp_split"   # Output folder to save mini-images
    
    split_image(image_path, output_folder)
