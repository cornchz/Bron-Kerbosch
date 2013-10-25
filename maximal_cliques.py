# coding: utf-8

MIN_SIZE = 3
NEIGHBORS = [
    [], # I want to start index from 1 instead of 0
    [2, 3, 4],
    [1, 3, 4, 5],
    [1, 2, 4, 5],
    [1, 2, 3],
    [2, 3, 6, 7],
    [5, 7],
    [5, 6],
]
NODES = set(range(1, len(NEIGHBORS)))


def bronker_bosch(clique, candidates, excluded, reporter, iterator):
    reporter.inc_count()
    if not candidates and not excluded:
        if len(clique) >= MIN_SIZE:
            reporter.record(clique)
        return

    for v in iterator(candidates, excluded):
        new_candidates = candidates.intersection(NEIGHBORS[v])
        new_excluded = excluded.intersection(NEIGHBORS[v])
        bronker_bosch(clique + [v], new_candidates, new_excluded, reporter, iterator)
        candidates.remove(v)
        excluded.add(v)


def bronker_bosch1(nodes, reporter):
    '''Naive Bron–Kerbosch algorithm'''
    def iterator(candidates, excluded):
        return list(candidates)

    bronker_bosch([], set(nodes), set(), reporter, iterator)


def bronker_bosch2(nodes, reporter):
    '''Bron–Kerbosch algorithm with pivot'''
    def iterator(candidates, excluded):
        pivot = pick_from_set(candidates) or pick_from_set(excluded)
        return list(candidates.difference(NEIGHBORS[pivot]))

    bronker_bosch([], set(nodes), set(), reporter, iterator)


def bronker_bosch3(nodes, reporter):
    '''Bron–Kerbosch algorithm with pivot and degeneracy ordering'''
    first = [True]

    def iterator(candidates, excluded):
        # Iterate in degeneracy order at the first depth
        if first[0]:
            first[0] = False
            return list(degeneracy_order(candidates))
        # In deeper calls, act like bronker_bosch2
        else:
            pivot = pick_from_set(candidates) or pick_from_set(excluded)
            return list(candidates.difference(NEIGHBORS[pivot]))

    bronker_bosch([], set(nodes), set(), reporter, iterator)


def pick_from_set(_set):
    if _set:
        elem = _set.pop()
        _set.add(elem)
        return elem

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


class Reporter(object):
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []

    def inc_count(self):
        self.cnt += 1

    def record(self, clique):
        self.cliques.append(clique)

    def print_report(self):
        print self.name
        print '%d recursive calls' % self.cnt
        for i, clique in enumerate(self.cliques):
            print '%d: %s' % (i, clique)
        print


def main():
    for version in xrange(1, 4):
        func = globals()['bronker_bosch%d' % version]
        report = Reporter('## %s' % func.func_doc)
        func(NODES, report)
        report.print_report()


if __name__ == '__main__':
    main()