# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:23:45 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 18:34:47 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tools import getFile, estimatePrice, calcError, saveTheta

def calcSums(th0, th1, dataList):
	sum0 = 0
	sum1 = 1
	for i in dataList:
		km = float(i[0])
		price = float(i[1])
		sum0 += estimatePrice(km, th0, th1) - price
		sum1 += (estimatePrice(km, th0, th1) - price) * km
	return sum0, sum1

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
	saveTheta(theta0, theta1)
	err = calcError(theta0, theta1, dataList, len(dataList))
	print(str(theta0) + ",,,,,,,," + str(theta1))

if __name__ == '__main__':
	main()
