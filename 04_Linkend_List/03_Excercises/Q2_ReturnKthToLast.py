
from LinkedList import LinkedList

def nthToLast(ll,n):
    pointer0 = ll.head
    pointer1 = ll.head
    # Acomplish the distant
    for i in range(n):
        if pointer1 is None:
            return None
        pointer1  = pointer1.next
    # Find the location
    while pointer1:
        pointer0 = pointer0.next
        pointer1 = pointer1.next
    return pointer0

ll = LinkedList()
ll.generate(10,0,49)
print(ll)
print(nthToLast(ll,3))