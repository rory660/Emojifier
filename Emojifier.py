import csv
import random

class Emojifier(object):

	def __init__(self, profileFilename):
		self.lookup = {}
		self.readProfile(filename = profileFilename)

	def readProfile(self, filename):
		with open(filename, "r") as profileCSV:
			profileReader = csv.reader(profileCSV, delimiter = ",", quotechar = '"')
			for row in profileReader:
				self.lookup[row[0]] = row[1:]

	def emojify(self, text):
		returnText = ""
		for i, char in enumerate(text):
			if char in self.lookup.keys():
				returnText += random.choice(self.lookup[char])
			else:
				returnText += char
		return returnText