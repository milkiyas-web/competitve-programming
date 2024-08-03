#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++)
    {
        cin >> b[i];
    }
    int i = 0, j = 0;
    vector<int> res(m);
    while (i < n || j < m)
    {
        if (j == m || (i < n && a[i] < b[j]))
        {
            i++;
        }
        else
        {
            res[j] = i;
            j++;
        }
    }
    for (int x : res)
    {
        cout << x << " ";
    }
}