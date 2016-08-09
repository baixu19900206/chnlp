#!/usr/bin/env python
#-*-coding:utf-8-*-

__author__ = "wu.zheng"

from common.wordnet import WordNet
import copy



class NShotPath(object):

    def __init__(self):
        pass

    def seg(self, sentence, n):

        if not sentence:
            return sentence

        stack = []
        path = []
        word_net = WordNet(sentence)

        last_node = word_net.get_last()
        stack.append(last_node)
        current_node = last_node

        while stack:
            while current_node!=0:
                first_node = word_net.get_vertex(current_node).get_current_node()

                stack.append(first_node)
                current_node = first_node

            path.append(copy.deepcopy(stack))

            # path[0] = sorted(path[0])
            # for index in range(len(path[0])-1):
            #     print sentence[path[0][index]:path[0][index+1]]
            # print path

            current_node = stack.pop()

            while True:
                print stack
                current_vertex = word_net.get_vertex(current_node)

                if not stack:
                    break

                if not current_vertex.has_pre() and stack:
                    current_node = stack.pop()
                    continue
                else:
                    stack.append(current_node)
                    current_node = current_vertex.pop_pre()
                    stack.append(current_node)
                    break



        return path


if __name__ == '__main__':
    # sentence = u'今天，刘志军案的关键人物,山西女商人丁书苗在市二中院出庭受审'
    sentence = u'商品和服务'
    sentence =u'安徽省合肥市长江路'
    sentence = u'他说的确实在理'
    segment = NShotPath()
    path = segment.seg(sentence, 3)
    for p in path :
        p = sorted(p)
        print p
        print "#"*10
        print len(p)
        for index in range(len(p)-1):
            print sentence[p[index]:p[index+1]]
