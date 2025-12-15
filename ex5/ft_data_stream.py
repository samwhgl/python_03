# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 16:28:03 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 13:13:01 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import time


def game_event_stream(total_events):
    """
    Generate a stream of game events.

    Args:
        total_events (int): Number of events to generate.

    Yields:
        dict: A game event containing id, player, action, and level.
    """
    players = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for event_id in range(1, total_events + 1):
        yield {
            "id": event_id,
            "player": random.choice(players),
            "action": random.choice(actions),
            "level": random.randint(1, 20),
        }


def fibonacci():
    """
    Generate an infinite Fibonacci sequence.

    Yields:
        int: Next Fibonacci number.
    """
    first, second = 0, 1

    while True:
        yield first
        first, second = second, first + second


def prime_numbers():
    """
    Generate an infinite sequence of prime numbers.

    Yields:
        int: Next prime number.
    """
    number = 2

    while True:
        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield number

        number += 1


def main():
    """
    Run the game data stream processor and generator demonstrations.
    """
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    start_time = time.time()

    events = game_event_stream(total_events)

    count = 0
    high_level = 0
    treasure = 0
    level_up = 0

    for event in events:
        count += 1

        # Display only the first three events
        if count <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )

        if event["level"] >= 10:
            high_level += 1

        if event["action"] == "found treasure":
            treasure += 1

        if event["action"] == "leveled up":
            level_up += 1

    duration = time.time() - start_time

    print("=== Stream Analytics ===")
    print("Total events processed:", count)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.4f} seconds")

    print("=== Generator Demonstration ===")

    fib = fibonacci()
    print(
        "Fibonacci sequence (first 10):",
        ", ".join(str(next(fib)) for _ in range(10)),
    )

    primes = prime_numbers()
    print(
        "Prime numbers (first 5):",
        ", ".join(str(next(primes)) for _ in range(5)),
    )


if __name__ == "__main__":
    main()
