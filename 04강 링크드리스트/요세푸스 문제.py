# n,k = map(int,input().split())
# list = [x for x in range(n)]
# num = 0
# osp = []

# for i in range(n):
#     num = (num + k - 1) % len(list)
#     osp.append(list[num]+1)
#     del list[num]
# print(osp)


# n,k = map(int,input().split())
# a = [x for x in range(n)]
# b = []
# osp = []
# switch = True
# while a+b:
#     for i in range(k):
#         if switch:
#             b.append(a.pop())
#         else:
#             a.append(b.pop()) 
#     osp.append(b.pop())




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class LinkedList:
#     def __init__(self,data):
#         node = Node(data)
#         self.head = node
#         self.tail = node
#         self.head.next = self.tail
#         self.head.prev = self.tail       
#         # self.tail.next = self.head
#         # self.tail.prev = self.head


#     def append(self, data):

#         new_node = Node(data)
#         self.tail.next = new_node
#         new_node.prev = self.tail
#         self.tail = new_node
#         new_node.next = self.head
#         self.head.prev = new_node
        

#     def delete(self,node):
#         if node:
#             node.prev.next = node.next
#             node.next.prev = node.prev       


# n,k = map(int,input().split())

# osp = []

# LL = LinkedList(0)
# for i in range(1,n):
#     LL.append(i)
# addr = LL.head

# for _ in range(n):
#     for _ in range(1,k):
#         addr = addr.next

#     osp.append(addr.data+1)
#     LL.delete(addr)
#     addr = addr.next

# print("<",end="") 
# print(*osp,sep=", ",end=">")




N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]

answer = []
num = 0
while arr:
    num += K-1
    num = num % len(arr)
    answer.append(str(arr.pop(num)))
print("<"+", ".join(answer)+">")
