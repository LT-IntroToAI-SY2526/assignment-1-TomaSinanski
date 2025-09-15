"""
Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check and we'll be doing them in class.

Make sure to complete the a1.py problems which should be AI generated.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.
    """
    if n < 0:
        return -n
    else:
        return n
    


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    #Java Method
    # result = []
    # for i in range(len(lst)):
    #     if i % 2 == 0:
    #         result.append(lst[i])
    # return result
    
    #Python Way
    return lst[::2]


def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    total = 0
    for i in lst:
        total += i
    return total


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    total = 0
    for i in lst:
        total += i
    return total/len(lst)


def median(lst: List[int]) -> float:
    length = len(lst)
    middle = length//2
    if length % 2 == 1:
        return float(lst[middle])
    else:
        return (list[middle] + list[middle-1])/2


def duck_duck_goose(lst: List[str]) -> List[str]:
    position = 0
    current = "duck1"
    while len(lst) > 2:
        if current == "duck1":
            current = "duck2"
            position += 1
        elif current == "duck2":
            current = "goose"
            position += 1
        else:
            current = "duck1"
            lst.pop(position)
        if position == len(lst):
            position = 0
    return lst
    


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"], "failed ddg 1"
    names = ["miguel", "emma", "franco", "lucas", "maks"]
    assert duck_duck_goose(names) == ["emma", "lucas"], "failed ddg 2"

    print("All tests passed!")