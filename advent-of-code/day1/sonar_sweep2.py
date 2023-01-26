def main():
    data = getInput("input.txt")

    prev_window_sum = None
    count = 0
    i=0
    while (i+2 < len(data)):
        if i + 2 < len(data):
            window_sum = data[i] + data[i+1] + data[i+2]

        if prev_window_sum != None:
            if window_sum > prev_window_sum:
                count += 1
        
        i+=1
        prev_window_sum = window_sum

    print(count)


def getInput(file: str) -> list[int]:
    file_handle = open(file, "r")

    values = file_handle.readlines()
    
    for i, value in enumerate(values):
        values[i] = int(value.strip())

    file_handle.close()

    return values

if __name__ == "__main__":
    main()
