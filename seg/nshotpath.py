#!/usr/bin/env python
#-*-coding:utf-8-*-

__author__ = "wu.zheng"

from common.wordnet import WordNet
import copy


class NShotPath(object):

    def __init__(self):
        pass

    def seg(self, sentence):
        stack = []
        path = []
        word_net = WordNet(sentence)
        if not word_net.size:
            return path

        last_vertex = word_net.get_last_vertex()
        stack.append(last_vertex.id)

        if word_net.isfinish():
            path.append(copy.deepcopy(stack))
            return path

        current_vertex = last_vertex
        while not word_net.isfinish():
            current_vertex = current_vertex.pop_pre()
            if not current_vertex:
                return
            
            stack.append(current_vertex.id)
            if current_vertex.id==0:
                path.append(copy.deepcopy(stack))
                p_id = stack.pop(0)
















if __name__ == '__main__':
    sentence = u'我是正午'
    segment = NShotPath()
    segment.seg(sentence)

