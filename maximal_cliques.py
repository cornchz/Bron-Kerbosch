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


def bronker_bosch1(clique, candidates, excluded, reporter):
	reporter.inc_count()
	if not candidates and not excluded:
		if len(clique) >= MIN_SIZE:
			reporter.report(clique)
		return

	for v in list(candidates):
		new_candidates = candidates.intersection(NEIGHBORS[v])
		new_excluded = excluded.intersection(NEIGHBORS[v])
		bronker_bosch1(clique + [v], new_candidates, new_excluded, reporter)
		candidates.remove(v)
		excluded.add(v)


def bronker_bosch2(clique, candidates, excluded, reporter):
	reporter.inc_count()
	if not candidates and not excluded:
		if len(clique) >= MIN_SIZE:
			reporter.report(clique)
		return

	pivot = pick_random(candidates) or pick_random(excluded)
	for v in list(candidates.difference(set(NEIGHBORS[pivot]))):
		new_candidates = candidates.intersection(NEIGHBORS[v])
		new_excluded = excluded.intersection(NEIGHBORS[v])
		bronker_bosch2(clique + [v], new_candidates, new_excluded, reporter)
		candidates.remove(v)
		excluded.add(v)


def bronker_bosch3(clique, candidates, excluded, reporter):
	reporter.inc_count()
	if not candidates and not excluded:
		if len(clique) >= MIN_SIZE:
			reporter.report(clique)
		return

	for v in degeneracy_order(candidates):
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
	def __init__(self):
		self.cnt = 0
		self.cliques = []

	def inc_count(self):
		self.cnt += 1

	def report(self, clique):
		self.cliques.append(clique)

	def _print(self):
		print '%d recursive calls' % self.cnt
		for i, clique in enumerate(self.cliques):
			print '%d: %s' % (i, clique)


def main():
	for version in xrange(1, 4):
		report = Reporter()
		globals()['bronker_bosch%d' % version]([], set(NODES), set(), report)
		report._print()


if __name__ == '__main__':
	main()