
from LinkedList import LinkedList

def Partition(ll,value):
    tempNode = ll.head
    ll.tail = ll.head
    while tempNode:
        nextNode = tempNode.next
        tempNode.next = None
        if tempNode.value < value:
            tempNode.next = ll.head
            ll.head = tempNode
        else:
            ll.tail.next = tempNode
            ll.tail = tempNode
        tempNode = nextNode
    if ll.tail.next is not None:
        ll.tail.next = None

ll = LinkedList()
ll.generate(10,0,15)
print(ll)
Partition(ll,8)
print(ll)
