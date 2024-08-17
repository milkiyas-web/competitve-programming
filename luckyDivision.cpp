#include <iostream>
#include <vector>

using namespace std;

// Function to check if a number is lucky (contains only the digits 4 and 7)
bool isLucky(int num)
{
    while (num > 0)
    {
        int digit = num % 10;
        if (digit != 4 && digit != 7)
        {
            return false;
        }
        num /= 10;
    }
    return true;
}

int main()
{
    int n;
    cin >> n;

    vector<int> luckyNumbers;

    // Generate all lucky numbers up to 1000
    for (int i = 1; i <= 1000; i++)
    {
        if (isLucky(i))
        {
            luckyNumbers.push_back(i);
        }
    }

    // Check if n is divisible by any lucky number
    for (int lucky : luckyNumbers)
    {
        if (n % lucky == 0)
        {
            cout << "YES" << endl;
            return 0;
        }
    }

    cout << "NO" << endl;
    return 0;
}
