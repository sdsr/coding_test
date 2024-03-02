#include <iostream>
#include <queue>
#include <vector>
#include <cstring> // memset 함수 사용
using namespace std;

const int MAX = 10000;
bool visited[MAX];
int A, B;

int D(int n) {
    return (2 * n) % 10000;
}

int S(int n) {
    return (n == 0) ? 9999 : n - 1;
}

int L(int n) {
    return (n % 1000) * 10 + n / 1000;
}

int R(int n) {
    return (n % 10) * 1000 + n / 10;
}

string bfs() {
    memset(visited, false, sizeof(visited));
    queue<pair<int, string>> q;
    q.push({A, ""});
    visited[A] = true;

    while (!q.empty()) {
        int current = q.front().first;
        string operations = q.front().second;
        q.pop();

        if (current == B) return operations;

        vector<pair<int, char>> next = {{D(current), 'D'}, {S(current), 'S'}, {L(current), 'L'}, {R(current), 'R'}};
        
        for (auto& [nxt, op] : next) {
            if (!visited[nxt]) {
                visited[nxt] = true;
                q.push({nxt, operations + op});
            }
        }
    }
    return "";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        cin >> A >> B;
        cout << bfs() << '\n';
    }
    return 0;
}
