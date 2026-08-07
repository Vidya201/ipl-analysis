import pandas as pd
import matplotlib.pyplot as plt
deliveries = pd.read_csv(r"C:\Users\vidya\OneDrive\Desktop\portfolio\ipl-analysis\deliveries.csv")

power_play = deliveries[deliveries['over']<=5]

power_play_runs=power_play['total_runs'].sum()

print(f"Total runs in Power Play : {power_play_runs}")

death_over = deliveries[deliveries['over']>=15]

death_over_runs=death_over['total_runs'].sum()

print(f"Total runs in death overs : {death_over_runs}")

labels=['Power_play' , 'Death_overs']
values=[power_play_runs,death_over_runs]

plt.figure(figsize=(6,4))
plt.bar(labels,values,color=['pink','blue'])
plt.title('Power_Play vs Death_overs')
plt.savefig('Power_Play_vs_Death_overs')
for i, v in enumerate(values):
    plt.text(i, v+500, f'{v:,}', ha='center', fontweight='bold')
plt.show()




