while True:
	try:
		height = int(input("Height: "))
		if height < 1 or height > 23:
			pass
		else:
			break
	except:
		pass
for line in range(0, height):
	for spaces in range(1, height - line):
		print(" ", end = '')
	for hashes in range(0, line + 2):
		print("#", end = '')
	print("")
