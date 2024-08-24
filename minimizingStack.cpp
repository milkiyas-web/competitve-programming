#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> bars(n);
    for (int i = 0; i < n; i++)
    {
        cin >> bars[i];
    }

    map<int, int> count;
    for (int bar : bars)
    {
        count[bar]++;
    }

    int max_height = 0, total_towers = 0;
    for (auto &pair : count)
    {
        max_height = max(max_height, pair.second);
        total_towers++;
    }

    cout << max_height << " " << total_towers << endl;

    return 0;
}