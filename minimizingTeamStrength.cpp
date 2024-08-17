#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void solve()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        map<int, int> freq;

        for (int i = 0; i < n; ++i)
        {
            cin >> a[i];
            freq[a[i]]++;
        }

        vector<int> counts;
        for (auto &p : freq)
        {
            counts.push_back(p.second);
        }

        sort(counts.rbegin(), counts.rend());

        vector<int> result(n, 0);
        int total_distinct = counts.size();

        for (int k = 1; k <= n; ++k)
        {
            int sum_strength = 0;
            for (int i = 0; i < total_distinct && i < k; ++i)
            {
                sum_strength += 1;
            }
            sum_strength += (k - total_distinct);

            result[k - 1] = max(sum_strength, k);
        }

        for (int i = 0; i < n; ++i)
        {
            cout << result[i] << " ";
        }
        cout << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();

    return 0;
}
