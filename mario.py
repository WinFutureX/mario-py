while True:
	try:
		height = int(input("Height: "))
		break
	except:
		pass
for line in range(0, height):
	for spaces in range(1, height - line):
		print(" ", end = '')
	for hashes in range(0, line + 2):
		print("#", end = '')
	print(" ");
