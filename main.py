import numpy as np
import random
from scipy import stats


class Cricket():
    """
    Initiate class cricket with number of overs and number of players
    """
    def __init__(self, overs, players):
        self.players = players
        self.runs = [0, 0]
        self.wickets = [0, 0]
        self.no_of_overs = overs
        self.outcomes = ['W', 6, 4, 3, 2, 1, '.']
        self.aggression_values = {1: [0, 0.05, 0.05, 0.15, 0.15, 0.3, 0.3], 2: [0.14, 0.14, 0.14, 0.14, 0.14, 0.15, 0.15], 3: [0.3, 0.3, 0.15, 0.15, 0.05, 0.05, 0]}
        self.start_match()

    def start_match(self):
        """Depending on number of players, the flow of game is determined"""
        self.batting(0)
        if self.players == 1:
            self.atharva()
        else:
            self.batting(1)
        self.winner()
    
    def print_overview(self, over, current_player, current_runs):
        """Print over-wise score"""
        print(f'Total Runs : {self.runs[current_player]}\t\tWickets: {self.wickets[current_player]}')
        print("OVER " + str(over+1) + " -> ", *current_runs, sep=" ")


    def batting(self, current_player):
        """Each over iterated with given constraints"""
        over = 1
        while over != self.no_of_overs + 1:
            batting_agression = self.get_input()
            current_runs = self.calculate_runs(batting_agression, current_player)
            self.print_overview(over, current_player, current_runs)
            over += 1
            if self.wickets[current_player] >= 10:
                break
        self.generate_overview(current_player)
        return self.runs

    def calculate_runs(self, batting_agression, player):
        """Calculate runs scored in an over depending on aggression level"""
        current_runs = np.random.choice(
            self.outcomes, size=6, p=self.aggression_values.get(batting_agression))
        self.update_scoreboard(player, current_runs)
        return current_runs

    def get_input(self):
        """Take user input"""
        while True:
            batting_agression = int(
                input("Batting Agression for this over (1-3) > "))
            if batting_agression < 1 or batting_agression > 3:
                print("Batting agression should be between 1 to 3!")
            else:
                break
        return batting_agression

    def update_scoreboard(self, player, current_runs):
        """Updates over-wise scoreboard"""
        for x in current_runs:
            if x.isdigit():
                self.runs[player] += int(x)
            elif x == "W":
                self.wickets[player] += 1

    def atharva(self):
        """A fun little piece of code"""
        for over in range(self.no_of_overs):
            current_runs = self.calculate_runs(random.randint(1, 3), 1)
            self.print_overview(over, 1, current_runs)
            if self.wickets[1] >= 10:
                break
        self.generate_overview(1)

    def generate_overview(self, player):
        """Generate overview after each player finishes"""
        if self.players == 1:
            if player == 1:
                playing = 'Atharva'
            else:
                playing = 'You'
        else:
            playing = 'Player {number}'.format(number=player+1)
        print("#####################################################################")
        print(
            f'{playing} Total Runs : {self.runs[player]}\t\tWickets: {self.wickets[player]}')
        print("#####################################################################\n")

    def winner(self):
        """Calculate and display the winner"""
        runs = max(self.runs)
        winnr = self.runs.index(runs)
        if self.players == 1:
            if winnr == 0:
                playing = 'YOU WIN'
            else:
                playing = "Atharva WINS"
        else:
            playing = f'PLAYER {winnr+1} WINS'

        print("\n#####################################################################")
        print(f'{playing} BY {runs - min(self.runs)} RUNS')
        print("#####################################################################")


overs = int(input("Number of overs : "))
players = int(input("Number of players (Single / 1v1): "))
Cricket(overs, players)
