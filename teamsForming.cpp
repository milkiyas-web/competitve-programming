//
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

    // Sort the skills in ascending order
    sort(a.begin(), a.end());

    int numOfTeams = n / 2;
    int numOfProblemsSolved = 0;

    // Pair students
    for (int i = 0; i < n; i += 2)
    {
        // Calculate the difference in skills for the two students in the team
        int diff = a[i + 1] - a[i];
        // Add the difference to the total number of problems to solve
        numOfProblemsSolved += diff;
    }

    cout << numOfProblemsSolved << endl;

    return 0;
}
