class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def get(self):
        return self.data
    
    def set(self, value):
        self.data = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
       

    def SetRoot(self,value):
        self.root = Node(value)
        return self.root
    
    

    def InsertNode(self, rootnode, value):
       
        #We are creating node at the root
        if self.root is None:
            self.SetRoot(value)

        #This else part covers insert of child nodes below root
        else:

             # Check if the current node's value is less than root node's value. Then in that 
             # case, the current node needs to be inserted as left child of the root node.
            if value < rootnode.data:
                print('Node to be inserted', value, 'is lesser than its root', rootnode.data)
                # We are making sure that the left child of root is empty
                if rootnode.left is None:
                    rootnode.left = Node(value)
                    print("The node", value, "has been inserted as left child of ", rootnode.data)
                    return
                else:
                    print('There is no space available to left of the root node', rootnode.data)
                    self.InsertNode(rootnode.left,value)


            # Check if the current node's value is greater than root node's value. Then in that 
            # case, the current node needs to be inserted as right child of the root node

            
            if value > rootnode.data:
                print('Node to be inserted', value, 'is greater than its root', rootnode.data)
                 # We are making sure that the right child of root is empty
                if rootnode.right is None:
                    rootnode.right = Node(value)
                    print("The node", value, "has been inserted as left child of ", rootnode.data)
                    return
                else:
                     print('There is no space available to right of the root node', rootnode.data)
                     self.InsertNode(rootnode.right,value)


#The following method helps to print the tree
    def PrintTree(self, rootnode):
        if(rootnode.left):
            self.PrintTree(rootnode.left)
        print(rootnode.data),
        if(rootnode.right):
            self.PrintTree(rootnode.right)

#The following function checks whether the current node has one child or not

    def IsOneChild(self, currentnode):
        if currentnode is not None:
            if (currentnode.left is not None ) and (currentnode.right is None):
                self.SingleChild = True
                self.ChildLink = "left"
                print('The current node',currentnode.data,  'has only one child-left',currentnode.left.data )
                
               
            elif (currentnode.left is None) and (currentnode.right is not None ):
                self.SingleChild = True
                self.ChildLink = "right"
                print('The current node',currentnode.data,  'has only one child-right',currentnode.right.data )
            
            else:
                self.SingleChild = False
            


 #The following function checks whether the current node has two children or not
    def IsTwoChild(self, currentnode):

        if currentnode.left is not None and currentnode.right is not None:
            print('the current node has two children')
            self.TwoChild = True
        else:
            print('the current node does not have two children')
            self.TwoChild = False
        return           

   

    def inOrderSuccessor(self,root, n): 
        
        # Step 1 of the above algorithm 
        if n.right is not None: 
            return self.minValue(n.right) 
    
        # Step 2 of the above algorithm 
        succ=Node(None) 
        
        
        while( root): 
            if(root.data<n.data): 
                root=root.right 
            elif(root.data>n.data): 
                succ=root 
                root=root.left 
            else: 
                break
        return succ 
        
    def minValue(self,node): 
        current = node 
    
        # loop down to find the leftmost leaf 
        while(current is not None): 
            if current.left is None: 
                break
            current = current.left 
    
        return current 


    def Search(self,value, rootnode):
        if (rootnode is None):
            print('The entire binary search tree is empty or node not found in binary search tree')
            return 
        else:
            #if the node to be searched is available at the root, then return the root
            if rootnode.data == value:
                print('The node ', value, 'is found in the binary tree')
                self.SearchResult = rootnode
                return 
           
            #if node to be searched is having value lesser than the root node traverse recursively
            #to the left child until we fine one.
            if value < rootnode.data:
                self.Search(value, rootnode.left)

            #if node to be searched is having value greater than the root node traverse recursively
            #to the right child until we fine one.
            if value > rootnode.data:
                self.Search(value, rootnode.right)

    def isLeafNode(self, x):

        if x.left == None and x.right == None:
            print('The node ', x.data , 'is the leaf node')
            return True
        else:
            return False


    def getParent(self, currentnode, rootnode):
        if rootnode.left is not None:
            if (rootnode.left.data == currentnode.data):
                print("The node", currentnode.data, "is the left child of the parent node", rootnode.data)
                self.ParentNode = rootnode
                self.LinkInParent = "left"
                return

        if rootnode.right is not None:
            if (rootnode.right.data == currentnode.data):
                print("The node", currentnode.data, "is the right child of the parent node", rootnode.data)
                self.ParentNode = rootnode
                self.LinkInParent = "right"
                return

        if rootnode.left is not None:
            if (currentnode.data < rootnode.data):
                self.getParent(currentnode, rootnode.left)

        if rootnode.right is not None:
            if (currentnode.data > rootnode.data):
                self.getParent(currentnode, rootnode.right)

           

    def DeleteNode(self, value, rootnode):
        # Call the search function to see if the Node is available in the tree
        self.Search(value, rootnode)
        x = self.SearchResult
        
        if x is None:
            print('Element' , value, ' not found')
            return None

        ret = x


        #Check if the node to be deleted is a leaf node
        if (self.isLeafNode(x)):
            self.getParent(x, rootnode)

            
            print('parent node',self.ParentNode.data)
            parent = self.ParentNode
            # check if the node to be deleted is the left child of its root, then break off its left link 
            # in the parent
            if self.LinkInParent == "left":
                parent.left=None
                
            #check if the node to be deleted is the right child of its root, then break of its right link
            if self.LinkInParent == "right":
                parent.right=None
            return ret

        #check if x is a node with only one child
        self.IsOneChild(x)

        if self.SingleChild:
            # Got to parent of x and replace it's link in the parent node with the child node of x
            self.getParent(x, rootnode)
            print('parent node',self.ParentNode.data)

            parent = self.ParentNode

            #if x is the left child of its parent replace its link with the available single child of x

            if self.LinkInParent == "left":
                print('inside left path')
                
                #replace if single left child is only available
                if self.SingleChild == True and self.ChildLink == "left":
                    parent.left = x.left
                    print('replace parent with left')
                    return ret
                    
                #replace if single right child is only available
                if self.SingleChild == True and self.ChildLink == "right":
                    parent.left = x.right
                    print('replace parent with right')
                    return ret

            
        ##if x is the right child of its parent replace its link with the available single child of x

            if self.LinkInParent == "right":
                print('inside right path')
                if self.SingleChild == True and self.ChildLink == "left":
                    parent.right = x.left
                    return ret

                #replace if single right child is only available
                if self.SingleChild == True and self.ChildLink == "right":
                    parent.right = x.right
                    return ret
                


        # if the node x has two children replace x with inorder successor

        self.IsTwoChild(x)

        if self.TwoChild:
           
            self.getParent(x, rootnode)

            print('parent node',self.ParentNode.data)
            parent = self.ParentNode
            i = self.inOrderSuccessor(rootnode, x)
            print('InOrder successor of',x.data, 'is', i.data)
           
            self.getParent(i,rootnode)
            parenti = self.ParentNode

        #Check if x is the left child of parent

            if parent.left.data == x.data:

                
                #Replace i as left subchild of p
                parent.left = i

                #Replace the children of x to childen of i
                i.left = x.left
                i.right = x.right

                if parenti.left == i:
                    parenti.left=None

                if parenti.right == i:
                    parenti.right==None

                return

        #Check if x is the right sub child of parent

            if parent.right.data == x.data:
                #Replace i as the right subchild of p
                parent.right = i

                #Replace the children of x to be children of i
                i.left = x.left


                i.right = x.right

                if parenti.left == i:
                    parenti.left=None

                if parenti.right == i:
                    parenti.right==None
                
                return ret





tree = BinarySearchTree()
rootnode = tree.SetRoot(20)

tree.InsertNode(rootnode, 8)
tree.InsertNode(rootnode, 4)
tree.InsertNode(rootnode, 12)
        
tree.InsertNode(rootnode, 10)
tree.InsertNode(rootnode, 14)
tree.InsertNode(rootnode, 22)
tree.InsertNode(rootnode, 21)
tree.InsertNode(rootnode, 30)
tree.InsertNode(rootnode, 29)
tree.InsertNode(rootnode, 45)
    
tree.PrintTree(rootnode)

tree.DeleteNode(30,rootnode)

tree.PrintTree(rootnode)


