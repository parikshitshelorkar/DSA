class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Each slot will store (key, value) tuple

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index] != "DELETED":
            # If same key found, update its value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                print(f"Key {key} updated with new value '{value}'")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash table is full")
                return

        self.table[index] = (key, value)
        print(f"Inserted ({key}, '{value}') at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != "DELETED" and self.table[index][0] == key:
                print(f"Key {key} found at index {index} with value '{self.table[index][1]}'")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print(f"Key {key} not found")

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != "DELETED" and self.table[index][0] == key:
                self.table[index] = "DELETED"
                print(f"Key {key} deleted")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print(f"Key {key} not found")

    def display(self):
        print("\nHash Table Contents:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

def main():
    size = int(input("Enter size of hash table: "))
    ht = HashTable(size)

    while True:
        print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key (integer): "))
            value = input("Enter value (string): ")
            ht.insert(key, value)
        elif choice == 2:
            key = int(input("Enter key to search: "))
            ht.search(key)
        elif choice == 3:
            key = int(input("Enter key to delete: "))
            ht.delete(key)
        elif choice == 4:
            ht.display()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
