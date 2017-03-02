# -*- coding: utf-8 -*-
"""
NBody Simulation

Created on Tue Feb 28 13:18:18 2017

@author: snuzz
"""

import sys
from ParticleList import ParticleSyst as P
import VelVerlet as vv
import MDUtilities as md
import histogram as hist
"""
# Read name of input file and value of density and temperature from command line
if len(sys.argv)!=4:
    print("Wrong number of arguments")
    print("Usage: " + sys.argv[0] + "<input file> <density as float> < temperature >")
    quit()
else:
    infile = sys.argv[1]  # System input file
    rho = float(sys.argv[2]) # Density of system
    temp = float(sys.argv[3])
"""
    
# Create ParticleSyst instance
System = P.createsystem("system1.in")
rho = 1.0
temp = 200.0

# Initialise with MDUtilities
boxdim = md.setInitialPositions(rho, System)
md.setInitialVelocities(temp, System)

# Set simulation parameters
numstep = 100
time = 0.0
dt = 0.2 # timestep
r_c = 3.0 #cutoff radius
k = 1 # timestep number

# Open output file for VMD trajectory information
VMDfile = open("VMD.out", "w")

# Open output file for radial distribution function information
RDFfile = open("rdf.out", "w")

# Start time integration loop
for i in range(1, numstep):
    # Perform VV time integration
    vv.VelVerlet(dt, System, boxdim, r_c, time)
    
    # Output trajectory information for VMD file
    trajectory = P.printVMD(System, k)
    VMDfile.write(trajectory)
    
    for l in range(0, System.N):
        
        # Output radial distances for RDF
        hist.particledistances(System, RDFfile,l)
    
    
    # Increase timestep number
    k += 1

# Close output files    
VMDfile.close()
RDFfile.close()
    
# Histogram for RDF function
hist.histogram("rdf.out")


