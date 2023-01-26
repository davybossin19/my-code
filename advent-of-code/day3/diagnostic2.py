
def main():
    ox_binaries = get_input("./input.txt")
    o2_binaries = get_input("./input.txt")




    ox_rate = filter_ox_rate(ox_binaries)
    o2_rate = filter_o2_rate(o2_binaries)

    print(ox_rate)
    print(o2_rate)
    
    
    print(int(ox_rate, base=2) * int(o2_rate, base=2))

def get_digits_by_position(binaries: list[str]) -> dict[int, dict[str, int]]:
    digits_by_position = {}

    for i in range(len(binaries[0])):
        digits_by_position[i] = {"0": 0, "1": 0}

    for binary in binaries:
        for i, char in enumerate(binary):
            digits_by_position[i][char] += 1
    
    return digits_by_position

def filter_ox_rate(binaries: list[str]) -> list[str]:
    digit_keys = get_most_common_digits(get_digits_by_position(binaries))
    for i, char in enumerate(digit_keys):
        j = 0
        while(j < len(binaries)):
            if len(binaries) > 1:
                cur_char = binaries[j][i]
                if cur_char != digit_keys[i]:
                    binaries.remove(binaries[j])
                    j -= 1
            j+=1
        digit_keys = get_most_common_digits(get_digits_by_position(binaries))
        
    return "0b"+binaries[0]
    
def filter_o2_rate(binaries: list[str]) -> list[str]:
    digit_keys = get_least_common_digits(get_digits_by_position(binaries))
    for i, char in enumerate(digit_keys):
        j = 0
        while(j < len(binaries)):
            if len(binaries) > 1:
                cur_char = binaries[j][i]
                if cur_char != digit_keys[i]:
                    binaries.remove(binaries[j])
                    j -= 1
            j+=1
        digit_keys = get_least_common_digits(get_digits_by_position(binaries))
        
    return "0b"+binaries[0]

def get_most_common_digits(digits_by_position: dict[int, dict[str, int]]) -> list[int]:
    result = []

    for position in digits_by_position.values():
        if position["0"] > position["1"]:
            result.append("0")
        else:
            result.append("1")
    
    return result
    
def get_least_common_digits(digits_by_position: dict[int, dict[str, int]]) -> list[int]:
    result = []

    for position in digits_by_position.values():
        if position["0"] <= position["1"]:
            result.append("0")
        else:
            result.append("1")
        
    return result

def get_input(file: str) -> list[int]:
    file_handle = open(file, "r")

    binaries = file_handle.readlines()
    
    for i, binary in enumerate(binaries):
        binaries[i] = binary.strip()

    file_handle.close()

    return binaries

if __name__ == "__main__":
    main()