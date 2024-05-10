class node:
    def __init__(s,data):
        s.data=data
        s.left=None
        s.right=None
class tree:  
    def leftnum(s,root):
        print(root.data)
        if root.left.left==None:
            return
        s.leftnum(root.left)    
    def child(s,root):
        if root is None:
            return
        if root.left==root.right==None:
            print(root.data)
        if root.left is not None:
            s.child(root.left)
        if root.right is not None:
            s.child(root.right)      
    def rightt(self, root,is_root=True):
        if root is None:
            return
        if root.right.right is not None:
            self.rightt(root.right,is_root=False)
        if not is_root:
            print(root.data)                  
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
l.leftnum(root)
l.child(root)
l.rightt(root)




'''

input is :
    
        1
       / \
      2   3
     / \   \
    4   5   6
   / \     / \
  7   8   9   10


output: 1,2,4,7,8,5,9,10,6,3
'''
