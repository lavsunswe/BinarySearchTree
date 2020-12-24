class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def Insert(self, value):
    
    # Check if the entire binary tree is empty or null
        if self is None:
            print("Entire tree is empty")
            return

    # Check if the current node's value is less than 's root node's value. Then in that 
    # case, the current node needs to be inserted as left child in the Binary Search Tree.
    
        if value < self.data:
            print('Node to be inserted', value, 'is lesser than its root', self.data)
            # We are making sure that the left child of root is empty
            if self.left is None:
                self.left = Node(value)
                print ("The node", value, "has been inserted as left child of ", self.data)
                return     

                # There is no space available to the left of the root node  and call insert again to create a new left sub tree 
            else:
                print('There is no space available to left of the root node', self.data)
                self.left.Insert(value)


    # Check if the current node's value is greater than it's root node's value. Then in that case
    #the current node needs to be inserted as right child of the root in the Binary Search Tree

        if value > self.data:
            print('Node to be inserted', value, 'is greater than its root ', self.data)
            # We are making sure that the right child of root is empty

            if self.right is None:
                # Assign the current node as the right subtree of the root
                self.right = Node(value)
                print ("The node", value, "has been inserted as right child of ", self.data)
                return
            else:
                print('There is no space available to right of rooot node', self.data)     
                # Recursively call the Insert function to find a space at the right sub tree
                self.right.Insert(value)

    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),

        if self.right:
            self.right.PrintTree()

    def SearchTree(self, value):
    
    # Check if entire tree is empty (or) the element is not found. Both conditions will be fulfilled by the folloowing check

        if self is None:
            print('Tree is empty or no more node to parse')

    # If data is found at the root node, then return the root node.
        if (self.data == value):
            print('data', value, 'is found')
    
    # If the data to be searched is less than its root, try to find whether it matches its left child by 
    # recursively calling Search function
        if (value < self.data):

            #If there is no left child, then the element to be searched in the tree is not found
            if self.left is None:
                print('the value', value, 'is not found in the tree')
                return
            else:
            # Recursievely called SearchTree to find out if element is there in the left child
                self.left.SearchTree(value)
        
    
    #if the value to be searched is greater than its root, try to find whether it matches its right child by 
    #recursively calling SearchTree function
        elif (value > self.data):
        #if there is no right child, then the element to be searched in the tree is not found
            if self.right is None:
                print('the value', value, 'is not found in the tree')
                return
            else:
        # Recursievely called SearchTree to find out if element is there in the left child
                self.right.SearchTree(value)

            

root = Node(10)
root.Insert(20)
root.Insert(100)
root.Insert(200)
root.Insert(430)

root.PrintTree()

root.SearchTree(100)

