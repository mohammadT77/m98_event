from menu.models import Node

n1 = Node('n1')
n2 = Node('n2', parent=n1)

n3 = Node('n3',parent=n1)
n4 = Node('n4', parent=n2)
nodes = [n1,n2,n3,n4]

children = lambda node: filter(lambda n: n.parent == node, nodes)
is_leaf = lambda node: not list(children(node))  # [] -> True , [n1] -> False
print(is_leaf(n1))