# -*- coding: utf-8 -*-
"""
Periodic Boundary Conditions module

A module complete with a method that implements Periodic Boundary Conditions.

Created on Wed Feb 22 21:03:52 2017

Author: Cara Lynch
"""



def PBCpos(syst, boxdim):
    """
    Periodic Boundary Conditions algorithm that returns the updated positions of the particles.
    
    :param syst: system represented as a ParticleSyst instance
    :param boxdim: dimensions of box represented as an (1,3) Numpy array
    :return: position of the particle according to the PBC update
    """
    position = syst.position
    for i in range(0, syst.N):
        # Applying to the i th particle
        
        for j in range(0,3):
            # for x, y and z directions
            
            if position[i,j] < 0.:
                # if the particle is in the negative region, add a length of the box to that coordinate
                position[i,j] = position[i,j]%boxdim[j]
            if position[i,j] > boxdim[j]:
                    # if the particle is outside the box in the positive direction, subtract a length of the box in that coordinate
                position[i,j] = position[i,j]%boxdim[j]
    return position
    
