
def main():
    binaries = getInput("input.txt")

    digits_by_position = {}

    for i in range(len(binaries[0])):
        digits_by_position[i] = {"0": 0, "1": 0}

    for binary in binaries:
        for i, char in enumerate(binary):
            digits_by_position[i][char] += 1
    
    gamma_rate = create_gamma_rate(digits_by_position)
    epsilon_rate = create_epsilon_rate(digits_by_position)

    print("Gamma rate:", gamma_rate)
    print("Epislon rate:", epsilon_rate)

    int_gamma_rate = int(gamma_rate, 2)
    int_epsilon_rate = int(epsilon_rate, 2)

    print(int_gamma_rate * int_epsilon_rate)

def create_gamma_rate(digits_by_position: dict[int, dict[str, int]]):
        gamma_rate = "0b"

        for dict in digits_by_position.values():
            if dict["0"] > dict["1"]:
                gamma_rate = gamma_rate + "0"
            else:
                gamma_rate = gamma_rate + "1"
            
        return gamma_rate

def create_epsilon_rate(digits_by_position: dict[int, dict[str, int]]):
        epsilon_rate = "0b"

        for position in digits_by_position.values():
            if position["0"] < position["1"]:
                epsilon_rate = epsilon_rate + "0"
            else:
                epsilon_rate = epsilon_rate + "1"
            
        return epsilon_rate


def getInput(file: str) -> list[int]:
    file_handle = open(file, "r")

    binaries = file_handle.readlines()
    
    for i, binary in enumerate(binaries):
        binaries[i] = binary.strip()

    file_handle.close()

    return binaries

if __name__ == "__main__":
    main()