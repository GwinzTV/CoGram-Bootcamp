import numpy as np
import math as m

class ProbabilitySimulator:
    def __init__(self):
        self.events = {}
        self.menu_text = "\nDo you wish to continue?\n\nPress:\n[1] - Main menu\n[2] - Exit\n\nEnter Your Selection: "

    def permutations(self):
        n = int(input("Please enter the number of items to choose from: "))
        r = int(input("Please enter the number of items chosen to be arranged: "))
        try:
            print(f"The permutation is: {m.perm(n,r)}\nThe probability of a permutation is: {100/m.perm(n,r): .4f}")
        except ValueError:
            print("Hey, the values entered must be non-negative integers")

    def combinations(self):
        n = int(input("Please enter the number of items to choose from: "))
        r = int(input("Please enter the number of items chosen to be chosen: "))
        try:
            print(f"The combination is: {m.comb(n,r)}\nThe probability of a combination is: {100/m.comb(n,r): .2f}")
        except ValueError:
            print("Hey, the values entered must be non-negative integers")

    def trials_sim(self, name):
        event = input(f'Hey {name}! Please enter the event you want to simulate:\n E.g. Drawing a king from a deck of cards\nEvent: ')
        probability_event = float(input(f'Please enter the probability of {event} happening: '))
        if not 0 < probability_event < 1:
            raise Exception(f"\nSorry {name}, you must enter a probability of event as a decimal between 0 - 1\n")
        
        trial = int(input("Please enter the number of trials: "))
        if trial < 0:
            raise Exception("Value of trial must be a non-negative integer")
        success = np.random.rand(trial) < probability_event
        success_count = np.sum(success)
        print("Value entered for number of trial must be non-negative")
        result = success_count / trial
        print(f"The probability of {event} happening, given {trial} trials is: {result*100}%")

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
        while True:
            print(f"Hi {name}! Please select one of the following operations:\n")
            print("[1] - Calculate Permutation\n[2] - Calculate Combinations")
            print("[3] - Simulate an event given a number of trials\n[4] - Update probability using Bayes' Theorem\n")
            selection = int(input(f'{name} enter your selection: ')) #EH

            # navigates to the users selected operation
            if selection == 1:
                self.permutations()
            elif selection == 2:
                self.combinations()
            elif selection == 3:
                self.trials_sim(name)
            elif selection == 4:
                self.bayes_theorem()
            
            menu_exit = int(input(self.menu_text))
            if menu_exit == 2:
                print("\nYou have reached the End of the simulation, Cheers!\n")
                break


# Script:
simulator = ProbabilitySimulator()
simulator.run_simulation()

    
    
    
    
    
    # def add_event(self, name):  # adds event and probability to the simulator
    #     ask_again = True
    #     while True:
    #         if ask_again:
    #             event = input(f"{name} please enter your event:\n")
    #             probability = float(input("Also, please enter the probability of this event:\n")) #EH
    #             self.events[event] = probability
    #             ask = input("Do you want to add anymore events? [Y/N]\n").lower()   #EH
    #             if ask == 'n':
    #                 ask_again = False
    #         else:
    #             break