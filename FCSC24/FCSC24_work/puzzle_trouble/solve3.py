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
    for i in range(16):
        for j in range(16):
            mini_image = rearranged_mini_images[i * 16 + j]
            grid_image.paste(mini_image, (j * 64, i * 64))
    grid_image.show()

def switch_images(rearranged_mini_images, switch_command):
    try:
        switch_command = switch_command.strip().split(' ')
        # if the first char is c , thent switch the columns 
        if switch_command[0] == 'C':
            for i in range(16):
                rearranged_mini_images[i * 16 + int(switch_command[1])], rearranged_mini_images[i * 16 + int(switch_command[2])] = rearranged_mini_images[i * 16 + int(switch_command[2])], rearranged_mini_images[i * 16 + int(switch_command[1])]
        # if the first char is r , thent switch the rows
        elif switch_command[0] == 'R':
            for i in range(16):
                rearranged_mini_images[int(switch_command[1]) * 16 + i], rearranged_mini_images[int(switch_command[2]) * 16 + i] = rearranged_mini_images[int(switch_command[2]) * 16 + i], rearranged_mini_images[int(switch_command[1]) * 16 + i]
        # if the first char is o, deplace all mini image on the line to the right x (command i O row_number number_times) (the last one become the first one, the first one become the second one, etc)
        elif switch_command[0] == 'O':
            # if len is != 3, then we rotate one time the line (all image go 1 place to the right)
            if len(switch_command) != 3:
                nb_rotate = 1
            else: nb_rotate = int(switch_command[2])
            for _ in range(nb_rotate):
                for i in range(16):
                    # Rotate the line : create a table with the image of the lines
                    line = [rearranged_mini_images[int(switch_command[1]) * 16 + i] for i in range(16)]
                # Rotate the line
                line = [line[-1]] + line[:-1]
                    # Put the line back in the grid
                for j in range(16):
                    rearranged_mini_images[int(switch_command[1]) * 16 + j] = line[j]
        # if the first char is S, save the image
        elif switch_command[0] == 'S':
            save_grid_image(rearranged_mini_images, "latest_changes.jpg")
        else:
            first_position = (switch_command[0], switch_command[1])
            second_position = (switch_command[2], switch_command[3])
            first_index = first_position[0] * 16 + first_position[1]
            second_index = second_position[0] * 16 + second_position[1]

            rearranged_mini_images[first_index], rearranged_mini_images[second_index] = rearranged_mini_images[second_index], rearranged_mini_images[first_index]

        # Display and save the updated grid image
        display_grid_image(rearranged_mini_images)
        #save_grid_image(rearranged_mini_images, "latest_changes.jpg")
    except Exception as e:
        print("Invalid input:", e)

def save_grid_image(rearranged_mini_images, output_path):
    grid_image = Image.new("RGB", (1024, 1024))
    for i in range(16):
        for j in range(16):
            mini_image = rearranged_mini_images[i * 16 + j]
            grid_image.paste(mini_image, (j * 64, i * 64))
    grid_image.save(output_path)

if __name__ == "__main__":
    image_folder = "tmp_split"  # Folder containing mini-images

    mini_images = []
    for file in os.listdir(image_folder):
        if file.endswith(".jpg"):

            mini_images.append(Image.open(os.path.join(image_folder, file)))
    display_grid_image(mini_images)

    while True:
        switch_command = input("Enter switch command (format: row1 col1 row2 col2 | {c/r} x y), or 'exit' to quit: ")
        if switch_command.lower() == "exit":
            break
        else:
            switch_images(mini_images, switch_command)
