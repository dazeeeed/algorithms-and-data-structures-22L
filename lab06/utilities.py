import numpy as np


def read_file_to_numpy(filepath: str):
    with open(filepath) as f:
        lines = f.read().splitlines()

        cols = len(lines[0])
        rows = len(lines)
        array = np.zeros(shape=(rows, cols))

        for i, line in enumerate(lines):
            array[i, :] = list(map(int, list(line)))

    return array

