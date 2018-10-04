# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:23:59 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 18:51:26 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tools import getTheta

def main():
	theta0, theta1 = getTheta()
	km = input("Please write the kilometers of the car\n")
	price = theta0 + theta1 * float(km)
	print("The price of a car at {}km is estimated at {}" .format(km, price))

if __name__ == '__main__':
	main()