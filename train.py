# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:23:45 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 18:23:53 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from os import path

def getFile():
	# file = input("Please write the path of the csv data file\n")
	file = "data.csv"
	if (file.find(".csv", 1) == -1 or not path.exists(file)):
		print("Wrong filetype!")
		getFile()
		return
	fileObj = open(file, "r")
	if (fileObj.readline() != "km,price\n"):
		print("Wrong Header")
		fileObj.close()
		getFile()
		return
	regex = re.compile("[0-9]+,[0-9]+\n")
	i = 1
	dataList = []
	for x in fileObj:
		i += 1
		if (not regex.match(x)):
			print("Wrong value, line" + str(i))
			dataDict.clear()
			fileObj.close()
			getFile()
			return
		x = x[:-1]
		x = x.split(",")
		x[0] = float(x[0]) / 1000
		x[1] = float(x[1]) / 1000
		dataList.append(x)
	fileObj.close()
	return dataList

def estimatePrice(miles, th0, th1):
	return (th0 + (th1 * miles))

def calcSums(th0, th1, dataList):
	sum0 = 0
	sum1 = 1
	for i in dataList:
		km = float(i[0])
		price = float(i[1])
		sum0 += estimatePrice(km, th0, th1) - price
		sum1 += (estimatePrice(km, th0, th1) - price) * km
	return sum0, sum1

def calcError(th0, th1, dataList, M):
	sum = 0
	for i in dataList:
		sum += (estimatePrice(i[0], th0, th1) - i[1]) ** 2
	sum = sum / M
	return (sum)

def calcTheta(theta0, theta1, learningRate, dataList):
	M = len(dataList)
	while (True):
		sum0, sum1 = calcSums(theta0, theta1, dataList)
		tmp0 = learningRate * sum0 / float(M)
		tmp1 = learningRate * sum1 / float(M)
		if abs(tmp0) < float(0.0000001) and abs(tmp1) < float(0.0000001):
			return (theta0 * 1000, theta1)
		theta0 = theta0 - tmp0
		theta1 = theta1 - tmp1

def main():
	dataList = getFile()
	theta0 = 0.0
	theta1 = 0.0
	learningRate = 0.0001
	theta0, theta1 = calcTheta(theta0, theta1, learningRate, dataList)
	err = calcError(theta0, theta1, dataList, len(dataList))
	print(str(theta0) + ",,,,,,,," + str(theta1))

if __name__ == '__main__':
	main()
