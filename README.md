# Markov Sentence Generator
 A second-order Markov chain generator that can be easily updated and merged 	with other instances of this type.
 
 **Usage:**

```

from Markov import MarkovModel


zen = ("Beautiful is better than ugly."
		"Explicit is better than implicit."
		"Simple is better than complex."
		"Complex is better than complicated."
		"Flat is better than nested."
		"Sparse is better than dense."
		"Readability counts."
		"Special cases aren't special enough to break the rules."
		"Although practicality beats purity."
		"Errors should never pass silently."
		"Unless explicitly silenced."
		"In the face of ambiguity, refuse the temptation to guess."
		"There should be one-- and preferably only one --obvious way to do it."
		"Although that way may not be obvious at first unless you're Dutch."
		"Now is better than never."
		"Although never is often better than *right* now."
		"If the implementation is hard to explain, it's a bad idea."
		"If the implementation is easy to explain, it may be a good idea."
		"Namespaces are one honking great idea -- let's do more of those!")

monty = ("He's not the Messiah—he's a very naughty boy!"
		 "Strange women lying in ponds, distributing swords, is no basis for a system of government!"
		"There's nothing wrong with you that an expensive operation can't prolong."
		"She's a witch! Burn her already!"
		"Oh! Now we see the violence inherent in the system! Help, help, I'm being repressed!"
		"It's just a flesh wound."
		"Are you suggesting that coconuts migrate?"
		"Your Mother was a Hamster, and your Father smelt of Elderberries!"
		"Help, I'm being oppressed. Come and see the violence inherent in the system."
		"We're an anarcho-syndicalist commune")

model1 = MarkovModel()
model1.update_corpus(zen)

model2 = MarkovModel()
model2.update_corpus(monty)

model1.merge_corpus(model2.corpus)

for i in range(10):
	print(model1.generate_sentence())
```

(Results are better the more you feed into it!)
