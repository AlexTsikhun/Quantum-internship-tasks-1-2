import time

## choose number
number = int(input("Enter a positive integer: "))
# number = 10**25
start_time = time.time()

def sum_numbers(number):
    """
        Function, that calculates the sum of first n natural numbers.

        Input:
            number - int
        Output:
            sum - int
    """
    # use formula for sum n elements
    sum = number * (number + 1) // 2
    return sum

end_time = time.time()
total_time = end_time - start_time

print("Sum: ", sum_numbers(number))
print("Execution time:", total_time, "seconds")
