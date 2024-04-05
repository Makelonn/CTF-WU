from PIL import Image
import os

def calculate_mean_brightness(image):
    # Convert image to grayscale
    grayscale_image = image.convert("L")
    # Calculate mean brightness
    mean_brightness = sum(grayscale_image.getdata()) / len(grayscale_image.getdata())
    return mean_brightness

def rearrange_mini_images(image_folder):
    # Load mini-images
    mini_images = []
    for file in os.listdir(image_folder):
        if file.endswith(".jpg"):
            mini_images.append(Image.open(os.path.join(image_folder, file)))

    # Calculate mean brightness for each mini-image
    mean_brightness_values = [(idx, calculate_mean_brightness(img)) for idx, img in enumerate(mini_images)]
    
    # Sort mini-images based on mean brightness
    sorted_mini_images = sorted(mean_brightness_values, key=lambda x: x[1], reverse=True)

    # Rearrange mini-images based on sorted order
    rearranged_mini_images = [mini_images[idx] for idx, _ in sorted_mini_images]
    
    return rearranged_mini_images

def save_grid_image(rearranged_mini_images, output_path):
    # Create a blank canvas for the grid image
    grid_image = Image.new("RGB", (1024, 1024))

    # Paste each mini-image onto the grid image
    for i in range(8):
        for j in range(8):
            mini_image = rearranged_mini_images[i * 8 + j]
            grid_image.paste(mini_image, (j * 128, i * 128))

    # Save the grid image
    grid_image.save(output_path)

if __name__ == "__main__":
    image_folder = "output"  # Folder containing mini-images
    output_path = "brightness_rearranged_grid.jpg"  # Output path for the grid image

    rearranged_mini_images = rearrange_mini_images(image_folder)
    save_grid_image(rearranged_mini_images, output_path)
