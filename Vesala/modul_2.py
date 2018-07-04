def fill(pos, hide, c):
	result = "";
	visible = [];

	for i in range(len(hide)):
		if hide[i] == "#":
			visible.append(0);
		else:
			visible.append(2);

	for i in pos:
		visible[i] = (1);

	length = len(visible);
	for i in range(length):
		if visible[i] == 1:
			result += c;
		if visible[i] == 0:
			result += "#";
		if visible[i] == 2:
			result += hide[i];

	return result;
