def fizz_buzz_game(start: int, stop: int) -> str:
    game_range = range(start, stop + 1)

    for number in game_range:
        if number == 0:
            print("It Is Zero!!!")

        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        elif number % 3 == 0:
            print("Fizz")

        elif number % 5 == 0:
            print("Buzz")

        else:
            print(number)


fizz_buzz_game(-10, 30)
