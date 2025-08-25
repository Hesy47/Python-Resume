from collections import Counter


def top_two_frequent(nums: list[int]) -> list[int]:
    counter = Counter(nums)

    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_items)

    return [num for num, _ in sorted_items[:2]]


print(top_two_frequent([1, 1, 2, 2, 3, 3, 3]))
print(top_two_frequent([5, 5, 4, 4, 4, 3]))
print(top_two_frequent([7, 7, 8, 8, 9]))

#fundamentals