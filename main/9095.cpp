#include <iostream>

using namespace std;

int solution(int);

int dp[11] = {
        0,
};

int main() {
    int T;
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;

    cin >> T;
    for (int i = 3; i < 11; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    int temp;
    while (T--) {
        cin >> temp;
        cout << dp[temp] << "\n";
    }
}
