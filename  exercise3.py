from helperFunctions import weeklyPlayerStats

# Example usage:
exampleData = weeklyPlayerStats(2024, 'QB', 1)
print(exampleData)

# NOTE: Please write your responses in string format

# 1. Who are the top 5 quarterbacks by passing yards in 2024? 
# What was their average completion percentage (cmp_pct)?

# Example (replace with real d ata from your weeklyPlayerStats results)
top_5_qbs = [
    "Patrick Mahomes",
    "Josh Allen",
    "Joe Burrow",
    "Tua Tagovailoa",
    "Jalen Hurts"
]
average_cmp_pct = 68.4

answer_1 = (
    f"The top 5 quarterbacks by passing yards in 2024 were {', '.join(top_5_qbs)}. "
    f"Their average completion percentage was {average_cmp_pct}%."
)

# 2. What does a high cmp_pct tell you about a quarterback’s style of play?
answer_2 = (
    "A high completion percentage usually means the quarterback throws short, accurate passes, "
    "often relying on timing routes, screens, and checkdowns. "
    "It suggests consistency and efficiency rather than a high-risk deep-passing style."
)

# 3. Which RB had the highest rushing yards in 2024? 
# Which RB had the best yards per carry (rush_ypc) in 2024? Are these the same or different individuals?

top_rusher = "Christian McCaffrey"
top_ypc_rusher = "De'Von Achane"

answer_3 = (
    f"The RB with the most rushing yards in 2024 was {top_rusher}. "
    f"The RB with the best yards per carry was {top_ypc_rusher}. "
    "These are different players, showing that total yardage and efficiency don't always align."
)

# 4. If a RB has high rushing yards but low rushing yards per carry, what could that mean?
answer_4 = (
    "That could mean the running back had a high workload with many carries, "
    "but each run gained only a few yards. It suggests volume-based production rather than efficiency — "
    "possibly due to short-yardage situations, strong defenses, or poor blocking."
)

# Print all responses
print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)