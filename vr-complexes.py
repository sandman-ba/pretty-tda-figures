import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


def sampleCircles(n, r, p, eps = 0.0):
    """
    This function samples nk points from a circle of radius rk centered at pk
    for each entry of n, r and p.
    If eps is positive, then samples will have noise of magnitud eps.
    Note: n, r, and p must have the same length.
    """
    x = np.array([])
    y = np.array([])
    for nk, rk, pk in zip(n, r, p):
        x0, y0 = pk
        angles = np.linspace(0.0, 2 * np.pi, nk, endpoint = False)
        if eps > 0.0:
            noise_x = eps * rand(nk)
            noise_y = eps * rand(nk)

            x = np.concatenate((x, x0 + rk * np.cos(angles) + noise_x))
            y = np.concatenate((y, y0 + rk * np.sin(angles) + noise_y))
        else:
            x = np.concatenate((x, x0 + rk * np.cos(angles)))
            y = np.concatenate((y, y0 + rk * np.sin(angles)))


    return np.array([x, y]).T

def sampleMarchese(n = 25, step = 0.01):
    """
    This function samples n points from the distributions
        v_k = U * sin(k * step) + N_k
        w_k = U * ( 1 + 0.5 * cos(k * step) ) * cos(k * step) + N_k
    where U ~ Unif(1, 3) and N_k ~ Normal(0, 0.1)
    """

    unif = np.random.default_rng().uniform(1.0, 3.0)
    norm = np.random.default_rng().normal(0, 0.1, n)
    grid = np.linspace(0, step * n, n)

    v = norm + (unif * np.sin(grid))

    w = norm + (unif * (1 + (0.3 * np.cos(6 * grid)) ) * np.cos(grid) )

    return (v, w)


def takens(timeSeries, tau, dim = 2):
    """
    This function returns Takens' delay embeding of a time series {x_t}
        X_k = ( x_k, x_{k + tau}, ..., x_{k + d*tau} )
    where tau is the delay parameter and d is the dimension minus 1.
    """

    T = timeSeries.size
    N = T - (dim - 1) * tau
    pointCloud = np.zeros( (N, dim) )

    for i in range(dim):
        pointCloud[:,i] = timeSeries[tau * i : N + tau * i]

    return pointCloud

def plotCloudData(pointCloud1, pointCloud2):
    rips1 = Rips()
    rips2 = Rips()

    diagram1 = rips1.fit_transform(pointCloud1)
    diagram2 = rips2.fit_transform(pointCloud2)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = 'row', sharex = 'row')

    ax1.plot(pointCloud1[:,0], pointCloud1[:,1], '.')
    ax2.plot(pointCloud2[:,0], pointCloud2[:,1], '.')

    rips1.plot(diagram1, ax = ax3, plot_only = [1], labels = '$H_1$', diagonal = False, show = False, legend = False)
    rips2.plot(diagram2, ax = ax4, plot_only = [1], labels = '$H_1$', diagonal = False, show = False, legend = False)

    plt.savefig('figures/data-point-cloud.png')

    return [diagram1, diagram2]

def plotSeriesData(timeSeries1, timeSeries2, tau):
    pointCloud1 = takens(timeSeries1, tau)
    pointCloud2 = takens(timeSeries2, tau)

    rips1 = Rips()
    rips2 = Rips()

    diagram1 = rips1.fit_transform(pointCloud1)
    diagram2 = rips2.fit_transform(pointCloud2)

    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(2, 3, sharey = 'row', sharex = 'row')

    ax1.plot(timeSeries1)
    ax2.plot(timeSeries2)

    ax3.plot(pointCloud1[:,0], pointCloud1[:,1], '.')
    ax4.plot(pointCloud2[:,0], pointCloud2[:,1], '.')

    rips1.plot(diagram1, ax = ax3, plot_only = [1], labels = '$H_1$', diagonal = False, show = False, legend = False)
    rips2.plot(diagram2, ax = ax4, plot_only = [1], labels = '$H_1$', diagonal = False, show = False, legend = False)

    plt.savefig('figures/data-time-series.png')

    return [diagram1, diagram2]
