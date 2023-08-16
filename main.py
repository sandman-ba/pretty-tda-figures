from vrComplexes import *
from persistenceDiagrams import *
import numpy as np

two_circles_plot = sampleCircles([40, 40], [1.0, 1.5], [[1.0, 1.0], [3.5, 3.5]])
two_circles_diagram = sampleCircles([40, 40], [1.0, 1.5], [[1.0, 1.0], [7.0, 1.5]])
_, time_series = sampleMarchese(5000)
tau = 4200
diagram1 = np.array([[1.0, 1.5], [2.0, 2.5]])
diagram2 = np.array([[0.6, 1.7]])

plotCloudData(two_circles_plot, name = 'two-circles-data.png', no_labels = True, figure_size = (4.8, 4.8))
plotSeriesData(time_series, tau)
plotPersistenceDiagram(two_circles_diagram)
plotWassersteinDistance(diagram1, diagram2)
plotDCPDistance(diagram1, diagram2)
