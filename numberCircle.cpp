#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    if (a[n - 1] < a[n - 2] + a[n - 3])
    {
        cout << "YES" << endl;
        // Swap the last two elements to ensure the condition holds in the circle
        swap(a[n - 1], a[n - 2]);
        for (int i = 0; i < n; ++i)
        {
            cout << a[i] << " ";
        }
        cout << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}
