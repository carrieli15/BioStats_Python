def climb_staircase(n: int) -> int:
    """
    This function uses a simple dynamic programming approach
    to calculate the number of ways to climb a
    staircase of `n` stairs, given that we
    can climb either 1 stair or 2 stairs at a time.

    Parameters:
    - n (int): The total number of stairs to climb.

    Returns:
    - int: The number of different ways to climb `n` stairs.

    """  # noqa: D205
    # climb 1 stair
    if n == 1:
        return 1
    # climb 2 stairs
    if n == 2:
        return 2

    # initialize an array to store the number of ways to reach each step
    # ways[i] will store the number of ways to climb to the 'i'th step
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    # apply dynamic programming to calculate the number of ways
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


if __name__ == "__main__":
    # number of ways to climb 10 stairs
    print(f"Ways to climb 10 stairs: {climb_staircase(10)}")
    # (output: 89)

    # number of ways to climb 100 stairs
    print(f"Ways to climb 100 stairs: {climb_staircase(100)}")
    # (output: 573147844013817084101)
