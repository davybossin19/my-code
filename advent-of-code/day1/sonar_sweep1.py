

def main():
	file_handle = open("input.txt", "r")
	
	values = file_handle.readlines()
	prev_val = None
	count = 0

	for i, value in enumerate(values):
		values[i] = int(value.strip())

		if prev_val != None:
			if values[i] > prev_val:
				count += 1

		prev_val = values[i]
	file_handle.close()

	print(count)

if __name__ == "__main__":
	main()

