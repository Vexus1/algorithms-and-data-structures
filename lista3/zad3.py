def sum_of_array(TAB):
    """Oblicza sumę wszystkich elementów tablicy n x n, reprezentowanej jako lista list."""
    sum = 0
    for i in TAB:
        for j in i:
            sum += j
    return sum

n = 8

TAB1 = [[10 for i in range(n)] for j in range(n)] 
TAB2 = [[4 for i in range(n)] for j in range(n)] 
TAB3 = [[23 for i in range(n)] for j in range(n)] 
print(TAB1)
print(sum_of_array(TAB1))
print(TAB2)
print(sum_of_array(TAB2))
print(TAB3)
print(sum_of_array(TAB3))
