def change_string(s):
	start = "Здравствуйте!"
	end = "До свидания!"
	return f"{start} {s} {end}"

string = input("Введите строку: ")
print(change_string(string))