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

if __name__ == "__main__":
    image_folder = "output"  # Folder containing mini-images
    output_folder = "brightness_rearranged"  # Output folder for rearranged images

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    rearranged_mini_images = rearrange_mini_images(image_folder)

    # Save rearranged images
    for idx, img in enumerate(rearranged_mini_images):
        img.save(os.path.join(output_folder, f"rearranged_image_{idx}.jpg"))
