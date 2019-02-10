
from reqs.utils import format_date
import glob
from socket import gethostname

audit_logfile = '/var/log/audit/audit.*'

with open('/var/log/audit/all.log','w') as outfile:
  for fname in glob.iglob(audit_logfile):
    with open(fname) as infile:
      for line in infile:
        if 'SYSCALL' in line:
          outfile.write(line)

_log_file = "/var/log/audit/all.log"
_log_list = []
# _node_list = []
# for i in range(1,8): 
#   _node_list.append("dp-train-0%s"%(i))
_master_node = gethostname()

_data = open(_log_file).readlines()

_txt_replace = ['\n','audit','(',')',':'] 

def get_log_list(data): 
    for i in data:
        #i = i.decode("utf-8") 
        if 'SYSCALL' in i and 'comm' in i and 'tty' in i:
            i = i.replace('\n','').replace('audit','').replace('(','').replace(')','').replace(':','')
            _log_list.append(dict(x.split('=') for x in i.split(' ')))
    for i in _log_list:
        i['time'] = i.pop('msg')
        i['time'] = format_date(i['time'])
        if not 'node' in i.keys():
            i['node'] = _master_node

    return _log_list

result = get_log_list(_data)