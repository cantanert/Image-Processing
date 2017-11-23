
#      P(A/B)=(P(B/A)P(A))/P(B)

#      -Diabete
#      -OCR
#      -Finger
#      -Face       BU 4'ü classify(sınıflandırma) cluster'dan farklı. 28x28+1 resim var a olan. resize edince
#                  düz metin olarak 1x700küsür. Numeric oldugunda bır metrıc vardır. Ortalama varyans ulaşabilirdik. 
#                  Nicelik değil nitelik varken olmaz.
#
#       Dataset ---->train %80
#           |------->test %20   bu ikiye ayırma işlemi : split.  
#    
#       Gönderdiğimiz x değeri hangi ortalama ve varyans değeriyle en üksek değere ulaşıyorsa o classa aittir 
#       diyoruz. test/connection.
#       Diabete, OCR, Finger, Face hepsi aynı tip örnekler.
# 
#       https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
#                              |----> Naive Bayes Algorithm Tutorial
#
#       1 satır vaka bilgisi. Hasataya ait bilgiler her biri.
#       %80/%20 en ideali. %99/%1de seçebilirdik ama mantıksız.
#       En son sütun classı söyler. Diabete de 0 ve 1 olarak 2. OCR'da ise 0dan9a kadar 10 tane olurdu.
#  
#       separateByClass() ile seperated[1] ve seperated[0] için = {[],[],[],[]} şeklinde veriler dicttype olarak atandı
#       stdev (standart  sapma)
#       calculateProbabilty() ---->  bir ortalama var. x, ortlamaya ve std sapmaya ait verisetinde %kaç bulounabilir?
#       predict() ---> Test seti için , her bir elemanı için, P(x) değerlerini bulacak ve 
#       en büyük sonucu vereni x i sınıf olarak ata
#       getPredictions()---> çoğulu
#

# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
import math

def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.items():
		summaries[classValue] = summarize(instances)
	return summaries

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions

def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def main():
	filename = 'pima-indians-diabetes.data.csv'
	splitRatio = 0.67
	dataset = loadCsv(filename)
	trainingSet, testSet = splitDataset(dataset, splitRatio)
	#print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
	# prepare model
	summaries = summarizeByClass(trainingSet)
	# test model
	predictions = getPredictions(summaries, testSet)
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + str(accuracy))

main()
