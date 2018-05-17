from random import shuffle
from time import sleep
from states import *

class StateCapitals():
	def __init__(self, dictionary):
		self.dict_states = {}
		self.answer_key= {'Correct': 0, 'Incorrect': 0 }
		self.shuffle_states(dictionary)
		self.intro()
		self.start()
		self.game_over()

	def intro(self):
		print('State capitals matching game!') ; sleep(2)
		print('Type in the capital or something') ; sleep(2)

	def shuffle_states(self, dictionary):
		keys = list(dictionary.keys())
		shuffle(keys)
		for key in keys:
			self.dict_states.update({key: dictionary[key]})

	def start(self):
		for key, value in self.dict_states.items():
			question = ('The capital of {} is ').format(key)
			answer = input(question)
			self.evaluate(answer, value)

	def evaluate(self, input, answer):
		if(input == answer):
			print('Oh wow, you got it right..') ; sleep(2)
			self.answer_key['Correct'] += 1
			print(('Current score: {} Correct {} Incorrect').format(self.answer_key['Correct'], self.answer_key['Incorrect'])) ; sleep(2)
		else:
			print('Lmao, is that the best you can do?') ; sleep(2)
			self.answer_key['Incorrect'] += 1
			print(('Current score: {} Correct {} Incorrect').format(self.answer_key['Correct'], self.answer_key['Incorrect'])) ; sleep(2)

	def game_over(self):
		play_again = input('Try again? Y/n ')
		if play_again == 'y':
			StateCapitals(state_dict)
		else:
			print('Fine, leave..') ; sleep(3)
			print('I SAID LEAVE!') ; sleep(1)




play = StateCapitals(state_dict)




