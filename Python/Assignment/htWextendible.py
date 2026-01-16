class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

def main():
    ht = HashTable()
    while True:
        print("\nHash Table Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            key = int(input("Enter key: "))
            value = input("Enter value: ")
            ht.insert(key, value)
            print("Key-value pair inserted successfully!")
        elif choice == "2":
            key = int(input("Enter key to search: "))
            result = ht.search(key)
            if result is not None:
                print(f"Value for key {key}: {result}")
            else:
                print(f"Key {key} not found!")
        elif choice == "3":
            key = int(input("Enter key to delete: "))
            result = ht.delete(key)
            if result:
                print(f"Key {key} deleted successfully!")
            else:
                print(f"Key {key} not found!")
        elif choice == "4":
            print("Hash Table:")
            ht.display()
        elif choice == "5":
            print("Exiting the program!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
