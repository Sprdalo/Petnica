from modul_1 import check
from modul_2 import fill
from modul_3 import lose
from modul_4 import random_word
import random

key = random_word();
hide = "";
life = 10;

for i in range(len(key)):
	hide += "#";

while(1):
	guess = input("Unesite slovo: ");
	pos = check(guess, key);
	if (not pos):
		life = lose(life);
		if not life:
			print("Izgubili ste, rec je bila: ");
			print(key);
			break;
	else:
		hide = fill(pos, hide, guess);
		print(hide);
		if hide == key:
			print("Gotovo");
			break;