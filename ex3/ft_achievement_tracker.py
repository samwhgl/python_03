# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 14:52:48 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 13:11:35 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
    """
    Track and analyze player achievements using set operations.
    """
    print("=== Achievement Tracker System ===")

    alice = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }
    bob = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print("Player Alice achievements:", alice)
    print("Player Bob achievements:", bob)
    print("Player Charlie achievements:", charlie)

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)

    rare_achievements = (
        all_achievements
        - alice.intersection(bob)
        - alice.intersection(charlie)
        - bob.intersection(charlie)
    )
    print("Rare achievements (1 player):", rare_achievements)

    common_alice_bob = alice.intersection(bob)
    print("Alice vs Bob common:", common_alice_bob)

    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)

    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    main()
