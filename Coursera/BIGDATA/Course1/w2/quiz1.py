import sys

current_id = None
value =""
for line in sys.stdin:
    new_id, value = line.strip().split("\t",1)
    if new_id != current_id:
        if current_id:
            print("%s\t%s" % (current_id, value))
        current_id = new_id


if current_id:
    print("%s\t%s" % (current_id,value))

