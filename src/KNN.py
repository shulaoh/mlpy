from numpy import *
import operator
from os import listdir

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistance = sqDiffMat.sum(axis=1)
	distances = sqDistance**0.5
	sortedDist = distances.argsort()
	classCount={}
	for i in range(k):
		voteLabel = labels[sortedDist[i]]
		classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
	print(classCount)
	sortedCout = sorted(classCount.items(), key=operator.itemgetter(1), reverse = True)
	return sortedCout[0][0];
	return 0

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

group, labels = createDataSet()

c = classify0([0, 0], group, labels, 3)
print("The label is: ", c)

