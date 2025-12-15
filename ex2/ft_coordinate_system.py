# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 14:08:08 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 13:14:26 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math


def distance(point_a, point_b):
    """
    Calculate the Euclidean distance between two 3D points.

    Args:
        point_a (tuple): First point (x, y, z).
        point_b (tuple): Second point (x, y, z).

    Returns:
        float: Distance between the two points.
    """
    return math.sqrt(
        (point_b[0] - point_a[0]) ** 2
        + (point_b[1] - point_a[1]) ** 2
        + (point_b[2] - point_a[2]) ** 2
    )


def parse_coordinates(points):
    """
    Parse a string of comma-separated values into 3D coordinates.

    Args:
        points (str): Coordinates in the form "x,y,z".

    Returns:
        tuple | None: A tuple (x, y, z) if parsing succeeds,
        otherwise None.
    """
    try:
        coordinates = points.split(",")

        if len(coordinates) != 3:
            raise ValueError("Need exactly 3 values")

        x, y, z = map(int, coordinates)
        return x, y, z

    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            "Error details - Type: "
            f"{type(error).__name__}, Args: {error.args}"
        )
        return None


def main():
    """
    Demonstrate coordinate parsing and distance calculations.
    """
    print("=== Game Coordinate System ===")

    position_a = (10, 20, 5)
    origin = (0, 0, 0)

    print("Position created:", position_a)
    print(
        f"Distance between {origin} and {position_a}: "
        f"{distance(origin, position_a):.2f}"
    )

    position_b = "3,4,0"
    print(f"Parsing coordinate: {position_b}")

    parsed_b = parse_coordinates(position_b)
    print("Parsed position:", parsed_b)

    print(
        f"Distance between {origin} and {parsed_b}: "
        f"{distance(origin, parsed_b)}"
    )

    position_c = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {position_c}")
    parse_coordinates(position_c)

    print("Unpacking demonstration:")
    x, y, z = parse_coordinates(position_b)

    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
