import numpy as np
from queue import PriorityQueue

class Vertex:
    def __init__(self, x, y, value, id):
        self.x = x
        self.y = y
        self.value = value
        self.id = id
        self.idx = self.x + Graph.MAXSIZE * self.y
        self.neighbours = []
        self.before = None

    def add_neighbour(self, neighbor_idx):
        self.neighbours.append(neighbor_idx)

    def show(self):
        return "Value: {}, index: {}. Neighbours: {}".format(self.value, self.idx, self.neighbors)

    def __lt__(self, n):
        return self.value < n.value


class Graph:
    MAXSIZE = 100

    def __init__(self, board):
        self.start = None
        self.end = None
        self.number_vertices = 0
        self._board = board
        self._visited = []
        self._vertices_dict = self._create_vertices_dict()
        self.edges = self._create_edges_list()
        self.vertices = self._create_vertices_list()
        self.path = [i for i in range(self.number_vertices)]

    def _create_vertices_dict(self):
        vertices = dict()

        for idx_y, row in enumerate(self._board):
            for idx_x, value in enumerate(row):
                vertex = Vertex(idx_x, idx_y, value, self.number_vertices)
                self.number_vertices += 1

                vertices[vertex.idx] = vertex
                if value == 0 and self.start is None:
                    self.start = vertex
                elif value == 0 and self.start is not None:
                    self.end = vertex

        return vertices

    def _create_edge(self, vertex: Vertex, shift: int):
        vertex_a = vertex.idx
        vertex_b = self._vertices_dict[vertex.idx + shift].idx
        cost = self._vertices_dict[vertex_b].value
        return [vertex_a, vertex_b, cost]

    def _create_edges_list(self):
        vertices_idx = list(self._vertices_dict.keys())
        edges = []

        # To shift left/right add +-1, to shift up/right add +-Graph.MAXSIZE
        shifts = [-1, 1, -Graph.MAXSIZE, Graph.MAXSIZE]

        for idx, vertex in self._vertices_dict.items():
            for shift in shifts:
                if (idx + shift) in vertices_idx:
                    vertex.add_neighbour(idx + shift)
                    edges.append(self._create_edge(vertex, shift))

        return edges

    def _create_vertices_list(self):
        return list(self._vertices_dict.values())

    def dijkstra(self):
        D = [np.Inf for _ in range(self.number_vertices)]
        D[self.start.id] = 0

        pq = PriorityQueue()
        pq.put((0, self.start))

        while not pq.empty():
            (distance, current_vertex) = pq.get()
            self._visited.append(current_vertex.id)

            for neighbour_vertex_id in current_vertex.neighbours:
                neighbour_vertex = self._vertices_dict[neighbour_vertex_id]
                distance = neighbour_vertex.value

                if neighbour_vertex.id not in self._visited:
                    old_cost = D[neighbour_vertex.id]
                    new_cost = int(D[current_vertex.id] + distance)

                    if new_cost < old_cost:
                        pq.put((new_cost, neighbour_vertex))
                        D[neighbour_vertex.id] = new_cost
                        neighbour_vertex.before = current_vertex.id

        before = self.end
        path = [before.id]
        while before.id != self.start.id:
            before = self.vertices[before.before]
            path.append(before.id)

        path.reverse()
        self.path = path
        return path

    def print(self):
        board = [[' ' for _ in range(self._board.shape[1])] for _ in range(self._board.shape[0])]

        for id in self.path:
            vertex = self.vertices[id]
            board[vertex.y][vertex.x] = str(int(vertex.value))
        board = '\n'.join([''.join(row) for row in board])
        print(board)
