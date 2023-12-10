from vrComplexes import *
from persistenceDiagrams import *
import numpy as np

clusters = sampleClusters(40, [[1.1, 0.9], [3.4, 3.6], [0.8, 3.3], [3.0, 1.3], [2.3, 2.5]])
two_circles_plot = sampleCircles([40, 50], [1.0, 1.5], [[1.0, 1.0], [3.5, 3.5]], eps = 0.1)
two_circles_diagram = sampleCircles([40, 50], [1.0, 1.5], [[1.0, 1.0], [7.0, 1.5]])
_, time_series = sampleMarchese(5000)
tau = 4200
diagram1 = np.array([[1.0, 1.5], [2.0, 2.5]])
diagram2 = np.array([[0.6, 1.7]])

plotCloudData(clusters, name = 'clusters.png', figure_size = (3.2, 3.1))
plotCloudData(two_circles_plot, name = 'two-circles-data.png', figure_size = (3.2, 3.1))
#plotCloudData(clusters, name = 'clusters.png', no_labels = True, figure_size = (4.8, 4.8))
#plotCloudData(two_circles_plot, name = 'two-circles-data.png', no_labels = True, figure_size = (4.8, 4.8))

plotPersistenceDiagram(two_circles_plot, name = 'circles-diagram.png')
plotPersistenceDiagram(clusters, name = 'clusters-diagram.png')

#plotSeriesData(time_series, tau)

plotWassersteinDistance(diagram1, diagram2, figure_size = (3.2, 3.1))
plotDCPDistance(diagram1, diagram2, figure_size = (3.2, 3.1))
