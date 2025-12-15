# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 16:28:03 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 16:58:00 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import time

# -------------------------
# Generator: event stream
# -------------------------
def game_event_stream(n):
    players = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        player = random.choice(players)
        action = random.choice(actions)
        level = random.randint(1, 20)

        yield {
            "id": i,
            "player": player,
            "action": action,
            "level": level
        }


# -------------------------
# Fibonacci generator
# -------------------------
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# -------------------------
# Prime number generator
# -------------------------
def prime_numbers():
    n = 2
    while True:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


# -------------------------
# Main program
# -------------------------
def main():
    print("=== Game Data Stream Processor ===")

    total = 1000
    print(f"Processing {total} game events...")

    start = time.time()  # measure processing duration

    events = game_event_stream(total)

    count = 0
    high_level = 0
    treasure = 0
    levelup = 0

    for event in events:
        count += 1

        # Show only first 3 events
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
            levelup += 1

    duration = time.time() - start

    print("=== Stream Analytics ===")
    print("Total events processed:", count)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure)
    print("Level-up events:", levelup)
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.4f} seconds")

    print("=== Generator Demonstration ===")
    fib = fibonacci()
    print("Fibonacci sequence (first 10):", ", ".join(str(next(fib)) for _ in range(10)))

    primes = prime_numbers()
    print("Prime numbers (first 5):", ", ".join(str(next(primes)) for _ in range(5)))


if __name__ == "__main__":
    main()
