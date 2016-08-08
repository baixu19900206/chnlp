#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = "wu.zheng"

from vertex import Vertex
from dictionary.coredictionary import Dictionary


class WordNet(object):
    def __init__(self, sentence):
        self.vertexs = {}
        self.sentence = sentence
        self.size = len(sentence)
        self.init_wordnet()


    def init_wordnet(self):
        pre = None
        for k, w in enumerate(list(self.sentence)):
            vertex = Vertex(w, k)

            if not pre:
                pre = vertex
            else:
                vertex.add_pre(pre)
            self.vertexs[k] = vertex


        for w in Dictionary():
            if len(w) == 1:
                continue
            if w in self.sentence:
                start_w = w[0]
                end_w = w[-1]
                end_index = self.sentence.index(end_w)
                self.vertexs[end_index].add_pre(start_w)


    def get_vertex(self, word_id):
        return self.vertexs.get(word_id)


    def ids(self):
        return range(self.size)

    def isfinish(self):
        return all([item.is_last() for item in self.vertexs.values()])

    def get_last_vertex(self):
        return self.vertexs.get(self.size-1)



if __name__ == '__main__':
    WordNet(u'我是正午')
