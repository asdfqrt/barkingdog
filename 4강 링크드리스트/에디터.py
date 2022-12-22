import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self,data):
        node = Node(data)
        # self.head = node
        self.head = Node("0")
        self.head.next = node
        self.tail = node
        node.prev = self.head

    def append(self, data):

        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
        

    def print_all(self):
        node = self.head
        mes = ""
        while node.next:
            mes += node.data
            node = node.next
        print(mes[1:]+node.data)

    def insert(self, node, data):
        new_node = Node(data)

        if node != self.tail:
            new_node.next = node.next
            new_node.prev = node
            
            node.next.prev = new_node
            node.next = new_node
            
        else:
            self.append(data)

    def delete(self,node):
        if node:
            if node == self.tail:
                node.prev.next = None
                self.tail = node.prev
            # elif node == self.head:
            #     self.head = node.next
            else:
                node.prev.next = node.next
                node.next.prev = node.prev       


x = input()

LL = LinkedList(x[0])
for i in range(1,len(x)):
    LL.append(x[i])
addr = LL.tail


num = int(input())
for i in range(num):
    x = sys.stdin.readline().split()
    if x[0] == 'L':
        if addr != LL.head:
               addr = addr.prev
        
    elif x[0] == 'D':
        if addr != LL.tail:
            addr = addr.next
    elif x[0] == 'B':
        if addr != LL.head:
            LL.delete(addr)
            addr = addr.prev
    else:
        LL.insert(addr,x[1])
        addr = addr.next
 

LL.print_all()
