import sys
import os
import random
from threading import Timer
import time

def sort():
    res = []
    root_path = 'hor/'

    fns = os.listdir(root_path)
    for fn in fns:
        path = os.path.join(root_path, fn)
        res.append(path)
    random.shuffle(res)
    with open('hor.txt', 'w') as f:
        for fn in res:
            f.write('{}\n'.format(fn))
    print "hor done"
    res = []
    root_path = 'ver/'

    fns = os.listdir(root_path)
    for fn in fns:
        path = os.path.join(root_path, fn)
        res.append(path)
    random.shuffle(res)
    with open('ver.txt', 'w') as f:
        for fn in res:
            f.write('{}\n'.format(fn))
    print "ver done"

if __name__ == '__main__':
    while True:
        sort()
        time.sleep(300)
