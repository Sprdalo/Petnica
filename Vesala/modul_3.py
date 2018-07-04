def lose(life):
	print("Netacno!");
	life -= 1;

	if (life):
		print("Ostalo Vam je jos ", end = "");
		print(life, end='');
		print(" zivota");

	return life;