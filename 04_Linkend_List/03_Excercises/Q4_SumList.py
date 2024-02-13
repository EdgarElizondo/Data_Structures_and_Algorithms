
from LinkedList import LinkedList

def sumList(llA,llB):
    carry = 0
    nA = llA.head
    nB = llB.head
    ll = LinkedList()

    while nA or nB or carry > 0:
        result = carry
        if nA:
            result += nA.value
            nA = nA.next
        if nB:
            result += nB.value
            nB = nB.next
        ll.add(int(result % 10))
        carry = result // 10

    return ll
# Creacion de Linked List
ll0 = LinkedList()
ll1 = LinkedList()
# Se generan valores aleatorios para las listas
ll0.generate(5,0,9)
ll1.generate(5,0,9)
print(ll0)
print(ll1)
llsum = sumList(ll0,ll1)
print(llsum)
