import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from ripser import Rips


# Example persistence diagram (two circles/ two squares)
# Probably same example used for VR complexes
def plotPersistenceDiagram(point_cloud, dimensions = [0, 1], name = 'persistence-diagram.png'):

    rips = Rips()

    diagram = rips.fit_transform(point_cloud)

    fig = plt.figure(dpi = 200)

    rips.plot(diagram, ax = plt.gca(), plot_only = dimensions, diagonal = True, show = False, legend = True)

#    for k in dimensions:
#        ax.plot(*diagram[k].T, '.', markersize = 20)

#    ax.set_xlim(0.0, 0.6)
#    ax.set_ylim(0.0, 0.8)

    plt.savefig(f"figures/{name}", bbox_inches = 'tight')

    return fig


# --------------------------------
# Wasserstein distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
def plotWassersteinDistance(diagram1, diagram2, name = 'wasserstein-distance.png'):

    projection = np.sum(diagram1[1, :]) / 2

    fig = plt.figure(figsize = (4.8, 4.8), dpi = 200)

    plt.plot([-0.1, 3.6], [-0.1, 3.6], '--k')
    plt.xlim(0.0, 3.5)
    plt.ylim(0.0, 3.5)
    plt.xlabel('Birth')
    plt.ylabel('Death')

    # Plot matching
    plt.plot([diagram1[0, 0], diagram2[0, 0]], [diagram1[0, 1], diagram2[0, 1]], ':m')
    plt.plot([diagram1[1, 0], projection], [diagram1[1, 1], projection], ':m')


    plt.plot(*diagram1.T, 'o', markersize = 8)

    plt.plot(*diagram2.T, '^', markersize = 8)

    plt.savefig(f"figures/{name}", bbox_inches = 'tight')

    return fig


# --------------------------------
# dcp distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
# Label unmatched points with c
def plotDCPDistance(diagram1, diagram2, name = 'dcp-distance.png'):

    fig, ax = plt.subplots(figsize = (4.8, 4.8), dpi = 200)

    ax.plot([-0.1, 3.6], [-0.1, 3.6], '--k')
    ax.set_xlim(0.0, 3.5)
    ax.set_ylim(0.0, 3.5)
    ax.set_xlabel('Birth')
    ax.set_ylabel('Death')

    # Plot matching
    ax.plot([diagram1[0, 0], diagram2[0, 0]], [diagram1[0, 1], diagram2[0, 1]], ':m')
    ax.annotate('$c$', xy = diagram1[1, :], xycoords = 'data', xytext = (-9, 5), textcoords = 'offset points', color = 'm')


    ax.plot(*diagram1.T, 'o', markersize = 8)

    ax.plot(*diagram2.T, '^', markersize = 8)

    plt.savefig(f"figures/{name}", bbox_inches = 'tight')

    return fig, ax
