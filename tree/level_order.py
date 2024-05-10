class node:
    def __init__(s,data):
        s.data=data
        s.left=None
        s.right=None
class tree:
    def height(s,root):
        if not root:
            return 0
        l=s.height(root.left)
        r=s.height(root.right)
        return max(l,r)+1
    def current_level(s,root,level):
        if not root:
            return 
        if level==1:
            print(root.data)
        elif level > 1:
            s.current_level(root.left,level-1)
            s.current_level(root.right,level-1)
    def level(s,root):
        h=s.height(root)
        for i in range(1,h+1):
            s.current_level(root,i)
            
    

root=node(1)
root.left=node(2)
root.right=node(3)
root.right.right=node(6)
root.right.right.left=node(9)
root.right.right.right=node(10)
root.left.left=node(4)
root.left.left.left=node(7)
root.left.left.right=node(8)
root.left.right=node(5)
l=tree()
print("output is :")
l.level(root)



'''
input tree:
       1
      / \
     2   3
    / \   \
   4   5   6
  / \  / \
 7  8 9  10
'''
'''
output is :
1
2
3
4
5
6
7
8
9
10
'''

