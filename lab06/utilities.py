import numpy as np
import random

def read_file_to_numpy(filepath: str):
    with open(filepath) as f:
        lines = f.read().splitlines()

        cols = len(lines[0])
        rows = len(lines)
        array = np.zeros(shape=(rows, cols))

        for i, line in enumerate(lines):
            array[i, :] = list(map(int, list(line)))

    return array


def generate_random_board(size):
    board = np.random.randint(low=1, high=9, size=(size, size), dtype=int)
    print('\n'.join(''.join(str(value) for value in row) for row in board))


if __name__ == "__main__":
    generate_random_board(10)

