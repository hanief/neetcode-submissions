from typing import List

def read_integers() -> List[int]:
    numbers = input()
    string_list = numbers.split(",")
    intgs = []
    for i in string_list:
        intgs.append(int(i))
    return intgs

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
