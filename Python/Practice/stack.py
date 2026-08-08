class Stack:
    def __init__(self):
        self.arrayStack = [None]*10
        self.top = -1
    
    def push(self, element):
        if self.top < len(self.arrayStack) -1 :
            self.top += 1
            self.arrayStack[self.top] = element
        else:
            print("Stack overflow...!")

    def pop(self):
        if self.top == -1 :
            print("Stack Underflow..!")
        poped = self.arrayStack[self.top]
        self.top -= 1
        return poped
    
    def is_empty(self):
        return self.top == -1
        
    
    def clear(self):
        self.top = -1
        return "Stack is Cleared"
    
class TextEditor:
    def __init__(self):
        self.undoStack = Stack()
        self.redoStack = Stack()
        self.document = [None]*50
        self.docIndex = -1

    def makeChange(self, text):
        if self.docIndex < len(self.document) - 1:
            self.docIndex += 1
            self.document[self.docIndex] = text
            self.undoStack.push(text)
        else:
            print("Document is Full")

    def undoAction(self):
        undo = self.undoStack.pop()
        self.redoStack.push(undo)
        self.document[self.docIndex] = undo
    

    def redoAction(self):
        redo = self.redoStack.pop()
        self.undoStack.push(redo)
        self.document[self.docIndex] = redo

    def delete(self):
        self.docIndex = -1
        self.undoStack.clear()
        self.redoStack.clear()

    def checkStatus(self):
        if self.docIndex == -1:
            print("Document is Empty..!")
        print(self.undoStack.is_empty())
        print(self.redoStack.is_empty())
    
    def display(self):
        for i in range(self.docIndex +1 ):
            print(self.document[i])

def main():
    editor = TextEditor()
    while(True):
        print("Welcome to Undo - Redo Stack Operation...")
        print()
        print("***MENU***")
        print("1: Make change ")
        print("2: Undo Action ")
        print("3: Redo Action ")
        print("4: Check if Empty ")
        print("5: Clear")
        print("6: Display")
        print("7: EXIT")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            text =  input("Enter the text..")
            editor.makeChange(text)

        elif choice == 2:
            editor.undoAction()

        elif choice == 3:
            editor.redoAction()

        elif choice == 4:
            editor.checkStatus()
        elif choice == 5:
            editor.delete()
        elif choice == 6:
            editor.display()
        elif choice == 7:
            exit()
        else:
            print("Enter appropriate choice..!")
main()  
