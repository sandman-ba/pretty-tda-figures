import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from ripser import Rips


# Example persistence diagram (two circles/ two squares)
# Probably same example used for VR complexes
def plotPersistenceDiagram(point_cloud, dimensions = [0, 1], name = 'persistence-diagram.png'):

    rips = Rips()

    diagram = rips.fit_transform(point_cloud)

    fig = plt.figure(figsize = (6.4, 4.8))

    rips.plot(diagram, ax = plt.gca(), plot_only = dimensions, diagonal = True, show = False, legend = True)

#    for k in dimensions:
#        ax.plot(*diagram[k].T, '.', markersize = 20)

#    ax.set_xlim(0.0, 0.6)
#    ax.set_ylim(0.0, 0.8)

    plt.savefig(f"figures/{name}")

    return fig


# --------------------------------
# Wasserstein distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
def plotWassersteinDistance(diagram1, diagram2, name = 'wasserstein-distance.png'):

    diagonal = np.linspace(-0.1, 3.6, 3)

    fig = plt.figure(figsize = (6.4, 4.8))

    plt.plot(diagonal, diagonal, '--k')
#    plt.set_xlim(0.0, 3.5)
#    plt.set_ylim(0.0, 3.5)


    plt.plot(*diagram1.T, '.', markersize = 20)

    plt.plot(*diagram2.T, '.', markersize = 20)

    # Plot matching

    plt.savefig(f"figures/{name}")

    return fig


# --------------------------------
# dcp distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
# Label unmatched points with c
def plotDCPDistance(diagram1, diagram2, name = 'dcp-distance.png'):

#    diagonal = np.linspace(-0.1, 1.1, 3)

    fig = plt.figure(figsize = (6.4, 4.8))

#    ax.plot(diagonal, diagonal, '--k')
    plt.plot([-0.1, 3.6], [-0.1, 3.6], '--k')
#    plt.set_xlim(0.0, 3.5)
#    plt.set_ylim(0.0, 3.5)


    plt.plot(*diagram1.T, '.', markersize = 20)

    plt.plot(*diagram2.T, '.', markersize = 20)

    # Plot matching

    plt.savefig(f"figures/{name}")

    return fig
