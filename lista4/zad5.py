# import collections

class Tree:
  #------------------------------- zagnieżdżona klasa Position -------------------------------
    class Position:

        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)            # opposite of __eq__

  # ---------- abstrakcyjne metody do zdefiniowania w podklasie ----------
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    # ---------- konkretne metody ----------
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):                 # works, but O(n^2) worst-case time
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):                  # time is linear in size of subtree
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)        # start _height2 recursion

    def __iter__(self):
        for p in self.positions():                        
            yield p.element()                               

    def positions(self):
        return self.preorder()                            # 

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # 
                yield p

    def _subtree_preorder(self, p):
        yield p                                           
        for c in self.children(p):                        
            for other in self._subtree_preorder(c):         
                yield other                                   

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):                        
            for other in self._subtree_postorder(c):        
                yield other                                   
        yield p        


class BinaryTree(Tree):
    # --------------------- dodatkowe metody abstrakcyjne ---------------------
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    # ---------- metody konkretne zaimplemetowane w tej klasie ----------
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None: # p must be the root
            return None # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent) # possibly None
            else:
                return self.left(parent) # possibly None
    
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None: # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p # visit p between its subtrees
        if self.right(p) is not None: # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        return self.inorder() 


class LinkedBinaryTree(BinaryTree):
  #-------------------------- zagnieżdżona klasa Node --------------------------
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right' 

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    #-------------------------- zagnieżdżona klasa Position --------------------------
    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    #------------------------------- metody użytkowe -------------------------------
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    #-------------------------- konstruktor drzewa --------------------------
    def __init__(self):
        self._root = None
        self._size = 0

    #-------------------------- metody publiczne --------------------------
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count

    #-------------------------- metody niepubliczne --------------------------
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)                  # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)                 # node is its parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent   # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node              # convention for deprecated node
        return node._element
    
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():         # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():         # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty
            t2._size = 0








class ExpressionTree(LinkedBinaryTree):

    def __init__(self, token, left=None, right=None):
        super().__init__()                        # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)                     # use inherited, nonpublic method
        if left is not None:                      # presumably three-parameter form
            if token not in '+-*/^':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)  # use inherited, nonpublic method

    def __str__(self):
        pieces = []                 # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))                    # leaf value as a string
        else:
            result.append('(')                                 # opening parenthesis
            self._parenthesize_recur(self.left(p), result)     # left subtree
            result.append(p.element())                         # operator
            self._parenthesize_recur(self.right(p), result)    # right subtree
            result.append(')')                                 # closing parenthesis

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())      # we assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            elif op == '^':
                return left_val ** right_val
            else:                          # treat 'x' or '*' as multiplication
                return left_val * right_val   

    def derivative(self, symbol="x"):
        return  self.actions_deriv(self.root(), symbol)

    def rewrite_deriv(self, p):
        if self.is_leaf(p):
            return ExpressionTree(p.element())
        else:
            # print(self.rewrite_deriv(self.left(p)))
            return ExpressionTree(p.element(), self.rewrite_deriv(self.left(p)), self.rewrite_deriv(self.right(p))) # Do reguły iloczynu i ilorazu 
            # jakby wyciągnięcie z drzewa elementów w odpowiedniej kolejności aby były użyteczne i przypisanie ich do zmiennej


    def add_deriv(self, left, right):
        # print(left, right)
        if left.root().element().isnumeric() and right.root().element().isnumeric(): # jeżeli na lewej i prawej storonie jest element przypisany do konkretnego
            # miejsca i jest numerem a nie symbolem(x) albo znakiem(+-*/^)
            return ExpressionTree(str(float(left.root().element()) + float(right.root().element()))) # dodaj elementy numeryczne
        elif left.root().element() == "0" or left.root().element() == "0.0": # gdy nie ma elementu z lewej strony dla zmiennoprzecinkowych też
            # eliminuje przypadki 0 + x itd
            return right
        elif right.root().element() == "0" or right.root().element() == "0.0": # gdy nie ma elementu z prawej strony dla zmiennoprzecinkowych też
            return left
        else:
            return ExpressionTree("+", left, right)

    def sub_deriv(self, left, right):
        if left.root().element().isnumeric() and right.root().element().isnumeric():
            return ExpressionTree(str(float(left.root().element()) - float(right.root().element())))
        elif left.root().element() == "0" or left.root().element() == "0.0":
            return -1*right
        elif right.root().element() == "0" or right.root().element() == "0.0":
            return left
        else:
            return ExpressionTree("-", left, right)

    def multi_deriv(self, left, right):
        if left.root().element().isnumeric() and right.root().element().isnumeric():
            return ExpressionTree(str(float(left.root().element()) * float(right.root().element())))
        elif left.root().element() == "0" or left.root().element() == "0.0": # eleminacja przypadków (0*x itd)
            return ExpressionTree("0")
        elif right.root().element() == "0" or right.root().element() == "0.0":
            return ExpressionTree("0")
        elif left.root().element() == "1" or left.root().element == "1.0": # eleminacja przypadków (1*x itd)
            return right
        elif right.root().element() == "1" or right.root().element == "1.0":
            return left
        else:
            return ExpressionTree("*", left, right)

    def div_deriv(self, left, right):
        if left.root().element().isnumeric() and right.root().element().isnumeric():
            return ExpressionTree(str(float(left.root().element()) * float(right.root().element())))
        elif left.root().element() == "0" or left.root().element() == "0.0": # eleminacja przypadków (0*x itd)
            return ExpressionTree("0")
        elif right.root().element() == "0" or right.root().element() == "0.0":
            return ExpressionTree("0")
        elif left.root().element() == "1" or left.root().element == "1.0": # eleminacja przypadków (1*x itd)
            return right
        elif right.root().element() == "1" or right.root().element == "1.0":
            return left
        else:
            return ExpressionTree("/", left, right)

    def pow_deriv(self, left, right):
        if left.root().element().isnumeric() and right.root().element().isnumeric():
            return ExpressionTree(str(float(left.root().element()) ** float(right.root().element())))
        elif left.root().element() == "0" or left.root().element() == "0.0": # eleminacja przypadków (0*x itd)
            return ExpressionTree("0")
        elif right.root().element() == "0" or right.root().element() == "0.0":
            return ExpressionTree("0")
        elif left.root().element() == "1" or left.root().element == "1.0": # eleminacja przypadków (1*x itd)
            return right
        elif right.root().element() == "1" or right.root().element == "1.0":
            return left
        else:
            return ExpressionTree("^", left, right)

        
    def actions_deriv(self, p, symbol):
        _p = p.element()
        if self.is_leaf(p): # jeżeli nie ma dziecka
            return ExpressionTree("1" if _p == symbol else "0") # różniczkowanie 
        else: 
            if _p == "+":
                left = self.actions_deriv(self.left(p), symbol)
                right = self.actions_deriv(self.right(p), symbol)
                return self.add_deriv(left,right)

            elif _p == "-":
                left = self.actions_deriv(self.left(p), symbol)
                right = self.actions_deriv(self.right(p), symbol)
                return self.sub_deriv(left,right)
            
            elif _p == "*":
                left_l = self.actions_deriv(self.left(p), symbol)
                left_r = self.rewrite_deriv(self.right(p))

                left = self.multi_deriv(left_l, left_r)

                right_l = self.rewrite_deriv(self.left(p))
                right_r = self.actions_deriv(self.right(p), symbol)

                right = self.multi_deriv(right_l, right_r)

                return self.add_deriv(left,right)

            elif _p == "/":
                left_l = self.actions_deriv(self.left(p), symbol)
                left_r = self.rewrite_deriv(self.right(p))

                left = self.multi_deriv(left_l, left_r)

                right_l = self.rewrite_deriv(self.left(p))
                right_r = self.actions_deriv(self.right(p), symbol)

                right = self.multi_deriv(right_l, right_r)

                numerator = self.sub_deriv(left, right)
                
                denominator_rewrite = self.rewrite_deriv(self.right(p))

                denominator = self.pow_deriv(denominator_rewrite, ExpressionTree("2"))

                return self.pow_deriv(numerator, denominator)
            

def tokenize(raw):
    SYMBOLS = set('+-*/()^ ')    # allow for '*' or 'x' for multiplication

    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:                 
                tokens.append(raw[mark:j])  # complete preceding token
            if raw[j] != ' ':
                tokens.append(raw[j])       # include this token
            mark = j+1                    # update mark to being at next index
    if mark != n:                 
        tokens.append(raw[mark:n])      # complete preceding token
    return tokens

def build_expression_tree(tokens):
    S = []                                        # we use Python list as stack
    for t in tokens:
        if t in '+-*/^':                            # t is an operator symbol
            S.append(t)                               # push the operator symbol
        elif t not in '()':                         # consider t to be a literal
            S.append(ExpressionTree(t))               # push trivial tree storing value
        elif t == ')':       # compose a new tree from three constituent parts
            right = S.pop()                           # right subtree as per LIFO
            op = S.pop()                              # operator symbol
            left = S.pop()                            # left subtree
            S.append(ExpressionTree(op, left, right)) # repush tree
            # we ignore a left parenthesis
    return S.pop()

if __name__ == '__main__':
    # big = build_expression_tree(tokenize('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'))
    big = build_expression_tree(tokenize('(((4*x) + (3*y))/((8*x))'))
    print("Equation: ", big)
    deriv_big = big.derivative()
    print("Derivative: ", deriv_big)
