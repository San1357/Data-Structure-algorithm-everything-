import LinkedList as l 
def helperFunction(myLinkedList, current,previous):
    #basecase
    if current.next is None:
        myLinkedList.head = current
        current.next = previous
        return

    next = current.next
    current.next = previous

    helperFunction(myLinkedList,next, current)

def reverse(myLinkedList):
    if myLinkedList.head is None:
        return
    
    helperFunction(myLinkedList, myLinkedList.head, None)

myLinkedList = l.LinkedList()
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(7)
myLinkedList.append(11)
print("Original Linked List")
myLinkedList.printList()
reverse(myLinkedList)
print("\nReversed Linked List")
myLinkedList.printList()
