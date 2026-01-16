class StudentNode:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        new_node = StudentNode(roll_no, name, marks)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_student(self, roll_no):
        current = self.head
        if current and current.roll_no == roll_no:
            self.head = current.next
            return
        prev = None
        while current and current.roll_no != roll_no:
            prev = current
            current = current.next
        if not current:
            print("Record not found")
            return
        prev.next = current.next

    def update_student(self, roll_no, name=None, marks=None):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                if name:
                    current.name = name
                if marks is not None:
                    current.marks = marks
                return
            current = current.next
        print("Record not found")

    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print(f"Roll No: {current.roll_no}, Name: {current.name}, Marks: {current.marks}")
                return
            current = current.next
        print("Record not found")

    def display_students(self, sort_by="roll_no", ascending=True):
        students = []
        current = self.head
        while current:
            students.append((current.roll_no, current.name, current.marks))
            current = current.next
        if not students: # if students == none:
            print("No records to display")
            return
        if sort_by == "roll_no":
            students.sort(key=lambda x: x[0], reverse=not ascending)
        elif sort_by == "marks":
            students.sort(key=lambda x: x[2], reverse=not ascending)
        for s in students:
            print(f"Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

s = StudentLinkedList()

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Display Sorted by Marks")
    print("7. Reverse List")
    print("8. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        s.add_student(roll_no, name, marks)
    elif ch == 2:
        roll_no = int(input("Enter Roll No to delete: "))
        s.delete_student(roll_no)
    elif ch == 3:
        roll_no = int(input("Enter Roll No to update: "))
        name = input("Enter new Name (press Enter to skip): ")
        marks_input = input("Enter new Marks (press Enter to skip): ")
        marks = float(marks_input) if marks_input else None
        s.update_student(roll_no, name if name else None, marks)
    elif ch == 4:
        roll_no = int(input("Enter Roll No to search: "))
        s.search_student(roll_no)
    elif ch == 5:
        s.display_students()
    elif ch == 6:
        s.display_students(sort_by="marks", ascending=True)
    elif ch == 7:
        s.reverse()
        print("List reversed")
    elif ch == 8:
        break
    else:
        print("Invalid choice")
