from PIL import Image
import numpy as np
import os

# Function to split the image into tiles
def split_image(image_path, tile_size):
    image = Image.open(image_path)
    width, height = image.size
    tiles = []
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            tiles.append(image.crop((x, y, x+tile_size, y+tile_size)))
    return tiles

# Function to calculate the similarity between two tile borders using a threshold
def calculate_similarity(border1, border2, threshold):
    similarity_score = np.sum(np.array(border1) == np.array(border2))
    return similarity_score >= threshold


# Function to solve the puzzle
def solve_puzzle(tiles, tile_size):
    num_tiles = len(tiles)
    puzzle_size = int(np.sqrt(num_tiles))
    puzzle = [[None]*puzzle_size for _ in range(puzzle_size)]
    tile_positions = [[None]*puzzle_size for _ in range(puzzle_size)]

    # Helper function to get the borders of a tile
    def get_borders(tile):
        top_border = tile.crop((0, 0, tile_size, 1)).getdata()
        right_border = tile.crop((tile_size-1, 0, tile_size, tile_size)).getdata()
        bottom_border = tile.crop((0, tile_size-1, tile_size, tile_size)).getdata()
        left_border = tile.crop((0, 0, 1, tile_size)).getdata()
        return [top_border, right_border, bottom_border, left_border]

    # Helper function to find the best matching tile for a position
    def find_best_match(tile, borders, used_tiles, threshold):
        best_match_index = -1
        best_similarity = -1
        for i, candidate_tile in enumerate(tiles):
            if i not in used_tiles:
                candidate_borders = get_borders(candidate_tile)
                for j, border in enumerate(candidate_borders):
                    similarity = calculate_similarity(border, borders[j], threshold)
                    if similarity  > best_similarity:
                        best_similarity = similarity
                        best_match_index = i
        return best_match_index


    # Start solving the puzzle
    used_tiles = set()
    for y in range(puzzle_size):
        for x in range(puzzle_size):
            if x == 0 and y == 0:  # Start with any tile
                puzzle[y][x] = tiles[0]
                tile_positions[y][x] = (0, 0)
                used_tiles.add(0)
            else:
                # Calculate the borders of adjacent tiles
                top_tile = puzzle[y-1][x] if y > 0 else None
                left_tile = puzzle[y][x-1] if x > 0 else None
                top_border = get_borders(top_tile)[2] if top_tile is not None else None
                left_border = get_borders(left_tile)[1] if left_tile is not None else None
                # Find the best matching tile
                borders = [top_border, None, None, left_border]
                best_match_index = find_best_match(None, borders, used_tiles, threshold=2)
                puzzle[y][x] = tiles[best_match_index]
                tile_positions[y][x] = (y, x)
                used_tiles.add(best_match_index)

    return puzzle, tile_positions

# Function to stitch tiles into a single image
def stitch_image(puzzle):
    width, height = puzzle[0][0].size
    result_image = Image.new('RGB', (width * len(puzzle), height * len(puzzle)))
    for y, row in enumerate(puzzle):
        for x, tile in enumerate(row):
            result_image.paste(tile, (x * width, y * height))
    return result_image

# Function to save tile positions to a text file
def save_tile_positions(tile_positions, output_file):
    with open(output_file, 'w') as f:
        for row in tile_positions:
            f.write(' '.join([str(pos) for pos in row]) + '\n')

# Main function
def main():
    input_image = 'hard_puzzle.jpg'
    output_image = 'solved_puzzle.jpg'
    output_tile_positions = 'tile_positions.txt'
    tile_size = 64  # Assuming each tile is 64x64 pixels

    # Split the image into tiles
    tiles = split_image(input_image, tile_size)

    # Solve the puzzle
    puzzle, tile_positions = solve_puzzle(tiles, tile_size)

    # Stitch the puzzle tiles into a single image
    solved_image = stitch_image(puzzle)

    # Save the solved image
    solved_image.save(output_image)

    # Save tile positions to a text file
    save_tile_positions(tile_positions, output_tile_positions)

if __name__ == "__main__":
    main()
