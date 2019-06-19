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
            self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

        


