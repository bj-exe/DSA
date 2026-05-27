def get_mode(lst):
    freq = {}

    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    freq_values = list(freq.values())
    highest = freq_values[0]
    for f in freq_values:
        if f > highest:
            highest = f
    
    if highest == 1:
        return None
    
    modes = []
    for num, count in freq.items():
        if count == highest:
            modes.append(num)
    return modes

a1 = [2, 4, 6, 8, 8, 10]
a2 = [3, 3, 4, 6, 10]
a3 = [10, 11, 9, -3]

print("Mode of a1:", get_mode(a1))
print("Mode of a2:", get_mode(a2))
print("Mode of a3:", get_mode(a3))
