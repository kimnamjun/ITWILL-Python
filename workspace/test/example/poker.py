class Tree:
    def __init__(self):
        self.nodes = list()
        self.total_value = 0

    def announce(self, value):
        self.total_value += value


class Node:
    def __init__(self, value=0):
        self.__value = value
        self.__observer = None

    def setValue(self, value):
        self.__value += value
        if self.__observer:
            self.__observer.announce(value)
        return self.__value

    def getValue(self):
        return self.__value

    def observe(self, observer):
        self.__observer = observer
        self.__observer.announce(self.__value)


tree = Tree()
nodes = list()
for i in range(7):
    nodes.append(Node(i * 10))
    nodes[i].observe(tree)

print(tree.total_value)