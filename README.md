# Markov Sentence Generator
 A second-order Markov chain generator that can be easily updated and merged 	with other instances of this type.
 
 **Usage:**

```
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

model = MarkovModel()
model.update_corpus(zen)

for i in range(10):
	print(model.generate_sentence())
```

```
Better than complex.
Unless explicitly silenced.
Never pass silently.
If the implementation is easy to explain, it may be a good idea.
There should be one-- and preferably only one --obvious way to do it.
Often better than *right* now.
Temptation to guess.
It's a bad idea.
Special cases aren't special enough to break the rules.
The face of ambiguity, refuse the temptation to guess.
```

(Results are better the more you feed into it!)
