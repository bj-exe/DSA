import math

def get_std_dev(lst):
    n = len(lst)
    mean = sum(lst) / n 
    total = 0
    for x in lst:
        total += (x - mean) ** 2  
    variance = total / (n - 1)    
    return math.sqrt(variance)     

m = [2, 4, 6, 8, 8, 10]
n = [3, 3, 4, 6, 10]
o = [10, 11, 9, -3]

print("Standard Deviation of o:", round(get_std_dev(m), 2))
print("Standard Deviation of n:", round(get_std_dev(n), 2))
print("Standard Deviation of m:", round(get_std_dev(o), 2))
