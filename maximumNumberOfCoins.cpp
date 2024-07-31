#include <algorithm>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxCoins(vector<int> &piles)
    {
        sort(piles.begin(), piles.end());
        int myCount = 0;
        int n = piles.size() / 3;
        for (int i = n; i < piles.size(); i += 2)
        {
            myCount += piles[i];
        }
        return myCount;
    }
};