class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)
        
    def print_tree(self, level=0):
        print(" " * (level * 4) + f"→ {self.value}")
        for child in self.children:
            child.print_tree(level + 1)
            
root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

root.add_child(node_b)  # B ist Kind von A
root.add_child(node_c)  # C ist Kind von A
node_b.add_child(node_d)  # D ist Kind von B
node_b.add_child(node_e)  # E ist Kind von B
node_c.add_child(node_f)  # F ist Kind von C

root.print_tree()