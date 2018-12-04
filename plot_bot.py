from words import verbs, nouns, adverbs, adjectives
import random

def openTemplate(template):
	temp = []
	with open(template, 'r') as t:
		for line in t:
			temp.append(line.split())
	return temp

def parseTemplate(template):
	parsed = []
	for line in template:
		parsed_line = []
		for obj in line:
			if obj.startswith('$'):
				parsed_line.append(getPOS(obj.strip('$').lower()))
			elif obj.startswith('['):
				parsed_line.append(random.choice(obj.strip('[').strip(']').split('|')))
			else: parsed_line.append(obj)
		parsed.append(parsed_line)
	return parsed

def getPOS(word):
	if word.startswith('adj'):
		return random.choice(adjectives.adjectives)
	elif word.startswith('adv'):
		return random.choice(adverbs.adverbs)
	elif word.startswith('n'):
		return random.choice(nouns.nouns)
	elif word.startswith('v'):
		return random.choice(verbs.verbs)['present']


def createPlot(script):
	plot = ''
	for line in script:
		plot = plot + ' '.join(line) + "\n"
	return plot

if __name__ == '__main__':
	from sys import argv
	template = openTemplate(argv[1])
	script = parseTemplate(template)
	print(createPlot(script))
