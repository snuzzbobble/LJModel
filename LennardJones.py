""" 
Lennard Jones: 
returns the force and potential energy acting on the ith particle through the Lennard-Jones pair potential 

Marina Ruiz Sanchez-Oro

Cara Lynch

21/02/2017
"""
import sys
import math
import matplotlib.pyplot as pyplot
import numpy as np
from ParticleList import ParticleSyst as P
import MIC as mic


# Calculates the force between two particles based on the separation, the cutoff radius and the box dimensions 

def ljforce(system,L,r) :
    force = np.empty(shape={P.N,3})
    for i in range(0, P.N + 1):
	for j in range(0, 3):
	    force[i,j] = 
	

	# Computes the vector separation of the particles
    rvector = mic.vecsep(p1,p2)
    # Computes the magnitue of the particle separation 
    rscalar = math.sqrt(np.inner(rvector,rvector))
        if rscalar > r_c :
	    return ljforce == 0
        else : 
	    return (48*((1/rscalar**14)-(1/(2*rscalar**8))))*rvector

# Calculates the Lennard Jones potential for the particle pair. 			
def ljpotential(p1,p2,L,r_c) :
    # Computes the vector separation of the particles
    rvector = mic.vecsep(p1,p2)
    # Computes the magnitude of the particle separation 
    rscalar = math.sqrt(np.inner(rvector,rvector)
        if rscalar > r_c :
	    return ljpotential == 0
        else : 
	    return (4*((1/rscalar**12)-(1/(r**6))))*rvector



	

 
