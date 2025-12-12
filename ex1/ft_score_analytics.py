# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 13:39:21 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 14:07:23 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	print("=== Player Scores Analytics ===")
	inputs = []
	i = 1
	while i < len(sys.argv):
		try:
			inputs.append(int(sys.argv[i]))
			i += 1
		except ValueError:
			print(f"Ignored invalid input: {sys.argv[i]}")
			i += 1
	if not inputs:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		return
	print("Scores proceded:",inputs)
	print("Total players:", len(inputs))
	print("Total score:", sum(inputs))
	print("Average score:", sum(inputs) / len(inputs))
	print("High score:", max(inputs))
	print("Low score:", min(inputs))
	print("Score range:", max(inputs) - min(inputs))

if __name__ == "__main__":
	main()
