# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 11:52:54 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 12:04:35 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	print("=== Command quest ===")
	program_name = sys.argv[0]
	total_args = len(sys.argv)

	if total_args == 1:
		print("No arguments provided!")
		print(program_name)
		print("Total arguments:", total_args)

	print(f"Program name: {program_name}")
	print(f"Arguments recieved: {total_args -1}")
	i = 1
	while i < total_args:
		print(f"Argument {i}: {sys.argv[i]}")
		i += 1
	print("Total arguments:", total_args)

if __name__ == "__main__":
	main()
