import random
from agent import Agent

def run_simulation(agents, steps):
    for _ in range(steps):
        speaker, listener = random.sample(agents, k=2)
        speaker.communicate(listener)
    
    for agent in agents:
        print(f"{agent.name} vocab: {agent.vocabulary}")


num_simulations = input("Input number of simulations: ")
num_agents = input("Input number of agents:")

agents = []
for i in range(int(num_agents)):
    agents.append(Agent(f"Agent {i+1}"))
    
run_simulation(agents, int(num_simulations))