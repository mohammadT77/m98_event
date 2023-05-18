
class Node:
    # parent: Node
    # children: list[Node]

    def __init__(self, name, parent = None) -> None:
        self.parent = parent
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
    








