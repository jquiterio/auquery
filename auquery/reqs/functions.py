from reqs.command import Command
from reqs.query import Query
from reqs.query import q_result
from reqs.query import tab
from reqs.utils import _print
from reqs.query import header_column

class Reset(Command):
    def run(self, line):
        tab.clear_rows()
        _print('\x1b[6;30;42m' + 'OK' + '\x1b[0m')

class AllCmd(Command):
    def run(self, line):
        r = Query()
        return r

class Username(Command):
    def run(self, line):
        last_arg = line.split()[-1]
        print("Filtering username for %s..." % last_arg)
        return Query(username=last_arg)

class CommandQ(Command):
    def run(self, line):
        last_arg = line.split()[-1]
        print("Filtering command for %s..." % last_arg)
        return Query(comm=last_arg)

class UserIDCmd(Command):
    def run(self, line):
        last_arg = line.split()[-1]
        print("Filtering userID for %s..." % last_arg)
        return Query(auid=last_arg)

class Node(Command):
    def run(self, line):
        last_arg = line.split()[-1]
        print("Filtering node for %s..." % last_arg)
        return Query(node=last_arg)


#### With Results
class Limit(Command):
    def run(self, line):
        last_arg = line.split()[-1]
        print(tab.get_string(start=0,end=int(last_arg)))

class AlignColumn(Command):
    def args(self):
        return ['l','c','r']

    def run(self, line):
        last_arg = line.split()[-1]
        tab.align = last_arg
        print(tab)

class Sort(Command):
    def args(self):
        return header_column

    def run(self, line):
        last_arg = line.split()[-1]
        print(tab.get_string(sortby=last_arg))

class ExportHTML(Command):
    def run(self,line):
        with open('/tmp/auquery.hml', 'w') as fp:
            fp.write(tab.get_html_string())
            fp.close
        print("Html file create!: /tmp/auquery.hml")

