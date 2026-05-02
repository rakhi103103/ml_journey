import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print(f"First five matches row:\n{matches.head()}")
print(f"\n\nMatches column:\n{matches.columns.tolist()}")
print(f"\n\nmatches Shape:\n{matches.shape}")

print(f"First five deliveries row:\n{deliveries.head()}")
print(f"\ndeliveries column:\n{deliveries.columns.tolist()}")
print(f"\ndeliveries Shape:\n{deliveries.shape}")

#step2:finding missing values in both dataframes

missing_matches = matches.isnull().sum()
missing_deliveries = deliveries.isnull().sum()
match_percentage = (missing_matches/len(matches))*100
delivery_percentage = (missing_deliveries/len(deliveries))*100

print(f"\n\nthe missing values in matches are:\n{missing_matches}")
print(f"\n\nthe missing values in deliveries are:\n{missing_deliveries}")
print(f"\n\nthe perentage of missing values in matches are:\n{match_percentage}")
print(f"\n\nthe perentage of missing values in deliveries are:\n{delivery_percentage}")

#step3:Clean both dataframes

#for matches dataframe
matches["city"] = matches['city'].fillna("Unknown")
matches["winner"] = matches["winner"].fillna("No_result")
matches = matches.drop(columns = "method")
matches["result_margin"] = matches["result_margin"].fillna(0)
matches["player_of_match"] = matches["player_of_match"].fillna("Unknown")
matches["target_runs"] = matches["target_runs"].fillna(0)
matches["target_overs"] = matches["target_overs"].fillna(0)

#for deliveries dataframe
deliveries["extras_type"] = deliveries["extras_type"].fillna("normal")
colums_to_fix = ["player_dismissed", "dismissal_kind", "fielder"]
deliveries[colums_to_fix] = deliveries[colums_to_fix].fillna("none")

print(f"\n\nAfter cleaning both the dataframe:\n Matches:\n{matches.isnull().sum()} \n Deliveries:\n {deliveries.isnull().sum()} ")

#Step 4 — Which team won the most matches?

top_10 = matches[matches["winner"]!="No_result"]["winner"].value_counts().head(10)
print(f"\n\n The top 10 teams are:\n {top_10}")

#Step 5 — Toss analysis
#Interesting question — does winning the toss help you win the match?
matches["toss_match_winner"]= np.where(matches["toss_winner"] == matches["winner"],"yes","No")
toss_winner = matches["toss_match_winner"].value_counts()
percentage_win = (matches["toss_match_winner"] =="yes").mean() *100
print(f"\n\nthe toss winner are: \n{toss_winner}")
print(f"\n\nThe  % of times toss winner also won the match:\n {percentage_win}")

#Step 6 — Toss decision analysis
# when teams win the toss, do they prefer to bat or field?
toss_decision = matches["toss_decision"].value_counts()
percentage_decision = (toss_decision/len(matches))*100

print(f"\n\nhow many times toss winners chose to bat vs field:\n{toss_decision}")
print(f"\n\nCalculated percentage of each:\n{percentage_decision}")

#Step 7 — Top 10 batsmen by total runs
top10_batsmen = deliveries.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(10)
print(f"\n\nTop 10 batsmen by total runs: \n{top10_batsmen}")

#Step 8 — Top 10 bowlers by wickets
filter_row = deliveries[
    (deliveries["is_wicket"] ==1) &
    (deliveries["dismissal_kind"]!="run out")
]
count_wickets = filter_row.groupby("bowler")["is_wicket"].sum().sort_values(ascending=False).head(10)
print(f"\n\nThe top 10 bowlers by wickets are: \n {count_wickets}")

#Step 9 — Most runs in a single match (batting performance)
combined = pd.merge(deliveries,matches,left_on="match_id",right_on="id")
# print(f"\n\n{combined.head()}")

# print(f"\n\n{combined.shape}")

#Step 10 — Top batsmen by season
tops_batsmen_seasons = combined.groupby(["season" ,"batter"])["batsman_runs"].sum().reset_index() 
top_per_season = tops_batsmen_seasons.sort_values("batsman_runs" , ascending=False).drop_duplicates(subset="season")
print(f"\n\nTop batsmen by season:\n {top_per_season}")

#Step 11 — Which venue has the highest average score?
total_score = combined.groupby(["venue","match_id"])["total_runs"].sum()
highest_average_score = total_score.groupby("venue").mean().reset_index().sort_values("total_runs",ascending=False)
print(f"\n\nvenue has the highest average score:\n{highest_average_score}")

#Step 12 — NumPy stats on runs per match
ts = total_score.values
mean =np.mean(ts)
std =np.std(ts)
p90 =np.percentile(ts,90)
print(f"\n\nMean: {mean:.2f}\nSTD: {std:.2f}\n 90th Percentile: {p90:.2f}")

#Step 13 — crosstab: Toss decision vs Match result
ct=pd.crosstab(matches["toss_decision"],matches["toss_match_winner"])
print(ct)

#Step 14 — pivot table: Average runs by batting team and season
pt = pd.pivot_table(
    combined,
    index="batting_team",
    columns="season",
    values="batsman_runs",
    aggfunc=np.mean
)

print(pt)

#Step 15 — Visualizations 🎨
#Chart 1 — Horizontal bar chart: Top 10 teams by wins
plt.barh(top_10.index,top_10.values)
plt.title("Top 10 teams by wins")
plt.xlabel("winners")
plt.ylabel("teams")
plt.gca().invert_yaxis()
plt.savefig("top_teams_wins.png")
plt.show()

#Chart 2 — Bar chart: Top 10 batsmen by runs
plt.bar(top10_batsmen.index,top10_batsmen.values)
plt.xticks(rotation=45,ha="right")
plt.title("Top 10 batsmen by runs")
plt.xlabel("Batsmen")
plt.ylabel("Runs")
plt.tight_layout()
plt.savefig("top_batsmen.png")
plt.show()

#Chart 3 — Bar chart: Top 10 bowlers by wickets
plt.bar(count_wickets.index,count_wickets.values)
plt.xticks(rotation=45,ha="right")
plt.title("Top 10 bowlers by wickets")
plt.xlabel("Bowler")
plt.ylabel("wickets")
plt.tight_layout()
plt.savefig("top_bowlers.png")
plt.show()

#Chart 4 — Bar chart: Toss decision wins
ct.plot(kind="bar",rot=0)
plt.title("Toss decision wins")
plt.xlabel("Toss Decision")
plt.ylabel("Number of Matches")
plt.legend(["lost","won"])
plt.tight_layout()
plt.savefig("Toss_decision_wins.png")
plt.show()
