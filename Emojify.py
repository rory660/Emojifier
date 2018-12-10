import argparse
import Emojifier

def main():
	parser = argparse.ArgumentParser(description = "Converts a string to emojis using a given profile.")
	parser.add_argument("source", help = "String to be emojified.")
	parser.add_argument("--profile", help = "Profile to use.")
	args = parser.parse_args()
	if args.profile:
		emojify(string = args.source, profileFilename = args.profile)
	else:
		emojify(string = args.source)

def emojify(string, profileFilename = "default.csv"):
	emojifier = Emojifier.Emojifier(profileFilename)
	print(emojifier.emojify(string))

if __name__ == "__main__":
	main()