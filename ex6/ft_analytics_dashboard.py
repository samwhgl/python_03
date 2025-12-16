#!/usr/bin/env python3
"""
Game Analytics Dashboard.

This module demonstrates the use of list, dict, and set comprehensions
to analyze player data such as scores, achievements, and regions.
"""


PLAYERS = ["alice", "bob", "charlie", "diana"]

SCORES = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 2050,
}

ACHIEVEMENTS = {
    "alice": [
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
        "explorer",
    ],
    "bob": ["first_kill", "level_5", "explorer"],
    "charlie": [
        "first_kill",
        "level_10",
        "boss_slayer",
        "speedrunner",
        "collector",
        "explorer",
        "veteran",
    ],
    "diana": ["first_kill", "level_10"],
}

REGIONS = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "north",
}


def list_comprehension_examples():
    """Display examples of list comprehensions."""
    print("\n=== List Comprehension Examples ===")

    high_scorers = [
        player for player, score in SCORES.items() if score > 2000
    ]
    print("High scorers (>2000):", high_scorers)

    doubled_scores = [score * 2 for score in SCORES.values()]
    print("Scores doubled:", doubled_scores)

    active_players = [
        player for player in PLAYERS if player in ACHIEVEMENTS
    ]
    print("Active players:", active_players)


def dict_comprehension_examples():
    """Display examples of dictionary comprehensions."""
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {player: SCORES[player] for player in PLAYERS}
    print("Player scores:", player_scores)

    score_categories = {
        "high": len([s for s in SCORES.values() if s >= 2200]),
        "medium": len(
            [s for s in SCORES.values() if 1800 <= s < 2200]
        ),
        "low": len([s for s in SCORES.values() if s < 1800]),
    }
    print("Score categories:", score_categories)

    achievement_counts = {
        player: len(achs) for player, achs in ACHIEVEMENTS.items()
    }
    print("Achievement counts:", achievement_counts)


def set_comprehension_examples():
    """Display examples of set comprehensions."""
    print("\n=== Set Comprehension Examples ===")

    unique_players = {player for player in PLAYERS}
    print("Unique players:", unique_players)

    unique_achievements = {
        ach for achs in ACHIEVEMENTS.values() for ach in achs
    }
    print("Unique achievements:", unique_achievements)

    active_regions = {region for region in REGIONS.values()}
    print("Active regions:", active_regions)

    return unique_achievements


def combined_analysis(unique_achievements):
    """Display combined statistics about players and achievements."""
    print("\n=== Combined Analysis ===")

    total_players = len(PLAYERS)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(SCORES.values()) / len(SCORES)

    top_player = max(SCORES, key=SCORES.get)
    top_score = SCORES[top_player]
    top_achievements = len(ACHIEVEMENTS[top_player])

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        f"Top performer: {top_player} "
        f"({top_score} points, {top_achievements} achievements)"
    )


def main():
    """Main entry point of the script."""
    print("=== Game Analytics Dashboard ===")

    list_comprehension_examples()
    dict_comprehension_examples()
    unique_achievements = set_comprehension_examples()
    combined_analysis(unique_achievements)


if __name__ == "__main__":
    main()
