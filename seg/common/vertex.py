#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = "wu.zheng"


class Vertex(object):
    def __init__(self, word, id):

        self.word = word
        self.id = id
        self.pre_nodes = []
        self.current_index = 0

    def __le__(self, other):
        return self.id <= other.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __str__(self):
        return self.word

    def add_pre(self, from_node):
        self.pre_nodes.append(from_node)
        self.pre_nodes = sorted(self.pre_nodes)

    def is_last(self):
        if not self.pre_nodes:
            return True
        else:
            return self.current_index == len(self.pre_nodes) - 1

    def pop_pre(self):
        if not self.is_last():
            self.current_index+=1
            return self.pre_nodes[self.current_index]
        return None

    def get_current_pre(self):
        return self.pre_nodes[self.current_index]
