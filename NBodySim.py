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


# Ask for name of system file
systemFile = str(raw_input("Name of file representing the system: "))

# Ask for density and temperature
rho = float(raw_input("Density of system: "))
temp = float(raw_input("Temperature of system: "))
    
# Create ParticleSyst instance
System = P.createsystem(systemFile)

# Initialise with MDUtilities
boxdim = md.setInitialPositions(rho, System)
md.setInitialVelocities(temp, System)

# Ask for and set simulation parameters
numstep = int(raw_input("Number of steps for time integration: "))
time = 0.0
dt = float(raw_input("Time step: ")) # timestep
r_c = float(raw_input("Cutoff radius (usually between 2.5 and 3.5): ")) #cutoff radius
k = 1 # timestep number

# Open output file for VMD trajectory information
VMDfile = open("VMD.xyz", "w")

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


