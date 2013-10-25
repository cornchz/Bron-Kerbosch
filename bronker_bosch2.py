# coding: utf-8
 
from data import *
MIN_SIZE = 3


def bronker_bosch2(clique, candidates, excluded, reporter):
    '''Bron–Kerbosch algorithm with pivot'''
    reporter.inc_count()
    if not candidates and not excluded:
        if len(clique) >= MIN_SIZE:
            reporter.record(clique)
        return
 
    pivot = pick_random(candidates) or pick_random(excluded)
    for v in list(candidates.difference(NEIGHBORS[pivot])):
        new_candidates = candidates.intersection(NEIGHBORS[v])
        new_excluded = excluded.intersection(NEIGHBORS[v])
        bronker_bosch2(clique + [v], new_candidates, new_excluded, reporter)
        candidates.remove(v)
        excluded.add(v)


def pick_random(s):
    if s:
        elem = s.pop()
        s.add(elem)
        return elem
