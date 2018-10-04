# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:30:31 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 20:19:24 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from os import path

def getFile():
	file = input("Please write the path of the csv data file\n")
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

def saveTheta(th0, th1, err, dataList):
	if (th0 != 0.0) and (th1 != 0.0):
		try:
			thFile = open('Theta_Values', 'w')
			thFile.write('theta0={}\ntheta1={}\nm.s.e.={}\ndataLs={}'.format(th0, th1, err, dataList))
			thFile.close()
		except Exception:
			print("message: An error happened ! Saiving Failed.")
	else:
		print("Theta values are not correct. Saving failed.")

def getTheta():
	try:
		f = open('Theta_Values', 'r')
		value = f.readlines()
		index = value[0].index('=')
		theta0 = value[0][index+1:]
		theta1 = value[1][index+1:]
		err = value[2][index+1:]
		dataList = eval(value[3][index+1:])
	except Exception as e:
		print("message: {}".format(e))
		exit()
	return float(theta0), float(theta1), float(err), dataList

def estimatePrice(miles, th0, th1):
	return (th0 + (th1 * miles))

def calcError(th0, th1, dataList, M):
	sum = 0
	for i in dataList:
		sum += (estimatePrice(i[0], th0, th1) - i[1]) ** 2
	sum = sum / M
	return (sum)
