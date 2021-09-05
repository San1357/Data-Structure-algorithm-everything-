class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self,level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks",[])
cold = TreeNode("Cold",[])
hot = TreeNode("hot",[])
tea = TreeNode("Tea",[])
Coffee = TreeNode("Coffee",[])
Cola = TreeNode("Cola",[])
Fanta = TreeNode("Fanta",[])
cold.addChild(Cola)
cold.addChild(Fanta)
hot.addChild(tea)
hot.addChild(Coffee)
tree.addChild(cold)
tree.addChild(hot)
print(tree)

