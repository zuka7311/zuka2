def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(7))



def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
        return total
    print(sum_list([1, 2, 3, 4, 5, 6]))
    print(sum_list([5 ,10, -3]))

