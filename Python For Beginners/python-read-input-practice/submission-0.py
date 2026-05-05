def add_two_numbers() -> int:
    params = input()
    splits = params.split(",")
    sums = 0
    for i in splits:
        sums += int(i)
    return sums


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
