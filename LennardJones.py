""" 
Lennard Jones Module 

Returns the force and potential energy acting on every particle through the Lennard-Jones pair potential as well as the total potential energy of the system.

Authors: Marina Ruiz Sanchez-Oro, Cara Lynch

21/02/2017
"""

import numpy as np
from ParticleList import ParticleSyst as P


def ljforce(system,boxdim,Rc) :
    """
    Computes the Lennard-Jones force acting on each particle in the system as an (N,3) Numpy array.
	
    :param system: ParticleSyst object representing the system of N particles
    :param boxdim: Box dimensions as an (1,3) Numpy array
    :param Rc: cutoff radius as a float
    :return force: an (N,3) Numpy array where the ith row is the force experienced by the ith particle
    """
    # Create force array with initial condition of 0.0 force everywhere
    force = np.zeros(shape=(system.N,3))
    
    # Compute force on ith particle
    for i in range (0,system.N):
        # Compute magnituge of vector separation and vector separation (both arrays)
        r = P.sepmag(system,boxdim,i)
        rvec = P.MICvecsep(system,boxdim,i)
        
        # Compute with respect to jth particle
        for j in range(0,system.N):
            # Not computing force particle has on itself
            if i !=j :
                # Cutoff radius condition
                if r[j]<Rc:
                    for k in range(0,3):
                        force[i,k] += 48.*(1./(r[j]**14.) + 1./(2.*r[j]**8.))*rvec[j,k]
                else:
                    pass
            else:
                pass
    return force
	
def ljpotential(system,boxdim,Rc) :
    """
    Computes the Lennard-Jones potential of each particle in the system as an (N,1) Numpy array.
    
    :param system: ParticleSyst object representing the system of N particles
    :param boxdim: Box dimensions as a (1,3) Numpy array
    :param Rc: cutoff radius
    :return force: an (N,1) Numpy array where the ith row is the potential of the ith particle
    """
    
    # Create potential array with initial condition of 0.0 potential on each particle
    potential = np.zeros(shape=(system.N))
    
    # Compute potential of ith particle
    for i in range (0,system.N):
        # Compute magnituge of vector separation with respect to all particles
        r = P.sepmag(system,boxdim,i)
        
        # Compute potential with respect to jth particle
        for j in range(0,system.N):
            # Not computing potential from itself
            if i !=j :
                # Cutoff radius condition
                if r[j]<Rc:
                    potential[i]+= 4.*(1./(r[j]**12.) - 1./(r[j]**6.))
                else:
                    pass
            else:
                pass
    return potential

def totPE(system, boxdim, Rc):
    """
    Computes the total potential energy of the system according to the Lennard-Jones potential.
    
    :param system: ParticleSyst object representing the system of N particles
    :param boxdim: Box dimensions
    :param Rc: cutoff radius
    :return totalPE: a float representing the potential of the system
    """
    # Compute the potential of each individual particle
    potential = ljpotential(system,boxdim,Rc)
    
    # Set initial potential as a float
    doubletotalPE = 0.0
    
    # Add all potentials
    for i in range(0,system.N):
        doubletotalPE += potential[i]
    # Every interaction is counted twice so must divide potential calculated by 2
    return doubletotalPE/2.0

 
