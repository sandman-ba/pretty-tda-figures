import numpy as np
from numpy import linalg as LA
from numpy.random import rand
import matplotlib.pyplot as plt
from ripser import Rips


# Example persistence diagram (two circles/ two squares)
# Probably same example used for VR complexes
def plotPersistenceDiagram(point_cloud, dimensions = [0, 1], name = 'persistence-diagram.png', figure_size = (3.2, 3.1) ):

    rips = Rips()

    diagram = rips.fit_transform(point_cloud)

    fig = plt.figure(figsize = figure_size, dpi = 200)

    rips.plot(diagram, ax = plt.gca(), plot_only = dimensions, diagonal = True, show = False, legend = True)

#    for k in dimensions:
#        ax.plot(*diagram[k].T, '.', markersize = 20)

#    ax.set_xlim(0.0, 0.6)
#    ax.set_ylim(0.0, 0.8)

    plt.savefig(f"figures/{name}", bbox_inches = 'tight')

    return fig


def distances(diagram, k = 1, p = 2, q = 2):

    def projection(point):
        x = (point[0] + point[1]) / 2
        proj = np.array([ x , x ])
        return proj

    def distance(difference):
        return LA.norm( difference, q, axis = 1 )

    difference = [ a - projection(a) for a in diagram ]
    dist = distance(difference)

    return dist


# --------------------------------
# Wasserstein distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
def plotWassersteinDistance(diagram1, diagram2, name = 'wasserstein-distance.png', figure_size = (4.8, 4.8)):

    projection = np.sum(diagram1[1, :]) / 2
    distances1 = distances(diagram1)
    distances2 = distances(diagram2)

    fig, ax = plt.subplots(figsize = figure_size, dpi = 200)

    ax.plot([-0.1, 3.6], [-0.1, 3.6], '--k')
    ax.set_xlim(0.0, 3.5)
    ax.set_ylim(0.0, 3.5)
    ax.set_xlabel('Birth')
    ax.set_ylabel('Death')

    # Plot circles
    for point, dist in zip(diagram1, distances1) :
        circle = plt.Circle(point, dist, color = 'tab:blue', alpha = 0.2)
        ax.add_patch(circle)

    for point, dist in zip(diagram2, distances2) :
        circle = plt.Circle(point, dist, color = 'tab:orange', alpha = 0.2)
        ax.add_patch(circle)

    # Plot matching
    ax.plot([diagram1[0, 0], diagram2[0, 0]], [diagram1[0, 1], diagram2[0, 1]], ':m')
    ax.plot([diagram1[1, 0], projection], [diagram1[1, 1], projection], ':m')


    ax.plot(*diagram1.T, 'o', markersize = 8)

    ax.plot(*diagram2.T, '^', markersize = 8)

    plt.savefig(f"figures/{name}", bbox_inches = 'tight')

    return fig


# --------------------------------
# dcp distance
# Two diagrams (two points each, a pair close and the other far away)
# Lines for the matching
# Label unmatched points with c
def plotDCPDistance(diagram1, diagram2, c = 0.5, name = 'dcp-distance.png', figure_size = (4.8, 4.8)):

    fig, ax = plt.subplots(figsize = figure_size, dpi = 200)

    ax.plot([-0.1, 3.6], [-0.1, 3.6], '--k')
    ax.set_xlim(0.0, 3.5)
    ax.set_ylim(0.0, 3.5)
    ax.set_xlabel('Birth')
    ax.set_ylabel('Death')

    # Plot circles
    for point in diagram1 :
        circle = plt.Circle(point, c, color = 'tab:blue', alpha = 0.2)
        ax.add_patch(circle)

    # Plot matching
    ax.plot([diagram1[0, 0], diagram2[0, 0]], [diagram1[0, 1], diagram2[0, 1]], ':m')
    ax.annotate('$c$', xy = diagram1[1, :], xycoords = 'data', xytext = (-9, 5), textcoords = 'offset points', color = 'm')


    ax.plot(*diagram1.T, 'o', markersize = 8)

    ax.plot(*diagram2.T, '^', markersize = 8)

    plt.savefig(f"figures/{name}", bbox_inches = 'tight')

    return fig, ax
