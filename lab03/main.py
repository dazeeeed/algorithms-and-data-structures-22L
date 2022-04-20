from BS_tree_node import BSTreeNode
from AVL_tree_node import AVLTreeNode
import random
import time
import matplotlib.pyplot as plt


def get_random_list(number, min, max):
    random_list = []
    for i in range(0, number):
        u = random.randint(min, max)
        random_list.append(u)
    return random_list

def build_BST_tree(numbers_list):
    root = BSTreeNode(numbers_list[0])
    for i in range(1, len(numbers_list)):
        root.add_child(numbers_list[i])
    return root

def build_AVL_tree(numbers_list):
    root = AVLTreeNode(numbers_list[0])
    for i in range(1, len(numbers_list)):
        root = root.add_element(root, numbers_list[i])
    return root

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -5, -1, -2]
    numbers = [11, 9, 8, 7, 6, 5, 4, 3, 1, 10, 12, 13, 14, 15, 16, 17, -5, -1, -2, 20, 21, 22, 30, 25, 26]
    
    # BST example
    tree = build_BST_tree(numbers)
    tree.printTree()
    print(tree.search_element(20))
    tree.delete_element(tree, 222)
    tree.printTree()

    print("\n AVL EXAMPLE\n")
    # AVL example
    tree = build_AVL_tree(numbers)
    tree.printTree()
    print(tree.search_element(105))
    print(tree.search_element(10))
    tree.delete_element(tree, 11)
    tree.delete_element(tree, 13)
    tree.delete_element(tree, 14)
    tree.printTree()
    tree.delete_element(tree, 8)
    tree.printTree()
    tree.delete_element(tree, 9)
    tree.printTree()
    tree.delete_element(tree, 10)
    print("\n\n\n")
    tree.printTree()
    tree.delete_element(tree, 21)
    tree.delete_element(tree, 22)
    print("\n\n\n")
    tree.printTree()


def experiments():
    random_numbers = get_random_list(10000, 0, 30000)
    ranges = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    # BS Tree - CREATION
    time_create_bs = []
    for i in range(0, len(ranges)):
        r = ranges[i]
        print("bs_tree ", r)
        current_list = random_numbers[0:r]
        time_start = time.time()
        bs_tree = build_BST_tree(current_list)
        time_stop = time.time()
        t = time_stop - time_start
        time_create_bs.append(t)

    # AVL Tree - CREATION
    time_create_avl = []
    for i in range(0, len(ranges)):
        r = ranges[i]
        print("avl_tree ", r)
        current_list = random_numbers[0:r]
        time_start = time.time()
        avl_tree = build_AVL_tree(current_list)
        time_stop = time.time()
        t = time_stop - time_start
        time_create_avl.append(t)

    # BS Tree - SEARCHING
    time_search_bs = []
    for i in range(0, len(ranges)):
        r = ranges[i]
        print("bs_tree ", r)
        current_list = random_numbers[0:r]
        time_start = time.time()
        for i in range(0, r):
            is_in = bs_tree.search_element(current_list[i])
        time_stop = time.time()
        t = time_stop - time_start
        time_search_bs.append(t)

    # AVL Tree - SEARCHING
    time_search_avl = []
    for i in range(0, len(ranges)):
        r = ranges[i]
        print("avl_tree ", r)
        current_list = random_numbers[0:r]
        time_start = time.time()
        for i in range(0, r):
           is_in = avl_tree.search_element(current_list[i])
        time_stop = time.time()
        t = time_stop - time_start
        time_search_avl.append(t)

    # BS Tree - DELATING
    time_delete_bs = []
    for i in range(0, len(ranges)):
        r = ranges[i]
        print("bs_tree ", r)
        current_list = random_numbers[0:r]
        time_start = time.time()
        for i in range(0, r):
            u = bs_tree.delete_element(bs_tree, current_list[i])
        time_stop = time.time()
        t = time_stop - time_start
        time_delete_bs.append(t)

    # AVL Tree - DELATING
    time_delete_avl = []
    for i in range(0, len(ranges)):
        r = ranges[i]
        print("avl_tree ", r)
        current_list = random_numbers[0:r]
        time_start = time.time()
        for i in range(0, r):
           is_in = avl_tree.delete_element(avl_tree, current_list[i])
        time_stop = time.time()
        t = time_stop - time_start
        time_delete_avl.append(t)
    

    fig1, ax1 = plt.subplots()
    ax1.plot(ranges, time_create_bs)
    ax1.plot(ranges, time_create_avl)
    ax1.set_xlabel("N")
    ax1.set_ylabel("Time [s]")
    ax1.legend(["drzewo bs", "drzewo avl"])
    ax1.set_title("Porównanie czasu tworzenia")
    fig1.tight_layout()

    fig2, ax2 = plt.subplots()
    ax2.plot(ranges, time_search_bs)
    ax2.plot(ranges, time_search_avl)
    ax2.set_xlabel("N")
    ax2.set_ylabel("Time [s]")
    ax2.legend(["drzewo bs", "drzewo avl"])
    ax2.set_title("Porównanie czasu szukania")
    fig2.tight_layout()

    fig3, ax3 = plt.subplots()
    ax3.plot(ranges, time_delete_bs)
    ax3.plot(ranges, time_delete_avl)
    ax3.set_xlabel("N")
    ax3.set_ylabel("Time [s]")
    ax3.legend(["drzewo bs", "drzewo avl"])
    ax3.set_title("Porównanie czasu usuwania")
    fig3.tight_layout()


    plt.show()


if __name__ == "__main__":
    experiments()