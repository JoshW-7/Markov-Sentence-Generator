import random
import copy


class MarkovModel:
	"""
    A second-order Markov chain generator that can be easily updated and merged
	with other instances of this type.

    'corpus': An optional parameter to start with an existing corpus dict
	'kwargs':
		'copy': Set to False if the passed-in corpus parameter can be modified
    """


	def __init__(self, corpus={}, **kwargs):
		if kwargs.get("copy") == True:
			self.corpus = copy.deepcopy(corpus)
		else:
			self.corpus = corpus


	def _sanitized(self, message):
		# Remove any undesired characters
		illegal_chars = [".", ",", "!", "?", "\n", ":", "'", '"']
		for char in illegal_chars:
			message = message.replace(char, "")
		return message

	def update_corpus(self, message):
		"""
		Updates the corpus with a new input message of any desired length
		"""


		sentences = [sentence for sentence in message.split(".") if len(sentence) > 0]
		for sentence in sentences:
			words = [word for word in sentence.split(" ") if len(word) > 0]

			# Break up the words into groups of three: (first, second), third
			for i in range(len(words)-2):
				first, second, third = (words[i], words[i+1], words[i+2])

				# Update the corpus with the new tuple (first, second)
				if (first,second) not in self.corpus.keys():
					self.corpus[(first,second)] = {
						"total": 1,
						"next": {
							third: 1,
						}
					}
				else:
					# If the tuple already exists, increment the total so it can be used for generation results based on probability
					self.corpus[(first,second)]["total"] += 1
					if third not in self.corpus[(first,second)]["next"].keys():
						self.corpus[(first,second)]["next"][third] = 1
					else:
						self.corpus[(first,second)]["next"][third] += 1

	def merge_corpus(self, other_corpus):
		"""
		Merges this instance's corpus with another one
		"""


		for key,values in other_corpus.items():
			if key not in self.corpus.keys():
				self.corpus[key] = {
					"total": values["total"],
					"next": values["next"],
				}
			else:
				self.corpus[key]["total"] += values["total"]
				for word in values["next"]:

					# The "next" key points to another dictionary, which will hold all the next words seen
					if word in self.corpus[key]["next"]:
						self.corpus[key]["next"][word] += values["next"][word]
					else:
						self.corpus[key]["next"][word] = values["next"][word]

	def generate_sentence(self, **kwargs):
		"""
		Generates a sentence with this instance's corpus
		'kwargs':
			'start': Optional argument for specifying which word to attempt to start with
			'length': Maximum length in words of the generated sentence
			'excitement': Set to 1 for maximum sentence excitement, 0 for no excitement
			'inquisitiveness': Set to 1 for maximum sentence inquisitiveness, 0 for no inquisitiveness
		"""


		start = kwargs.get("start")
		if start is not None:
			found = False
			for key in self.corpus.keys():
				if key[0].lower().startswith(start.lower()):
					pair = key
					found = True
			if not found:
				pair = random.choice(list(self.corpus.keys()))
		else:
			pair = random.choice(list(self.corpus.keys()))

		# Start with the first two words
		words = [pair[0], pair[1]]
		next_word = ""
		capitalize = False
		for i in range(kwargs.get("length", 20)):

			# If the pair or sanitized version of the pair exists
			if self.corpus.get(pair) or self.corpus.get( (self._sanitized(pair[0]), self._sanitized(pair[1]) )):
				if not self.corpus.get(pair):
					pair = (self._sanitized(pair[0]), self._sanitized(pair[1]))

				# Randomly choose one of the next words seen for this particular pair of words
				choices = [word for word in self.corpus[pair]["next"].keys()]
				weights = [n for n in self.corpus[pair]["next"].values()]
				next_word = random.choices(choices, weights=weights, k=1)[0]
				if capitalize:
					next_word = next_word.capitalize()
				pair = (pair[1], next_word)
				if next_word.endswith(".") or next_word.endswith("!") or next_word.endswith("?"):
					capitalize = True
				else:
					capitalize = False
				words.append(next_word)
			else:
				break

		words[0] = words[0].capitalize()
		if (not words[-1].endswith(".") and not words[-1].endswith("!") and not words[-1].endswith("?")) or words[-1].endswith(","):
			if words[-1].endswith(","):
				words[-1] = words[-1].strip(",")
			words[-1] = words[-1] + random.choices([".", "!", "?"], weights=[1, kwargs.get("exitement", 0), kwargs.get("inquisitiveness", 0)], k=1)[0]

		return " ".join(words)
