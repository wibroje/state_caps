

state_dict = {
	'Delaware': 'Dover',
	'Nebraska': 'Lincoln',
	'Utah': 'Salt Lake City'
}

class StateCapitals():
	def __init__(self, dict):
		self.intro()
		self.answer_key= {'Correct': 0, 'Incorrect': 0 }
		self.dictionary = {}
		self.start()
		self.shuffle_states(dict)

	def intro(self):
		print('State capitals matching game!')
		print('Wow, you seem capable..')
		print('But I have been wrong before.')

	def shuffle_states(self, states):
		keys = list(states.keys())
		shuffle(keys)
		for key in keys:
			self.dictionary.update({key: states[key]})

	def start(self):
		for key, value in self.dictionary.items():
			question = ('The capital of {} is').format(key)
			answer = input(question)
			self.evaluate(answer, value)

	def evaluate(self, input, answer):
		if(input == answer):
			print('Oh wow, you got it right..')
			self.answer_key['Correct'] += 1
			print(('Current score: {} Correct {} Incorrect').format(self.answer_key['Correct'], self.answer_key['Incorrect']))
		else:
			print('Lmao, is that the best you can do?')
			self.answer_key['Incorrect'] += 1
			print(('You currenty have {} right and {} wrong.').format(self.answer_key['Correct'], self.answer_key['Incorrect']))


play = StateCapitals(state_dict)

