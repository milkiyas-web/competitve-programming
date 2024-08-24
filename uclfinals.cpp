#include <iostream>
#include <unordered_map>
#include <string>

int main()
{
    int n;
    std::cin >> n;
    std::cin.ignore(); // Ignore the newline character after the number

    std::unordered_map<std::string, int> goalCount;
    std::string teamName;

    // Read each goal and count them
    for (int i = 0; i < n; ++i)
    {
        std::getline(std::cin, teamName);
        goalCount[teamName]++;
    }

    std::string winner;
    int maxGoals = 0;

    for (const auto &entry : goalCount)
    {
        if (entry.second > maxGoals)
        {
            maxGoals = entry.second;
            winner = entry.first;
        }
    }

    std::cout << winner << std::endl;

    return 0;
}
