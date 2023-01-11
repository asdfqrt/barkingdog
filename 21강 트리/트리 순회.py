import sys
input= sys.stdin.readline
n= int(input())
lc = [0]*(n+1)
rc = [0]*(n+1)

for _ in range(n):
    c,l,r = map(lambda x:ord(x)-64, input().split())
    if l!= -18 : lc[c] = l
    if r!= -18 : rc[c] = r

def preord(cur):
    print(chr(cur+64),end="")
    if lc[cur]!=0: preord(lc[cur])
    if rc[cur]!=0: preord(rc[cur])


def inord(cur):
    if lc[cur]!=0: inord(lc[cur])
    print(chr(cur+64),end="")    
    if rc[cur]!=0: inord(rc[cur])


def postord(cur):
    if lc[cur]!=0: postord(lc[cur])    
    if rc[cur]!=0: postord(rc[cur])
    print(chr(cur+64),end="")

preord(1)
print()
inord(1)
print()
postord(1)


###################
n = int(input())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
    
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')  
        inorder(tree[root][1])  

def postorder(root):
    if root != '.':
        postorder(tree[root][0]) 
        postorder(tree[root][1])  
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

#############################