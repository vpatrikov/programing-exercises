#include <iostream>
#include <string>

using namespace std;

int main ()
{
    int a, count = 0;

    bool tooBig = false;

    cout << "\nEnter a number: ";
    cin >> a;

    if (a >= 2147483647)
    {
        tooBig = true;
    }
    
    int sum = 0;

    string str = to_string(a);

    for (size_t i = 0; i < str.size(); i++)
    {   
        sum += str[i] - '0';
        count++;
    }

    if (a < 0)
    {
        count--;
    }
    
    if (!tooBig)
    {
        cout << "\nNumber of digits:" << count << endl;
        cout << "Sum of digits:" << sum << endl;
    }
    else
    {
        cout << "Number is too big!" << endl;
    }
    
    
    return 0;
}