

class TreeNode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children
        print(children)

    def __str__(self, level = 0):
        value = "  " * level + str(self.data) + "\n"
        for child in self.children:
            value += child.__str__(level + 1)
        return value

    def addChild(self,node):
        self.children.append(node)


tree = TreeNode('Drinks',[])
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])
tree.addChild(cold)
tree.addChild(hot)
"""
tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])
cola = TreeNode('Cola',[])
fanta = TreeNode('Fanta',[])

cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
"""
print(tree)
















