import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


# General topologial objects to explain tda and betti numbers
# Ball, sphere, circle, torus...
# Or perhaps clusters, circles, line...


# --------------------------------
# Simple example for VR complexes (two squares, two circles)

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


def plotCloudData(point_cloud, name = 'data-point-cloud.png'):

    fig = plt.figure(figsize = (6.4, 4.8))

    plt.plot(point_cloud[:,0], point_cloud[:,1], '.')

    plt.savefig(f"figures/{name}")

    return fig


# --------------------------------
# Time series example
# Takens embedding

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


def takens(time_series, tau, dim = 2):
    """
    This function returns Takens' delay embeding of a time series {x_t}
        X_k = ( x_k, x_{k + tau}, ..., x_{k + d*tau} )
    where tau is the delay parameter and d is the dimension minus 1.
    """

    T = time_series.size
    N = T - (dim - 1) * tau
    point_cloud = np.zeros( (N, dim) )

    for i in range(dim):
        point_cloud[:,i] = time_series[tau * i : N + tau * i]

    return point_cloud


def plotSeriesData(time_series, tau, name = 'data-time-series.png'):
    point_cloud = takens(time_series, tau)

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(time_series)

    ax2.plot(point_cloud[:,0], point_cloud[:,1], '.')

    plt.savefig(f"figures/{name}")

    return fig, (ax1, ax2)
