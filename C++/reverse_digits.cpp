#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a;
    char temp;
    cout << "Enter a number: ";
    cin >> a;

    for (size_t i = (a[0] == '-') ? 1 : 0, j = a.size() - 1; i < j; i++, j--)
    {
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    cout << a << endl;

    return 0;
}
