def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num
    


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
