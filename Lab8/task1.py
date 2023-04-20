with open("file.txt", "r", encoding="utf-8") as file_read:

	lines = file_read.readlines()
	lines_count = len(lines)

	with open("write.txt", "w", encoding="utf-8") as file_write:
		for i in range(lines_count):
			line = lines[i]
			if i % 2 == 0:
				file_write.write(line.upper())
			else:
				file_write.write(line.lower())