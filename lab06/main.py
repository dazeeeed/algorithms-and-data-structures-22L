import sys
from utilities import read_file_to_numpy


def main():
    if len(sys.argv) != 2:
        print("Input file not specified! Exiting...")
        sys.exit(1)

    try:
        graph = read_file_to_numpy(str(sys.argv[1]))
    except FileNotFoundError as error:
        print("Couldn't read file '{}' due to: \n{}\n".format(sys.argv[1], error))


if __name__ == '__main__':
    main()
