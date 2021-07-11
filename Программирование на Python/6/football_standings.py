# results of all games
games = []

# open the file and read the results of all games into the list
with open("game_results.txt") as results:
    for game in results:
        games.append(
            [int(i) if i.isdigit() else i for i in game.rstrip().split(";")])

# list of all teams that played
teams = set()
for team in games:
    teams.add(team[0])
    teams.add(team[2])

# total table
results = []
for team in teams:
    num_matches = 0
    num_wins = 0
    num_draws = 0
    num_losses = 0
    # listing each completed game
    for i in range(len(games)):
        # the team was playing the game
        if team in games[i]:
            num_matches += 1

            # the result of the game
            ind = games[i].index(team)
            if games[i][ind + 1] > games[i][ind - 1]:
                num_wins += 1
            elif games[i][ind + 1] == games[i][ind - 1]:
                num_draws += 1
            else:
                num_losses += 1

    points = num_wins * 3 + num_draws * 1

    print(team, end=': ')
    print(num_matches, num_wins, num_draws, num_losses, points)
