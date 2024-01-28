def count_has_2(list_1) -> int:
    """Find 2 in unit digit in a list."""
    a = 0
    count = 0
    number = 3
    for i in range(number):
        a = list_1[i] % 10
        if a == 2:
            count += 1
    return count
