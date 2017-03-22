"""
Mean Squared Distance vs timestep plotter.

Cara Lynch

19/03/2017
"""

import matplotlib.pyplot as pyplot

def plot(fileName,name):
    """
    Plots MSD as a function of time
    
    :param fileName: name of file with MSD data as a string
    :param name: name of system as a string
    """
    
    # Set up data lists for plotting MSD
    dtValue = []
    MSDValue = []
    
    # Open MSD file for reading
    Infile = open(fileName, "r")
    lines = Infile.readlines()
    numstep = len(lines)

    # Start loop to append values to data lists
    for i in range(0,numstep):
        data = lines[i].split()
        dtValue.append(data[0])
        MSDValue.append(data[1])
    
    # Plot graph of MSD vs timestep number
    pyplot.plot(dtValue,MSDValue, "g")
    pyplot.title("Mean Squared Distance over time for a " + str(name))
    pyplot.xlabel("Time step number")
    pyplot.ylabel("MSD ")
    pyplot.savefig(str(name)+'MSDevolution')
    pyplot.show()



