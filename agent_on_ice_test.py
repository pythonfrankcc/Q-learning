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
'''
#calculate and print the average reward per thousand episodes
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes),num_episodes/1000)
count = 1000
print('the average reward per thousand episodes\n')
for r in rewards_per_thouasand_episodes:
	print(count,':',str(sum(r/1000)))

	count +=1000'''
#after the training of the agenyt lets now see the agent in action on the environment using just 3 episodes
for episode in range (3):
	state = env.reset()
	done = False
	print('this is the beiginning of episode one')
	time.sleep(1)#this is time given for us to see the print out on the console befre it disappears

	#take on new time step params
	for step in range(max_steps_per_episode):
		clear_output(wait = True)#this is the IPython which clears the output from current cell and the wait ensures that the clear output waits to be overwritten by another output
		env.render()#this renders the current state where the agent is located on the grid
		time.sleep(0.3)#gives us time to see the rendered state that the agent is located in

		action = np.argmax(q_table[state,:])#this sets the action to be the highest action in the Q-table for our current state 
		new_state, reward, done, info = env.step(action) 

		#after getting the tuple with the new_state,reward and whether the action terminated our episode we can now keep on moving
		if done:
			clear_output(Wait= True)
			env.render()
			if reward == 1:
				print('you reached the goal')
				time.sleep(3)
			else:#we know that if we do not get a reward of 1 then the reward is a 0
				print('you fell into the hole')
				time.sleep(3)
				clear_output(wait = True)
			break
	        #if the last action did not complete the episode then we skip over the conditional clause and transition to the new state and move to the next time step
	        #since we had already trained the model then we know that we can make actions based on exploitation rather than exploration
	    state = new_state

#close the environment on completion of the episodes
env.close()

