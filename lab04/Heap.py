import numpy as np


class Heap:
    def __init__(self, data_list, ary):    # n is an ary of a heap
        self.ary = ary
        self.data = data_list
        self.build_heap()
    
    def get_children(self, idx):
        children_list = []
        data_size = len(self.data)

        for i in range(1, self.ary + 1):
            child_id = self.ary * idx + i
            if child_id < data_size:
                children_list.append(child_id)
        return children_list

    def heapify(self, idx):
        current_max_node = idx
        children = self.get_children(idx)
        considered_nodes = children + [idx]
        considered_nodes_values = []

        for element in considered_nodes:
            considered_nodes_values.append(self.data[element])

        # max_value = max(considered_nodes_values)
        # max_id = self.data.index(max_value)
        max_value = np.max(considered_nodes_values)
        max_id = np.where(self.data == max_value)[0][-1]

        if current_max_node != max_id:
            self.data[current_max_node], self.data[max_id] = self.data[max_id], self.data[current_max_node]
            self.heapify(max_id)

    def build_heap(self):
        idx = len(self.data) // self.ary - 1
        for i in range(idx, 0, -1):
            self.heapify(i)

    def print_heap(self, idx, level=0):
        if len(self.data) > 0:
            print(level*"   |", self.data[idx])
            children = self.get_children(idx)
            for ch in children:
                self.print_heap(ch, level+1)

    def delete_root(self):
        if len(self.data) > 0:
            self.data[0] = self.data[len(self.data) - 1]
            self.data = self.data[:-1]
            if len(self.data) > 0:
                self.heapify(0)

    def get_parent(self, idx):
        """Returns index of the parent node"""
        if idx == 0:
            return None
        return (idx - 1) // self.ary 

    def insert_element(self, element):
        self.data = self.data + [element]
        current_index = len(self.data) - 1
        parent = self.get_parent(current_index)
        while(parent != None and (self.data[parent] < self.data[current_index])):
            self.heapify(parent)
            current_index = parent
            parent = self.get_parent(current_index)
