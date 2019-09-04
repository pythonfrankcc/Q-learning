#so we are going to be using openAIgymn library which is a collection of environments that we can use with the reinforcement learning algorithms
#in frozen the environment is a grid with various states as seen below
'''
----------------------------------------------------------------
| State|Description            |   Reward                        |
|      |                       |                                 |
|   S  |  starting point(safe) |    0                            |                                
|      |                       |                                 |
|   F  |  frozen surface(safe) |    0                            |
|      |                       |                                 |
|   H  |  hole(game over)      |    0                            |
|      |                       |                                 | 
|   G  |  goal(game over)      |    1                            |
-----------------------------------------------------------------
'''
#import necessary libraries
import numpy as np
import gym
import random
import time 
from IPython.display import clear_output

#creating the frozen lake environment
env = gym.make("FrozenLake-v0")

'''with this env object created we can query for information about the environment ,sample states and actions,retrieve awards and have the agent 
navigate the frozen lake which is made available by the use of gym.'''

#creating the Q-table
'''remember in the initial states the the initial Q-values are all zeros
rows are equivalaent to the state space and the columns are equivalent to action space 
'''
action_space_size = env.action_space.n
state_space_size = env.observation_space.n

#initailiaze the initial table to have all zeros
q_table=np.zeros((state_space_size,action_space_size))
#lets check the q_table created
print(q_table)

#initializing the Q-learning parameters
num_episodes = 10000
max_steps_per_episode = 100
#if the agent within the 100th step hasnt gotten the frisbee or fallen into a hole the episode ends and the agent gets a zero reward

learning_rate=0.1#(alpha)used to update the q-value as the agent continues to learn
discount_rate = 0.99#(gamma) used to calculate the sum of cumulative discounted rewards
#defining the epsilon that is used in epsilon-greedy policy for exploration and exploitation trade_off
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
#play around with the decay rate to determine which is best to use 
exploration_decay_rate = 0.001

#creating the Q-learning algorithm 
rewards_all_episodes = []
#this empty list will hold all the rewards we will get from each episode and this helps show how the game score changes over time
#looking at training the agent 
for episode in range(num_episodes):
	state = env.reset()#this involves resetting the state back to the starting or initial state
	done = False#this keeps track of whether the episode is finished 
	rewards_current_episode = 0#initial reward is always zero

	#initailize new episode params

	for step in range(max_steps_per_episode):
		#exploration-exploitation trade-off
		exploration_rate_threshold=random.uniform(0, 1)
		if exploration_rate_threshold > exploration_rate:#the agent will exploit and pick the greatest Q-value in Q-table in that state
			action = np.argmax(q_table[state,:])
		else:
			action = env.action_space.sample()#the agent explores by sampling an action at random

		#take action after choosing whether to explore or exploit the environment
		new_state, reward, done, info = env.step(action)
		'''the taking of the step action returns a tuple containing the new_state,the reward for the action that was taken,whether taking the action
		ended the episode and diagnostic information about the environment that may be useful if we need to do debugging.
		'''

		#update Q-table
		'''since taking an action gave us a certain reward we can then update the Q-table with the new Q-value for the state-action pair.'''
		q_table[state,action] = q_table[state,action] * (1 - learning_rate) + \
		     learning_rate * (reward + discount_rate * np.max(q_table[new_state, :])) #the optimal future Q-value for the next state-action pair
		#set new state/transition to the next state 
		state = new_state
		#add new reward
		rewards_current_episode += reward#increementing the reward from previous zero to the gained reward
		#now lets check if taking the action that we did ended the episode,if it did we jump out of this episode and if not we transition to next time step
		if done == True:#returned in the tuple after taking action it may have ended if it fell in a hole or acquirewd the frisbee
			break
		#set an exploration rate decay if the episode has ended 
		exploration_rate = min_exploration_rate + \
		  (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)#means that the exploration rate decreases at a rate proportional to its cureebnt value
		#add current episode reward to total reward list
		rewards_all_episodes.append(rewards_current_episode)#append the rewards from the current episode to rewards for all episodes
#calculate anad print the average reward per thousand episodes
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes),num_episodes/1000)
count = 1000
print('the average reward per thouasand episodes\n')
for r in rewards_per_thouasand_episodes:
	print(count,':',str(sum(r/1000)))
	count +=1000
