from time import perf_counter

def time(tab):
    start = perf_counter()
    max_element(tab)
    stop = perf_counter()
    return (stop-start)*1000


def max_element(tab):

    if len(tab) == 1:
        return tab[0]
    elif tab[0] < tab[1]:
        return max_element(tab[1:])
    else:
        tab[1] = tab[0]
        return max_element(tab[1:])


tab1 = [1,2,45,6,21,3,6,2,2,5656,3,6,78,8,2,1,1,3,6,78,8]
tab2 = [2,6,3,6,3,7,6,1,3,6,74,71,23,45,6,78,5,2,4524,567,7,23,4]
tab3 = [2,6,87,3,21,2,15,67,78,334,45,5,1,123,3,5,6,7,845,45,6,22,2,2]
tab4 = [-6,-5,-7,-1,-1234]

# złożoność O(n)
print(max_element(tab1))
print(time(tab1))
print(max_element(tab2))
print(time(tab2))
print(max_element(tab3))
print(time(tab3))
print(max_element(tab4))
print(time(tab4))
