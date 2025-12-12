# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 14:08:08 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 14:50:17 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

def distance(p1, p2):
	return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def parsing(points):
	try:
		coord = points.split(",")
		if len(coord) != 3:
			raise ValueError("Need exactly 3 values")
		x, y, z = map(int, coord)
		return (x, y, z)
	except ValueError as e:
		print(f"Error parsing coordinates: {e}")
		print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
		return None



def main():
	print("=== Game Coordinate System ===")
	position_a = (10, 20, 5)
	print("Position created:", position_a)
	origin = (0, 0, 0)
	print(f"Distance between {origin} and {position_a}: {distance(origin, position_a):.2f}")
	position_b = "3,4,0"
	print(f"Parsing coordinate: {position_b}")
	print("Parsed position:", parsing(position_b))
	print(f"Distance between {origin} and {parsing(position_b)}: {distance(origin, parsing(position_b))}")
	position_c = "abc,def,ghi"
	print(f"Parsing invalid coordinates: {position_c}")
	parsing(position_c)
	print("Unpacking demonstration:")
	x, y, z = parsing(position_b)
	print(f"Player at x={x}, y={y}, z={z}")
	print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
	main()
