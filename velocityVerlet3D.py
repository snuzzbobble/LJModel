
"""
Velocity Verlet
Authors: Marina Ruiz Sanchez-Oro, Cara Lynch
Date: 26/02/2017
Perform time integration for a particle's motion in 3D.This program requires two input arguments: a file name for the trajectory data and a file name for the energy data.
"""

import sys
import math 
import matplotlib.pyplot as pyplot
import numpy as np
from ParticleList import ParticleSyst as P
from LennardJones import LennardJones as lj
from MDUtilities import MDUtilities as mdu


# Read name of output files from command line
if len(sys.argv)!=3:
    print "Wrong number of arguments."
    print "Usage: " + sys.argv[0] + " < input file >  < energy difference output file >"
    quit()
else:
    infileName1 = sys.argv[1]		# Trajectory output file
    outfileName2 = sys.argv[2]		# Energy difference output file
# Open output files for writing
infile1 = open(infileName1, "r")
outfile2 = open(outfileName2, "w")
# Import particle from file
particlelist = P.createsystem(infile1)


# Set up simulation parameters
numstep = 100
time = 0.0
dt = 0.5888
rho=1
T=200
r_c= 2

boxsize=mdu.setInitialPositions(rho,particlelist)
initialvelocities= mdu.setInitialVelocities(T, particlelist)


# For plotting variation of energy difference (energy-initial energy) over time
tValue = [time]
eValue = [0]


# Calculate the initial force
force=lj.ljforce(particlelist,boxsize,r_c)
# Calculate the initial energy
initialE = particlelist.energy(boxsize, r_c)


# Start the time integration loop
for i in range(numstep):
    # Update particle position
    particlelist.leapPos2nd(dt,force)
    # Update force
    force_new =lj.ljforce(particlelist,boxsize,r_c)
    # Update particle velocity, based on average current and new forces
    particlelist.leapVelocity(dt, 0.5*(force+force_new))
    # Reset force variable
    force = force_new
    # Increase time
    time = time + dt
