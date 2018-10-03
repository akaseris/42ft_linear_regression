import re
from os import path

dataList = []
theta0 = 0
theta1 = 0
learningRate = 0.0001
iterNum = 1000

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

def calcTheta():
	global theta0
	global theta1
	tmp0 = theta0
	tmp1 = theta1
	for i in dataList:
		tmp0 += learningRate * (1 / len(dataList)) * (estimatePrice(i[0]) - i[1])
		tmp1 += learningRate * (1 / len(dataList)) * (estimatePrice(i[0]) - i[1]) * i[0]
	theta0 = theta0 - (learningRate * tmp0)
	theta1 = theta1 - (learningRate * tmp1)

def main():
	getFile()
	for i in range(0, iterNum):
		calcTheta()
	print(str(theta0) + ",,,,,,,," + str(theta1))

if __name__ == '__main__':
	main()
