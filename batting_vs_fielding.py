import pandas as pd
import matplotlib.pyplot as plt

matches=pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\matches.csv")
deliveries = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\deliveries.csv")

"""sql : select winner from matches where toss decision = "bat" """

win=matches[matches['toss_winner'] == matches['winner']]

loss=matches[matches['toss_winner']!=matches['winner']]

bat_and_won = matches[(matches['toss_decision']=='bat') & (matches['toss_winner']==matches['winner'])]

bat_and_lost = matches[(matches['toss_decision']=='bat') & (matches['toss_winner']!=matches['winner'])]

field_and_won = matches[(matches['toss_decision']=='field') & (matches['toss_winner']==matches['winner'])]

field_and_lost = matches[(matches['toss_decision']=='field') & (matches['toss_winner']!=matches['winner'])]

bat_won_count=len(bat_and_won)

bat_lost_count=len(bat_and_lost)

field_won_count=len(field_and_won)

field_lost_count=len(field_and_lost)

print(f"number of matches won when batting is choosen : {bat_won_count}")

print(f"number of matches lost when batting is choosen : {bat_lost_count}")

print(f"number of matches won when fielding is choosen : {field_won_count}")

print(f"number of matches lost when fielding is choosen : {field_lost_count}")

if(bat_won_count>field_won_count):
    print("Choosing batting first is better to win")
else:
    print("Choosing fielding first is better to win")

bat_win_pct = bat_won_count / (bat_won_count + bat_lost_count) * 100
field_win_pct = field_won_count / (field_won_count + field_lost_count) * 100

labels = ['Bat First', 'Field First']
values = [bat_win_pct, field_win_pct]

plt.figure(figsize=(6,4))
plt.bar(labels, values, color=['blue', 'orange'])
plt.title('Win % — Batting First vs Fielding First')
plt.ylabel('Win Percentage %')
plt.ylim(35, 65)
for i, v in enumerate(values):
    plt.text(i, v+0.3, f'{v:.1f}%', ha='center', fontweight='bold')
plt.savefig('batting_vs_fielding.png')
plt.show()





