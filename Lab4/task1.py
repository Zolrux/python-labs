def get_first_substr(s):
	return s[: int(len(s) / 3)].lower()

def get_second_substr(s, first_substr):
	without_first_substr = s[len(first_substr): ]
	return s[len(first_substr): len(without_first_substr)]

def get_third_substr(s, second_substr):
	return s[s.find(second_substr) + len(second_substr): ].upper()

s = "В лесу я встретил 27 волков, 4 из них были серые, я схватил палку, и он убежал."

first_substr = get_first_substr(s)
second_substr = get_second_substr(s, first_substr)
third_substr = get_third_substr(s, second_substr)

print(f"3-я часть: {third_substr}")
print(f"1-я часть: {first_substr}")
print(f"2-я часть: {second_substr}")