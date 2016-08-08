#!/usr/bin/env python
# -*-coding=utf-8-*-

import copy


def dijkstra(graph, start):
    path = []
    vertex_list = copy.deepcopy(graph)
    for v in vertex_list:
        if v.id == start.id:
            v.distance = 0

    vertex_list = sorted(vertex_list)

    while vertex_list:
        current_node = vertex_list.pop(0)
        path.append(current_node)
        for v, distance in current_node.connections.items():
            new_distance = current_node.get_distance() + distance
            if new_distance < v.distance:
                v.distance = new_distance
                v.pre = current_node
        vertex_list = sorted(vertex_list)

    for v in path:
        print (str(v), v.distance, str(v.pre))


if __name__ == '__main__':
    import graph

    g = graph.Graph()
    v_1 = graph.Vertex(1)
    v_2 = graph.Vertex(2)
    v_3 = graph.Vertex(3)

    g.add_edge(v_1, v_2, 1)
    g.add_edge(v_1, v_3, 3)
    g.add_edge(v_2, v_3, 2)
    dijkstra(g, v_1)
