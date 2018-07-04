import random

def random_word():
	
	huge_list = []

	with open("words.txt", "r") as f:
		for line in f:
			huge_list.extend(line.split())

	ind = random.randint(0, len(huge_list) - 1);
	return huge_list[ind];
