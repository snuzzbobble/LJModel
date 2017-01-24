"""
Compmod project

Particle tester
"""

import sys
import math
import numpy as np
from Particle3D import Particle3D as P

#Read name of input file
if len(sys.argv)!=2:
    print "Wrong number of arguments."
    quit()
else:
    infile = sys.argv[1] 

p_file = open(infile, "r")
particle = P.createparticle(p_file)
print particle
