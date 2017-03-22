# -*- coding: utf-8 -*-
"""
Velocity Verlet time integration method

Created on Tue Feb 28 12:49:52 2017

Author: Cara Lynch, Marina Ruiz Sanchez-Oro
"""

from ParticleList import ParticleSyst as P
import LennardJones as lj
import PBC

# Method to compute total energy of the system
def totE(syst, boxdim, R_c):
    """
    Calculates the total energy of the system
    
    :param syst: N body system represented as a ParticleSyst instance
    :param boxdim: box dimensions as a (1, N) numpy array
    :param R_c: cutoff radius
    :return: total energy of system as a float
    """
    return P.kineticEnergy(syst) + lj.totPE(syst, boxdim, R_c)

def VelVerlet(dt, syst, boxdim, R_c):
    """
    Performs one velocity verlet time integration loop
    
    :param dt: timestep as a float
    :param syst: ParticleSyst instance representing the system
    :param boxdim: box dimensions as a (1,N) Numpy array
    :param R_c: cutoff radius
    """
    force = lj.ljforce(syst, boxdim, R_c)
    # Update particle position
    P.leapPos2nd(syst, dt, force)
    
    # Apply periodic boundary conditions to position update
    syst.position = PBC.PBCpos(syst, boxdim)
    # Update force
    force_new =  lj.ljforce(syst, boxdim, R_c)
    # Update particle velocity based on average and current new forces
    P.leapVelocity(syst, dt, 0.5*(force + force_new))
    
