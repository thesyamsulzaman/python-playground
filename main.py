def recursive_countdown(number):
    if number == 0:
        return 0

    print(number)

    return recursive_countdown(number - 1)

recursive_countdown(10)

