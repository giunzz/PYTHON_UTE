# Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2. Store
# this information in a dictionary where the keys are the team names and the values are lists of
# the form [wins, losses].

team_dict = {}
while True:
    result = input("enter game scores in a format like team1 score1 - team2 score2(type done to finish): ")
    if result.lower()=="done":
        break
    team1,score1,team2,score2 = result.split()
    score1=int(score1)
    score2=int(score2)
    
    if score1>score2:
        team_dict[team1][0]+=1
        team_dict[team2][1]+=1
    else:
        team_dict[team2][0]+=1
        team_dict[team1][1]+=1
print("\nTeam Records:")
for team, record in team_dict.items():
    print(f"{team}: Wins - {record[0]}, Losses - {record[1]}")