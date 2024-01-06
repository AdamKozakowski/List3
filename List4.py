# List 4 III. RandomWalks and PageRank
import numpy as np
import random as r
import collections
import seaborn as sns
import matplotlib.pyplot as plt
# Let G = ({1, 2, 3, 4, 5, 7, 8, 9, 10}, {1 → 2, 2 → 1, 2 → 3, 2 → 2, 3 → 4, 3 → 2, 4 → 2, 4 →
# 4, 4 → 5, 5 → 4, 4 → 1, 1 → 5, 9 → 10, 8 → 7, 7 → 8, 4 → 9, 10 → 7, 8 → 1}). An
# agent is placed at in a vertex 1. In each step the agent chooses randomly out-going
# edge and goes to the vertex pointed by this edge. Find the distribution of the position
# of the agent after 2, 3, 4, 50 and 100 steps. HINT: Do this numerically. Remember that
# p(t+1) = p(t)P .

#Let G
adjacency_matrix = np.array([
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]   
])

def run_agent(steps):
    #An agent is placed at in a vertex 1.
    agent_position = 0

    for step in range(steps): 
        neighbours = []
        #out-going edges
        for i in range(len(adjacency_matrix)):
            if adjacency_matrix[agent_position][i] == 1:
                neighbours.append(i)
        #in each step the agent chooses randomly out-going edge and goes to the vertex pointed by this edge
        agent_position = r.choice(neighbours)
    return agent_position
# Find the distribution of the position
# of the agent after 2, 3, 4, 50 and 100 steps
list_of_steps = [2,3,4,50,100]
MCS = 1000
def run_agent_multiple_times(steps, MCS):
    final_positions =[]
    for i in range(MCS):
        final_positions.append(run_agent(steps))
    # Postprocessing data
    frequencies = collections.Counter(final_positions)
    positions_ranked = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    # filename = f"{steps}_{MCS}.txt"

    # with open(filename, "w", encoding="utf8") as output_file:
    #     output_file.write("Rank\tFinal Position\tCount\tFreq\n")
    #     for rank, (position, count) in enumerate(positions_ranked, start=1):
    #         output_file.write(f"{rank}\t{position}\t{count}\t{count/MCS:.6f}\n")
    # print(f"Result saved to {filename}")

for steps in list_of_steps:
    run_agent_multiple_times(steps,MCS)