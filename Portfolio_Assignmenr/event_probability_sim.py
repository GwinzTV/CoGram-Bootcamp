import numpy as np
import math as m

class ProbabilitySimulator:
    def __init__(self):
        self.events = {}

    def permutations(self):
        n = int(input("Please enter the number of items to choose from: "))         #EH
        r = int(input("Please enter the number of items chosen to be arranged: "))  #EH
        print(f"The permutation is: {m.perm(n,r)}\nThe probability of a permutation is: {1/m.perm(n,r): .4f}")

    def combinations(self):
        n = int(input("Please enter the number of items to choose from: "))         #EH
        r = int(input("Please enter the number of items chosen to be chosen: "))    #EH
        print(f"The combination is: {m.comb(n,r)}\nThe probability of a combination is: {1/m.comb(n,r): .4f}")

    def add_event(self, name):  # adds event and probability to the simulator
        ask_again = True
        while True:
            if ask_again:
                event = input(f"{name} please enter your event:\n")
                probability = float(input("Also, please enter the probability of this event:\n")) #EH
                self.events[event] = probability
                ask = input("Do you want to add anymore events? [Y/N]\n").lower()   #EH
                if ask == 'n':
                    ask_again = False
            else:
                break

    def trials(self, name):
        trial = int(input(f"{name} please enter the number of trials: ")) #EH
        return trial

    def bayes_theorem(self, a, b_given_a, b):
        denominator = b
        numerator = b_given_a * a
        a_given_b = numerator / denominator
        return a_given_b

    
    # facilitates the simulation of the scenarios and returns the probabilities
    def run_simulation(self):
        print("Welcome to the Event Probability Simulator!")
        name = input("Please enter your name: ")
        print(f"Hi {name}! Please select one of the following operations:\n")
        print("[1] - Calculate Permutation\n[2] - Calculate Combinations\n[3] - Update probability using Bayes' Theorem\n")
        selection = int(input(f'{name} enter your selection: ')) #EH

        # navigates to the users selected operation
        if selection == 1:
            self.permutations()
        elif selection == 2:
            self.combinations()
        elif selection == 3:
            self.bayes_theorem()

        # trial = self.trials(name)
        # self.add_event(name)


# Script:
simulator = ProbabilitySimulator()
simulator.run_simulation()
