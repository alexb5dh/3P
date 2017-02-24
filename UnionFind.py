class UnionFind:
    def __init__(self, value):
        self.value = value
        self.parent, self.rank = None, 0

    def find(self):
        root = self
        while (root.parent != None):
            root = root.parent

        # Path compression (rank not updated)
        if root not in {self, self.parent}:
            self.parent = root

        return root

    def union(self, other):
        root1, root2 = self.find(), other.find()
        
        if root1 is root2: 
            return False
        if root1.rank < root2.rank:
            root1, root2 = root2, root1

        root2.parent = root1
        root1.rank = max(root1.rank, root2.rank + 1) # Only current node rank is updated

        return True

# Tests
print(f'?: {str(UnionFind)}')

uf1 = UnionFind(1)
uf2 = UnionFind(2)
assert(uf1.union(uf2))
assert(not uf1.union(uf2))
assert(uf1.find() == uf2.find())
assert(uf1.find().rank == 1)

uf1 = UnionFind(1)
uf2 = UnionFind(2)
uf1.union(UnionFind(3))
assert(uf1.find() == uf1)
assert(uf1.rank == 1)
uf1.union(uf2)
assert(uf2.find() == uf1)
assert(uf1.rank == 1)

uf1 = UnionFind(1)
uf2 = UnionFind(2)
uf3 = UnionFind(3)
uf4 = UnionFind(4)
uf1.union(uf3)
uf2.union(uf4)
uf1.union(uf2)
assert(uf3.find() == uf1)
assert(uf1.rank == 2)

print(f'✔: {str(UnionFind)}')
