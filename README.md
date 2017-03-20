# Lennard-Jones N Body System

## Overview
This program describes N-body systems interacting through the Lennard-Jones pair potential. It can be used to simulate a Lennard-Jones solid, fluid and gas.

## Notes on class used
Instead of using the Particle3D class, we created a ParticleSyst class which deals with the whole system with arrays in an attempt to make the simulation more efficient. We therefore do not use our Particle3D class, but our ParticleSyst class is very similar, just deals with a whole system of particles instead of 1 particle.

A ParticleSyst instance has the following properties:
* name: name of system as a string
* label: labels of particles as an (N,1) Numpy array of strings (where the label of the nth particle is at label[n,0]
* N: number of particles in the system as an integer
* position: positions of the particles as an (N,3) Numpy array of floats (where the position of the nth particle is in position[n])
* velocity: velocities of the particles as an (N,3) Numpy array of floats (where the velocity of the nth particle is in velocity[n])
* mass: mass of the particles in the system (all having equal mass) as a float. *The code can be modified by making this an (N,1) array and changing force calculations etc* 

## Running the simulation
NBodySyst.py must be run using Python 3 [1]. It requires the input of a file name, which it will prompt from the user. The mass of the particles and simulation timestep are set to 1.0 and 0.01.

## Input

### Input format
The input file must be in the following format:


[name of system]  [number of particles]  [temperature]  [density]

[cutoff radius]  [number of steps]

All data is in reduced units.

### Input files

There are 3 input files contained in our submission:
* solid.in
* fluid.in
* gas.in

## Output

NBodySim creates output files and plots, all in reduced units. These all have the name of system, followed by the data contained in the file, as their names.

### Output files and format

* __[name of system]msd.out__ - *file of mean squared displacement data where each line is:* [timestep number]  [MSD of system]
* __[name of system]rdf.out__ - file of radial distribution data where each line is: [radial distance of a particle from the reference particle at a certain time]
* __[name of system]energy.out__ - file of energy data where each line is: [timestep number]  [kinetic energy of system]  [potential energy of system]  [total energy of system]
* __[name of system]VMD.xyz__ -  trajectory file for plotting the system using VMD
* __[name of system]Energyevolution.png__  - graph of energy evolution (KE, PE and total E) of system vs timestep number
* __[name of system]Histogram.png__ - radial distribution function of system as a histogram, with frequency density vs radial distance from reference particle r
* __[name of system]MSD.png__ - graph of mean squared displacement of system vs timestep number

[1] Python 3 is used instead of 2.7 as there are issues with the Python 2.7 numpy.histogram package installed in the computer lab
