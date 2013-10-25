# coding: utf-8

class Reporter(object):
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []
 
    def inc_count(self):
        self.cnt += 1
 
    def report(self, clique):
        self.cliques.append(clique)
 
    def _print(self):
        print self.name
        print '%d recursive calls' % self.cnt
        for i, clique in enumerate(self.cliques):
            print '%d: %s' % (i, clique)
        print
