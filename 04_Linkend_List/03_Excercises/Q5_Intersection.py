

from LinkedList import LinkedList,node


def intersection(llA,llB):
    if llA.tail is not llB.tail:
        return False
    # Find maximun and minimum linked list len
    lenA = len(llA)
    lenB = len(llB)
    shortest = llA if lenA < lenB else llB
    largest = llB if lenA < lenB else llA
    # Create gap between linked list based on its len
    diff = len(largest) - len(shortest)
    node0 = shortest.head
    node1 = largest.head
    for i in range(diff):
        node1 = node1.next
    #
    while node0 is not node1:
        node0 = node0.next
        node1 = node1.next

    return node1

# Helper aditional method
def addSameNode(llA,llB,value):
    newNode = node(value)
    llA.tail.next = newNode
    llA.tail = newNode
    llB.tail.next = newNode
    llB.tail = newNode



llA = LinkedList()
llB = LinkedList()
llA.generate(8,0,10)
llB.generate(5,0,10)

addSameNode(llA,llB,14)
addSameNode(llA,llB,18)

print(llA)
print(llB)
print(intersection(llA,llB))





