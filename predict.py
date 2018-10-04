# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akaseris <akaseris@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 18:23:59 by akaseris          #+#    #+#              #
#    Updated: 2018/10/04 18:29:38 by akaseris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def getTheta()


def main():
	theta0, theta1 = getTheta()
	km = input("Please write the kilometers of the car")
	price = theta0 + theta1 * km
	print("The price of a car at {}km is estimated at {}" .format(km, price))

if __name__ == '__main__':
	main()