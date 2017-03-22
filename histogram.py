# -*- coding: utf-8 -*-
"""
Radial Distribution Function algorithm

Collects distances between pairs of particles and plots the RDF.

Created on Sun Feb 26 11:43:43 2017

Author: Cara Lynch, Marina Ruiz Sanchez-Oro
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from ParticleList import ParticleSyst as P

def particledistances(syst, fileName,boxdim, k):
    """
    Collects distances between pairs of particles at a specific point in time with respect to the k th particle (the reference particle) and exports into a file.
    
    :param syst: N body system represented as a ParticleSyst instance
    :param fileName: name of file which the trajectories will be exported to as a string
    :param boxdim: box dimensions as a Numpy array
    :param k: index of reference particle as an integer
    """
   
    # Compute radial distances from reference particle k
    radialdistance = P.sepmag(syst,boxdim,k)

    for i in range(0, syst.N):
        
        # If reference particle, do not append data to file
        if i == k:
            pass
        else:
            fileName.write("{0:.4f} \n".format(radialdistance[i]))
            
        



def histogram(fileName, name, syst, rho, numstep):
    """
    Plots a normalised histogram of the radial distribution function.
    
    :param fileName: name of file with RDF data as a string
    :param name: name of system as a string
    :param syst: ParticleSyst instance representing the system
    :param rho: density of system
    :param numstep: number of timesteps
    """
    
    # Open the file of radial distances for reading
    fileIn = open(fileName, "r")

    # Make array of distances
    distances = fileIn.readlines()
    rdfArray = np.array(distances, dtype = float)
    
    
    # Bin values
    hist,bin_edges=np.histogram(rdfArray, bins = 100, density = False)
    
    # Compute bin size
    dr = bin_edges[1]-bin_edges[0]
    
    # Normalise histogram
    histnormalised = hist
    for i in range(0, hist.size):
        histnormalised[i] = hist[i]/(4*math.pi*bin_edges[i]**(2)*rho*syst.N*numstep*dr)
    
    # Delete one element of bin_edges array so that histnormalised and xdata have the same shape
    xdata = np.delete(bin_edges,hist.size-1)
    
    # Plot histogram
    plt.plot(xdata,histnormalised, "g", label="rdf")
    plt.title("Histogram of radial distribution function for a " + str(name))
    plt.xlabel("Radial distance")
    plt.ylabel("Frequency density")
    plt.savefig(str(name)+'Histogram')
    plt.show()


    
