from abc import ABC, abstractmethod

class Node(ABC):
    # parent: Node
    children: list

    @abstractmethod
    def __init__(self, parent = None) -> None:
        assert parent is None or isinstance(parent, Node)
        self.children = []
        self.parent = parent    

        if parent:
            self.parent.children.append(self)

    def print_tree(self, prefix='', last=False):
        pointer = '\b\u2514' if last else ('\b\u251C' if prefix else '')
        print(prefix+pointer, repr(self))
        
        for i, child in enumerate(self.children):
            last = i == len(self.children) - 1
            if last:
                child.print_tree(prefix+'\t ', last=True)
            else:
                child.print_tree(prefix+'\t|')

            
    def remove(self):
        if self.parent:
            self.parent.children.remove(self)












