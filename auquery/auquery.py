#!/bin/env python

from reqs.command import Command
from reqs.console import Console
import reqs.functions as fn


console = Console(prompt="auquery", prompt_delim=">")

#### SHOW SUBCOMMANDS
show = Command('show', help='Show command')
allcmd = fn.AllCmd('all', help='Show All results happening now')
username = fn.Username('username', help='Query by username')
userid = fn.UserIDCmd('userid', help="Query by userid")
cmdq = fn.CommandQ('command', help='Command by command')
node = fn.Node('node', help='Query by Node name')

console.addChild(show).addChild(userid)
console.addChild(show).addChild(allcmd)
console.addChild(show).addChild(username)
console.addChild(show).addChild(cmdq)
console.addChild(show).addChild(node)


##### WITH RESULT SUBCOMMAND
wr = Command('withresult', help='Do something with last result')
sort = fn.Sort('sortby', help='Sort result', dynamic_args=True)
limit = fn.Limit('limit', help='Limit Result... 1,2,3 or 4')
align = fn.AlignColumn('align', help='Align a all Column: Left, Center or Right', dynamic_args=True)
export = fn.ExportHTML('exportHTML', help='Export result')

console.addChild(wr).addChild(sort)
console.addChild(wr).addChild(limit)
console.addChild(wr).addChild(align)
console.addChild(wr).addChild(export)

### RESET
reset = fn.Reset('reset', help='Reset results')
console.addChild(reset)
console.loop()
