# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:23:59 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 20:32:05 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from tools import getTheta

def drawGraph(theta0, theta1, km, price, dataList):
	print("I will draw something")

def main():
	theta0, theta1, err, dataList = getTheta()
	graph = 0
	if (len(sys.argv) > 1 and sys.argv[1] == "graph"):
		graph = 1
	km = input("Please write the kilometers of the car\n")
	price = theta0 + theta1 * float(km)
	price = round(price, 2)
	err = round(err, 2)
	print("The price of a car at {}km is estimated at {}" .format(km, price))
	print("The mean standard error for predictions is {}" .format(err))
	if (graph):
		drawGraph(theta0, theta1, km, price, dataList)

if __name__ == '__main__':
	main()