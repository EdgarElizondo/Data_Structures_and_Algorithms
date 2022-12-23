
from LinkedList import LinkedList

def removeDup(ll):
    if ll.head is None:
        pass
    else:
        tempNode = ll.head
        tempSet = set([tempNode.value])
        while tempNode.next:
            if tempNode.next.value not in tempSet:
                tempSet.add(tempNode.next.value)
                tempNode = tempNode.next
            else:
                tempNode.next = tempNode.next.next
        return ll

ll = LinkedList()
ll.generate(10,0,8)
print(ll)
ll_unique = removeDup(ll)
print(ll_unique)
