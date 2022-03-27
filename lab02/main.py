import time
import sys
import codecs
import numpy as np
import gc  # garbage collector
from collections import defaultdict
import matplotlib.pyplot as plt


def load_textfile(filename: str):
    try:
        with codecs.open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
    except:
        print("Couldn't read the file!")
        sys.exit(1)

    illegal_chars = "()'-:,.?!;—"

    content = content.lower()
    for char in illegal_chars:
        content = content.replace(char, "")

    return content


def bubble_sort(data):
    tmp_data = data
    for pass_nr in range(len(tmp_data) - 1, 0, -1):
        for i in range(pass_nr):
            if tmp_data[i] > tmp_data[i + 1]:
                tmp_data[i], tmp_data[i + 1] = tmp_data[i + 1], tmp_data[i]

    return tmp_data


def insertion_sort(data):
    tmp_data = data
    for i in range(1, len(tmp_data)):
        j = i - 1
        next_element = tmp_data[i]
        while (tmp_data[j] > next_element and j >= 0):
            tmp_data[j + 1] = tmp_data[j]
            j = j - 1
        tmp_data[j + 1] = next_element

    return tmp_data


def merge_sort(data):
    tmp_data = data
    if (len(tmp_data) > 1):
        mid_idx = len(tmp_data) // 2
        left_data = tmp_data[:mid_idx]
        right_data = tmp_data[mid_idx:]

        merge_sort(left_data)
        merge_sort(right_data)

        a, b, c = 0, 0, 0
        while ((a < len(left_data) and (b < len(right_data)))):
            if (left_data[a] < right_data[b]):
                tmp_data[c] = left_data[a]
                a += 1
            else:
                tmp_data[c] = right_data[b]
                b += 1
            c += 1

        while (a < len(left_data)):
            tmp_data[c] = left_data[a]
            a += 1
            c += 1

        while (b < len(right_data)):
            tmp_data[c] = right_data[b]
            b += 1
            c += 1

    return tmp_data


def partition(start, end, tmp_data):
    pivot_idx = start
    pivot = tmp_data[pivot_idx]

    while (start < end):
        while ((start < len(tmp_data)) and (tmp_data[start] <= pivot)):
            start += 1

        while (tmp_data[end] > pivot):
            end -= 1

        if (start < end):
            tmp_data[start], tmp_data[end] = tmp_data[end], tmp_data[start]

    tmp_data[end], tmp_data[pivot_idx] = tmp_data[pivot_idx], tmp_data[end]
    return end


def quick_sort(start, end, data):
    tmp_data = data
    if (start < end):
        partitioning_idx = partition(start, end, tmp_data)
        quick_sort(start, partitioning_idx - 1, tmp_data)
        quick_sort(partitioning_idx + 1, end, tmp_data)

    return tmp_data


def main():
    # garbage collector
    gc_old = gc.isenabled()
    gc.disable()

    sys.setrecursionlimit(100000)

    N_range = np.array([1000 * i for i in range(1, 11)])  # how many elements in the table
    NUMBER_OF_REALIZATIONS = 2
    possible_sorts = [bubble_sort, insertion_sort]
    # possible_sorts = [merge_sort, quick_sort]

    content = load_textfile("pan-tadeusz.txt").split()
    results = defaultdict(dict)

    for sort in possible_sorts:
        for n in N_range:
            time_sum = 0
            for _ in range(0, NUMBER_OF_REALIZATIONS):
                content_n_elem = np.array(content[:n])

                start_time = time.time()
                if (sort == quick_sort):
                    quick_sort(0, len(content_n_elem) - 1, content_n_elem)
                else:
                    sort(content_n_elem)
                end_time = time.time()

                time_sum += (end_time - start_time)
            mean_time = time_sum / NUMBER_OF_REALIZATIONS
            results[sort.__name__][n] = mean_time

            print("{:.2f}: Dont ctrl+c me! At: {}-{}".format(time.time(), sort.__name__, n))

    fig, ax = plt.subplots()
    for sort in possible_sorts:
        ax.plot(results.get(sort.__name__).keys(), results.get(sort.__name__).values(), label=sort.__name__)

    ax.set_xlabel("N")
    ax.set_ylabel("Time [s]")
    ax.legend()
    fig.tight_layout()
    plt.show()
    plt.savefig("{}_vs_{}.png".format(possible_sorts[0].__name__, possible_sorts[1].__name__))

    if(gc_old):
        gc.enable()


if __name__ == "__main__":
    main()
