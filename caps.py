

state_dict = {
	"Delaware": "Dover",
	"Nebraska": "Lincoln",
	"Utah": "Salt Lake City"
}

class StateCapitals():
	def __init__(self, dict):
		self.intro()

	def intro(self):
		print('State capitals matching game!')
		print('Wow, you seem capable..')
		print('But I have been wrong before.')


play = StateCapitals(state_dict)

