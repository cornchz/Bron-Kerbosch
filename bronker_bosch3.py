# coding: utf-8

from data import *
from bronker_bosch2 import bronker_bosch2
MIN_SIZE = 3


def bronker_bosch3(clique, candidates, excluded, reporter):
    '''Bron–Kerbosch algorithm with pivot and degeneracy ordering'''
    reporter.inc_count()
    if not candidates and not excluded:
        if len(clique) >= MIN_SIZE:
            reporter.record(clique)
        return
 
    for v in list(degeneracy_order(candidates)):
        new_candidates = candidates.intersection(NEIGHBORS[v])
        new_excluded = excluded.intersection(NEIGHBORS[v])
        bronker_bosch2(clique + [v], new_candidates, new_excluded, reporter)
        candidates.remove(v)
        excluded.add(v)


def degeneracy_order(nodes):
    # FIXME: can improve it to linear time
    deg = {}
    for node in nodes:
        deg[node] = len(NEIGHBORS[node])
 
    while deg:
        i, v = min(deg.iteritems(), key=lambda (i, v): v)
        yield i
        del deg[i]
        for v in NEIGHBORS[i]:
            if v in deg:

                deg[v] -= 1