#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    cout << "Enter an integer: ";
    int number;
    string symbols;
    cin >> number;

    vector<int> digitCounts(10, 0);
    while (number != 0) {
        int digit = abs(number % 10);
        digitCounts[digit]++;
        number /= 10;
    }

    cout << "Digit Histogram:" << endl;
    for (int i = 0; i < 10; ++i) {
        symbols.erase();
        cout << i << ": ";
        for (int j = 0; j < digitCounts[i]; ++j) {
            symbols = symbols + '*';
        }
        cout << symbols.size();
        cout << endl;
    }

    return 0;
}