# Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost. Store this information in a dictionary where the keys are the team names and the values are lists of the form [wins, losses].
# (a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
# (b) Using the dictionary, create a list whose entries are the number of wins of each team.
# (c) Using the dictionary, create a list of all those teams that have winning records.

team_dict = {}
while True:
    team_name = input("Enter a team name:(type done to finish) ")
    if team_name.lower()=="done":
        break
    wins = int(input("Enter the number of games the team won: "))
    losses = int(input("Enter the number of games the team lost: "))
    team_dict[team_name] = [wins, losses]
# (a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
team_to_find=input("Enter a team to find the winning percentage: ")
if team_to_find in team_dict:
    print((team_dict[team_to_find][0]/(team_dict[team_to_find][1]+team_dict[team_to_find][0]))*100,"%")
else:
    print("team not found")

# (b) Using the dictionary, create a list whose entries are the number of wins of each team.
list_of_winners = [team_dict[team][0] for team in team_dict]

print(list_of_winners)

# (c) Using the dictionary, create a list of all those teams that have winning records.
list_of_winning = [team for team in team_dict if team_dict[team][0]>team_dict[team][1]]
print(list_of_winning)