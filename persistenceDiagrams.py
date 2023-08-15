import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from ripser import Rips


# Example persistence diagram (two circles/ two squares)
# Probably same example used for VR complexes
def plotPersistenceDiagram(point_cloud, dimensions = [0, 1], name = 'persistence-diagram.png'):

    rips = Rips()

    diagram = rips.fit_transform(point_cloud)

    fig, ax = plt.figure(figsize = (6.4, 4.8))

    rips1.plot(diagram1, ax = ax, plot_only = dimensions, labels = '$H_1$', diagonal = True, show = True, legend = True)

#    for k in dimensions:
#        ax.plot(*diagram[k].T, '.', markersize = 20)

#    ax.set_xlim(0.0, 0.6)
#    ax.set_ylim(0.0, 0.8)

    plt.savefig(f"figures/{name}")

    return fig, ax


# --------------------------------
# Wasserstein distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
def plotWassersteinDistance(diagram1, diagram2, name = 'wasserstein-distance.png'):

    diagonal = np.linspace(-0.1, 1.1, 3)

    fig, ax = plt.figure(figsize = (6.4, 4.8))

    ax.plot(diagonal, diagonal, '--k')
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)


    ax.plot(*diagram1.T, '.', markersize = 20)

    ax.plot(*diagram2.T, '.', markersize = 20)

    # Plot matching

    plt.savefig(f"figures/{name}")

    return fig, ax


# --------------------------------
# dcp distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
# Label unmatched points with c
def plotDCPDistance(diagram1, diagram2, name = 'dcp-distance.png'):

#    diagonal = np.linspace(-0.1, 1.1, 3)

    fig, ax = plt.figure(figsize = (6.4, 4.8))

#    ax.plot(diagonal, diagonal, '--k')
    ax.plot([-0.1, 1.1], [-0.1, 1.1], '--k')
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)


    ax.plot(*diagram1.T, '.', markersize = 20)

    ax.plot(*diagram2.T, '.', markersize = 20)

    # Plot matching

    plt.savefig(f"figures/{name}")

    return fig, ax
