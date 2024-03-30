import numpy as np
import math as m

class ProbabilitySimulator:
    def __init__(self):
        self.events = {}

    def permutations(self):
        n = int(input("Please enter the number of items to choose from: "))         #EH
        r = int(input("Please enter the number of items chosen to be arranged: "))  #EH
        print(f"The permutation is: {m.perm(n,r)}\nThe probability of a permutation is: {100/m.perm(n,r): .4f}")

    def combinations(self):
        n = int(input("Please enter the number of items to choose from: "))         #EH
        r = int(input("Please enter the number of items chosen to be chosen: "))    #EH
        print(f"The combination is: {m.comb(n,r)}\nThe probability of a combination is: {100/m.comb(n,r): .2f}")

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

    def bayes_theorem(self):
        text = "Please enter the scenario you want to compute\nIn the format: 'event A' given 'event B'\nE.g. stock price going 5%, given the CEO of the company is fired\n**It is important that the 'given' keyword is specified!"
        scenario = input(f"{text}\n\nScenario: ").split('given')
        event_a, event_b = scenario[0].strip(), scenario[1].strip()
        b_given_a = float(input(f"Please enter the probability of {event_b}, given {event_a} has happened:\n"))  #EH
        a = float(input(f"Please enter the probability of {event_a} happening:\n"))        #EH
        b = float(input(f"Please enter the probability of {event_b} happening:\n"))        #EH
        denominator = b
        numerator = b_given_a * a
        a_given_b = numerator / denominator
        print(f'The probability of {''.join(scenario)}, is {a_given_b*100: .2f}%')

    
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
