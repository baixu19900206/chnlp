#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = "wu.zheng"

from vertex import Vertex
from dictionary.coredictionary import Dictionary


class WordNet(object):
    def __init__(self, word_list):
        self.vertexs = {}
        self.size = len(word_list)
        self.word_list = word_list


    def add_vertex(self, w_index):

        w = self.word_list[w_index]
        self.vertexs[w_index] = Vertex(w_index, w)


    def add_connect(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertexs.keys():
            self.add_vertex(from_vertex_id)

        if to_vertex_id not in self.vertexs.keys():
            self.add_vertex(to_vertex_id)

        self.vertexs[to_vertex_id].add_pre(from_vertex_id)



if __name__ == '__main__':
    graph = WordNet([u'始##始', u'商', u'商品', u'品', u'和',u'和服',u'服' u'服务', u'务', u'末##末'])
    graph.add_connect(0,1)
    graph.add_connect(0,2,)
    graph.add_connect(1,3)
    graph.add_connect(2,4)
    graph.add_connect(3,4)
    graph.add_connect(2,5)
    graph.add_connect(3,5)
    graph.add_connect(4,6)
    graph.add_connect(4,7)
    graph.add_connect(5,8)
    graph.add_connect(6,8)
    graph.add_connect(7,9)
    graph.add_connect(8,9)

