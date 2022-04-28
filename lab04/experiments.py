import copy
from heap import Heap
from time import time
import numpy as np
import random
import matplotlib.pyplot as plt
import sys


def perform_experiment():
    # sys.setrecursionlimit(10000000)

    colors = ['blue', 'orange', 'red']
    MAX_elements = 200000
    heap_types = [2, 3, 4]
    # possible_values = np.linspace(1, MAX_elements, MAX_elements)
    # samples = random.sample(possible_values.tolist(), 100000)
    samples = np.random.choice(1000000, MAX_elements, replace=False)

    all_heaps_creation = []
    all_heaps_deletion = []

    # x = np.linspace(10000, 100000, 10)
    x = np.linspace(1000, 100000, 10)

    # heap creation experiment
    # for heap_n in heap_types:
    #     heap_creation_data = []
    #     heap_deletion_data = []
    #     for size in x:
    #         size = int(size)
    #         subset = samples[:size]
    #
    #         time_start = time()
    #         current_heap = Heap(subset, heap_n)
    #         time_computation = time() - time_start
    #         heap_creation_data.append(time_computation)
    #
    #         # time_start = time()
    #         # for _ in range(size-1):
    #         #     current_heap.delete_root()
    #         # time_computation = time() - time_start
    #         # heap_deletion_data.append(time_computation)
    #
    #     all_heaps_creation.append(heap_creation_data)
    #     # all_heaps_deletion.append(heap_deletion_data)
    #
    # fig = plt.figure()
    # # fig.subplots_adjust(top=0.8)
    # ax1 = fig.add_subplot(111)
    # ax1.set_ylabel('czas [s]')
    # ax1.set_xlabel('n elementów')
    # ax1.set_title('Czas tworzenia poszczególnych kopców')
    #
    # color_id = 0
    # for y_data in all_heaps_creation:
    #     ax1.plot(x, y_data, color=colors[color_id], lw=2, label=str(heap_types[color_id]))
    #     color_id = color_id + 1
    # plt.legend()
    # plt.show()

    # element deletion experiment
    for heap_n in heap_types:
        heap_deletion_data = []
        allset = samples[0:int(x[-1])]
        current_heap = Heap(allset, heap_n)
        for size in x:
            size = int(size)
            subset = samples[:size]
            heap_all = copy.deepcopy(current_heap)

            time_start = time()
            for _ in subset:
                heap_all.delete_root()
            time_computation = time() - time_start
            heap_deletion_data.append(time_computation)

        all_heaps_deletion.append(heap_deletion_data)

    fig = plt.figure()
    # fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('time [s]')
    ax1.set_xlabel('n elements')
    ax1.set_title('Time of root deletion in heaps')

    color_id = 0
    for y_data in all_heaps_deletion:
        ax1.plot(x, y_data, color=colors[color_id], lw=2, label=str(heap_types[color_id]))
        color_id = color_id + 1
    plt.legend()
    plt.show()


if __name__ == "__main__":
    perform_experiment()
