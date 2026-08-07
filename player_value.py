import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\deliveries.csv")

print(deliveries.columns.tolist())

"""sql:select batter,batsman_runs , sum(batsman_runs) from data group by batter order by rusn desc """

batter_performance = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False)

top_10_batter=batter_performance.head(10)

print(f"The Top 10 best batters are :")

print(top_10_batter)

bowler_performance=deliveries.groupby('bowler')['is_wicket'].sum().sort_values(ascending=False)

top_10_bowler=bowler_performance.head(10)

print("The Top 10 best bowlers are : ")

print(top_10_bowler)

labels =  top_10_batter.index
values = top_10_batter.values
plt.figure(figsize=(6,4))
plt.barh(labels,values,color = 'green')
plt.ylabel('Runs Scored by Batters')
plt.title("Top 10 Best batters")
plt.tight_layout()
plt.savefig("Best Batters")
plt.show()

labels=top_10_bowler.index
values=top_10_bowler.values
plt.figure(figsize=(6,4))
plt.barh(labels,values,color='blue')
plt.ylabel('Wickets taken by Bowlers')
plt.title("Top 10 best bowlers")
plt.tight_layout()
plt.savefig("Best Bowlers")
plt.show()

