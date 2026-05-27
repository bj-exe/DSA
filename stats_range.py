def get_range_sorted(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-1] - sorted_lst[0]

a1 = [2, 4, 6, 8, 8, 10]
a2 = [3, 3, 4, 6, 10]
a3 = [10, 11, 9, -3]

for name, lst in [('a1', a1), ('a2', a2), ('a3', a3)]:
    print("  Range:", get_range_sorted(lst))