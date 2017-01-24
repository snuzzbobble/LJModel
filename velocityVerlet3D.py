
"""
Computer Modelling Exercise 3: Symplectic Euler 3D

Authors: Marina Ruiz Sanchez-Oro, Cara Lynch

Date: 08/11/2016

Perform time integration for a particle's motion in 3D and plot its trajectory in the xy-plane using the velocity Verlet time integration algorithm.This program requires two input arguments: a file name for the trajectory data and a file name for the energy data.
"""

import sys
import math 
import matplotlib.pyplot as pyplot
import numpy as np
from Particle3D import Particle3D as P

# Method to compute gravitational force between two point masses as a vector using a (1,3) Numpy array 
def vectorforce(p1,p2):
    # Compute vector separation of particles
    rvector = P.vectorseparation(p1,p2)
    # Compute magnitude of separation of particles
    rscalar = math.sqrt(np.inner(rvector,rvector))
    return (-p1.mass*p2.mass/rscalar**3)*rvector

# Method to compute the potential energy of the system
def potential(p1,p2):
    # Compute vector separation of particles
    rvector = P.vectorseparation(p1,p2)
    return -p1.mass*p2.mass/math.sqrt(np.inner(rvector,rvector))

# Method to compute total energy of the system
def energy(p1,p2):
    return P.kineticEnergy(p1)+ P.kineticEnergy(p2) + potential(p1,p2)


# Read name of output files from command line
if len(sys.argv)!=3:
    print "Wrong number of arguments."
    print "Usage: " + sys.argv[0] + " < output file >  < energy difference output file >"
    quit()
else:
    outfileName1 = sys.argv[1]		# Trajectory output file
    outfileName2 = sys.argv[2]		# Energy difference output file


# Open output files for witing
outfile1 = open(outfileName1, "w")
outfile2 = open(outfileName2, "w")

# Import particle from file
p_file = open("orbitingparticle.in", "r")
particle = P.createparticle(p_file)

# Import central mass
mass_file = open("centralmass.in", "r")
centralmass = P.createparticle(mass_file)

# Set up simulation parameters
numstep = 100
time = 0.0
dt = 0.5888


# Set up data lists
# For plotting trjectory
xValue = [particle.position[0]]
yValue = [particle.position[1]]

outfile1.write("{0:f} {1:f}\n".format(particle.position[0],particle.position[1]))



# For plotting variation of energy difference (energy-initial energy) over time
tValue = [time]
eValue = [0]

outfile2.write("{0:f} {1:f}\n".format(time,0))

# Calculate the initial force
force=vectorforce(particle, centralmass)

# Calculate the initial energy
initialE = energy(particle, centralmass)


# Start the time integration loop
for i in range(numstep):
    # Update particle position
    particle.leapPos2nd(dt,force)
    # Update force
    force_new = vectorforce(particle, centralmass)
    # Update particle velocity, based on average current and new forces
    particle.leapVelocity(dt, 0.5*(force+force_new))
    # Reset force variable
    force = force_new
    # Increase time
    time = time + dt
    
    # Output particle information
    xValue.append(particle.position[0])
    yValue.append(particle.position[1])

    outfile1.write("{0:f} {1:f}\n".format(particle.position[0], particle.position[1]))
    
    # Output energy and time information
    tValue.append(time)
    eValue.append(energy(particle, centralmass)- initialE)

    outfile2.write("{0:f} {1:16.12f}\n".format(time,energy(particle, centralmass) - initialE))

# Close output files
outfile1.close()
outfile2.close()

pyplot.figure(1)
# Plot graph of trajectory in x-y plane
pyplot.plot(xValue,yValue)
pyplot.title("Trajectory of particle")
pyplot.xlabel("x axis")
pyplot.ylabel("y axis")
pyplot.savefig('verlettrajectory')


pyplot.figure(2)
# Plot graph of energy of system - initial energy over time
pyplot.plot(tValue,eValue, "g")
pyplot.title("Difference in energy over time")
pyplot.xlabel("Time (s)")
pyplot.ylabel("Energy difference (J)")
pyplot.savefig('verletenergy difference')


pyplot.show()
