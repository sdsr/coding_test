#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>

using namespace std;

int D(int);

int S(int);

int L(int);

int R(int);

string bfs(int, int);

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int start, target;
        cin >> start >> target;
        cout << bfs(start, target) << "\n";
    }

    return 0;
}

string bfs(int start, int target) {
    queue<pair<int, string>> q;
    unordered_set<int> visited;
    q.emplace(start, "");
    visited.insert(start);

    while (!q.empty()) {
        auto [cur, ops] = q.front();
        q.pop();
        if (cur == target) {
            return ops;
        }

        int next;
        next = D(cur);
        if (visited.find(next) == visited.end()) {
            q.push({next, ops + "D"});
            visited.insert(next);
        }
        next = S(cur);
        if (visited.find(next) == visited.end()) {
            q.push({next, ops + "S"});
            visited.insert(next);
        }
        next = L(cur);
        if (visited.find(next) == visited.end()) {
            q.push({next, ops + "L"});
            visited.insert(next);
        }
        next = R(cur);
        if (visited.find(next) == visited.end()) {
            q.push({next, ops + "R"});
            visited.insert(next);
        }
    }
    return "ERROR";
}

int D(int input) {
    input *= 2;
    if (input < 10000)
        return input;
    else {
        return input / 10000;
    }
}

int S(int input) {
    if (input == 0)
        return 9999;
    else
        return input - 1;
}

int L(int input) {
    string temp = to_string(input);
    char c = temp[0];
    temp.erase(0, 1);
    temp += c;
    return stoi(temp);
}

int R(int input) {
    string temp = to_string(input);
    if (temp.length() > 1) {
        char lastChar = temp[temp.length() - 1];
        temp.erase(temp.length() - 1);
        temp = lastChar + temp;
    }
    return stoi(temp);
}
