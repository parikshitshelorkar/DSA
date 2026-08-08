#include <iostream>
using namespace std;

class DynamicArray
{
private:
    int *arr;
    int size;

public:
    DynamicArray()
    {
        arr = nullptr;
        size = 0;
    }

    // CREATE (Insert)
    void insert(int value)
    {
        int *temp = new int[size + 1];

        for (int i = 0; i < size; i++)
        {
            temp[i] = arr[i];
        }

        temp[size] = value;

        delete[] arr;
        arr = temp;
        size++;
    }

    // READ (Display)
    void display()
    {
        if (size == 0)
        {
            cout << "Array is Empty\n";
            return;
        }

        cout << "Array Elements : ";

        for (int i = 0; i < size; i++)
        {
            cout << arr[i] << " ";
        }

        cout << endl;
    }

    // UPDATE
    void update(int index, int value)
    {
        if (index < 0 || index >= size)
        {
            cout << "Invalid Index\n";
            return;
        }

        arr[index] = value;
        cout << "Updated Successfully\n";
    }

    // DELETE
    void remove(int index)
    {
        if (index < 0 || index >= size)
        {
            cout << "Invalid Index\n";
            return;
        }

        int *temp = new int[size - 1];

        int j = 0;

        for (int i = 0; i < size; i++)
        {
            if (i != index)
            {
                temp[j++] = arr[i];
            }
        }

        delete[] arr;
        arr = temp;
        size--;

        cout << "Deleted Successfully\n";
    }

    ~DynamicArray()
    {
        delete[] arr;
    }
};

int main()
{
    DynamicArray obj;

    obj.insert(10);
    obj.insert(20);
    obj.insert(30);

    obj.display();

    obj.update(1, 50);

    obj.display();

    obj.remove(0);

    obj.display();

    return 0;
}