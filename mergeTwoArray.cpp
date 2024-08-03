#include <vector>
#include <iostream>
#include <algorithm>
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
    int i = 0, j = 0, k = 0;
    vector<int> c(n + m);
    while (i < n || j < m)
    {
        if (j == m || i < n && a[i] < b[j])
        {
            c[k] = a[i];
            i++;
            k++;
        }
        else
        {
            c[k] = b[j];
            j++;
            k++;
        }
    }
    for (int i = 0; i < n + m; i++)
    {
        cout << c[i] << " ";
    }
}