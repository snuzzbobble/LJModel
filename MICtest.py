"""
MIC tester
"""

from Particle3D import Particle3D as P
import numpy as np
import math
import sys
import MIC as mic

#Read name of input file
if len(sys.argv)!=4:
    print "Wrong number of arguments."
    quit()
else:
    infile1 = sys.argv[1] #particle1
    infile2 = sys.argv[2] #particle2
    L = float(sys.argv[3]) #box length

#Create particles
p1_file = open(infile1, "r")
p1 = P.createparticle(p1_file)

p2_file = open(infile2, "r")
p2 = P.createparticle(p2_file)

print mic.vecsep(p1,p2, L)


