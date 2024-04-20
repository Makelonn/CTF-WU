from PIL import Image, ImageDraw
import os
import numpy as np

def _oldcalculate_color_score(pixel):
    # Define color weights based on your criteria
    yellow_white_weight = 2
    blue_weight = 1
    brown_weight = 0.5

    # Extract RGB components
    red, green, blue = pixel

    # Check if the pixel is black
    if (red, green, blue) == (0, 0, 0):
        return 0  # Black pixel, return 0 score

    # Calculate color scores based on weights
    yellow_white_score = (red + green) / 2  # Average of red and green
    blue_score = blue
    brown_score = (red + green) / 2  # Average of red and green

    # Apply weights
    color_score = (
        yellow_white_weight * yellow_white_score +
        blue_weight * blue_score +
        brown_weight * brown_score
    )
    return color_score

def _old_calculate_mean_color(image):
    # Convert the image to RGB mode
    rgb_image = image.convert("RGB")
    pixel_data = list(rgb_image.getdata())

    # Calculate the sum of RGB values excluding black (RGB: 0, 0, 0)
    non_black_pixels = [pixel for pixel in pixel_data if pixel != (0, 0, 0)]
    total_pixels = len(non_black_pixels)

    if total_pixels == 0:
        return (0, 0, 0)  # If all pixels are black, return black
    else:
        # Calculate the mean color (excluding black)
        mean_color = (
            sum(pixel[0] for pixel in non_black_pixels) // total_pixels,
            sum(pixel[1] for pixel in non_black_pixels) // total_pixels,
            sum(pixel[2] for pixel in non_black_pixels) // total_pixels
        )
        return mean_color

def _old_switch_images(rearranged_mini_images, switch_command):
    switch_command = switch_command.strip().split('/')
    nb_tiles = 16
    try:
        first_position = tuple(map(int, switch_command[0].strip().split()))
        second_position = tuple(map(int, switch_command[1].strip().split()))
        first_index = first_position[0] * nb_tiles + first_position[1]
        second_index = second_position[0] * nb_tiles + second_position[1]

        rearranged_mini_images[first_index], rearranged_mini_images[second_index] = rearranged_mini_images[second_index], rearranged_mini_images[first_index]

        # Display and save the updated grid image
        #display_grid_image(rearranged_mini_images)
        save_grid_image(rearranged_mini_images, "latest_changes.jpg")
    except Exception as e:
        print("Invalid input:", e)

def calculate_border_similarity_mean(tile1, tile2, threshold=50):
    """
    Calculate the border similarity score between two tiles.
    """
    border1 = tile1[:, -1]  # Right border of tile1
    border2 = tile2[:, 0]   # Left border of tile2
    similarity = np.mean(border1 == border2)
    return similarity

def calculate_border_similarity_grey(tile1, tile2, threshold=55):
    """
    Calculate the border similarity score between two tiles.
    """
    border1 = tile1[:, -1]  # Right border of tile1
    border2 = tile2[:, 0]   # Left border of tile2
    
    # Convert borders to grayscale
    border1_gray = np.mean(border1, axis=1)
    border2_gray = np.mean(border2, axis=1)
    
    # Calculate absolute difference between grayscale borders
    diff = np.abs(border1_gray - border2_gray)
    
    # Count how many pixels have a difference less than the threshold
    similar_pixels = np.sum(diff < threshold)
    
    # Calculate similarity as the ratio of similar pixels to total pixels
    similarity = similar_pixels / len(border1_gray)
    
    return similarity


def sort_tiles_by_border(tiles):
    """
    Sort the tiles based on their borders.
    """
    sorted_tiles = []
    remaining_tiles = list(range(len(tiles)))

    # Start with any tile
    sorted_tiles.append(remaining_tiles.pop(0))

    while remaining_tiles:
        last_tile_index = sorted_tiles[-1]
        best_score = -1
        best_tile_index = None

        for i in remaining_tiles:
            score = calculate_border_similarity_mean(tiles[last_tile_index], tiles[i])
            if score > best_score:
                best_score = score
                best_tile_index = i

        sorted_tiles.append(best_tile_index)
        remaining_tiles.remove(best_tile_index)

    return sorted_tiles

def rearrange_mini_images(image_folder):
    mini_images = []
    for file in os.listdir(image_folder):
        if file.endswith(".jpg"):
            mini_images.append(Image.open(os.path.join(image_folder, file)))

    # Sort images based on border similarity
    sorted_indices = sort_tiles_by_border([np.array(img) for img in mini_images])
    sorted_mini_images = [mini_images[i] for i in sorted_indices]

    return sorted_mini_images

def display_grid_image(rearranged_mini_images):
    grid_image = Image.new("RGB", (1024, 1024))
    nb_tiles = 16
    for i in range(nb_tiles):
        for j in range(nb_tiles):
            mini_image = rearranged_mini_images[i * nb_tiles + j]
            grid_image.paste(mini_image, (j * 64, i * 64))
    grid_image.show()

def save_grid_image(rearranged_mini_images, output_path):
    grid_image = Image.new("RGB", (1024, 1024))
    nb_tiles = 16
    for i in range(nb_tiles):
        for j in range(nb_tiles):
            mini_image = rearranged_mini_images[i * nb_tiles + j]
            grid_image.paste(mini_image, (j * 64, i * 64))
    grid_image.save(output_path)

if __name__ == "__main__":
    image_folder = "brightness_rearranged"  # Folder containing mini-images

    rearranged_mini_images = rearrange_mini_images(image_folder)
    display_grid_image(rearranged_mini_images)

    # Save the grid image
    save_folder = "solve_output"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    save_grid_image(rearranged_mini_images, f"./{save_folder}/grid_image_grey_55pg")