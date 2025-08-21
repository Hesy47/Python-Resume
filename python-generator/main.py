from time import time


def list_comprehension(number_range: int):
    start_time = time()
    nums = [x * x for x in range(number_range)]
    end_time = time()

    print(f"time took by list comprehension: {(total_time := end_time - start_time)}")


def the_generator(number_range: int):
    start_time = time()
    nums = (x * x for x in range(number_range))
    end_time = time()

    print(f"time took by generator: {(total_time := end_time - start_time)}")


the_generator(100_000_000_000)
list_comprehension(100_000_000_000)
