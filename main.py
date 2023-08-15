from vrComplexes import *
from persistenceDiagrams import *

two_circles = sampleCircles([20, 20], [1.0, 2.0], [[1.0, 1.0], [3.0, 3.0]])
_, time_series = sampleMarchese()
tau = 1
diagram1 = [[1.0, 1.5], [2.0, 2.5]]
diagram2 = [[0.8, 1.6], [3.0, 3.5]]

plotCloudData(two_circles, name = 'two-circles-data.png')
plotSeriesData(time_series, tau)
plotPersistenceDiagram(two_circles)
plotWassersteinDistance(diagram1, diagram2)
plotDCPDistance(diagram1, diagram2)
