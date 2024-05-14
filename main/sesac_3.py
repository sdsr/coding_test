def sum_big_two_numbers(num_list):
    num_list_copy = num_list[:]
    a = max(num_list_copy)
    num_list_copy.remove(a)
    b = max(num_list_copy)
    return a+b

print(sum_big_two_numbers([1, 2, 5, 3, 9, 8]))