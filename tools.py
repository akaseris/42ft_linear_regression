# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:30:31 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 18:32:07 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from os import path

def getFile():
	# file = input("Please write the path of the csv data file")
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

def calcError(th0, th1, dataList, M):
	sum = 0
	for i in dataList:
		sum += (estimatePrice(i[0], th0, th1) - i[1]) ** 2
	sum = sum / M
	return (sum)
