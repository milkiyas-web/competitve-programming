#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);

    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < m; ++i)
        cin >> b[i];

    int i = 0, j = 0;
    long long count = 0; // Use long long to prevent overflow

    while (i < n && j < m)
    {
        if (a[i] == b[j])
        {
            // Count occurrences of a[i] in a
            int countA = 0, countB = 0;
            int value = a[i];
            while (i < n && a[i] == value)
            {
                countA++;
                i++;
            }
            // Count occurrences of b[j] in b
            while (j < m && b[j] == value)
            {
                countB++;
                j++;
            }
            // Multiply the counts and add to the total count
            count += (long long)countA * countB;
        }
        else if (a[i] < b[j])
        {
            i++;
        }
        else
        {
            j++;
        }
    }

    cout << count << endl;
    return 0;
}
