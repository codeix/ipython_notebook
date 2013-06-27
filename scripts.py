# -*- coding: utf-8 -*-
import os
import sys


def notebook():
    script = os.path.join(os.path.dirname(sys.argv[0]), 'ipython')
    os.environ['PYTHONPATH'] = ':'.join(sys.path)
    os.execve(script, [script, 'notebook', '--pylab'] + sys.argv[1:],
              os.environ)
