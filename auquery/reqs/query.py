import time
from reqs.prettytable import PrettyTable
from reqs.utils import get_username
from reqs.logparse import result as res

header_column = ["time", "node", "command", "exit", "user_id", "username"]
_values_key =    ["time", "node", "comm", "exit", "auid"]
tab = PrettyTable(header_column)

q_result = []

class Query(object):
    def __init__(self, time_start='', time_end='', node='', comm='', exit='', auid='', username=''):
        ''' '''
        now = time.strftime("%d/%b/%Y %H:%M", time.localtime())
        #now = False
        self.obj_list = [str(time_start), str(time_end), str(node), str(comm).split(' ')[0], str(exit), str(auid)]
        self.values_keys = ["time", "node", "comm", "exit", "auid"]
        self.list = []

        self.show(self.obj_list)
    
    def query(self, obj_list):
        global q_result
        ql = []
        obj_l = []
        for obj in self.obj_list:
            if obj:
                obj_l.append(obj)
        if obj_l:
            for i in range(len(res)):
                if set(obj_l).issubset(res[i].values()):
                    ql.append(res[i])
            q_result = ql
        else:
            q_result =  res
        return q_result
    
    def show(self, obj_list):
        """ """
        res = self.query(obj_list)
        if not res:
            print("No Result")
        for row in range(len(res)):
            values = []
            for r in self.values_keys:
                values.append(res[row][r])
            values.append(get_username(res[-1],res,row))
            tab.add_row(values)
        print(tab.get_string(sortby="time"))
        #tab.clear_rows()