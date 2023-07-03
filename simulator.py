import random
import matplotlib.pyplot as plt
from agent import Agent, num_agreements


def run_simulation(agents, steps):
    agreement_rates = []    
    num_agreements = 0
    
    done = None
    
    for step in range(steps):
        speaker, listener = random.sample(agents, k=2)
        num_agreements += speaker.communicate(listener)
        agreement_rates.append((num_agreements / (step+1)) * 100)
        
        # check for complete agreement
        if check_agents(agents=agents):
            if not done:
                done = step
    
    # print final results
    for agent in agents:
        print(f"{agent.name} vocab: {agent.vocabulary}")
        
    
    # plot agreement-rates
    plt.plot(agreement_rates)
    if done:
        plt.axvline(x=done, color='red', linestyle='--')
    plt.xlabel('Simulation Round')
    plt.ylabel('Agreement Rate (%)')
    plt.title(f'Agreement Rates over Time with {steps} steps, {len(agents)} agents.')
    plt.show()


def check_agents(agents):
    # check if agents is empty
    if len(agents) == 0:
        return True
    
    # compare every agent's vocab w/ the first agent's vocab
    first_vocab = agents[0].vocabulary
    for agent in agents[1:]:
        if agent.vocabulary != first_vocab:
            return False
        
    # all vocabs are the same
    return True


num_simulations = input("Input number of simulations: ")
num_agents = input("Input number of agents:")

agents = []
for i in range(int(num_agents)):
    agents.append(Agent(f"Agent {i+1}"))
    
run_simulation(agents, int(num_simulations))