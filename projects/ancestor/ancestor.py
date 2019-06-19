# approach it as a depth-first problem
# we have a graph of relationships between parents and children over generations
# each individual is assigned a unique integer identifier
# return the earliest known ancestor, from the farthest distance from the input
# if one or more ancestor tied for the earliest, then return the one with the lowest numeric ID
# return -1 if the input individual that has no parents


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Ancestory:
    def __init__(self):
        self.ancestor = {}

    def add_ancestory(self, ancestory):
        self.ancestor[ancestory] = set()

    def add_edge_ancestory(self, parent, child):
        if parent in self.ancestor and child in self.ancestor:
            self.ancestor[child].add(parent)
        else:
            raise IndexError("Ancestor does not exist")

    def earliest_ancestor(self, starting_ancestory):
        visited = set()
        s = Stack()

        s.push([starting_ancestory])
        heritages = {}
        while s.size() > 0:
            heritage = s.pop()
            p = heritage[-1]
            if not p in visited:
                visited.add(p)

                if not len(self.ancestor[p]):
                    h = len(heritage)
                    if h in heritages:
                        heritages[h].append(heritage)
                    else:
                        heritages[h] = [heritage]
                else:
                    for parent in self.ancestor[p]:
                        s.push([*heritage, parent])
        longest = max(heritages.keys())
        last_heritage = []
        for ancestory in heritages[longest]:
            last_heritage.append(ancestory[-1])
        if len(last_heritage) == 1:
            return last_heritage[0]
        else:
            return last_heritage

ancestors = Ancestory()

for i in range(1, 12):
    ancestors.add_ancestory(i)

ancestors.add_edge_ancestory(10, 1)
ancestors.add_edge_ancestory(1, 3)
ancestors.add_edge_ancestory(2, 3)
ancestors.add_edge_ancestory(4, 5)
ancestors.add_edge_ancestory(4, 8)
ancestors.add_edge_ancestory(11, 8)
ancestors.add_edge_ancestory(3, 6)
ancestors.add_edge_ancestory(5, 6)
ancestors.add_edge_ancestory(5, 7)
ancestors.add_edge_ancestory(8, 9)

print(ancestors.ancestor)

print(ancestors.earliest_ancestor(6))


