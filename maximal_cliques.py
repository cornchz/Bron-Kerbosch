# coding: utf-8

from bronker_bosch1 import bronker_bosch1
from bronker_bosch2 import bronker_bosch2
from bronker_bosch3 import bronker_bosch3
from data import *
from reporter import Reporter
 
 
if __name__ == '__main__':
    funcs = [bronker_bosch1,
             bronker_bosch2,
             bronker_bosch3]

    for func in funcs:
        report = Reporter('## %s' % func.func_doc)
        func([], set(NODES), set(), report)
        report.print_report()
