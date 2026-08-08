class Node:
    def __init__(self, value):          
        self.value = value              
        self.left = None                
        self.right = None         

def insert(root, value):
    if root == None:                 
        return Node(value)
    if value < root.value:         
        root.left = insert(root.left, value)
    else:                              
        root.right = insert(root.right, value)
    return root


def find_min(node):
    while node.left is not None:       
        node = node.left
    return node

def delete(root, value):
    if root is None:                    
        return None
    if value < root.value:              
        root.left = delete(root.left, value)
    elif value > root.value:          
        root.right = delete(root.right, value)
    else:                            
        if root.left is None:         
            return root.right
        elif root.right is None:        
            return root.left
        temp = find_min(root.right)    
        root.value = temp.value      
        root.right = delete(root.right, temp.value)  
    return root


def search(root, value):
    if root is None:                    
        return False
    if root.value == value:             
        return True
    elif value < root.value:          
        return search(root.left, value)
    else:                               
        return search(root.right, value)


def inorder(root):
    if root is not None:
        inorder(root.left)             
        print(root.value, end=" ")     
        inorder(root.right)           

root = None                          

while True:
    
    print("\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: ")) 

    if choice == 1:
        val = int(input("Enter value to insert: "))  
        root = insert(root, val)
    elif choice == 2:
        val = int(input("Enter value to delete: ")) 
        root = delete(root, val)
    elif choice == 3:
        val = int(input("Enter value to search: ")) 
        found = search(root, val)
        if found:
            print("Value found in BST")
        else:
            print("Value not found in BST")
    elif choice == 4:
        print("BST in-order: ", end="")
        inorder(root)
        print()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
