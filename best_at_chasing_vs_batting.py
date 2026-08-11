import pandas as pd
import matplotlib.pyplot as plt
matches = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\matches.csv")
deliveries = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\deliveries.csv")
print(matches.columns.tolist())
print(deliveries.columns.tolist())
print(matches['toss_decision'])
print(matches['winner'])

best_at_chasing = matches[matches['toss_decision']=='field'].groupby('winner')['id'].count().sort_values(ascending=False)
print(f"Top 5 Teams that are best at chasing are : {best_at_chasing.head(5)}")

best_at_batting = matches[matches['toss_decision']=='bat'].groupby('winner')['id'].count().sort_values(ascending=False)
print(f"Top 5 Teams that are best at batting are : {best_at_batting.head(5)}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# chasing chart
ax1.barh(best_at_chasing.head(5).index,best_at_chasing.head(5).values, color='green')
ax1.set_title('Best Chasing Teams')
ax1.set_xlabel('Wins while Chasing')

# batting first chart
ax2.barh(best_at_batting.head(5).index,best_at_batting.head(5).values, color='blue')
ax2.set_title('Best Batting First Teams')
ax2.set_xlabel('Wins while Batting First')

plt.tight_layout()
plt.savefig('best_chasing_vs_batting.png')
plt.show()