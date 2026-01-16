class Stack:
    def __init__(self):
        self.items = [None] * 100
        self.top = -1

    def push(self, item):
        if self.top < len(self.items) - 1:
            self.top += 1
            self.items[self.top] = item
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        item = self.items[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            return None
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def clear(self):
        self.top = -1


class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.document = [""] * 100
        self.doc_index = -1

    def make_change(self, text):
        if self.doc_index < len(self.document) - 1:
            self.doc_index += 1
            self.document[self.doc_index] = text
            self.undo_stack.push(text)
            self.redo_stack.clear()
            print("Change added.")
        else:
            print("Document is full.")

    def undo_action(self):
        if self.undo_stack.is_empty():
            print("Nothing to undo.")
        else:
            change = self.undo_stack.pop()
            self.redo_stack.push(change)
            self.document[self.doc_index] = ""
            self.doc_index -= 1
            print("Undo performed.")

    def redo_action(self):
        if self.redo_stack.is_empty():
            print("Nothing to redo.")
        else:
            change = self.redo_stack.pop()
            if self.doc_index < len(self.document) - 1:
                self.doc_index += 1
                self.document[self.doc_index] = change
                self.undo_stack.push(change)
                print("Redo performed.")
            else:
                print("Cannot redo, document is full.")

    def display_document(self):
        print("\nCurrent Document State:")
        if self.doc_index == -1:
            print("[Empty Document]")
        else:
            for i in range(self.doc_index + 1):
                print(self.document[i])
        print()


def main():
    editor = TextEditor()
    while True:
        print("Options:")
        print("1. Make a Change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display Document")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            text = input("Enter the text to add: ")
            editor.make_change(text)
        elif choice == '2':
            editor.undo_action()
        elif choice == '3':
            editor.redo_action()
        elif choice == '4':
            editor.display_document()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


main()
