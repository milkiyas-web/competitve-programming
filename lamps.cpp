#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// Function to calculate maximum points
long long maxPoints(vector<pair<int, int>> &lamps, int n)
{
    // Sort lamps by ai
    sort(lamps.begin(), lamps.end());

    priority_queue<int> maxHeap;
    long long totalPoints = 0;
    int activeLamps = 0;
    int currentIndex = 0;

    // Process each lamp by its ai value
    for (int i = 1; i <= n; ++i)
    {
        // Add all lamps with ai <= i to the max-heap
        while (currentIndex < n && lamps[currentIndex].first <= i)
        {
            maxHeap.push(lamps[currentIndex].second);
            currentIndex++;
        }

        // Turn on the lamp with the maximum bi value
        if (!maxHeap.empty())
        {
            totalPoints += maxHeap.top();
            maxHeap.pop();
        }
    }

    return totalPoints;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        vector<pair<int, int>> lamps(n);

        for (int i = 0; i < n; ++i)
        {
            int a, b;
            cin >> a >> b;
            lamps[i] = {a, b};
        }

        cout << maxPoints(lamps, n) << endl;
    }

    return 0;
}
