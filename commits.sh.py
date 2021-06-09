import os
import sys
import subprocess
import string
import random

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """manycommits() {
    h=@; t=`git rev-parse @^{tree}`
    for i in `seq 2 "$1"`; do
        h=`echo "$*" | git commit-tree $t -p $h`
    done
    echo $h
}
twice() { "$@" a & "$@" b ; wait; }
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
    bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)