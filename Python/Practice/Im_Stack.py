#initilize
class Stack:
    def __init__(self):
        self.stack = [None]*100
        self.pointer = -1

    def push(self, stack):
        if self.pointer == len(self.stack)-1:
            print("Stack is full!!")
        else:
            self.pointer +=1
            self.stack[self.pointer]=stack
            return "Push operation Successfull!"

    def pop(self):
        if (self.pointer == -1):
            print("Stack Underflow: ")
            return None
        else:
            stack = self.stack[self.pointer]
            self.pointer -= 1
            return stack
        
    def peek(self):
        if self.pointer == -1:
            print("Stack is empty")
            return None
        else:
            return self.stack[self.pointer]
        
    def isEmpty(self):
        if self.pointer == -1:
            print("Stack is Empty!")
        else:
            print("Not Empty!")

    def clear(self):
        self.pointer = -1
        

class TextEditor:
    def __init__(self):
        self.undostack = Stack()
        self.redostack = Stack()
        self.document = [""]*100
        self.docIndex = -1

    def makeChange(self, text):
        if self.docIndex < len(self.document)-1 :
            self.docIndex += 1
            self.document[self.docIndex] = text
            self.undostack.push(text)
            self.redostack.clear()
            print("Change Added!")
        else:
            print("No space to add change!")

    def undoaction(self):
        if self.undostack.isEmpty():
            print("Nothing to undo!")
        else:
            change = self.undostack.pop()
            self.document[self.docIndex] = ""
            self.redostack.push(change)
            self.docIndex -= 1
            print("undo performed!")

    def redoaction(self):
        if self.redostack.isEmpty():
            print("Nothing to redo!")
        else:
            change = self.redostack.pop()
            if self.docIndex < len(self.document)-1:
                self.docIndex +=1
                self.document[self.docIndex] = change
                self.undostack.push(change)
                print("Redo performed!")
    

    def displayDoc(self):
        print("\nCurrent State of the Document..")
        if self.docIndex == -1:
            print("The document is Empty.!")
        else:
            for i in range (0, self.docIndex):
                print(self.document[i])
            print()
            
def main():
    editor = TextEditor()
    while True:
        print("******MENU******")
        print("Select desired option..")
        print("1. Make Change ")
        print("2. Undo")
        print("3. Redo")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice here!: "))
        

        if choice == 1:
            text = input("Enter the text to add..: ")
            editor.makeChange(text)
            print()
        elif choice == 2:
            editor.undoaction()
            print()

        elif choice == 3:
            editor.redoaction()
            print()


        elif choice == 4:
            editor.displayDoc()
            print()

        elif choice == 5:
            print("Exiting..")
            break
        else:
            print("Invalid choice!!; Try Again")
            print()


main()