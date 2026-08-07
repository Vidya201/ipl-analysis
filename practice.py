import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\matches.csv")
deliveries = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\deliveries.csv")

print(matches.shape)
print(matches.head())
print(deliveries.shape)
print(deliveries.head())
print(matches.columns.to_list())

print(matches['toss_winner'].head(10))

df=pd.DataFrame(matches)

win=df[df['toss_winner'] == df['winner']]
print(win)

loss=df[df['toss_winner']!=df['winner']]
print(loss)

number_of_wins=len(win)
number_of_loss=len(loss)

print("\n")

print(f"number of wins : {number_of_wins}\n")
print(f"number of loss : {number_of_loss}\n")

win_percentage=number_of_wins/len(df) * 100
print(f"win_percent : {win_percentage}%\n")

loss_percentage=number_of_loss/len(df)*100
print(f"loss_percent: {loss_percentage}%\n")

print(f"toss winner also won {win_percentage:.2f}% of matches\n")

print(f"toss winner has lost {loss_percentage:.2f}% of matches\n")

difference=win_percentage-loss_percentage
print(f"difference : {difference:.2f}%\n")

if(difference>10):
    print("toss has a impact on match winning")

else:
    print("toss has no impact on match winning")

print(matches.groupby('toss_decision')['winner'].count())

labels = ['Toss Winner Won', 'Toss Winner Lost']
values = [win_percentage, loss_percentage]

plt.figure(figsize=(6,4))
plt.bar(labels, values, color=['green', 'red'])
plt.title('Does Winning Toss Help Win the Match?')
plt.ylabel('Win Percentage %')
plt.ylim(40, 55)          
for i, v in enumerate(values):
    plt.text(i, v+0.1, f'{v:.2f}%', ha='center')   
plt.savefig('toss_impact.png')
plt.show()