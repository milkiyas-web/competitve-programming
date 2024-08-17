#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Helper function to get the maximum burles given a string, number of operations, and string length
int maxBurles(int n, int k, const string &s)
{
    unordered_map<char, int> lowerCount;
    unordered_map<char, int> upperCount;
    unordered_map<char, int> potentialPairs;

    // Count the frequency of each letter in both cases
    for (char c : s)
    {
        if (islower(c))
        {
            lowerCount[c]++;
        }
        else
        {
            upperCount[c]++;
        }
    }

    int currentPairs = 0;
    vector<int> additionalPairs;

    // Calculate the number of current pairs and potential additional pairs
    for (char c = 'a'; c <= 'z'; ++c)
    {
        char upperC = c - 'a' + 'A';
        int pairs = min(lowerCount[c], upperCount[upperC]);
        currentPairs += pairs;

        // Calculate potential pairs if we convert lowercase to uppercase or vice versa
        int lowerToUpper = max(0, lowerCount[c] - pairs);
        int upperToLower = max(0, upperCount[upperC] - pairs);

        if (lowerToUpper > 0)
        {
            potentialPairs[c] = lowerToUpper;
        }
        if (upperToLower > 0)
        {
            potentialPairs[upperC] = upperToLower;
        }
    }

    // Sort the additional pairs by the number of operations needed
    vector<int> operationsNeeded;
    for (const auto &p : potentialPairs)
    {
        operationsNeeded.push_back(p.second);
    }
    sort(operationsNeeded.begin(), operationsNeeded.end());

    // Calculate the maximum additional pairs we can achieve with the given number of operations
    int additionalPairsPossible = 0;
    for (int operations : operationsNeeded)
    {
        if (k >= operations)
        {
            k -= operations;
            additionalPairsPossible++;
        }
        else
        {
            break;
        }
    }

    return currentPairs + additionalPairsPossible;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;

        cout << maxBurles(n, k, s) << endl;
    }

    return 0;
}
