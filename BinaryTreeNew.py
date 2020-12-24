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

#The following function is for seearching the binary tree

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
        

    def DeleteNode(self, value, rootnode):
        # Call the search function to see if the Node is available in the tree
        self.Search(value, rootnode)
        x = self.SearchResult
      

        if x is None:
            print('Element' , value, ' not found')
            return None

        ret = x

        # Check if the node to be deleted is a root node
        if (self.isLeafNode(x)):



        
        # if x is the leaf node, go to the parent of x and break of x from it




tree = BinarySearchTree()
rootnode = tree.SetRoot(10)

tree.InsertNode(rootnode, 9)
tree.InsertNode(rootnode, 7)
tree.InsertNode(rootnode, 5)
        
tree.InsertNode(rootnode, 30)
tree.InsertNode(rootnode, 50)
tree.InsertNode(rootnode, 100)
    
tree.PrintTree(rootnode)

tree.DeleteNode(100,rootnode)


