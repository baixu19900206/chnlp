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
            # todo push
            # step 3
            while current_vertex.id > 0:
                first_vertex = current_vertex.get_current_pre()
                stack.append(first_vertex.id)
                current_vertex = first_vertex
            path.append(copy.deepcopy(stack))

            if not stack:
                return path

            while stack:
                current_vertex= word_net.get_vertex(stack.pop())
                if current_vertex.is_last():
                    continue
                else:
                    break
                print 'stack'

        return path


if __name__ == '__main__':
    # sentence = u'今天，刘志军案的关键人物,山西女商人丁书苗在市二中院出庭受审'
    sentence = u'他说的确实在理'
    segment = NShotPath()
    path = segment.seg(sentence)
    for p in path :
        print p
