from PIL import Image, ImageDraw
import os

def calculate_mean_brightness(image):
    grayscale_image = image.convert("L")
    mean_brightness = sum(grayscale_image.getdata()) / len(grayscale_image.getdata())
    return mean_brightness

def rearrange_mini_images(image_folder):
    mini_images = []
    for file in os.listdir(image_folder):
        if file.endswith(".jpg"):
            mini_images.append(Image.open(os.path.join(image_folder, file)))

    mean_brightness_values = [(idx, calculate_mean_brightness(img)) for idx, img in enumerate(mini_images)]
    sorted_mini_images = [mini_images[idx] for idx, _ in sorted(mean_brightness_values, key=lambda x: x[1], reverse=True)]

    return sorted_mini_images

def display_grid_image(rearranged_mini_images):
    grid_image = Image.new("RGB", (1024, 1024))
    for i in range(8):
        for j in range(8):
            mini_image = rearranged_mini_images[i * 8 + j]
            grid_image.paste(mini_image, (j * 128, i * 128))
    grid_image.show()

def switch_images(rearranged_mini_images, switch_command):
    switch_command = switch_command.strip().split('-')
    try:
        first_position = tuple(map(int, switch_command[0].strip().split()))
        second_position = tuple(map(int, switch_command[1].strip().split()))
        first_index = first_position[0] * 8 + first_position[1]
        second_index = second_position[0] * 8 + second_position[1]

        rearranged_mini_images[first_index], rearranged_mini_images[second_index] = rearranged_mini_images[second_index], rearranged_mini_images[first_index]

        # Display and save the updated grid image
        display_grid_image(rearranged_mini_images)
        save_grid_image(rearranged_mini_images, "latest_changes.jpg")
    except Exception as e:
        print("Invalid input:", e)

def save_grid_image(rearranged_mini_images, output_path):
    grid_image = Image.new("RGB", (1024, 1024))
    for i in range(8):
        for j in range(8):
            mini_image = rearranged_mini_images[i * 8 + j]
            grid_image.paste(mini_image, (j * 128, i * 128))
    grid_image.save(output_path)

if __name__ == "__main__":
    image_folder = "mini-images"  # Folder containing mini-images

    rearranged_mini_images = rearrange_mini_images(image_folder)
    display_grid_image(rearranged_mini_images)

    while True:
        switch_command = input("Enter switch command (format: row1 col1 - row2 col2), or 'exit' to quit: ")
        if switch_command.lower() == "exit":
            break
        else:
            switch_images(rearranged_mini_images, switch_command)
