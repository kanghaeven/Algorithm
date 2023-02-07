N = int(input())
tree = {} # 빈 딕셔너리 생성

for n in range(N):
    root, left, right = map(str,input().split())
    tree[root] = left, right
# print(tree) # {'A': ('B', 'C'), 'B': ('D', '.'), 'C': ('E', 'F'), 'E': ('.', '.'), 'F': ('.', 'G'), 'D': ('.', '.'), 'G': ('.', '.')}

def preorder(root): # 전위
    if root != '.': 
        print(root, end='') # 루트
        preorder(tree[root][0]) # 왼
        preorder(tree[root][1]) # 오
#  a b d c e f g

def inorder(root): # 중위
    if root != '.':
        inorder(tree[root][0]) # 왼
        print(root, end='') # 루트
        inorder(tree[root][1]) # 오
#  d b a e c f g

def postorder(root): # 후위
    if root != '.':
        postorder(tree[root][0]) # 왼
        postorder(tree[root][1]) # 오
        print(root, end='') # 루트
#   d b e g f c a

preorder('A')
print()
inorder('A')
print()
postorder('A')