import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="IPL Strategic Intelligence", page_icon="🏏", layout="wide")

st.title("🏏 IPL Strategic Intelligence Dashboard")
st.markdown("*Data-driven analysis of 1095 IPL matches across 17 seasons*")
st.sidebar.title("📊 Select Analysis")

analysis = st.sidebar.selectbox(
    "Choose Analysis",
    ["🏆 Toss Impact",
    "🏏 Batting vs Fielding First",
    "🎯 Best Chasing Teams",
    "⚡ Powerplay vs Death Overs",
    "⭐ Top Performers",
    ]
)

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# ─── Q1: TOSS IMPACT ───
if analysis == "🏆 Toss Impact":
    st.header("Does Winning Toss Help Win the Match?")

    win = matches[matches['toss_winner'] == matches['winner']]
    loss = matches[matches['toss_winner'] != matches['winner']]

    number_of_wins = len(win)
    number_of_loss = len(loss)
    win_pct = number_of_wins / len(matches) * 100
    loss_pct = number_of_loss / len(matches) * 100
    difference = win_pct - loss_pct

    col1, col2, col3 = st.columns(3)
    col1.metric("Toss Winner Won", f"{number_of_wins} matches", f"{win_pct:.1f}%")
    col2.metric("Toss Winner Lost", f"{number_of_loss} matches", f"{loss_pct:.1f}%")
    col3.metric("Difference", f"{difference:.2f}%", "Minimal Impact")

    st.info("📊 Toss winner wins only 50.59% of matches — essentially a coin flip. Toss has no significant impact on IPL match results.")

    labels = ['Toss Winner Won', 'Toss Winner Lost']
    values = [win_pct, loss_pct]
    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color=['#2ecc71', '#e74c3c'], width=0.4)
    plt.title('Toss Winner Win % vs Loss %')
    plt.ylabel('Win Percentage %')
    plt.ylim(40, 55)
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, f'{v:.2f}%', ha='center', fontweight='bold')
    plt.tight_layout()
    st.pyplot(plt)

# ─── Q2: BATTING VS FIELDING FIRST ───
elif analysis == "🏏 Batting vs Fielding First":
    st.header("Batting First vs Fielding First — Which Wins More?")

    bat_won = matches[(matches['toss_decision'] == 'bat') & (matches['toss_winner'] == matches['winner'])]
    bat_lost = matches[(matches['toss_decision'] == 'bat') & (matches['toss_winner'] != matches['winner'])]
    field_won = matches[(matches['toss_decision'] == 'field') & (matches['toss_winner'] == matches['winner'])]
    field_lost = matches[(matches['toss_decision'] == 'field') & (matches['toss_winner'] != matches['winner'])]

    bat_win_pct = len(bat_won) / (len(bat_won) + len(bat_lost)) * 100
    field_win_pct = len(field_won) / (len(field_won) + len(field_lost)) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Bat First Win %", f"{bat_win_pct:.1f}%", f"{len(bat_won)} wins")
    col2.metric("Field First Win %", f"{field_win_pct:.1f}%", f"{len(field_won)} wins")
    col3.metric("Advantage", "Fielding First", f"+{field_win_pct - bat_win_pct:.1f}%")

    st.info("📊 Teams choosing to field first win 53.5% of matches vs only 45.3% when batting first. Chasing is the dominant strategy in modern IPL.")

    labels = ['Bat First', 'Field First']
    values = [bat_win_pct, field_win_pct]
    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color=['#3498db', '#e67e22'], width=0.4)
    plt.title('Win % — Batting First vs Fielding First')
    plt.ylabel('Win Percentage %')
    plt.ylim(35, 65)
    for i, v in enumerate(values):
        plt.text(i, v + 0.3, f'{v:.1f}%', ha='center', fontweight='bold')
    plt.tight_layout()
    st.pyplot(plt)

# ─── Q3: TOP PERFORMERS ───
elif analysis == "⭐ Top Performers":
    st.header("Top Performers — Batsmen & Bowlers")

    batter_perf = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
    bowler_perf = deliveries.groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(10)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏏 Top 10 Run Scorers")
        st.dataframe(batter_perf.reset_index().rename(columns={'batter': 'Player', 'batsman_runs': 'Total Runs'}))

    with col2:
        st.subheader("🎳 Top 10 Wicket Takers")
        st.dataframe(bowler_perf.reset_index().rename(columns={'bowler': 'Player', 'is_wicket': 'Total Wickets'}))

    st.info("📊 V Kohli leads all-time run scorers with 8,014 runs. YS Chahal leads wicket takers with 213 wickets.")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.barh(batter_perf.index, batter_perf.values, color='#2ecc71')
    ax1.set_title('Top 10 Run Scorers')
    ax1.set_xlabel('Total Runs')
    ax1.invert_yaxis()

    ax2.barh(bowler_perf.index, bowler_perf.values, color='#3498db')
    ax2.set_title('Top 10 Wicket Takers')
    ax2.set_xlabel('Total Wickets')
    ax2.invert_yaxis()

    plt.tight_layout()
    st.pyplot(fig)

# ─── Q4: POWERPLAY VS DEATH OVERS ───
elif analysis == "⚡ Powerplay vs Death Overs":
    st.header("Powerplay vs Death Overs — Which Phase Scores More?")

    powerplay_runs = deliveries[deliveries['over'] <= 5]['total_runs'].sum()
    death_runs = deliveries[deliveries['over'] >= 15]['total_runs'].sum()
    difference = powerplay_runs - death_runs

    col1, col2, col3 = st.columns(3)
    col1.metric("Powerplay Runs (Ov 1-6)", f"{powerplay_runs:,}")
    col2.metric("Death Over Runs (Ov 16-20)", f"{death_runs:,}")
    col3.metric("Powerplay Advantage", f"{difference:,} more runs")

    st.info("📊 Powerplay overs score 103,217 total runs vs 93,884 in death overs across all IPL matches. Fielding restrictions in powerplay create more scoring opportunities.")

    labels = ['Powerplay (Ov 1-6)', 'Death Overs (Ov 16-20)']
    values = [powerplay_runs, death_runs]
    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color=['#f39c12', '#9b59b6'], width=0.4)
    plt.title('Total Runs — Powerplay vs Death Overs')
    plt.ylabel('Total Runs')
    for i, v in enumerate(values):
        plt.text(i, v + 500, f'{v:,}', ha='center', fontweight='bold')
    plt.tight_layout()
    st.pyplot(plt)

# ─── Q5: BEST CHASING TEAMS ───
elif analysis == "🎯 Best Chasing Teams":
    st.header("Best Chasing Teams vs Best Batting First Teams")

    best_chasing = matches[matches['toss_decision'] == 'field'].groupby('winner')['id'].count().sort_values(ascending=False).head(5)
    best_batting = matches[matches['toss_decision'] == 'bat'].groupby('winner')['id'].count().sort_values(ascending=False).head(5)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏃 Best Chasing Teams")
        st.dataframe(best_chasing.reset_index().rename(columns={'winner': 'Team', 'id': 'Wins while Chasing'}))

    with col2:
        st.subheader("🏏 Best Batting First Teams")
        st.dataframe(best_batting.reset_index().rename(columns={'winner': 'Team', 'id': 'Wins Batting First'}))

    st.info("📊 Mumbai Indians are the best chasing team with 90 wins while chasing. CSK leads batting first with 63 wins — explaining their preference for setting targets.")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.barh(best_chasing.index, best_chasing.values, color='#2ecc71')
    ax1.set_title('Best Chasing Teams')
    ax1.set_xlabel('Wins while Chasing')
    ax1.invert_yaxis()

    ax2.barh(best_batting.index, best_batting.values, color='#3498db')
    ax2.set_title('Best Batting First Teams')
    ax2.set_xlabel('Wins Batting First')
    ax2.invert_yaxis()

    plt.tight_layout()
    st.pyplot(fig)