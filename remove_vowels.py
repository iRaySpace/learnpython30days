def remove_vowels(a):
	"""Removes vowel from string input"""
	new_text = ""
	for x in a:
		if x not in ('a', 'e', 'i', 'o', 'u'):
			new_text = new_text + x
	return new_text

print(remove_vowels(input("Input a string: ")))