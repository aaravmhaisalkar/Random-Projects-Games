import requests
import tabulate
import sys
from rich import print
import random
#Use files and api 
teams = {
    "Arsenal": 42, 
    "Aston Villa": 66,
    "Bournemouth": 35,
    "Brentford":55,
    "Brighton":51,
    "Chelsea":49,
    "Crystal Palace":52,
    "Everton": 45,
    "Fulham": 36,
    "Ipswich Town": 57,
    "Leicester":46,
    "Liverpool": 40,
    "Manchester City":50,
    "Manchester United": 33,
    "Newcastle United": 34,
    "Nottingham Forest":65,
    "Southampton": 41,
    "Tottenham": 47, 
    "West Ham": 48, 
    "Wolves": 39
}
team = random.choice(list(teams.items()))

url = f'https://v3.football.api-sports.io/teams/statistics?league=39&team={team[1]}&season=2024'
headers = {
    'x-apisports-key': "d20de7be4a03ec3474c63330ef5acdc4"
}
response = requests.get(url, headers=headers)
data = response.json()
stats = data["response"]



maxGuesses = input("What is the maximum number of guesses you want? (<7)\n")
if int(maxGuesses) > 7:
    print("Maximum number of guesses should be below 7.\n")
    sys.exit()
hardMode = input("Would you like to play on hard mode? This mode removes all the unlimited hints given on normal mode. (y/n)\n")
if hardMode == "y":
    hardMode = True
else:
    hardMode=False
guessCount = 1
hintCount = 1



    
def findFormValues(form):
    draws, wins, loss = 0,0,0
    for i in form:
        if i == "W":
            wins +=1
        if i == "D":
            draws +=1
        if i == "L":
                loss +=1
    return f'Wins: {wins}\n Draws: {draws}\n Losses: {loss}'

def formations(stats):
    formations = ''
    for i in stats["lineups"]:
        formations += f'Formation: {i["formation"]}\n Games Used: {i["played"]}\n'
    return formations


tabulate_table = []
team_form = findFormValues(stats["form"])
team_goals_for, team_goals_again =stats["goals"]["for"]["total"]["total"],stats["goals"]["against"]["total"]["total"]
biggest_winstreak =stats["biggest"]["streak"]["wins"]
biggest_wins = f'Home: {stats["biggest"]["wins"]["home"]}\n Away: {stats["biggest"]["wins"]["away"]}'
biggest_loss = f'Home: {stats["biggest"]["loses"]["home"]}\n Away: {stats["biggest"]["loses"]["away"]}'
cleansheets =stats["clean_sheet"]["total"]
formationsResult = formations(stats)

team_stats = {
    "Season Form (2024)": team_form,
    "Goals For": team_goals_for,
    "Goals Against": team_goals_again,
    "Biggest Win Streak": biggest_winstreak,
    "Biggest Wins": biggest_wins,
    "Biggest Loss": biggest_loss,
    "Clean Sheets": cleansheets,
    "Formations": formationsResult
}

tabulate_table.append(team_stats)

print(tabulate.tabulate(
        tabulate_table,
        headers='keys', 
        tablefmt="fancy_grid",
        maxcolwidths= [15,5,5,10,10,10,10,20],
        numalign= "center",
        stralign= "center",
))

if hardMode:
    print("\n[bold red]Respond with full team name with correct spelling.\nYou have no hints since you picked hard mode.[/bold red]")
else:
    print("\n[bold red]Respond with full team name with correct spelling.\nYou have unlimited hints, type 'hint' to recieve one. Each hint uses one of your guesses.[/bold red]")
    
while guessCount <= int(maxGuesses):
    team_guess = input(f"\nWhat is your guess as to what the team is?  (Guess {guessCount}/{maxGuesses})\n")
    if team_guess == team[0]:
        print(f"[bold yellow]Correct! The team was {team[0]}![/bold yellow]")
        sys.exit()
    elif team_guess.lower() == "hint" and hardMode==False:
        print(f"The first letter of the team's name is {team[0][:hintCount]}")
        guessCount+=1
        hintCount+=1
    elif team_guess.lower() == "hint"  and hardMode==True:
        print(f"No hints given on hard mode. A guess will be added as a penalty.")
        guessCount+=1

    else:
        print("Incorrect guess. Check your spelling if you are sure it is correct.")
        guessCount+=1

print(f"\n[bold yellow]The team was {team[0]}, you were unable to find the answer in {maxGuesses} guesses.[/bold yellow]")


