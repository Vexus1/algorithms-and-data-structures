T = 34
tree = [None] * T

def root(p):
    if tree[0] != None:
        print("Root already exist")
    else:
        tree[0] = p
    
def left(p, q):
    if tree[q] == None:
        print(f"Can't set at index {(q * 2) + 1} Parent not exist")
    else:
        tree[(q * 2) + 1] = p

def right(p, q):
    if tree[q] == None:
        print(f"Can't set at index {(q * 2) + 2} Parent not exist")
    else:
        tree[(q * 2) + 2] = p


def print_tree():
    for i in range(T):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print(" ", end="")

root("-")
left("/", 0)
right("+", 0)
left("x", 1)
right("+",1)
left("x", 2)
right("6", 2)
left("+", 3)
right("3", 3)
left("-", 4)
right("2", 4)
left("3", 5)
right("-", 5)
left("3", 7)
right("1", 7)
left("9", 9)
right("5", 9)
left("7", 12)
right("4", 12)
left("A", 13)
right("B", 13)
left("A", 15)
right("B", 15)

print_tree()