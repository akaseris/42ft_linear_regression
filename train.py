import re
from os import path

dataList = []
theta0 = 0
theta1 = 0
float(theta0)
float(theta1)
learningRate = 0.5

def getFile():
	file = input("Please write the path of the csv data file\n")
	if (file.find(".csv", 1) == -1 or not path.exists(file)):
		print("Wrong filetype!")
		getFile()
		return
	fileObj = open(file, "r")
	if (fileObj.readline() != "km,price\n"):
		print("Wrong Header")
		getFile()
		return
	regex = re.compile("[0-9]+,[0-9]+\n")
	i = 1
	for x in fileObj:
		i += 1
		if (not regex.match(x)):
			print("Wrong value, line" + str(i))
			dataDict.clear()
			getFile()
			return
		x = x[:-1]
		x = x.split(",")
		x[0] = int(x[0])
		x[1] = int(x[1])
		dataList.append(x)

def estimatePrice(miles):
	return (theta0 + (theta1 * miles))

def diffSum():
	diffSum = 0
	for j in dataList:
		diffSum += estimatePrice(j[0]) - j[1]
	return (diffSum)

def calcTheta():
	global theta0
	global theta1
	for i in dataList:
		tmp0 = learningRate * (1 / len(dataList)) * diffSum()
		tmp1 = learningRate * (1 / len(dataList)) * diffSum() * i[0]
		theta0 = tmp0
		theta1 = tmp1
getFile()
calcTheta()
print(str(theta0) + ",,,,,,,," + str(theta1))
