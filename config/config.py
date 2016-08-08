#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = "wu.zheng"

import os

BASE_PATH = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])


class Config(object):
    CORE_DICTIONARY_PATH = os.path.join(BASE_PATH, 'data/CoreNatureDictionary.txt')
