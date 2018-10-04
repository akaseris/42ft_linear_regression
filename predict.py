# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:23:59 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 19:55:14 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tools import getTheta

def main():
	theta0, theta1, err = getTheta()
	km = input("Please write the kilometers of the car\n")
	price = theta0 + theta1 * float(km)
	print("The price of a car at {}km is estimated at {}" .format(km, price))
	print("The mean standard error for predictions is {}" .format(err))

if __name__ == '__main__':
	main()