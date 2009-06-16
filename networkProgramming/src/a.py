#my first python program :}

import string

def _ReadFile(text,numlines):
    lines = string.split(text,' ')
    while lines:
        chunk = lines[:numlines]
        for line in chunk:
            if line:
                print line

        lines = lines[numlines:]       
        if lines:
            if raw_input('More?') not in ['y','Y']:
                print "read over."
                break
        else:
            print "read over."
            break

if __name__ == '__main__':
    import sys
    file = open(sys.argv[1],'r')
    numlines = raw_input("enter read char num:");
    if numlines:
        _ReadFile(file.read(),string.atoi(numlines))
    else:
        _ReadFile(file.read(),1)
    file.close()

