#Q2
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    >>> paths(5, 3) # There is no valid path from x to y
    []
    """
    if x == y:
        return [[x]]
    elif x > y:
        return []
    else:
        a = paths(x * 2, y)
        b = paths(x + 1, y)
        return [[x] + i for i in (a + b)]
    

#Q3
def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...              Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels += [[i.label for i in x]]
        x = sum([k.branches for k in x], [])
    return max(levels, key = lambda lst: len(lst))




#Q4
def level_mutation_link(t, funcs):
    """Mutates t using the functions in the linked list funcs.

    >>> t = Tree(1, [Tree(2, [Tree(3)])])
    >>> funcs = Link(lambda x: x + 1, Link(lambda y: y * 5, Link(lambda z: z ** 2)))
    >>> level_mutation_link(t, funcs)
    >>> t
    Tree(2, [Tree(10, [Tree(9)])])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> level_mutation_link(t2, funcs)
    >>> t2
    Tree(2, [Tree(100), Tree(15, [Tree(16)])])
    >>> t3 = Tree(1, [Tree(2)])
    >>> level_mutation_link(t3, funcs)
    >>> t3
    Tree(2, [Tree(100)])
    """
    if funcs is Link.empty:
        return
    t.label = funcs.first(t.label)
    remaining = funcs.rest
    if t.is_leaf() and not remaining is Link.empty:
        while not remaining is Link.empty:
            t.label = remaining.first(t.label)
            remaining = remaining.rest
    for b in t.branches:
          level_mutation_link(b, funcs.rest)


          
#Q5
def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['H', 'D', 'S', 'C']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    >>> cards[26:30]
    ['7S', '7C', '8H', '8D']
    >>> shuffle(cards)[:12]
    ['AH', '7S', 'AD', '7C', 'AS', '8H', 'AC', '8D', '2H', '8S', '2D', '8C']
    >>> shuffle(shuffle(cards))[:12]
    ['AH', '4D', '7S', '10C', 'AD', '4S', '7C', 'JH', 'AS', '4C', '8H', 'JD']
    >>> cards[:12]  # Should not be changed
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half = len(cards) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(cards[i])
        shuffled.append(cards[i + half])
    return shuffled




#Q7
def lgk_pow(n,k):
    """Computes n^k.

    >>> lgk_pow(2, 3)
    8
    >>> lgk_pow(4, 2)
    16
    >>> a = lgk_pow(2, 100000) # make sure you have log time
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    elif k % 2 == 0:
        return lgk_pow(n, k // 2) ** 2
    else:
        return n * lgk_pow(n, k - 1)


# Q10
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2023
    >>> dime = mint.create(Dime)
    >>> dime.year
    2023
    >>> Mint.present_year = 2103  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2023
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2102
    >>> Mint.present_year = 2178     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2023

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        return coin(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.present_year



class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        if (Mint.present_year - self.year) > 50:
            return self.cents + Mint.present_year - self.year - 50
        else:
            return self.cents
        
class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

# Q11
def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty:
        return
    elif s.rest is Link.empty:
        s = Link.empty
    else:
        s.rest = s.rest.rest
        every_other(s.rest)

# Q12
def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> other_link = link
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> link is other_link # Make sure you are using mutation! Don't create a new linked list.
    True
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    Traceback (most recent call last):
        ...
    IndexError: Out of bounds!
    """
    "*** YOUR CODE HERE ***"
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link.rest is Link.empty and index >= 1:
        raise IndexError('Out of bounds!')
    else:
        insert(link.rest, value, index - 1)


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
    



