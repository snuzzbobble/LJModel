"""
Lennard-Jones N-Body Simulation

Simulates an N-body system of particles interacting through the Lennard-Jones pair potential.

Outputs radial distribution function, mean squared distance and energy over time.

Created on Tue Feb 28 13:18:18 2017

Author: Cara Lynch, Marina Ruiz Sanchez-Oro
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
import MSDplot as MSDplot

# Input file name from command line
fileName = str(input("File name: "))

# Will be used to indicate time taken to complete simulation
systime.clock()

# Option to input timestep if needed
# dt = float(input("timestep: "))

# Ideal timestep found
dt = 0.01

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
m = 1.0 # Mass of particles

# Create system file which will be used to create a ParticleSyst instance
systemFile = open("system.in", "w")
systemFile.write(name + " " + str(N) + " " + str(m) + "\n")
for i in range (0, N):
    label = "p" + str(i)
    systemFile.write(str(label) +  " 0.0 0.0 0.0 0.0 0.0 0.0 \n")
systemFile.close()

# Create ParticleSyst instance
System = P.createsystem("system.in")

# Initialise with MDUtilities
boxdim = md.setInitialPositions(rho, System)
md.setInitialVelocities(temp, System)

k = 0 # timestep number

# Open output files 
VMDfile = open(str(name)+"VMD.xyz", "w") # VMD trajectory information
RDFfile = open(str(name)+"rdf.out", "w") # radial distribution function information
MSDfile = open(str(name)+"msd.out","w") # mean squared displacement information 
Energyfile = open(str(name)+"energy.out","w") # energy fluctuations in format: Kinetic Potential Total

# Save initial positions of particles to an array to compute the MSD
initialpositions = System.position

# Set up data lists for plotting energy
tValue = [0]
KEValue = [P.kineticEnergy(System)]
PEValue = [lj.totPE(System,boxdim,r_c)]
totEValue = [vv.totE(System, boxdim, r_c)]
             
# Write initial energy values to file
Energyfile.write("0 " + str.format("{0:.4f}",P.kineticEnergy(System)) + " "  + str.format("{0:.4f}",lj.totPE(System,boxdim,r_c)) + " " + str.format("{0:.4f}",vv.totE(System, boxdim, r_c)) + "\n")

# Print system time at beginning of loop
print(str(systime.strftime("%H:%M:%S") + " - " + " 0% of loop completed"))

# Start time integration loop
for i in range(1, numstep):
    
    # Perform VV time integration
    vv.VelVerlet(dt, System, boxdim, r_c)
    force = lj.ljforce(System,boxdim,r_c)
    
    # Output trajectory information for VMD file
    trajectory = P.printVMD(System, k)
    VMDfile.write(trajectory)
    
    
    # For a small enough number of steps, get Energy, RDF and MSD data for every step
    if numstep <= 1000:
        
        # Output energy information for energy file
        tValue.append(i)
        KEValue.append(P.kineticEnergy(System))
        PEValue.append(lj.totPE(System,boxdim,r_c))
        totEValue.append(vv.totE(System, boxdim, r_c))
    
        Energyfile.write(str(i) + " " + str.format("{0:.4f}",P.kineticEnergy(System)) + " "  + str.format("{0:.4f}",lj.totPE(System,boxdim,r_c)) + " " + str.format("{0:.4f}",vv.totE(System, boxdim, r_c)) + "\n")
        
        # RDF histogram and MSD calculation
        for l in range(0, System.N):
        
            # Output radial distances for RDF
            hist.particledistances(System, RDFfile,boxdim,l)
            
            # MSD calculation
            displacementarray = System.position - initialpositions
        
        MSDtimesN = 0.0
        # Sum over all squared displacements
        for m in range(0, System.N):
            MSDtimesN += np.inner(displacementarray[m],displacementarray[m])
        
        # Divide by N
        MSD = MSDtimesN/System.N
            
        # Add to MSD file with format: timestep MSD
        MSDfile.write(str(i)+ " " + str.format("{0:.4f}",MSD) + "\n")
         
    # For a large number of steps, only get Energy, RDF and MSD data every 4th step
    else:
        if i%4.0 == 0:
            
            # Output energy information for energy file
            tValue.append(i)
            KEValue.append(P.kineticEnergy(System))
            PEValue.append(lj.totPE(System,boxdim,r_c))
            totEValue.append(vv.totE(System, boxdim, r_c))
    
            Energyfile.write(str(i) + " " + str.format("{0:.4f}",P.kineticEnergy(System)) + " "  + str.format("{0:.4f}",lj.totPE(System,boxdim,r_c)) + " " + str.format("{0:.4f}",vv.totE(System, boxdim, r_c)) + "\n")
            
            # RDF histogram and MSD calculation
            for l in range(0, System.N):
        
                # Output radial distances for RDF
                hist.particledistances(System, RDFfile,boxdim,l)
                
                # MSD calculation
                displacementarray = System.position - initialpositions
        
            MSDtimesN = 0.0
            # Sum over all squared displacements
            for m in range(0, System.N):
                MSDtimesN += np.inner(displacementarray[m],displacementarray[m])
            # Divide by N
            MSD = MSDtimesN/System.N
            
            # Add to MSD file with format: timestep MSD
            MSDfile.write(str(i)+ " " + str.format("{0:.4f}",MSD) + "\n")
            
        else:
            pass
    

    # Increase timestep number tracker
    k += 1
    
    # Give percentage of completion of simulation every 5%
    if i%(numstep/20.0) == 0:
        print(str(systime.strftime("%H:%M:%S") + " - " + str(int(i*100/numstep)) + "% of loop completed"))

# Close output files    
VMDfile.close()
RDFfile.close()
MSDfile.close()
Energyfile.close()

print(str(systime.strftime("%H:%M:%S") + " - 100% of loop completed"))

# Indicate simulation time before graph plotting
print("It took "+ str(systime.clock()) + " seconds to compute the time evolution of an " + str(N) + " body system over " + str(numstep) + " steps")


# plot graph of mean squared distance evolution (MSD)
MSDplot.plot(str(name)+"msd.out",name)

    
# Histogram for RDF function
hist.histogram(str(name)+"rdf.out",name, System, rho)


# plot graph of energy fluctuations
pyplot.plot(tValue,totEValue, "g", label="Total Energy")
pyplot.plot(tValue, KEValue, "r", label = "Kinetic Energy")
pyplot.plot(tValue, PEValue, "b", label = "Potential Energy")
pyplot.legend()
pyplot.title("Energy over timesteps")
pyplot.xlabel("Time step number")
pyplot.ylabel("Energy ")
pyplot.savefig(str(name)+'Energyevolution')
pyplot.show()



