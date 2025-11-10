# exercise4_solution.py

from helperFunctions import (
    weeklyPlayerStats,
    plot_player_stat,
    plot_weekly_player_stats,
    get_position_columns
)
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Example visualization
# -----------------------------
# Get weekly stats for Running Backs
rb_stats = weeklyPlayerStats(2024, "RB")

# Plot a custom metric: rushing yards per carry
plot_player_stat(
    rb_stats,
    stat="rush_ypc",
    top_n=5,
    title="Top 5 RBs by Yards per Carry (2024)",
    save_path="RB_rush_ypc_2024.png"
)

print("✅ Saved graph: RB_rush_ypc_2024.png")
print("Description: I created a graph showing highest yards per carry among RBs in 2024.\n")

# -----------------------------
# 2️⃣ Most total touchdowns (RB + WR)
# -----------------------------
rb_stats = weeklyPlayerStats(2024, "RB")
wr_stats = weeklyPlayerStats(2024, "WR")

# Sum rushing and receiving TDs per player
rb_td = rb_stats.groupby("player")["rush_tds"].sum()
wr_td = wr_stats.groupby("player")["rec_tds"].sum()

combined_tds = rb_td.add(wr_td, fill_value=
