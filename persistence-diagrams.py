import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from ripser import Rips


def plotPersistenceDiagrams(diagram1, diagram2, k = 1):

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(*diagram1[k].T, '.', markersize = 20)
    ax1.set_xlim(0.0, 0.6)
    ax1.set_ylim(0.0, 0.8)

    ax2.plot(*diagram2[k].T, '.', markersize = 20)
    ax2.set_xlim(0.0, 0.6)
    ax2.set_ylim(0.0, 0.8)

    plt.savefig('figures/persistence-diagrams.png')

    return 1
