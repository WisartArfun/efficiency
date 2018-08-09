# -*- coding: utf-8 -*-
from __future__ import division, print_function
import pickle
import random
import numpy as np
import sys
import argparse
import os.path
import datetime

import pprint
import json
import pdb
import inspect

import multiprocessing


def show_var(expression):

    for i in expression:
        frame = sys._getframe(1)
        value = eval(i, frame.f_globals, frame.f_locals)

        if ' object at ' in repr(value):
            value = vars(value)
            value = json.dumps(value, indent=2)
            print(i, ':', value)
        else:
            print(i, ':', repr(value))


def write_var(var, path='data/debug/var'):
    with open(path, 'w') as f:
        f.write(path.split('/')[-1] +
                ' = ' + repr(var) + '\n')


def fwrite(new_doc, path):
    if not path:
        print("[Info] Path does not exist in fwrite():", str(path))
        return
    with open(path, 'w') as f:
        f.write(new_doc)


def fread(path):
    with open(path, 'r') as f:
        return f.readlines()


def show_time(what_happens=''):
    disp = '⏰\ttime: ' + \
        datetime.datetime.now().strftime('%m%d%H%M-%S')
    disp = disp + '\t' + what_happens if what_happens else disp
    print(disp)
    return datetime.datetime.now().strftime('%m%d%H%M')


def bug():
    import pdb
    pdb.set_trace()
    # you can use "c" for continue, "p variable", "p locals", "n" for next
    # you can use "!a += 1" for changes of variables
    # you can use "import code; code.interact(local=locals)" to iPython with all variables


def shell(cmd, show_res=False):
    import sys
    import os
    import subprocess
    from subprocess import PIPE, Popen

    subp = Popen(cmd, shell=True, stdout=PIPE, stderr=subprocess.STDOUT)
    subp_output = subp.communicate()[0]

    if show_res:
        print("Here is the output:", subp_output, "[[end]]")
    return subp_output


def mproc(func, input_list, avail_cpu=multiprocessing.cpu_count() - 4):
    '''
    This is a multiprocess function where you execute the function with 
    every input in the input_list simutaneously.
    @ return output_list: the list of outputs w.r.t. input_list
    '''
    from multiprocessing import Pool
    pool = Pool(processes=min(len(input_list), avail_cpu))
    output_list = pool.map(func, input_list)
    return output_list
