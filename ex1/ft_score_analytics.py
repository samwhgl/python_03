# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 13:39:21 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 13:10:27 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    """
    Analyze player scores provided as command-line arguments.

    The script accepts integer scores, ignores invalid inputs,
    and displays basic statistics such as total, average,
    highest, lowest, and range of scores.
    """
    print("=== Player Scores Analytics ===")

    scores = []
    index = 1

    while index < len(sys.argv):
        try:
            scores.append(int(sys.argv[index]))
        except ValueError:
            print(f"Ignored invalid input: {sys.argv[index]}")
        index += 1

    if not scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    main()
