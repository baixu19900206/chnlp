#!/usr/bin/env python
# -*-coding=utf-8-*-

import warnings
import sys


class Vertex(object):
    """

    vertex
    param:
    vertex_id : id
    """

    def __init__(self, vertex_id):
        self.id = vertex_id
        self.connections = {}
        self.distance = sys.maxsize
        self.pre = None
        self.visited = False

    def __str__(self):
        return 'vertex_' + str(self.id)

    def get_weight(self, vertex):
        return self.connections.get(vertex, sys.maxsize)

    def add_connection(self, to_vertex, distance):
        self.connections[to_vertex] = distance

    def get_distance(self):
        return self.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __hash__(self):
        return self.id


class Graph(object):
    def __init__(self):
        self.vertexs = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex in self.vertexs:
            warnings.warn('%s is in graph' % (vertex))
            return
        self.vertexs.append(vertex)

    def get_vertex(self, vertex):
        if vertex in self.vertexs:
            return vertex
        return None

    def add_edge(self, from_vertex, to_vertex, distance):

        if from_vertex not in self.vertexs:
            self.add_vertex(from_vertex)

        if to_vertex not in self.vertexs:
            self.add_vertex(to_vertex)
        from_vertex.add_connection(to_vertex, distance)

    def __iter__(self):
        return iter(self.vertexs)


if __name__ == '__main__':
    graph = Graph()
    v_1 = Vertex(1)
    v_2 = Vertex(2)
    graph.add_edge(v_1, v_2, 10)
    print(graph.vertexs[0].get_connections())
