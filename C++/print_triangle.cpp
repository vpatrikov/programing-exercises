#include <iostream>
using namespace std;

int main ()
{
    int size;

    cout << "Enter the size of your triangle: ";
    cin >> size;

    for (size_t i = 1; i < size + 1; i++)
    {
        for (size_t j = 0; j < i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    
}