#include <iostream>
#include <map>
#include <vector>

using namespace std;


int solution(const map<string, vector<string>> &closet) {
    size_t result = 1;
    for (const auto &item: closet) {
        result *= (item.second.size() + 1);
    }
    return (int) result - 1;
}

int main() {
    int T, n;
    string category, item;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> n;
        map<string, vector<string>> closet;
        for (int j = 0; j < n; j++) {
            cin >> item >> category;
            closet[category].push_back(item);
        }
        cout << solution(closet) << "\n";
    }
}
