def check(s, key):
	pos = [];
	for i in range(len(key)):
		if key[i] == s:
			pos.append(i);
	return pos;