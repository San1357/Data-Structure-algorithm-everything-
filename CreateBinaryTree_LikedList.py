import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBt = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBt.leftChild = leftChild
newBt.rightChild = rightChild

def preOrderTraversal(rootNode):           #time: O(n) & space: O(n)
    if not rootNode:                         #----->  O(1)
        return
    print(rootNode.data)                     #-----> O(1)
    preOrderTraversal(rootNode.leftChild)    #------> O(n/2)
    preOrderTraversal(rootNode.rightChild)   # -----> O(n/2)

def inOrderTraversal(rootNode):                #time: O(n) , Space: O(n)
    if not rootNode:                           #-----> O(1)
        return
    inOrderTraversal(rootNode.leftChild)       #------> O(n/2)
    print(rootNode.data)                       #------> O(1)
    inOrderTraversal(rootNode.rightChild)      #------> O(n/2)

def postOrderTraversal(rootNode):              #time: O(n) , Space: O(n)
    if not rootNode:                           #-----> O(1)
        return
    postOrderTraversal(rootNode.leftChild)     #------> O(n/2)
    postOrderTraversal(rootNode.rightChild)    #------> O(n/2)
    print(rootNode.data)                       #------> O(1)

def levelOrderTraversal(rootNode):              #time : O(n) , space = O(n) 
    if not rootNode:                            #------> O(1)
        return
    else:
        customQueue = queue.Queue()                         #------> O(1)
        customQueue.enqueue(rootNode)                       #-----> O(1)
        while not(customQueue.isEmpty()):                   #-----> O(n)
            root = customQueue.dequeue()                    #-----> O(1)
            print(root.value.data)                          #-----> O(1)
            if (root.value.leftChild is not None):          #----->O(1)
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):         #------>O(1)
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):                          # time: O(n), space: O(n)
    if not rootNode:                                        # O(1)
        return 
    else:
        customQueue = queue.Queue()                         #O(1)
        customQueue.enqueue(rootNode)                       #O(1)
        while not(customQueue.isEmpty()):                   #O(n)
            root = customQueue.dequeue()                    #O(1)
            if (root.value.data == nodeValue):              #O(1)
                return "Success"
            if (root.value.leftChild is not None):          #O(1)
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):        #O(1)
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

def insertNodeBT(rootNode, newNode):                        #time: O(n), space:O(n)
    if not rootNode:                                        #time: O(1)
        rootNode =  newNode
    else:
        customQueue =  queue.Queue()                        #time: O(1)
        customQueue.enqueue(rootNode)                       #time: O(1)
        while not(customQueue.isEmpty()):                   #O(n)
            root = customQueue.dequeue()                    #O(1)
            if root.value.leftChild is not None:            #O(1)
                customQueue.enqueue(root.value.leftChild)   #O(1)
            else:
                root.value.leftChild = newNode              #O(1)
                return "Successfully Inserted"
            if root.value.rightChild is not None:           #O(1)
                customQueue.enqueue(root.value.rightChild)  #O(1)
            else:
                root.value.rightChild = newNode             #O(1)
                return "Successfully Inserted"

def getDeepestNode(rootNode):                       #time:O(n) , space:O(n)
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


def deleteNodeBT(rootNode, node):           #time: O(n), space:O(n)
    if not rootNode:                        #-----> O(1)
        return
    else:
        customQueue = queue.Queue()                         #-----> O(1)
        customQueue.enqueue(rootNode)                       #-----> O(1)
        while not(customQueue.isEmpty()):                   #-----> O(n)
            root = customQueue.dequeue()                    #-----> O(1)
            if root.value.data == node:                     #-----> O(1)
                dNode = getDeepestNode(rootNode)            #-----> O(1)
                root.value.data = dNode.data                #-----> O(n)
                deleteDeepestNode(rootNode, dNode)          #-----> O(1)
                return "node been successfully deleted"     #-----> O(1)
            if (root.value.leftChild is not None):          #-----> O(1)
                customQueue.enqueue(root.value.leftChild)   #-----> O(1)

            if (root.value.rightChild is not None):         #-----> O(1)
                customQueue.enqueue(root.value.rightChild)  #-----> O(1)
        return "Failed"

def deleteEntireBT(rootNode):           # time: O(1) , space : O(1)
    rootNode.data = None                # O(1)
    rootNode.leftChild = None           # O(1)
    rootNode.rightChild = None          # O(1)
    return "Entire BT deleted"

deleteEntireBT(newBt)
levelOrderTraversal(newBt)









