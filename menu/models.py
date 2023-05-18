from abc import ABC, abstractmethod

from .utils import get_input


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


    def walk_children(self):
        yield (self, self.children)  # (HW1, [main.py])
        
        for child in self.children:
            yield from child.walk_children()


class MenuNode(Node):
    
    def __init__(self, name, description="", parent=None) -> None:
        assert parent is None or isinstance(parent, MenuNode)
        super().__init__(parent)
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.name}'>"

    def __str__(self) -> str:
        return self.name + (": " + self.description if self.description else "")


    @abstractmethod
    def __call__(self):
        pass


class ListMenu(MenuNode):
    
    def user_choice_type(self, value: str):
        value = int(value)
        if value == 0:
            return None
        return self.children[value-1]

    def __call__(self):
        if self.parent:
            print(self.parent.name, end=' > ')
        print(self.name)

        if self.description:  # Reserve for events and enjoy!!!!
            print(self.description)            

        print('\nItem:')
        for i, child in enumerate(self.children):
            print(f"  {i+1}.", child)

        print()
        user_choice = get_input("Select (0 to Return): ", target_type=self.user_choice_type)
        
        print('\n------------------------')
        (user_choice or self.parent or exit)()
        # if user_choice:
        #     user_choice()
        # else:
        #     if self.parent:
        #         self.parent()
        #     else:
        #         exit()




class PageMenu(MenuNode):
    
    def __init__(self, action, name=None, description="", parent=None) -> None:
        assert callable(action)
        assert parent
        
        self.action = action
        name = name or action.__name__
        
        super().__init__(name, description, parent)
        

    def __call__(self):
        # print header
        if self.parent:
            print(self.parent.name, end=' > ')
        print(self.name)
        
        # run action function
        self.action()

        print('\n------------------------\n')
        
        # go back parent
        self.parent()










