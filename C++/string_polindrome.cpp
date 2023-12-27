#include <iostream>
#include <cctype>
#include <cstring>

using namespace std;

int main(void)
{
    char n[3];
    int size;

    cout << "Enter size of string: " << endl;

    while (true)
    {
        cin >> n;
        cin.ignore();

        if (strlen(n) == 1 && isdigit(n[0]) && n[0] >= '1' && n[0] <= '9')
        {
            size = n[0] - '0';
            break;
        }
        else if (strlen(n) == 2)
        {
            if (isdigit(n[0]) && isdigit(n[1]) && n[2] == '\0')
            {
                size = (n[0] - '0') * 10 + (n[1] - '0');

                if (size <= 19)
                {
                    break;
                }
                else
                {
                    cout << "Invalid input. Please enter a valid number (1-19)." << endl;
                }
            }
            else
            {
                cout << "Invalid input. Please enter a valid number." << endl;
            }
        }
        else
        {
            cout << "Invalid input. Please enter a valid number." << endl;
        }
    }

    char *input = new char[size + 1];
    char *rev_input = new char[size + 1];

    cout << "Enter string: ";
    cin.getline(input, size + 1);

    if (strlen(input) > size)
    {
        cout << "String is too long!" << endl;
        return 1;
    }

    int len = strlen(input);

    for (int i = len - 1, j = 0; i >= 0; i--, j++)
    {
        rev_input[j] = input[i];
    }

    rev_input[len] = '\0';

    cout << "Original string: " << input << endl;
    cout << "Reversed string: " << rev_input << endl;

    if (strcmp(input, rev_input) == 0)
    {
        cout << "The given string is a polindrome." << endl;
    }else{
        cout << "The given string is not a polindrome." << endl;
    }

    return 0;
}
