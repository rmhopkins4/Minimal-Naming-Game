import random
import matplotlib.pyplot as plt
from agent import Agent, num_agreements


def run_simulation(agents, steps):
    agreement_rates = []    
    num_agreements = 0
    
    for step in range(steps):
        speaker, listener = random.sample(agents, k=2)
        num_agreements += speaker.communicate(listener)
        agreement_rates.append((num_agreements / (step+1)) * 100)
    
    # print final results
    for agent in agents:
        print(f"{agent.name} vocab: {agent.vocabulary}")
    # plot agreement-rates
    plt.plot(agreement_rates)
    plt.xlabel('Simulation Round')
    plt.ylabel('Agreement Rate (%)')
    plt.title('Agreement Rates over Time in Simulated Minimal Naming Game')
    plt.show()


num_simulations = input("Input number of simulations: ")
num_agents = input("Input number of agents:")

agents = []
for i in range(int(num_agents)):
    agents.append(Agent(f"Agent {i+1}"))
    
run_simulation(agents, int(num_simulations))