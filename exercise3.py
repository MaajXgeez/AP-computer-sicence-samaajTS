def weeklyPlayerStats(position, year, week):
    # Your function to return player stats for the given position, year, and week
    pass

from helperFunction import weeklyPlayerStats

# Load QB and RB data for Week 1 of 2025
qb_stats = weeklyPlayerStats('QB', 2025, 1)
rb_stats = weeklyPlayerStats('RB', 2025, 1)

# Convert to DataFrame if it's not already
import pandas as pd

if not isinstance(qb_stats, pd.DataFrame):
    qb_stats = pd.DataFrame(qb_stats)
if not isinstance(rb_stats, pd.DataFrame):
    rb_stats = pd.DataFrame(rb_stats)

### 1. Top 5 QBs by Passing Yards and their average completion percentage ###
top_5_qbs = qb_stats.sort_values(by='pass_yards', ascending=False).head(5)
avg_cmp_pct = top_5_qbs['cmp_pct'].mean()

print("Top 5 QBs by Passing Yards:")
print(top_5_qbs[['player_name', 'pass_yards', 'cmp_pct']])
print(f"\nAverage Completion Percentage of Top 5 QBs: {avg_cmp_pct:.2f}%\n")

### 2. Interpretation of High Completion Percentage ###
print("Q2: A high completion percentage (cmp_pct) often indicates that a quarterback:")
print("- Throws high-percentage, short to intermediate passes.")
print("- Has good accuracy and decision-making.")
print("- Plays in an offensive scheme that prioritizes short, quick throws.\n")

### 3. RB with Most Rushing Yards and Best Yards per Carry ###
top_rusher = rb_stats.sort_values(by='rush_yards', ascending=False).iloc[0]
best_ypc = rb_stats.sort_values(by='rush_ypc', ascending=False).iloc[0]

print("Top RB by Rushing Yards:")
print(f"{top_rusher['player_name']} - {top_rusher['rush_yards']} yards")

print("\nRB with Best Yards per Carry:")
print(f"{best_ypc['player_name']} - {best_ypc['rush_ypc']} YPC\n")

### 4. Interpretation of High Rush Yards but Low YPC ###
print("Q4: High rushing yards but low yards per carry may suggest:")
print("- The player had many attempts but gained fewer yards per run.")
print("- Usage in short-yardage or goal-line situations.")
print("- Offensive line or defensive matchup challenges limiting efficiency.")
