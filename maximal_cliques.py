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


class BronkerBosch(object):
    def __init__(self):
        self.reporter = Reporter(self.__class__.__name__)

    def iterator(self, candidates, excluded):
        raise NotImplementedError()

    def run(self, nodes):
        self.reporter.clear()
        self.recur([], set(nodes), set())
        self.reporter.print_report()

    def recur(self, clique, candidates, excluded):
        self.reporter.inc_count()
        if not candidates and not excluded:
            if len(clique) >= MIN_SIZE:
                self.reporter.record(clique)
            return

        for v in self.iterator(candidates, excluded):
            new_candidates = candidates.intersection(NEIGHBORS[v])
            new_excluded = excluded.intersection(NEIGHBORS[v])
            self.recur(clique + [v], new_candidates, new_excluded)
            candidates.remove(v)
            excluded.add(v)


class BronkerBosch1(BronkerBosch):
    def iterator(self, candidates, excluded):
        return list(candidates)


class BronkerBosch2(BronkerBosch):
    def iterator(self, candidates, excluded):
        pivot = self.pick_from_set(candidates) or self.pick_from_set(excluded)
        return list(candidates.difference(NEIGHBORS[pivot]))

    def pick_from_set(self, _set):
        if _set:
            elem = _set.pop()
            _set.add(elem)
            return elem


class BronkerBosch3(BronkerBosch2):
    def run(self, nodes):
        self.first = True
        super(BronkerBosch3, self).run(nodes)

    def iterator(self, candidates, excluded):
        # Iterate in degeneracy order at the first depth
        if self.first:
            self.first = False
            return list(self.degeneracy_order(candidates))
        # In deeper calls, act like bronker_bosch2
        else:
            return super(BronkerBosch3, self).iterator(candidates, excluded)

    def degeneracy_order(self, nodes):
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
        self.clear()

    def clear(self):
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
    BronkerBosch1().run(NODES)
    BronkerBosch2().run(NODES)
    BronkerBosch3().run(NODES)


if __name__ == '__main__':
    main()