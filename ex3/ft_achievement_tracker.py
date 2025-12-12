# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 14:52:48 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 15:49:59 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
	print("=== Achievement Tracker System ===")
	alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
	bob = {"first_kill", "level_10", "boss_slayer", "collector"}
	charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}
	print("Player alice achievement:", alice)
	print("Player bob achievement:", bob)
	print("Player charlie achievement list:", charlie)

	print("=== Achievement Analytics ===")
	unique = alice.union(bob).union(charlie)
	print("All unique achievements:", unique)
	print(f"Total unique achievements: {len(unique)}")

	print(f"Common to all players:", alice.intersection(bob).intersection(charlie))
	rare_achievements = (alice.union(bob).union(charlie)) - (alice.intersection(bob).union(alice.intersection(charlie)).union(bob.intersection(charlie)))
	print("Rare achievements (1 player):", rare_achievements)
	common_alice_bob = alice.intersection(bob)
	print("Alice vs Bob common:", common_alice_bob)

	alice_unique = alice.difference(bob)
	bob_unique = bob.difference(alice)
	print("Alice unique:", alice_unique)
	print("Bob unique:", bob_unique)

if __name__ == "__main__":
    main()


main()

