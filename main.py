from menu.models import FileSystemNode

n1 = FileSystemNode("Maktab folder")
n2 = FileSystemNode("HW1", parent=n1)

n3 = FileSystemNode("Final project", parent=n1)
n4 = FileSystemNode("main.py",parent=n2)

n1.print_tree()
