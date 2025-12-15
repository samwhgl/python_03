# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 11:52:54 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 13:09:57 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    """
    Display the program name and command-line arguments.

    Prints the total number of arguments and lists each argument
    passed to the script.
    """
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
        print(program_name)
        print("Total arguments:", total_args)

    print(f"Program name: {program_name}")
    print(f"Arguments received: {total_args - 1}")

    index = 1
    while index < total_args:
        print(f"Argument {index}: {sys.argv[index]}")
        index += 1

    print("Total arguments:", total_args)


if __name__ == "__main__":
    main()
