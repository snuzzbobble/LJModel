# -*- coding: utf-8 -*-
"""
NBody Simulation

Created on Tue Feb 28 13:18:18 2017

@author: snuzz
"""

import matplotlib.pyplot as pyplot
from ParticleList import ParticleSyst as P
import VelVerlet as vv
import MDUtilities as md
import histogram as hist
import numpy as np
import random
import LennardJones as lj
import time as systime

# Input file name from command line
fileName = str(input("File name: "))
dt = float(input("timestep: "))

# Open file for reading 
file = open(fileName, "r")
lines = file.readlines()
line0 = lines[0].split()
line1 = lines[1].split()

# Extract simulation parameters
name = str(line0[0]) #name of system
N = int(line0[1]) # number of particles
temp = float(line0[2]) # temperature
rho = float(line0[3]) # density
r_c = float(line1[0]) # LJ cutoff radius
numstep = int(line1[1]) # number of steps
# dt = float(line1[2]) # timestep




# Set additional parameters
m = 1.0
boxdim = (N/rho)**(1./3.)

# Open system file for writing
systemFile = open("system.in", "w")

systemFile.write(name + " " + str(N) + " " + str(m) + "\n")

for i in range (0, N):
    label = "p" + str(i)
    pos1 = random.uniform(0.0, boxdim)
    pos2 = random.uniform(0.0, boxdim)
    pos3 = random.uniform(0.0, boxdim)
    systemFile.write(label + " " + str(pos1) + " " + str(pos2) + " " + str(pos3) + " 0.0 0.0 0.0 \n")

systemFile.close()



   
# Create ParticleSyst instance
System = P.createsystem("system.in")

# Initialise with MDUtilities
boxdim = md.setInitialPositions(rho, System)
md.setInitialVelocities(temp, System)


k = 0 # timestep number

# Open output file for VMD trajectory information
VMDfile = open("VMD.xyz", "w")

# Open output file for radial distribution function information
RDFfile = open("rdf.out", "w")

# Open output file for mean squared displacement information
MSDfile = open("msd.out","w")

# Open output file for energy fluctuations in the format: Kinetic Potential Total
Energyfile = open("energy.out","w")

# Save initial positions to an array to compute the MSD
initialpositions = System.position

# Set up data lists for plotting energy
tValue = [0]
KEValue = [P.kineticEnergy(System)]
PEValue = [lj.totPE(System,boxdim,r_c)]
totEValue = [vv.totE(System, boxdim, r_c)]
             
# Write values to files
Energyfile.write("0 " + str(P.kineticEnergy(System)) + " "  + str(lj.totPE(System,boxdim,r_c)) + " " + str(vv.totE(System, boxdim, r_c)) + "\n")


# Start time integration loop
for i in range(1, numstep):
    # Perform VV time integration
    vv.VelVerlet(dt, System, boxdim, r_c)
    force = lj.ljforce(System,boxdim,r_c)
    # Output trajectory information for VMD file
    trajectory = P.printVMD(System, k)
    VMDfile.write(trajectory)
    
    # Output energy information for energy file
    tValue.append(i)
    KEValue.append(P.kineticEnergy(System))
    PEValue.append(lj.totPE(System,boxdim,r_c))
    totEValue.append(vv.totE(System, boxdim, r_c))
    
    Energyfile.write(str(i) + " " + str(P.kineticEnergy(System)) + " "  + str(lj.totPE(System,boxdim,r_c)) + " " + str(vv.totE(System, boxdim, r_c)) + "\n")
    
    # Only save trajectory information for RDF and MSD every second timestep
    # if i%2. == 0:
    # RDF histogram calculation
    for l in range(0, System.N):
        # Output radial distances for RDF
        hist.particledistances(System, RDFfile,l)
        # MSD calculation
        displacementarray = System.position - initialpositions
        
    MSDtimesN = 0.0
    # Sum over all squared displacements
    for m in range(0, System.N):
        MSDtimesN += np.inner(displacementarray[m],displacementarray[m])
        # Divide by N
    MSD = MSDtimesN/System.N
            
    # Add to MSD file with format: timestep MSD
    MSDfile.write(str(i)+ " " + str(MSD) + "\n")
    
    # Increase timestep number tracker
    k += 1
    
    # Give percentage of completion of simulation
    
    if i%(numstep/10.0) == 0:
        print(str(systime.strftime("%H:%M:%S") + " - " + str(int(i*100/numstep)) + "% Completed"))

# Close output files    
VMDfile.close()
RDFfile.close()
MSDfile.close()
Energyfile.close()

# plot graph of energy fluctuations
pyplot.plot(tValue,totEValue, "g", label="Total Energy")
pyplot.plot(tValue, KEValue, "r", label = "Kinetic Energy")
pyplot.plot(tValue, PEValue, "b", label = "Potential Energy")
pyplot.legend()
pyplot.title("Energy over timesteps")
pyplot.xlabel("Time step number")
pyplot.ylabel("Energy ")
pyplot.savefig('Energyevolution')


pyplot.show()

    
# Histogram for RDF function
hist.histogram("rdf.out")


