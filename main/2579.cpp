#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int num;
  cin >> num;
  int *score = new int[num + 1];
  int *dp = new int[num + 1];

  for (int i = 1; i <= num; i++) {
    cin >> score[i];
  }

  dp[0] = 0;
  dp[1] = score[1];

  if (num > 1) {
    dp[2] = score[1] + score[2];
  }

  for (int i = 3; i <= num; i++) {
    dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i]);
  }

  cout << dp[num] << "\n";

  delete[] score;
  delete[] dp;

  return 0;
}
