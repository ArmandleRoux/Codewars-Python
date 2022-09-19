def two_lowest(numbers):
    min_1 = min(numbers)
    numbers.remove(min_1)
    min_2 = min(numbers)
    return min_1 + min_2


print(two_lowest([10, 343445353, 3453445, 3453545353453]))
