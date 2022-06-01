import sys
from utilities import read_file_to_numpy
from graph import Graph


def main():
    # if len(sys.argv) != 2:
    #     print("Input file not specified! Exiting...")
    #     sys.exit(1)

    # filename = sys.argv[1]
    filename = "boards\\board3.txt"
    try:
        board = read_file_to_numpy(str(filename))
    except FileNotFoundError as error:
        print("Couldn't read file '{}' due to: \n{}\n".format(sys.argv[1], error))
        sys.exit(1)

    g = Graph(board)

    dijkstra = g.dijkstra()
    print("{} PATH {}".format("=" * 10, "=" * 10))
    g.print()
    print("{} COST {}".format("=" * 10, "=" * 10))
    print(dijkstra)


if __name__ == '__main__':
    main()
