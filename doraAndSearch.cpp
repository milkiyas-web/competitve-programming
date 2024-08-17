#include <iostream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#define ll long long int
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin >> T;
    while (T--)
    {
        ll n;
        cin >> n;
        ll arr[n];
        set<ll> s;
        for (ll i = 0; i < n; i++)
        {
            cin >> arr[i];
            s.insert(arr[i]);
        }
        ll l = 0, r = n - 1;
        while (r - l > 1)
        {
            ll mn = *s.begin(), mx = *s.rbegin();
            if (arr[l] != mn && arr[l] != mx && arr[r] != mn && arr[r] != mx)
            {
                break;
            }
            if (arr[l] == mn || arr[l] == mx)
            {
                l++;
                s.erase(arr[l - 1]);
            }
            if (arr[r] == mn || arr[r] == mx)
            {
                r--;
                s.erase(arr[r + 1]);
            }
        }
        if (r - l > 1)
        {
            cout << l + 1 << ' ' << r + 1 << '\n';
        }
        else
        {
            cout << "-1\n";
        }
    }
    return 0;
}