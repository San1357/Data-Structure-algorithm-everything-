class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " "* level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

    
root = TreeNode("Furniture",[])
child1 = TreeNode("Plastic",[])
child2 = TreeNode("Wooden",[])
child3 = TreeNode("Iron&Steel",[])
root.addChild(child1)
root.addChild(child2)
root.addChild(child3)
p_chair = TreeNode("Plastic_Chair",[])
p_peeda = TreeNode("peeda",[])
p_Table = TreeNode("Plastic_Table",[])
w_Table = TreeNode("WoodenTable",[])
w_chair = TreeNode("WoodenChair",[])
I_door = TreeNode("IronDoor",[])
I_rod = TreeNode("IronRod",[])
child1.addChild(p_Table)
child1.addChild(p_peeda)
child1.addChild(p_chair)
child2.addChild(w_chair)
child2.addChild(w_Table)
child3.addChild(I_door)
child3.addChild(I_rod)
print(root)
