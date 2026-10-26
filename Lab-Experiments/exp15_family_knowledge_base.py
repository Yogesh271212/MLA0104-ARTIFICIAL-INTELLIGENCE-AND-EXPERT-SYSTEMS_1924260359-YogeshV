males = {'John', 'Bob', 'Mike', 'Tom'}
females = {'Mary', 'Alice', 'Sara', 'Anna'}
parents = [
    ('John', 'Bob'), ('Mary', 'Bob'),
    ('John', 'Alice'), ('Mary', 'Alice'),
    ('Bob', 'Mike'), ('Sara', 'Mike'),
    ('Bob', 'Anna'), ('Sara', 'Anna')
]

def is_father(x, y):
    return x in males and (x, y) in parents

def is_mother(x, y):
    return x in females and (x, y) in parents

def is_sibling(x, y):
    if x == y:
        return False
    return any((p, x) in parents and (p, y) in parents for p in males | females)

def is_grandparent(x, z):
    return any((x, y) in parents and (y, z) in parents for y in males | females)

print("Is John father of Bob?", is_father('John', 'Bob'))
print("Is Mary mother of Alice?", is_mother('Mary', 'Alice'))
print("Are Bob and Alice siblings?", is_sibling('Bob', 'Alice'))
print("Is John grandparent of Mike?", is_grandparent('John', 'Mike'))
