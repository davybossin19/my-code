

HORIZONTAL = 0
DEPTH = 1

def main():
    directions = getInput("input.txt")

    pos = [0,0]
    aim = 0

    for direction in directions:
        aim = moveSub(aim, pos, direction[0], direction[1])
    
    print(pos)
    print(pos[HORIZONTAL]*pos[DEPTH])

def moveSub(aim: int, pos: list[int], direction: str, magnitude: int) -> None:
    if direction == "forward":
        pos[HORIZONTAL] += magnitude
        pos[DEPTH] += aim * magnitude
    elif direction == "down":
        aim += magnitude
    elif direction == "up":
        aim -= magnitude

    return aim

def getInput(file: str) -> list[int]:
    file_handle = open(file, "r")

    directions = file_handle.readlines()
    
    for i, direction in enumerate(directions):
        directions[i] = (direction.split()[0],int(direction.split()[1]))

    file_handle.close()

    return directions

if __name__ == "__main__":
    main()
