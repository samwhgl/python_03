#!/usr/bin/env python3

# ======================
# Sample Data
# ======================

players = ["alice", "bob", "charlie", "diana"]

scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 2050
}

achievements = {
    "alice": ["first_kill", "level_10", "boss_slayer", "collector", "explorer"],
    "bob": ["first_kill", "level_5", "explorer"],
    "charlie": ["first_kill", "level_10", "boss_slayer", "speedrunner", "collector", "explorer", "veteran"],
    "diana": ["first_kill", "level_10"]
}

regions = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "north"
}

print("=== Game Analytics Dashboard ===")

# ======================
# List Comprehensions
# ======================

print("\n=== List Comprehension Examples ===")

high_scorers = [player for player, score in scores.items() if score > 2000]
print("High scorers (>2000):", high_scorers)

doubled_scores = [score * 2 for score in scores.values()]
print("Scores doubled:", doubled_scores)

active_players = [player for player in players if player in achievements]
print("Active players:", active_players)

# ======================
# Dict Comprehensions
# ======================

print("\n=== Dict Comprehension Examples ===")

player_scores = {player: scores[player] for player in players}
print("Player scores:", player_scores)

score_categories = {
    "high": len([s for s in scores.values() if s >= 2200]),
    "medium": len([s for s in scores.values() if 1800 <= s < 2200]),
    "low": len([s for s in scores.values() if s < 1800])
}
print("Score categories:", score_categories)

achievement_counts = {player: len(achs) for player, achs in achievements.items()}
print("Achievement counts:", achievement_counts)

# ======================
# Set Comprehensions
# ======================

print("\n=== Set Comprehension Examples ===")

unique_players = {player for player in players}
print("Unique players:", unique_players)

unique_achievements = {ach for achs in achievements.values() for ach in achs}
print("Unique achievements:", unique_achievements)

active_regions = {region for region in regions.values()}
print("Active regions:", active_regions)

# ======================
# Combined Analysis
# ======================

print("\n=== Combined Analysis ===")

total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(scores.values()) / len(scores)

top_player = max(scores, key=scores.get)
top_score = scores[top_player]
top_achievements = len(achievements[top_player])

print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print("Average score:", average_score)
print(f"Top performer: {top_player} ({top_score} points, {top_achievements} achievements)")
