#  This is slicing
l = [10,20,30,40]
print(l[2:])
print(l[:2])
my_list = [[]]*3
board = [['_']*3 for i in range(3)]
print(board)
board2 = [['_']*3]*3
print(board)
print('Lets add some stuff inside the boards')
board[1][2] = 'X'
board2[1][2] = 'X'
print(board)
print(board2)

l = [1,2,3]
print(id(l))
l*= 2
print(id(l))
print(l)

t = (1,2,3)
print(id(t))
t *= 3
print(t)
print(id(t))
t = (1,2,[30,40])
#t[2] += [50,60]
import dis
def func():
    t[2] += [50,60]
    return(t)

dis.dis(func)

# performing Search in Python
print('Now moving on to searching stuff in Python')

import bisect
import sys

HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position *'    |'
        print(ROW_FMT.format(needle,position,offset))

if __name__ == '__main__':
    if sys.argv[-1] ==  'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)
print('haystack->','    '.join("%2d" % n for n in HAYSTACK))
demo(bisect_fn)
