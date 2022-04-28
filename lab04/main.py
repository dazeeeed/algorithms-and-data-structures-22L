from heap import Heap


def main():
    data = [10, 2, 5, 11, 7, 9, 3, 1, 12, 21, 23, 22, 25, 26, 27, 18, 30, 31]
    data = [1, 3]
    heap_test = Heap(data, 3)
    print(heap_test.data)
    heap_test.print_heap(0)

    heap_test.delete_root()
    print()
    print(heap_test.data)
    heap_test.print_heap(0)

    heap_test.insert_element(41)
    print()
    print(heap_test.data)
    heap_test.print_heap(0)


if __name__ == "__main__":
    main()