---
layout: post
title: Natural Language Processing
categories: data science, data engineering
---

<h1> Natural Language Processing </h1>

Take a second to visualize a city, focusing on it's aphysical components and all of the unique building elements. There are some structures which are similar in building material - they use bricks, wooden beams, and steel bars. The roads are made of asphalt, the sidewalks of concrete. On a whole, this represents a city, but if individual elements are separated from the mix, there are individual structures. These can be further broken down into their building components.

In the same frame, the concept of natural language processing (NLP) can be placed and the idea holds true - only replace the building components and structures with the word token. NLP visualizes language as a group of tokens, that is, each word in a sentence can represent a token, while at the same time a sentence in a paragraph may represent a token. Depending on the request, tokens can change their mould to fit the ask.

Jumping straight to an example in which a sentence is broken into tokens.
<pre><code>
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Our example 'building' / sentence
text = "The city is a living entity. Each building, road, and sidewalk contributes to its unique character."

# Creating tokens from the text block (multiple sentences)
sentences = sent_tokenize(text)
print("Sentences as tokens:")
print(sentences)

# Creating tokens from the words in the individual sentences
word_tokens = [word_tokenize(sentence) for sentence in sentences]
print("\nWords as tokens for each sentence:")
for i, words in enumerate(word_tokens):
    print(f"Sentence {i+1}: {words}")
</code></pre>

The result:

<pre><code>
Sentences as tokens:
['The city is a living entity.', 'Each building, road, and sidewalk contributes to its unique character.']

Words as tokens for each sentence:
Sentence 1: ['The', 'city', 'is', 'a', 'living', 'entity', '.']
Sentence 2: ['Each', 'building', ',', 'road', ',', 'and', 'sidewalk', 'contributes', 'to', 'its', 'unique', 'character', '.']
</code></pre>

The individual sentences are given as tokens, while these sentences can be further broken down into tokens. In fact, each individual character of a word can constitute a token.

These concepts are the building blocks for more advanced concepts like chatbots. And while the example above already implements pre-baked methods thanks to the nltk module, it is useful to understand the ideas of regex - short for regular expression.

Regex takes advantage of string parsing to find user-defined patterns in text.
- \w
- \s
- \d
- \w+
- [a@#] : matches any 1 character
- [a-z] : matches a to z, the hypen indicates this spread capture
- [AGF]\w+ : matches words beginning with A G or F and greedily captures the following characters


- re.match() - only evaluates the start of the string
- re.search() - scans the entire string, returns the first match found
- both .match() and .search() return a 'match' object if a matching string is found

- nltk.regexp_tokenize(text, pattern) : unlike re.match/search(), nltk passes the string before the pattern

abc = re.search()
abc.start(), abc.end()