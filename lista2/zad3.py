
# tab[0] <-- min
# tab[1] <-- max

# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]

def min_max(tab):
    """Znajduje najwięszką największą i najmniejszą wartość w podanej tablicy przy użyciu rekurencji."""

    if len(tab) == 1:
        return f"min: {tab[0]}, max:{tab[0]}"

    elif len(tab) == 2 and tab[0] <= tab[1]:
        return f"min: {tab[0]}, max:{tab[1]}"

    elif len(tab) == 2 and tab[0] >= tab[1]:
        return f"min: {tab[1]}, max:{tab[0]}"

    elif tab[0] <= tab[1] and tab[0] <= tab[2] and tab[1] <= tab[2]:
        tab[1] = tab[0]
        return min_max(tab[1:])

    elif tab[0] <= tab[1] and tab[0] <= tab[2] and tab[1] >= tab[2]:
        tab[2] = tab[1]
        tab[1] = tab[0]
        return min_max(tab[1:])
        
    elif tab[0] >= tab[1] and tab[0] <= tab[2] and tab[1] <= tab[2]:
        return min_max(tab[1:])
        
    elif tab[0] <= tab[1] and tab[0] >= tab[2] and tab[1] >= tab[2]:
        tab[2], tab[1] = tab[1], tab[2]
        return min_max(tab[1:])
    
    elif tab[0] >= tab[1] and tab[0] >= tab[2] and tab[1] <= tab[2]:
        tab[2] = tab[1]
        return min_max(tab[1:])

    elif tab[0] >= tab[1] and tab[0] >= tab[2] and tab[1] >= tab[2]:
        tab[1] = tab[2]
        tab[2] = tab[0]
        return min_max(tab[1:])


tab0 = [1]
tab1 = [2,1,45,6,21,3,6,2,2,5656,3,6,78,8,2,1,1,3,6,78,8]
tab2 = [523452345,6,3,6,3,7,6,0,3,6,74,71,23,45,6,78,5,2,4524,567,7,23,4,4]
tab3 = [2,6,87,3,21,2,15,67,-8,-56,78,334,45,5,1,123,3,5,6,7,845,45,6,22,2,2]
tab4 = [1,6,2,6,245,6,7,7,1,1,-4,-7,-1]
tab5 = [2,1]
print(min_max(tab0))
print(min_max(tab1))
print(min_max(tab2))
print(min_max(tab3))
print(min_max(tab4))
print(min_max(tab5))
print(min_max.__doc__)


