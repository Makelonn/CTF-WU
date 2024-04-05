from PIL import Image

def split_image(image_path, output_folder):
    image = Image.open(image_path)
    
    # Calculate dimensions for each mini-image
    width, height = image.size
    mini_width = width // 8
    mini_height = height // 8
    
    # Create output folder if it doesn't exist
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Split the image and save mini-images
    for i in range(8):
        for j in range(8):
            box = (j * mini_width, i * mini_height, (j + 1) * mini_width, (i + 1) * mini_height)
            mini_image = image.crop(box)
            mini_image.save(f"{output_folder}/mini_image_{i}_{j}.jpg")

if __name__ == "__main__":
    image_path = "./puzzle-trouble-easy.jpg"  # Path to your input image
    output_folder = "output"   # Output folder to save mini-images
    
    split_image(image_path, output_folder)
