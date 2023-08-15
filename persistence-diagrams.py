import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from ripser import Rips


# Example persistence diagram (two circles/ two squares)
# Probably same example used for VR complexes
def plotPersistenceDiagram(diagram, dimensions = [0, 1]):

    fig, ax = plt.figure()

    for k in dimensions:
        ax.plot(*diagram[k].T, '.', markersize = 20)

    ax.set_xlim(0.0, 0.6)
    ax.set_ylim(0.0, 0.8)

    plt.savefig('figures/persistence-diagram.png')

    return fig, ax

    rips1 = Rips()
    rips2 = Rips()

    diagram1 = rips1.fit_transform(pointCloud1)
    diagram2 = rips2.fit_transform(pointCloud2)

    rips1.plot(diagram1, ax = ax3, plot_only = [1], labels = '$H_1$', diagonal = False, show = False, legend = False)
    rips2.plot(diagram2, ax = ax4, plot_only = [1], labels = '$H_1$', diagonal = False, show = False, legend = False)

# --------------------------------
# Wasserstein distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
def plotWassersteinDistance(diagram1, diagram2):

    diagonal = np.linspace(-0.1, 1.1, 3)

    fig, ax = plt.figure()

    ax.plot(diagonal, diagonal, '--k')
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)


    ax.plot(*diagram1.T, '.b', markersize = 20)

    ax.plot(*diagram2.T, '.o', markersize = 20)

    # Plot matching

    plt.savefig('figures/wasserstein-distance.png')

    return fig, ax


# --------------------------------
# dcp distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
# Label unmatched points with c
def plotDCPDistance(diagram1, diagram2):

    diagonal = np.linspace(-0.1, 1.1, 3)

    fig, ax = plt.figure()

    ax.plot(diagonal, diagonal, '--k')
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)


    ax.plot(*diagram1.T, '.b', markersize = 20)

    ax.plot(*diagram2.T, '.o', markersize = 20)

    # Plot matching

    plt.savefig('figures/dcp-distance.png')

    return fig, ax
